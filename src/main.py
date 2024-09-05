from fastapi import FastAPI
from src.routers.user import graphql_router

app = FastAPI()

# register routes
app.include_router(graphql_router, prefix="/graphql")
