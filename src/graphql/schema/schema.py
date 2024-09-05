import strawberry
from src.graphql.schema.query import Query
from src.graphql.schema.mutation import Mutation

# Create the Strawberry schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
