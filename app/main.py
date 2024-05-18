# app/main.py

import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from app.services import get_spot_price, get_conversion_rate, get_historical_data

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class ConversionRequest(BaseModel):
    metal_type: str
    amount: float
    currency: str

@app.post("/convert-price/")
def convert_price(request: ConversionRequest):
    try:
        spot_price = get_spot_price(request.metal_type)
        conversion_rate = get_conversion_rate(request.currency)
        converted_price = request.amount * spot_price['price'] * conversion_rate
        return {"converted_price": converted_price}
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/spot-price/{metal_type}")
def read_spot_price(metal_type: str):
    try:
        return get_spot_price(metal_type)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/historical-data/{metal_type}")
def read_historical_data(metal_type: str, start_date: str, end_date: str):
    try:
        return get_historical_data(metal_type, start_date, end_date)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/protected-endpoint/")
def read_protected_data(token: str = Depends(oauth2_scheme)):
    # Validate token and return data
    pass
