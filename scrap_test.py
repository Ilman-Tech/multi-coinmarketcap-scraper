import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

us = UserAgent()
session = requests.Session()
session.headers.update({'User-Agent': us.random})

try:
    r = session.get('https://coinmarketcap.com/currencies/bitcoin/')
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    
    coin_name = soup.find('span', class_="sc-65e7f566-0 lsTl")
    coni_saymbol = soup.find("span", class_="sc-65e7f566-0 czZVlm base-text")
    coin_rank = soup.find("div", class_="sc-65e7f566-0 eQBACe BaseChip_labelWrapper__pQXPT")
    coin_price = soup.find("span", class_="sc-65e7f566-0 WXGwg base-text")
    
    print(f"Coin Name: {coin_name.get_text(strip=True).split('p')[0] if coin_name else 'N/A'}")
    print(f"Coin Symbol: {coni_saymbol.get_text(strip=True) if coni_saymbol else 'N/A'}")
    print(f"Coin Rank: {coin_rank.get_text(strip=True) if coin_rank else 'N/A'}")
    print(f"Coin Price: {coin_price.get_text(strip=True) if coin_price else 'N/A'}")
    
    
except Exception as e:
    print(f"An error occurred: {e}")
