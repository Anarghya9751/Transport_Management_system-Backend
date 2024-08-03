from django.db import models

class ConfigurationManager(models.Manager):
    def get_value(self, key, default=None):
        try:
            return self.get(key=key).value
        except self.model.DoesNotExist:
            return default

    def set_value(self, key, value):
        obj, created = self.update_or_create(key=key, defaults={'value': value})
        return obj
