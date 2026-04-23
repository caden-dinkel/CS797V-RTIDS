import sys
import zipfile
from pathlib import Path

import pandas as pd

# Data structure:
# CICIDS2017 DATASET INCLUDES: 'GeneratedLabelledFlows.zip', 'MachineLearningCSV.zip'
# CIC-DDoS2019 DATASET INCLUDES: 'CSV-01-12.zip', 'CSV-03-11.zip'

# Each zip file in 'raw/' contains multiple folders of csv data.

# The internal folder structure of the zip files should be conserved.

# Each csv file should be converted to parquet, and then deleted.

# The resulting folder structure should be:

# data/
#   CICIDS2017/
#       internal_folder1/
#           condents.parquet
#       internal_folder2/
#   CIC-DDoS2019/ ...
# raw/
#   <empty>


ZIP_TO_DATASET = {
    "GeneratedLabelledFlows.zip": "CICIDS2017",
    "CSV-01-12.zip": "CIC-DDoS2019",
    "CSV-03-11.zip": "CIC-DDoS2019",
}

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"
DATA_DIR = ROOT / "data" / "unprocessed"


def csv_to_parquet(csv_path: Path):
    parquet_path = csv_path.with_suffix(".parquet")
    try:
        df = pd.read_csv(csv_path, low_memory=False, encoding="latin-1")

        # Normalize column names: strip surrounding whitespace
        df.columns = df.columns.str.strip()

        # Drop spurious pandas index columns (e.g. "Unnamed: 0")
        df = df.loc[:, ~df.columns.str.match(r"^Unnamed")]

        # Fix mixed-type object columns (e.g. SimillarHTTP has both int 0 and str '0').
        # If every non-null value converts to a number without introducing new NaNs,
        # store as float. Otherwise keep as string (handles IPs, labels, etc.).
        for col in df.select_dtypes(include="object").columns:
            converted = pd.to_numeric(df[col], errors="coerce")
            newly_null = converted.isna() & df[col].notna()
            if not newly_null.any():
                df[col] = converted
            else:
                df[col] = df[col].astype(str)

        df.to_parquet(parquet_path, index=False)
    except Exception as e:
        print(f"Error converting '{csv_path}': {e}", file=sys.stderr)


def extract_zip(zip_path: Path, dataset: str):
    dest = DATA_DIR / dataset
    dest.mkdir(parents=True, exist_ok=True)
    print(f"Extracting {zip_path.name} -> {dest.relative_to(ROOT)}/")
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(dest)


if __name__ == "__main__":
    zip_files = [RAW_DIR / name for name in ZIP_TO_DATASET if (RAW_DIR / name).exists()]

    if not zip_files:
        print(f"No known zip files found in {RAW_DIR}")
        sys.exit(1)

    datasets_processed = set()

    for zip_path in zip_files:
        dataset = ZIP_TO_DATASET[zip_path.name]
        extract_zip(zip_path, dataset)
        datasets_processed.add(dataset)

    print("Done.")
