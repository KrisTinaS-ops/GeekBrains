import re


def email_parse(email):
    RE_GET_PARSER = re.compile(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+')
    if not RE_GET_PARSER.match(email):
        raise ValueError(f'Неверный e-mail: {email}')
    else:
        email_vocab = {}
        E_MAIL = re.compile(r'[a-zA-Z0-9_-]+')
        e_mail = E_MAIL.match(email).group()
        email_vocab['username'] = e_mail
        DOMAIN = re.compile(r'[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+')
        domain_name = DOMAIN.search(email).group()
        email_vocab['domain'] = domain_name
        return (email_vocab)


print(email_parse(input('Введите e-mail: ')))
