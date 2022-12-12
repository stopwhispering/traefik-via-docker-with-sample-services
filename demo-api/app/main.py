from random import randint

from fastapi import FastAPI
from names import get_full_name

from logging.config import dictConfig
import logging

from log import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("demo-api")

logger.info("Dummy Info")
logger.error("Dummy Error")
logger.debug("Dummy Debug")
logger.warning("Dummy Warning")


app = FastAPI()

print('Printing: App2 initialized')


@app.get("/")
def get_sales_data():
    print('Printing: App2 running')
    sales_data = {
        "sales": [
            {
                "id": i,
                "name": get_full_name(),
                "revenue": randint(100, 600) * 100,
            } for i in range(5)
        ]
    }
    return sales_data
