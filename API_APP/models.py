from django.db import models
state_choices=((
    ('Jaipur','Jaipur'),
    ('Kota','Kota'),
    ('Jodhpur','Jodhpur'),
    ('Nagaur','Nagaur')
               ))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    DOB = models.DateField(auto_now=False,auto_now_add=False)
    state = models.CharField(choices=state_choices, max_length=100)
    Gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

