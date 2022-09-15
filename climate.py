import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()
cursor.execute("SELECT years FROM ClimateData") 
result = cursor.fetchall() 
for r in result:
    years.append(r)

cursor.execute("SELECT co2 FROM ClimateData") 
result = cursor.fetchall() 
for r in result:
    co2.append(r)


cursor.execute("SELECT temp FROM ClimateData") 
result = cursor.fetchall() 
for r in result:
    temp.append(r)


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()



