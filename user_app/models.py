from django.db import models
from django.contrib.auth.models import User 


class MemberProfile(User):
    age = models.PositiveIntegerField()
    img = models.ImageField(upload_to = "member_photos/", default= 'default_user.png')

    class Meta:
        verbose_name = 'Member Profile'


class StaffProfile(User):
    img = models.ImageField(upload_to = "staff_photos/", default= 'default_user.png')

    class Meta:
        verbose_name = 'Staff Profile'

    def save(self) -> None:
        self.is_staff=True
        return super().save()