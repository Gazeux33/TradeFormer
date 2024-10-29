from utils.utils import load_json
from config import PUBLIC, SECRET

from datetime import datetime
import os
import time
import json

from alpaca.data import StockHistoricalDataClient, StockBarsRequest, TimeFrame
from alpaca.common import APIError
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

class DataCollector:
    def __init__(self, public: str, secret: str, out_dir: str, symbols_dir: str,processed_dir:str, start: datetime, end: datetime, timeframe: TimeFrame):
        self.public = public
        self.secret = secret
        self.out_dir = out_dir
        self.processed_dir = processed_dir
        self.symbols_dir = symbols_dir
        self.start = start
        self.end = end
        self.timeframe = timeframe
        self.client = StockHistoricalDataClient(self.public, self.secret)
        self.lock = threading.Lock()
        self.freq = 100

        self.list_of_symbols: list[str] = []
        self.processed_symbols: list[str] = []
        self._load_symbols()

    def _load_symbols(self):
        if os.path.exists(self.processed_dir):
            symbol_list_already_processed = load_json(self.processed_dir)
            self.processed_symbols = symbol_list_already_processed
            print(f"Assets already processed: {len(symbol_list_already_processed)}")
        else:
            symbol_list_already_processed = []
            print("No assets already processed")
        symbol_list_csv = load_json(self.symbols_dir)
        self.list_of_symbols = [s['symbol'].replace(".csv","") for s in symbol_list_csv if s['symbol'].replace(".csv","") not in symbol_list_already_processed]
        print(f"Assets to download: {len(self.list_of_symbols)}")

    def _save_processed_symbols(self):
        with open(self.processed_dir, 'w') as f:
            json.dump(self.processed_symbols, f, indent=4)
            print("saved processed symbols")

    def get_all_data(self):
        max_workers = 5
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self._download_and_save, symbol): symbol for symbol in self.list_of_symbols}
            for i, future in enumerate(tqdm(as_completed(futures), total=len(futures), desc="Downloading data")):
                symbol = futures[future]
                self.processed_symbols.append(symbol)
                try:
                    future.result()
                except Exception as e:
                    print(f"Error downloading data for {symbol}: {e}")

                if (i + 1) % self.freq == 0:
                    self._save_processed_symbols()

            # Save any remaining processed symbols after the loop
            self._save_processed_symbols()

    def _download_and_save(self, symbol: str):
        #print(f"Starting downloading data for {symbol}")
        data = self._get_data(symbol)
        if data is not None and not data.df.empty:
            with self.lock:
                self._save_data(symbol, data.df)

        else:
            pass
        time.sleep(1)

    def _get_data(self, symbol: str):
        try:
            request = self._build_request(symbol)
            return self.client.get_stock_bars(request)
        except APIError as e:
            print(f"API error for {symbol}: {e}")
        except Exception as e:
            print(f"Unexpected error for {symbol}: {e}")

    def _build_request(self, symbol: str):
        return StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe=self.timeframe,
            start=self.start,
            end=self.end
        )

    def _save_data(self, symbol: str, df):
        df = df.reset_index().rename(columns={"timestamp": "date"}).drop(columns=["trade_count", "vwap"])
        csv_path = os.path.join(self.out_dir, f"{symbol}.csv")
        df.to_csv(csv_path, index=False)


if __name__ == '__main__':
    datacollector = DataCollector(
        public=PUBLIC,
        secret=SECRET,
        out_dir="csv/",
        symbols_dir="symbols.json",
        processed_dir="processed.json",
        start=datetime(2020, 1, 1),
        end=datetime(2022, 1, 1),
        timeframe=TimeFrame.Minute
    )
    datacollector.get_all_data()
