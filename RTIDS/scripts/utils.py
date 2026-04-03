
import pandas as pd
import sys
import zipfile
from pathlib import Path
import os
import gc


ROOT = Path(__file__).resolve().parents[2]


def extract_zip(zip_path: Path, dest: Path):
    dest.mkdir(parents=True, exist_ok=True)
    print(f"Extracting {zip_path.name} -> {dest.relative_to(ROOT)}/")
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(dest)

def dir_file_sizes(dir_path: Path):
    dir_size = 0
    
    for file in dir_path.rglob("*"):
        if file.is_file():
            size = os.path.getsize(file)
            dir_size += size
            print(f"File, File size: {file}, {size} bytes | {size / 2**30:.2f} gigabytes")
    print(f"Directory, Total File Size: {dir_path}, {dir_size} bytes | {dir_size / 2**30:.2f} gigabytes")
    print(list(dir_path.iterdir()))
        
def dir_has_matching_data(dir_path: Path) -> bool:
    datatypes = []
    for file in dir_path.rglob("*.csv"):
        if file.is_file():
            
            print(f"Loading file: {file}")
            df = pd.read_csv(file, nrows=100)  # small sample
            datatypes.append(df.dtypes)
            del df
            gc.collect()     

    truth = compare_dtypes(datatypes)
    print(f"{dir_path}")
    
    print(f"All CSVs in {dir_path} have the same schema. Status: {truth}.")

def compare_dtypes(collection: list[pd.Series]) -> Tuple[bool, list[Path]]:
    first = collection[0]
    truth = (True, None)
    for i, other in enumerate(collection[1:], start=1):
        if not first.equals(other):
            print(f"Mismatch found in file #{i}")
            print("Differences:")
            print(first.compare(other))
            truth[0] = False
        else:
            print(f"Schema matches in file #{i}")
    return truth

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: utils.py <path/to/file.csv|parquet>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    
    dir_file_sizes(path)
    
    
    