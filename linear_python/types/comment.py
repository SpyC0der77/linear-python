import strawberry
from typing import Optional

@strawberry.type
class Comment:
    id: strawberry.ID
    body: str
    createdAt: str
    updatedAt: Optional[str]

@strawberry.type
class CommentPayload:
    success: bool
    comment: Optional[Comment]

@strawberry.input
class CommentCreateInput:
    issueId: str
    body: str

@strawberry.input
class CommentUpdateInput:
    body: Optional[str]
