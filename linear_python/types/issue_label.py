import strawberry
from typing import Optional

@strawberry.type
class IssueLabel:
    id: strawberry.ID
    name: str
    color: str

@strawberry.type
class IssueLabelPayload:
    success: bool
    issueLabel: Optional[IssueLabel]

@strawberry.input
class IssueLabelCreateInput:
    name: str
    color: str

@strawberry.input
class IssueLabelUpdateInput:
    name: Optional[str]
    color: Optional[str]
