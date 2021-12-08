import requests
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

t = [0]
p = [0]

dag = dt.datetime.now().strftime("%Y%m%d")

tokenkey = '65d38477-fb71-4328-a1a1-7340ba39b2af'
omraade  = '10YNO-3--------J' # Alesund,Molde,Trondheim
#10YNO-1--------2
#10YNO-2--------T
#10YNO-4--------9

# Fetch price of EUR in NOK
def geteurnok():
    url_nb = 'https://data.norges-bank.no/api/data/EXR/M.EUR.NOK.SP?lastNObservations=1'
    eurnok = str(requests.Session().get(url=url_nb).text)
    outeur = eurnok.split('OBS_VALUE="')[1].split('"/></S')[0]
    eurprice = (100/(float(outeur)))
    return eurprice

# Fetch todays energy price in EUR
def getentsoe():
    url_entso = 'https://transparency.entsoe.eu/api?documentType=A44&in_Domain='+omraade+'&out_Domain='+omraade+'&periodStart='+dag+'0000&periodEnd='+dag+'2300&securityToken='+tokenkey
    ele = str(requests.Session().get(url=url_entso).text)
    klipp = ele.split("<Period>")[1].split("</Period>")[0]
    return klipp

# Create a nice plot with prices, one bar pr price 
def lagplot():
    global t,p
    y_pos = np.arange(len(t))
    plt.bar(t, p)
    plt.xticks(y_pos, t)
    plt.title("Energipris")
    plt.ylabel('Pris i NOK', labelpad=15, color='#333333')
    plt.xlabel('Klokkeslett', labelpad=15, color='#333333')
    plt.show()

eur = geteurnok()
print(eur)
epris = getentsoe()
#print(epris)

# Create list of NOK prices in p and a list of hours of day in t
i = 1
while i<24: 
    output = epris.split("<position>"+str(i))[1].split("</price.amount>")[0]
    pris = float(output.split("<price.amount>")[1].split("</price.amount>")[0])
    p.append(pris*eur/1000)
    t.append(i)
    i = i+1
    
#lagplot()