import time
from data_extractor import extract_data

if __name__ == "__main__":
    """
    """

    print("Starting extraction...")
    start = time.time()
    extract_data()
    finish = time.time() - start
    print(f"Finished data extraction {finish}")