user_id = input('Please enther id code: ')
if len(user_id) != 11:
    if len(user_id) > 11:
        print('Code is too long')
    else:
        print('Code is too short')
else:
    if user_id.isdigit():
        print(f'Your ID is {user_id}')
    else:
        print('Invalid id')


#x = 'Hello world'
#if ' world' in x:
    #print('Greater than 100')
#elif x == 150:
   # print('x is 150')



#user_input = input('Please choose:')
#if user_input == '1':
    #print ('1')
#elif user_input == '2':
   # print ('2')
   # elif user_input != '3':
   # print('3')
#else:
   # print('Hello world')
#x = 150

#if x == 100: # если здесь тру. То дальше смотреть не будет
    #print('Greater than 100')
#elif x == 150: # разные условия в случае False первого оператора
   # print('X is 150')
#elif x != 150:
    #print('x is not 150')

#else:
   # print('Ure fucked')



#name = 'john'
#surname = 'smith'
#age = 30
#price = 500


#result = f'Price is {}.' # f вначале - как форматированная строка
#result = f'Hello {name.capitalize()} {surname.capitalize()} . You are {age} years old. Your salary is {price:.2f}$'
#print(result)


#result = 'Prise is {:.2f}.' # :.2f поставит 2 нуля после точки 3f - 3 4f - 4
#print(result.format(price))

#print(round(1.5))
#print(round(2.5))
#print(round(3.5))

#result = '{user_name:} {user_surname:} is {user_age:} years old' # старый метод #
#print(result.format(user_age=age, user_surname=surname, user_name=name)) # старый метод

#result = '{} {} is {} years old' # {} внутри можно проставить индексы {1} {0} {2}
#print(result.format(name, surname, age)) # {} при использовании формата - нужно задать аргумент в format ()

#string_sample = "Hello world world"
#string_sample2 = "first letteR is lowErcase"
#string_sample3 = " extra whitespace string "
#german_sample = "der Fluß"

#print(string_sample2.upper())
#print(string_sample2.isupper())
#print(german_sample.lower())
#print(german_sample.islower())
#print(german_sample.casefold())

#a = 'Hello'
#b = 'World'
#c = a + b
#print()
#print(a, b)
#print(c)

#x, y = input('Please enter Name and Surname').split(' ')
#print(x)
#print(y)
#x = 'hello wo r ld'.split('el')
#print(x)

#print(string_sample.find('world', 7)) # находит на каком индексе начинается слово

#print(string_sample.count('w')) # считает сколько подстрока появляется внутри строки. любые символы

#print(string_sample.replace('world', 'planet').replace('Hello', 'Bumbas').upper()) # замена слова на другое

#print(string_sample2.capitalize()) # первая буква большая
#print(string_sample2.title()) #все слова с большой буквы
#print(string_sample2 == string_sample2.lower())
#print(string_sample3.strip()) # убирает пробелы
#print(string_sample3.lstrip()) # левый пробел убирает
#print(string_sample3.rstrip()) # убирает правый пробел
#user_name = input().title()

#user_entry = input().lower() # всё записывается маленькими буквами

#print('world' in string_sample)

#print(string_sample[-5:])
#print(string_sample[0:100])
#print(string_sample[0:10:4])
#print(string_sample[::-2])
#print(string_sample[5:len(string_sample)]) # лен - возвращает назад
