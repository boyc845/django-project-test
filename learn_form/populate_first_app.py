import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_form.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        #create the fake data for that entry
        fake_lastName = fakegen.name()
        fake_firstName = fakegen.name()
        fake_email = fakegen.email()

        #create the new webpage entry
        webpg = User.objects.get_or_create(lastName=fake_lastName,firstName=fake_firstName,email=fake_email)[0]

        print(webpg)


if __name__ == '__main__':
    print("populating script!")
    populate(5)
    print("populating complete!")
