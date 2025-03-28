from ..base import BaseClient
from ..types import IssueLabel, IssueLabelPayload, IssueLabelCreateInput, IssueLabelUpdateInput

class IssueLabelClient(BaseClient):
    def create_issue_label(self, data: dict) -> IssueLabelPayload:
        """
        Create a new issue label.
        Required fields in data: name, color.
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        if "name" not in data:
            raise ValueError("name is required in data")
        if "color" not in data:
            raise ValueError("color is required in data")

        mutation = """
        mutation CreateIssueLabel($input: IssueLabelCreateInput!) {
            issueLabelCreate(input: $input) {
                success
                issueLabel {
                    id
                    name
                    color
                }
            }
        }
        """
        api_data = {"input": data}
        response = self._make_request(mutation, api_data)
        if not response:
            return response
        return response["data"]["issueLabelCreate"]

    def update_issue_label(self, label_id: str, data: dict) -> IssueLabelPayload:
        """
        Update an existing issue label.
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        mutation = """
        mutation UpdateIssueLabel($id: String!, $input: IssueLabelUpdateInput!) {
            issueLabelUpdate(id: $id, input: $input) {
                success
                issueLabel {
                    id
                    name
                    color
                }
            }
        }
        """
        api_data = {"id": label_id, "input": data}
        response = self._make_request(mutation, api_data)
        if not response:
            return response
        return response["data"]["issueLabelUpdate"]

    def delete_issue_label(self, label_id: str) -> dict:
        """
        Delete an issue label.
        """
        mutation = """
        mutation DeleteIssueLabel($id: String!) {
            issueLabelDelete(id: $id) {
                success
                deletedId
            }
        }
        """
        api_data = {"id": label_id}
        response = self._make_request(mutation, api_data)
        if not response:
            return response
        return response["data"]["issueLabelDelete"]
