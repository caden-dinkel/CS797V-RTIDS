import pandas as pd
import sys
from pathlib import Path

LABEL_COLUMN = " Label"
RAW_DIR = ROOT / "raw"
DATA_DIR = ROOT / "data"

def get_labels(file_path: Path) -> set:
    if file_path.suffix == ".parquet":
        df = pd.read_parquet(file_path, columns=[LABEL_COLUMN])
    elif file_path.suffix == ".csv":
        df = pd.read_csv(file_path, usecols=[LABEL_COLUMN])
    else:
        raise ValueError(f"Unsupported file type: {file_path.suffix}")
    return set(df[LABEL_COLUMN].unique())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: contains_labels.py <path/to/file.csv|parquet>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    labels = get_labels(path)
    print(labels)
