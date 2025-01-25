import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine



def build_dburl():
    """load_params"""
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST", None)
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_USER = os.getenv("DB_USER", None)
    DB_PASS = os.getenv("DB_PASS", None)
    DB_NAME = os.getenv("DB_NAME", "postgres")

    return  URL.create(
        "postgresql",
        username = DB_USER,
        password = DB_PASS,  
        host = DB_HOST,
        port = DB_PORT,
        database = DB_NAME,
    )

def build_engine():
    """make_engine"""
    url_object = build_dburl()
    print(url_object)
    engine = create_engine(url_object)
    return engine
        
        
    
    
    