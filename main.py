from fastapi import FastAPI

app = FastAPI()


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from routes.route import route

app.include_router(route)