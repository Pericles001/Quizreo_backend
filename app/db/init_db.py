import time

import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.config import settings

while True:
    try:
        connector = psycopg2.connect(host=settings.POSTGRES_SERVER, database=settings.POSTGRES_DB,
                                     user=settings.POSTGRES_USER, password=settings.POSTGRES_PASSWORD,
                                     cursor_factory=RealDictCursor)
        cursor = connector.cursor()
        print("Database connection was successfully")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)
