from django.db import models
from courses.models import Subcategory
from django.contrib.auth.models import User, Group


class SubcategoryRoles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    role_type = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)