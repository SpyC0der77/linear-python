from ..base import BaseClient
from ..types import Comment, CommentPayload, CommentCreateInput, CommentUpdateInput

class CommentClient(BaseClient):
    def create_comment(self, data: dict) -> CommentPayload:
        """
        Create a new comment.
        Required fields in data: issueId, body.
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        if "issueId" not in data:
            raise ValueError("issueId is required in data")
        if "body" not in data:
            raise ValueError("body is required in data")

        mutation = """
        mutation CreateComment($input: CommentCreateInput!) {
            commentCreate(input: $input) {
                success
                comment {
                    id
                    body
                    createdAt
                }
            }
        }
        """
        api_data = {"input": data}
        response = self._make_request(mutation, api_data)
        if not response:
            return response
        return response["data"]["commentCreate"]

    def update_comment(self, comment_id: str, data: dict) -> CommentPayload:
        """
        Update an existing comment.
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        mutation = """
        mutation UpdateComment($id: String!, $input: CommentUpdateInput!) {
            commentUpdate(id: $id, input: $input) {
                success
                comment {
                    id
                    body
                    updatedAt
                }
            }
        }
        """
        api_data = {"id": comment_id, "input": data}
        response = self._make_request(mutation, api_data)
        if not response:
            return response
        return response["data"]["commentUpdate"]

    def delete_comment(self, comment_id: str) -> dict:
        """
        Delete a comment.
        """
        mutation = """
        mutation DeleteComment($id: String!) {
            commentDelete(id: $id) {
                success
                deletedId
            }
        }
        """
        api_data = {"id": comment_id}
        response = self._make_request(mutation, api_data)
        if not response:
            return response
        return response["data"]["commentDelete"]
