from django.db import models
from datetime import datetime, date
import random
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

def get_date_20_years_ago():

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    return date(year - 20, month, day)

class MyUser(AbstractUser):

    
    USER_TYPES = [
        ('SU', 'superuser'),
        ('CS', 'customer support'),
        ('CU', 'customer user'),
        ('QA', 'quality assurance')
    ]

    type = models.CharField(
        max_length=2,
        choices=USER_TYPES,
        default='CU'
    )

    date_of_birth = models.DateField(default=get_date_20_years_ago())  # default is 20 years old

    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)

    some_file = models.FileField(upload_to='uploaded_files', blank=True, null=True)

    gets_discount = models.BooleanField(default=False)

    def has_delete_permission(self):
        # return self.is_superuser_or_customer_service()
        return self.is_superuser_or_staff()

    def execute_after_login(self):
        user_gets_randomly_selected_for_discount = random.choice([True, False])

        if user_gets_randomly_selected_for_discount:
            self.gets_discount = True
            self.save()

    def has_birthday_today(self):
        now = datetime.now()
        today_month = now.month
        today_day = now.day

        users_birth_month = self.date_of_birth.month
        users_birth_day = self.date_of_birth.day

        its_the_users_birthday = users_birth_month == today_month and users_birth_day == today_day

        return its_the_users_birthday
    

    def is_superuser_or_customer_support(self):
        if self.type == 'SU' or self.type == 'CS':
            return True
        else:
            return False # TODO: simplify as other method?

    def is_superuser_or_staff(self):
        return self.is_superuser or self.is_staff

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({str(self.date_of_birth)})'
