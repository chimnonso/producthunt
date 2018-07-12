import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','producthunt.settings')

import django
django.setup()

import random
from products.models import User
from faker import Faker

fakegen = Faker()

def pop_user(N=10):
    
    for i, entry in enumerate(range(N)):

        user_name = fakegen.first_name_female().lower()
        pword = 'foobar'
        mail = fakegen.email()
        # user = Person(first_name=first, last_name=last, email=mail)
        if User.objects.filter(username=user_name):
            user_name += str(i)
        user = User.objects.create_user(username=user_name, email=mail, password=pword)
        user.save()




if __name__ == '__main__':
    print("-----------------------Populating user_db------------------")
    pop_user()
    print("Done populating the user_db")