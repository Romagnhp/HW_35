import cgi
import json

print("Content-type: text/html")
print()

form = cgi.FieldStorage()

temp = None 

with open ('cgi-bin/usersList.json', 'r+') as file1:
    tempJson = json.load(file1)

if form['login'].value in tempJson:

    if int(tempJson[form['login'].value]) == int(form['password'].value):
        print('Вход разрешен')
        print('<p>login', form['login'].value)
    else:
        print("пароль не соответствует указанному логину")
    
else:
    # print("Пользователь с указанным логином отсутствует")
    def creatureHtmlThurePython(fileName):
        with open ('cgi-bin/html_pages/' + fileName + '.html', 'r') as file:
            temp = file.readlines()
            for tempLine in temp:
                print(tempLine, end='')

    def assemblePage(namePage):
        creatureHtmlThurePython('start')
        creatureHtmlThurePython('header')
        creatureHtmlThurePython(namePage)
        creatureHtmlThurePython('footer')
        creatureHtmlThurePython('end')

    assemblePage('registrationForm')



