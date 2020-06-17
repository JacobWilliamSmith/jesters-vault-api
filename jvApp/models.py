from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    passhash = models.CharField(max_length=64)
    email = models.EmailField()
    timer_countdown = models.IntegerField()
    timer_enabled = models.BooleanField()

    def __str__(self):
        return self.username

class WildCard(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    default_ac = models.IntegerField()
    default_max_hp = models.IntegerField()
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name