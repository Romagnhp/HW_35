import cgi
import re
import json

print("Content-type: text/html")
print()

formRegistation = cgi.FieldStorage()

login = formRegistation['login'].value
password = formRegistation['password'].value
repeatPasword = formRegistation['repeatPasword'].value

tempJson = None

if password == repeatPasword and re.findall("[0-9A-Za-z]", password) and re.findall("[0-9A-Za-z]", login):
    print("Регистрация успешно завершина")

    with open('cgi-bin/usersList.json', 'r+') as file2:
        tempJson = json.load(file2)
    with open('cgi-bin/usersList.json', 'w+') as file2:
        tempJson[login] = password
        json.dump(tempJson, file2)
else:
    print("Не корректные данные")