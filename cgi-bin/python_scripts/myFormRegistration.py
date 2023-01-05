import cgi

print("Content-type: text/html")
print()


formRegistation = cgi.FieldStorage()
if formRegistation['password'].value.isdigit():
    print("Регистрация успешно завершина")
else:
    print("Не корректные данные")