import requests
from infra.api.response_wrapper import ResponseWrapper


class APIWrapper:
    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, headers=None, json=None):
        """
        Sends a GET request to the specified URL with optional headers and JSON payload.
        Args:
            url (str): The URL to which the GET request is sent.
            headers (dict, optional): Headers to include in the request.
            json (dict, optional): JSON payload to include in the request.

        Returns:
            ResponseWrapper: A ResponseWrapper object containing the response status,
                              success indicator, and the response data in JSON format.
                              Returns None if an error occurs.
        """
        response = requests.get(
            url,
            headers=headers,
            json=json
        )
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())

    @staticmethod
    def post_request(url, headers=None, json=None):
        """
        Sends a POST request to the specified URL with optional headers and JSON payload.
        Args:
            url (str): The URL to which the POST request is sent.
            headers (dict, optional): Headers to include in the request.
            json (dict, optional): JSON payload to include in the request.

        Returns:
            ResponseWrapper: A ResponseWrapper object containing the response status,
                              success indicator, and the response data in JSON format.
                              Returns None if an error occurs.
        """
        response = requests.post(
            url,
            headers=headers,
            json=json
        )
        return ResponseWrapper(ok=response.ok, status=response.status_code, data=response.json())
