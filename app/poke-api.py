import requests
from sqlalchemy import create_engine
import pandas as pd

API_URL = "https://catfact.ninja/fact"

def fetch_data_from_API(API_URL: str) -> dict:
    """Fetch data from the test API"""
    response = requests.get(API_URL)
    data = response.json()

    return data

def to_df(data: dict) -> pd.DataFrame:
    """Convert JSON data to a DataFrame"""
    df = pd.DataFrame.from_dict(data, orient='index').transpose()

    return df

def load_data_into_db(df: pd.DataFrame) -> None:
    
    # Connect to the PostgreSQL database
    engine = create_engine('postgresql://admin:domino@localhost:5432/app_db')

    # Insert DataFrame data into the PostgreSQL table
    df.to_sql('cat_facts',con=engine, if_exists='append', index=False)
    print('Data loaded into PostgreSQL successfully!')

if __name__ == "__main__":
    data = fetch_data_from_API(API_URL)
    df = to_df(data)
    load_data_into_db(df)