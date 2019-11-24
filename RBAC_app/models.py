#from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _



READ = 1
READ_AND_APPEND = 2
APPEND_AND_WRITE = 3
WRITE_AND_DELETE = 4

ACCESS_CHOICES= (
    (READ, _('Read')),
    (READ_AND_APPEND, _('Append')),
    (APPEND_AND_WRITE, _('Write')),
    (WRITE_AND_DELETE, _('Delete')),
)

class User(models.Model):
    username = models.CharField(max_length=100,unique=True)
    user_id = models.CharField(max_length=5,unique=True)
    mail_id = models.EmailField(unique=True)
    def __str__(self):
        return self.username + ' ' +self.mail_id


class Resources(models.Model):
    resourceName = models.CharField(max_length = 250)
    accessLevel = models.PositiveSmallIntegerField(
        choices=ACCESS_CHOICES, 
        default=READ
    )

    
    #accessLevel = models.IntegerField(default =0,validators=[MinValueValidator(0), MaxValueValidator(3)])
'''
class RoleMaster(models.Model):
    roleType = models.CharField(max_length = 50)
    accessLevel = models.PositiveSmallIntegerField(
        choices=ACCESS_CHOICES, 
        default=READ
    )
    accessLevel = models.IntegerField(default =0,validators=[MinValueValidator(0), MaxValueValidator(3)])'''

class Role_id(models.Model):
    user_id = models.CharField(max_length=5,unique=True)
    accessLevel = models.PositiveSmallIntegerField(
        choices=ACCESS_CHOICES, 
        default=READ
    )

    

    #accessLevel = models.IntegerField(default =0,validators=[MinValueValidator(0), MaxValueValidator(3)])


