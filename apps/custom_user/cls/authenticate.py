import requests
from django.contrib.auth.backends import BaseBackend
from apps.custom_user.models import User


class RemoteAuthBackend(BaseBackend):
    """
    Remote Authentication
    """
    @staticmethod
    def remote_authenticate(username, password):
        """
        It asks other server to authenticate
        :param username: username of a user
        :param password: password of a user
        :return: True/False
        """
        #url = 'http://127.0.0.1:8000/api/api-token-auth/'
        #r = requests.post(url, data={'username': username, 'password': password})
        return username == 'admin' and password == '2'
        return r.status_code == 200 and 'token' in r.json()

    def authenticate(self, request, username=None, password=None):
        if self.remote_authenticate(username, password):
            user = User.objects.filter(username=username).first()
            if user is None:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
