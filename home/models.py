from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institute = models.CharField(max_length=150, blank=False,null=False)
    course = models.CharField(max_length=150, blank=False,null=False)
    subject = models.CharField(max_length=150, blank=False,null=False)
    startingDate = models.DateField(null=False, blank=False)
    endingDate = models.DateField(null=False, blank=False)
    sex = models.CharField(max_length=10, blank=False, null=False)
    fullAddress = models.CharField(max_length=150, blank=False,null=False)
    city = models.CharField(max_length=150, blank=False,null=False)
    state = models.CharField(max_length=150, blank=False,null=False)
    zip = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

    
    


