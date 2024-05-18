# app/services.py

import requests
import logging

API_KEY = 'goldapi-1g1hjslw98njsr-io'  # Replace with your actual Gold API key
BASE_URL = 'https://www.goldapi.io/api/'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

METAL_SYMBOLS = {
    'gold': 'XAU',
    'silver': 'XAG',
    'platinum': 'XPT',
    'palladium': 'XPD'
}

def get_spot_price(metal_type: str):
    headers = {
        'x-access-token': API_KEY,
        'Content-Type': 'application/json'
    }
    symbol = METAL_SYMBOLS.get(metal_type.lower())
    if not symbol:
        raise ValueError("Invalid metal type. Use 'gold', 'silver', 'platinum', or 'palladium'.")
    url = f"{BASE_URL}{symbol}/USD"
    logger.info(f"Requesting URL: {url}")
    logger.info(f"Headers: {headers}")
    response = requests.get(url, headers=headers)
    logger.info(f"Response: {response.status_code} {response.text}")
    response.raise_for_status()  # This will raise an HTTPError for bad responses
    return response.json()

def get_conversion_rate(currency: str):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/USD")
    response.raise_for_status()  # This will raise an HTTPError for bad responses
    rates = response.json().get('rates', {})
    return rates.get(currency.upper(), 1)

def get_historical_data(metal_type: str, start_date: str, end_date: str):
    headers = {
        'x-access-token': API_KEY,
        'Content-Type': 'application/json'
    }
    symbol = METAL_SYMBOLS.get(metal_type.lower())
    if not symbol:
        raise ValueError("Invalid metal type. Use 'gold', 'silver', 'platinum', or 'palladium'.")
    url = f"{BASE_URL}{symbol}/USD?start_date={start_date}&end_date={end_date}"
    logger.info(f"Requesting URL: {url}")
    logger.info(f"Headers: {headers}")
    response = requests.get(url, headers=headers)
    logger.info(f"Response: {response.status_code} {response.text}")
    response.raise_for_status()  # This will raise an HTTPError for bad responses
    return response.json()
