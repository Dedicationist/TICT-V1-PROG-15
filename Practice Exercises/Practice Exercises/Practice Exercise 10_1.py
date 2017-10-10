import xmltodict

with open('PE10_1.xml') as MyXMLFile:
    info = xmltodict.parse(MyXMLFile.read())
    regels = info['artikelen']
    for artikel in regels['artikel']:
        print(artikel['naam'])
