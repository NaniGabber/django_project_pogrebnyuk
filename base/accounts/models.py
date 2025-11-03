from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png")
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("N", "Non-binary"),
            ("O", "Other"),
        ],
        blank=True,
        null=True,  # ← виправлено з null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # ← виправлено назву поля
    is_verified = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"