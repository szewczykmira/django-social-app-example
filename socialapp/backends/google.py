from social_core.backends.google import GoogleOAuth2
from app.models import Secrets


class CustomGoogleOAuth2(GoogleOAuth2):
    DB_NAME = 'google-oauth2'

    def get_key_and_secret(self):
        """Return tuple with Consumer Key and Consumer Secret for current
        service provider. Must return (key, secret), order *must* be respected.
        """
        return Secrets.objects.get_backend(self.DB_NAME).get_secrets()
