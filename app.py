from fastapi import FastAPI
from routes.API import api

app = FastAPI()

app.include_router(api)                                                                                                                                                            