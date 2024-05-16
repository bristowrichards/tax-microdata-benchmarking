"""
This module enables generation of all datasets involved in the repo.
"""

from tax_microdata_benchmarking.datasets import (
    create_ecps,
    create_puf,
    create_puf_ecps_flat_file,
    load_taxdata_puf,
)
from tax_microdata_benchmarking.storage import STORAGE_FOLDER
import time

outputs = STORAGE_FOLDER / "output"

generation_functions = [
    (lambda: create_puf_ecps_flat_file(2021), "puf_ecps_2021.csv.gz"),
    (lambda: create_puf_ecps_flat_file(2023), "puf_ecps_2023.csv.gz"),
    (lambda: load_taxdata_puf(2021), "taxdata_puf_2023.csv.gz"),
]


def main():
    for generation_function, filename in generation_functions:
        print(f"Generating {filename}...")
        start_time = time.time()
        data = generation_function()
        data.to_csv(outputs / filename, index=False)
        duration = time.time() - start_time
        print(f"   ...completed {filename} in {duration:.2f} seconds")


if __name__ == "__main__":
    main()
