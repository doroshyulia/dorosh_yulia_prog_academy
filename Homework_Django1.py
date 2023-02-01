# Завдання №1
print('1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R, за якою \n'
      'слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр')
import re

txt = 'Rbbr'
x = re.search(r'^Rb+r$', txt)
print(txt)
print(x)


# Завдання №2
print('2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).')


def validate_card_number(card_number):
  regex = re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}')
  if regex.match(card_number):
    return True
  else:
    return False

print(validate_card_number('9999-9999-9999-9999'))
print(validate_card_number('9999-9999-9999-99'))
print(validate_card_number('9999-9999--9999-9999'))

# Завдання №3
print('3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.\n'
      'Вимоги: \n'
      '- Цифри (0-9). \n'
      '- лише латинські літери у великому (A-Z) та малому (a-z) регістрах. \n'
      '- у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу. \n'
      '- Символ "-" не може повторюватися.')

def check_email(email):
    regex = r'^[0-9a-zA-Z]([\w\.]-?){1,63}@[0-9a-zA-Z]([\w\.]-?){1,63}$'
    search = re.search(regex, email)
    if search:
        return True
    else:
        return False

print(check_email('yulia15@gmail.com'))
print(check_email(",yulia@yulia"))



# Завдання №4
print('4. Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що \n'
      'містить лише літери та цифри.')


def check_login(login):
  if re.match("^[a-zA-Z0-9]{2,10}$", login):
    return True
  else:
    return False

print(check_login('ivan123'))
print(check_login('iiiivaaaaaan123'))
print(check_login('ivan1_23'))