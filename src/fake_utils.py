from datetime import datetime
from faker import Faker
from random import Random
from src.handlers import add_contact, add_note

fake = Faker()
random = Random()


def create_fake_contacts():
    names = [fake.unique.first_name() for i in range(300)]
    for i in range(300):
        name = names[i]
        phone = str(random.randint(1, 9999999999)).rjust(10, '0')
        birthday = str(fake.date_between_dates(date_start=datetime(
            1980, 1, 1), date_end=datetime(2005, 12, 31)).strftime('%d.%m.%Y'))
        email = fake.email()
        print(add_contact(name, phone, email, birthday))


def create_fake_notes():
    for _ in range(100):
        title = fake.unique.text(max_nb_chars=20)
        content = fake.paragraph(nb_sentences=5)
        tags = ' '.join(fake.words())
        print(add_note([title, content, tags]))


if __name__ == "__main__":
    create_fake_contacts()
    create_fake_notes()
