from asks import Session

from emberwind.models.emberwind.user import User


class AuthorizationController:
    @staticmethod
    async def login(session: Session, url: str, email: str, password: str) -> User:
        """
        Login to the API.
        :param session:
        :param url:
        :param email:
        :param password:
        :return:
        """
        response = await session.post(
            f"{url}/auth/login",
            json={
                "email": email,
                "password": password,
            },
        )

        return User.from_json(response.json())

    @staticmethod
    def logout(session, url):
        """
        Logout of the API.
        :param session:
        :param url:
        :return:
        """
        return session.post(f"{url}/auth/logout")
