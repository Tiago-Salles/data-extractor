import json

from excel_data_generator import FileGenerator

def generate_file(data):
    FileGenerator().generate_xlsx("file", [{"name": "Tiago"}, {"name": "Pietra"}])

def extract_data():
    """
    """

    with open("config.json", "r") as f:
        data = json.load(f)
        f.close()

    if data:
        return generate_file(data)

    print(f"It is necessary to specify the extraction config.")

