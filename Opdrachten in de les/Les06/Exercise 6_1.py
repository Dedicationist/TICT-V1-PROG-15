gewicht = eval(input('Hoeveel weeg je?'))
lengte = eval(input('Hoe lang ben je?'))
BMI = gewicht /(lengte/100)**2

if BMI < 18.5:
    print('Je hebt ondergewicht')
elif BMI >= 18.5 and BMI <= 25:
    print('Je hebt een normaal gewicht')
else:
    print('Je hebt overgewicht')
