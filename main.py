import requests, json
from fake_useragent import UserAgent
from Bot.DB.db import Database

from colorama import Fore, Style, init
init()


class CoinMarketCapAPI:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.ua.random,
            "Accept": "application/json",
            "Referer": "https://coinmarketcap.com/"
        })
        self.URL_COIN_ID = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"
        self.db = Database()

    def get_total_coinId(self, start=1, limit=1):
        params = {"start": start, "limit": limit}
        try:
            r = self.session.get(self.URL_COIN_ID, params=params)
            r.raise_for_status()
            data = r.json()
            return data["data"]["totalCount"]
        except Exception as e:
            print(f"An error occurred while fetching total coin IDs: {e}")
            return None
        
    def start_scrap(self, limit, start=1):
        params = {"start": start, "limit": limit}
        try:
            r = self.session.get(self.URL_COIN_ID, params=params)
            r.raise_for_status()
            data = r.json()
            return data["data"]["cryptoCurrencyList"]
        except Exception as e:
            print(f"An error occurred while fetching total coin IDs: {e}")
            return None
    
    def show_mune(self):
                print(Fore.CYAN + """
        ╔════════════════════════════════════════╗
        ║        Multi CoinMarketCap Menu        ║
        ╠════════════════════════════════════════╣
        ║  [1]. Extract cryptocurrency IDs       ║
        ║  [2]. Extract cryptocurrency data      ║
        ║  [3]. Exit                             ║
        ╚════════════════════════════════════════╝
        """ + Style.RESET_ALL)
    def start(self):
        self.show_mune()
        while True:
            try:
                choice = int(input("Select Choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if choice > 3 or choice < 1:
                print("Invalid input. Please enter a number between 1 and 3.")
                continue
            
            if choice == 3:
                print('GoodBye✨')
                break
            
            if choice == 1:
                total_coinId = self.get_total_coinId()
                print(f"Total coin IDs: {total_coinId}")
                while True:
                    try:
                        count_coin_id = int(
                            input(f"[INPUT] Number of coins to extract (min : 1 ,max : {total_coinId}): ")
                        )

                        if 1 <= count_coin_id <= total_coinId:
                            break
                        
                        print(f"Invalid input. Please enter a number between 1 and, {total_coinId}")
                        
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
                
                
start = CoinMarketCapAPI()
if __name__ == "__main__":
    start.start()