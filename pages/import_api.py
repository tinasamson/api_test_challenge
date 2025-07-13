import requests


class PersonAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

    def post_request_person_data(self, person_id):
        payload = {"personId": person_id}
        response = requests.post(
            f"{self.base_url}/import", headers=self.headers, json=payload
        )
        return response