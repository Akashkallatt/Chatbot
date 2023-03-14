from django.db import models

class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    stupid_clicks = models.IntegerField(default=0)
    fat_clicks = models.IntegerField(default=0)
    dumb_clicks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.telegram_id)
