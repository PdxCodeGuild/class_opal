from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# post form
class Post(models.Model):
    content = models.TextField(max_length=128)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        ordering = ("-id",)
