from django.db import models


from django.contrib.auth.models import User

# class Post(models.Model):
#     id=models.AutoField(primary_key=True)
#     post_title=models.CharField(max_length=255)
#     post_description=models.TextField()
#     created_at=models.DateField(auto_now_add=True)


# class UserProfile(User):
# 	phone=models.CharField(max_length=225)


# class userinformation(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_information')
# 	phonenumber = models.CharField(max_length=100)
# 	address = models.CharField(max_length=200)
# 	class Meta:
# 		verbose_name_plural = "User Information"
# 	def __str__(self):
# 		return str(self.user)+' - '+self.phonenumber+' - '+self.address


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=225)

