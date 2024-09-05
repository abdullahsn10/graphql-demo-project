import strawberry
from src.graphql.types.user.query import UserQuery
from src.graphql.types.blog.query import BlogQuery


@strawberry.type
class Query(UserQuery, BlogQuery):
    pass
