from social_core.backends.google import GoogleOAuth2
from socialapp.secrets import KEY, SECRET


class CustomGoogleOAuth2(GoogleOAuth2):
    def get_key_and_secret(self):
        """Return tuple with Consumer Key and Consumer Secret for current
        service provider. Must return (key, secret), order *must* be respected.
        """
        return KEY, SECRET
