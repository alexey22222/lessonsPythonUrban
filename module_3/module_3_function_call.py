import re
def is_valid_email(email):
    string_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.((([c][o][m])?)|(([r][u])?)|'
                              r'(([n][e][t])?))?)')
    if re.fullmatch(string_regex,email):
        return True
    else:
        return False
def send_email(message, recipient, *, sender="university.help@gmail.net"):
    if not(is_valid_email(recipient)) or not(is_valid_email(sender)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.net':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

