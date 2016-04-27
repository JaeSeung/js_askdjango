from __future__ import unicode_literals
import re
from django.core.validators import RegexValidator
#from django.contrib.auth.models import User
from django.db import models


phone_number_validator = RegexValidator(r'^01[016789][1-9]\d{6,7}$', message ='please enter phone_number')
def ktf_validator(phone_number):
    phone_number = re.findall(r'\d+', phone_number)
    if phone_number[2] != '6':
        raise ValidationError('ktf ')

class PhoneNumberField(models.CharField):
   def __init__(self, *args, **kwargs):
    # 
       kwargs.setdefault('max_length', 20)
       kwargs.setdefault('validators',[])
       kwargs['validators'].append(phone_number_validator)
       super(PhoneNumberField, self).__init__(*args, **kwargs)
       #qnahrk gownsmsdlfdmf rmeofh gownjdiehla.
       #sorkgkfdlf gkrh qnahrkgkfdlf gkrh


# Create your models here.

class Profile(models.Model):
    #user = models.OneToOneField(User)
    user = models.OneToOneField('auth.User')
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
