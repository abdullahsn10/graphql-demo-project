import strawberry
from src.graphql.schema.query import Query

# Create the Strawberry schema
schema = strawberry.Schema(query=Query)
