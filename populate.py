import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','producthunt.settings')

import django
django.setup()

import random
from products.models import Product
# from django.contrib.auth.models import User
from accounts.models import User
from faker import Faker

fakegen = Faker()


def all_users():
    user_list = User.objects.values_list('username', flat=True)
    return user_list

my_user_list = all_users()

def get_user():
    u = User.objects.get(username=random.choice(my_user_list))
    return u

def populate(N=5):
    for i, entry in enumerate(range(N)):
        user = get_user()
        i += 1
        # user = User.objects.get(pk=1)

        fake_title = fakegen.company()
        fake_body = fakegen.paragraphs(nb=50, ext_word_list=None)
        new_fake_body = " ".join(fake_body)
        fake_image ='image/' + str(i) + '.jpg'
        fake_slug = fakegen.slug(fake_title)    

        product = Product.objects.get_or_create(
            title = fake_title,
            body = new_fake_body,
            image = fake_image,
            slug = fake_slug,
            hunter = user,
            domain = random.choice(Product.DOMAIN_CHOICES)[0]
        )[0]



if __name__ == '__main__':
    print('Start populating')
    print('---------------')
    populate(20)
    print('Done populating')