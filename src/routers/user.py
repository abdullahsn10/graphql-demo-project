from strawberry.fastapi import GraphQLRouter
from src.graphql.schema.schema import schema
from fastapi import Depends
from src.settings.database import get_db
from sqlalchemy.orm import Session


def get_context(db: Session = Depends(get_db)):
    return {"db": db}


# Create the GraphQL router
graphql_router = GraphQLRouter(schema, context_getter=get_context)
