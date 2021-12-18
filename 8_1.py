import re


def email_parse(email_address):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f'wrong email: {email_address}')
    print(re_email.match(email_address).groupdict())

email_list = ['someone@geekbrains.ru', 'som&eone@geekbrainsru', 'someone@geekbrainsru']

for i in email_list:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)
    