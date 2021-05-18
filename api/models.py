from django.db import models
from django.utils.timezone import now


# Create your models here.


class User(models.Model):
    first_name = models.TextField(max_length=50)
    second_name = models.TextField(max_length=50)
    additional_info = models.JSONField()


class Friendship(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='First user+')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Second user+')
    start_date = models.DateTimeField(default=now())

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('first_user', 'second_user'), name='fst_constraint')
        ]

    def save(self, *args, **kwargs):
        if self.first_user.id == self.second_user.id:
            raise Exception('Users must not be equal')
        super(Friendship, self).save(*args, **kwargs)
