agencies = {'CCC':'Civilian Conservation Corps', 'FCC':'Federal Communications Comission', 'FDIC':'Federal Deposit Insurance Corporation', 'SSB':'Social Security Board', 'WPA':'Works Progress Administration'}
print(agencies)
agencies['SEC'] = 'Securities and Exchange Comission'
print(agencies)
agencies['SSB'] = 'Social Security Administration'
print(agencies)
agencies.pop('CCC')
agencies.pop('WPA')
print(agencies)
