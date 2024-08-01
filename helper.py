import random
import string


def get_random_name():
    return random.choice(string.ascii_uppercase) + ''.join(
        random.choices(string.ascii_lowercase, k=random.randint(3, 10)))


def get_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(6, 20)))


def get_random_email():
    domains = ['mail.ru', 'gmail.com', ' yandex.ru', '@vk.com', '@bk.ru', '@inbox.ru', '@list.ru', '@internet.ru',
               '@rambler.ru', '@outlook.com', '@yahoo.com', '@mailfence.com']

    email = ''.join(random.choices(string.ascii_lowercase + '._', k=random.randint(6, 20))) + str(
        random.randint(0, 9999)) + random.choice(domains)

    return email
