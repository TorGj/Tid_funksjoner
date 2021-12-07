import datetime as dt

yyyy = int(input('Hvilket år? '))
mnd = int(input('Hvilken måned nr? '))
dag = int(input('Hvilken dag? '))
hour = int(input('Hvilken timenr (24h)? '))
minutt = int(input('Hvilket minutt? '))
sek = int(input('Hvilket sekund? '))

x = dt.datetime(yyyy, mnd, dag, hour, minutt, sek)
print('Du la inn:',x)

y = dt.datetime.now()
print('Standard format:',y)
print('Forskjell:', x-y)
print('År:',y.year,
      'Ukedag:', y.strftime("%A"),
      'Måned:' , y.strftime("%B"),
      'Uke nr:', y.strftime("%W"),
      'Dag nr:', y.strftime("%j")) 

z = dt.timedelta(days = 1, hours= 2, minutes=3, seconds=4)
print('Nå + tidsforskjell:',y+z)

