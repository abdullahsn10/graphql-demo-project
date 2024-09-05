import strawberry
from src.graphql.types.user.mutation import UserMutation
from src.graphql.types.blog.mutation import BlogMutation


@strawberry.type
class Mutation(UserMutation, BlogMutation):
    pass
