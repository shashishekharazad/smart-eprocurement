from django.db import models

class administrater(models.Model):

    Admin_Name = models.CharField(max_length=200,default=0)
    Admin_Email = models.EmailField(max_length=200, default=0)
    Admin_Mobile = models.CharField(max_length=500,default=0)
    Admin_Password = models.CharField(max_length=500,default=0)

    @staticmethod
    def get_user_by_email(Admin_Email):
        try:
            return User.objects.get(Admin_Email=Admin_Email)
        except:
            return False