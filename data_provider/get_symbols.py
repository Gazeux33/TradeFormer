from config import PUBLIC, SECRET
from utils.utils import save_json

from alpaca.trading import TradingClient


def get_all_symbols(client:TradingClient, save:bool=False , path:str=None) -> list:
    assets = client.get_all_assets()
    assets_list = [{"name":a.name,"symbol":a.symbol,"tradable":a.tradable,"exchange":a.exchange} for a in assets]
    if save :
        save_json(assets_list, path)
        print(f"{len(assets_list)} symbols saved to {path}")
    return assets_list



if __name__ == "__main__":
    # create client
    traid_client = TradingClient(PUBLIC,SECRET)

    # get all symbols
    symbols = get_all_symbols(traid_client, save=True, path="symbols.json")


