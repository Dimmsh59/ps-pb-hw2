pass_test = 8
pass_in = input('Введите пароль: ')

try:
    pass_check = (pass_test / len(pass_in)) / int(pass_in) * (pass_in)
    
except ValueError:
    print('Требования к паролю соблюдены, пароль: ' + str(pass_in))

except ZeroDivisionError:
     print('Вы ввели пустой пароль')

except TypeError:
    print('Ваш пароль состоит только из цифр')   

except Exception:
    print("Неопознанная ошибка")

print("Завершение программы")
