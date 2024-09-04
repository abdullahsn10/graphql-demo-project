import strawberry


@strawberry.type
class BlogType:
    id: int
    title: str
    content: str
    owner_id: int
