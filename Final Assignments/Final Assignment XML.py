import xmltodict

def processXML(filename):
    import xmltodict
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationsdict = processXML('FA XML.xml')
stations = stationsdict['Stations']

print('Dit zijn de codes en types van de 4 stations: ')
for station in stations['Station']:
    print('{:4} - {}'.format(station['Code'], station['Type']))

print()

print('Dit zijn alle stations met één of meer synoniemen: ')
for station in stations['Station']:
    if station['Synoniemen'] != None:
        print('{:4} - {}'.format(station['Code'], station['Synoniemen']))

print()

print('Dit is de lange naam van elk station: ')
for station in stations['Station']:
    namen = station['Namen']
    print('{:4} - {}'.format(station['Code'], namen['Lang']))


