import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'one.settings')

import django

django.setup()

import random
from one_app.models import Topic, AccessRecord, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Game', 'Social', 'News', 'Tech', 'Weather']


def foo():
    return 'bar'

def add_topi():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    numbers = N
    for entry in range(N):
        top = add_topi()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_id = random.randint(0, N)

        Wbpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name, defaults=foo)[
            0]
        acc_rec = AccessRecord.objects.get_or_create(name=Wbpage, date=fake_date, defaults=foo)[0]


if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print("populating done")
