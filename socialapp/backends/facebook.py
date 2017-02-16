from social_core.backends.facebook import FacebookOAuth2
from app.models import Secrets


class CustomFacebookOAuth2(FacebookOAuth2):
    DB_NAME = 'facebook'

    def get_key_and_secret(self):
        """Return tuple with Consumer Key and Consumer Secret for current
        service provider. Must return (key, secret), order *must* be respected.
        """
        return Secrets.objects.get_backend(self.DB_NAME).get_secrets()
