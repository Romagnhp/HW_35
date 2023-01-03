import cgi

print("Content-type: text/html")
print()

def creatureHtmlThurePython(fileName):
    with open ('cgi-bin/' + fileName + '.html', 'r') as file:
        temp = file.readlines()
        for tempLine in temp:
            print(tempLine, end='')

def assemblePage(namePage):
    creatureHtmlThurePython('start')
    creatureHtmlThurePython('header')
    creatureHtmlThurePython(namePage)
    creatureHtmlThurePython('footer')
    creatureHtmlThurePython('end')

assemblePage('form')