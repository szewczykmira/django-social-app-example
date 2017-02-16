from django.db import models


class SecretsQueryset(models.QuerySet):
    def get_backend(self, name):
        return self.get(name=name)


class Secrets(models.Model):
    name = models.CharField(max_length=20)
    key = models.TextField()
    secret = models.TextField()
    objects = SecretsQueryset.as_manager()

    def get_secrets(self):
        return self.key, self.secret
