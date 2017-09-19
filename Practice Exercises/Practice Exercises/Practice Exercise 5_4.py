import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
hardloper = input('Wat is je naam?')

infile = open('hardlopers.txt','a')
invoer = infile.write('{}, {}\n'.format(s, hardloper))
infile.close()


