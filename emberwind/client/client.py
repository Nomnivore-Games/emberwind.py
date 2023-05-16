import anyio


class Client:
    def __init__(self, key: str, email: str = "", password: str = ""):
        """Initialize the client with the key, email, and password.
        :param key: The API key for the client.
        :param email: The email for the client.
        :param password: The password for the client."""

        self.key = key
        self.email = email
        self.password = password
