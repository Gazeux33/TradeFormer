import torch


ENDPOINT = "https://paper-api.alpaca.markets/v2"
PUBLIC = ""
SECRET = ""

DATA_DIR = "data/"
CSV_DIR = f"{DATA_DIR}csv_files/"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")



