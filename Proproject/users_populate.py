import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Proproject.settings')

import django
django.setup()

import random
from appTwo.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.free_email()

        user = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email = fake_email)

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
