"""Connects to the database"""

from json import loads

from requests import post, exceptions

from common import UN, PW, HOST, ACCESS_TOKEN_KEY

from get_secrets import get_secret


# pylint: disable=too-few-public-methods
class _DBBase:
    """The base class for the DB connection"""

    call = "call"
    auth = "auth"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    host = get_secret(file_name=HOST)
    _username = get_secret(file_name=UN)
    _password = get_secret(file_name=PW)

    def request(self, path: str, args: dict) -> tuple:
        """Sends a request to the DB

        :param string path: The URL path (i.e 'call' or 'auth')
        :param dictionary args: The Kwargs to send to the DB interface

        """
        error = False
        return_vals = None
        try:

            response = post(**{"url": f"{self.host}/{path}", "headers": self.headers, "json": args})
            if response.status_code != 200:
                error = True
                return_vals = return_vals.text
            else:
                return_vals = loads(response.content)

        except (exceptions.ConnectionError, exceptions.InvalidURL) as exc:
            error = True
            return_vals = str(exc)

        return error, return_vals


class DBInterface(_DBBase):
    """The Database interface class"""

    def __init__(self) -> None:
        self.headers = self.headers | {"Authorization": f"Bearer {self._token}"}

    @property
    def _token(self):
        """The JWT token for the DB connection"""
        error, resp = self.request(path=f"{self.auth}", args={"username": self._username, "password": self._password})
        if error:
            raise ConnectionError(f"Token not returned. Response: {resp}")

        return resp[ACCESS_TOKEN_KEY]
