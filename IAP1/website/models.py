from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager

# class register(AbstractBaseUser):
# 	objects=UserManager()
# 	name=models.CharField(max_length=50)
# 	emailid=models.EmailField(max_length=70,blank=True, null= True)
# 	password=models.CharField(max_length=11)
# 	USERNAME_FIELD='emailid'
# 	REQUIRED_FIELDS=['password']


class register(models.Model):
	objects=UserManager()
	name=models.CharField(max_length=5000)
	emailid=models.EmailField(max_length=70)
	password=models.CharField(max_length=700)
	# USERNAME_FIELD='emailid'
	# REQUIRED_FIELDS=['password']

	def __str__(self):
		return self.name
		
		