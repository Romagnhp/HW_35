import cgi

print("Content-type: text/html")
print()


form = cgi.FieldStorage()
print("Пользователь с указанным логином отсутствует")

# with open ('userList.txt', 'r', encoding='utf') as file:
#     data = file.readlines()
    
    # if form['login'].value in data:
    #     print('<p>login', form['login'].value)
    # else:
    #     print("Пользователь с указанным логином отсутствует")