import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_column', None)
# Q1-1 Store	the	COVID19.csv	data	into	a	DataFrame	covid
covid = pd.read_csv('COVID19.CSV')

# Q1-2 Print the	dimensions	of	the	covid (number	of	rows	and	columns).
print(covid.shape)

# Q1-3 Print	a	summary	of	the	features,	number	of	non-null	samples	and	feature	types.
print(covid.info())

# Q1-4 Print	the	first	5	rows,	making	sure	to	display	all	the	columns.
print(covid.head())

# Q1-5 Print summary	statistics	(i.e.	count,	mean,	…	75%,	max).
print(covid.describe())

# Q1-6Print	a	list	of	the	columns	and	the	percentage	of	the rows	that	have	missing	values for	each column
print(covid.isnull().sum()/len(covid) * 100)

# Q2-1 What	are	the	total	number	of	confirmed	cases	of	coronavirus?
confirmed = covid['Confirmed'].sum()
print('Confirmed Cases:',str(confirmed))

# Q2-2 What	percentage	of	cases	of	coronavirus	have	resulted	in	deaths?
deaths = covid['Deaths'].sum()
print('Percentage of cases resulted in death:',str(deaths/confirmed * 100),"%")

# Q2-3 What	percentage	of	cases	of	coronavirus	have	resulted	in	recovery?
recovery = covid['Recovered']
print('Percentage of cases resulted in revcovery:',str(recovery/confirmed * 100),"%")

# Q2-4 How	many	countries	has	the	coronavirus	spread	to?
print('Number of countries the coronavirus has spread to:',str(len(covid.Country.unique())))

# Q2-5 Which	countries	have	suffered	deaths	due	to	the	coronavirus?
print('Countries suffered deaths:')
print(covid.Country[covid['Deaths']>0].unique())

# Q2-6 How	many	confirmed	cases	of	the	coronavirus	are	there	for	each	country,	from	greatest	to	least
countries = covid.groupby('Country').sum()['Confirmed']
print(countries.sort_values(ascending=False))


# Plot	the	number	of	coronavirus	related	deaths	and	recoveries	over	time.
fig = plt.figure()
covid = pd.read_csv('COVID19.CSV')

# Convert to datetime
covid['date'] = pd.to_datetime(covid['Date']).dt.normalize()

deaths = covid[['date','Deaths']].groupby('date').sum()
print(deaths)

plt.plot(deaths,c='k',linestyle='-', marker='o',label = 'Deaths')

recovery = covid[['date','Recovered']].groupby('date').sum()

plt.plot(recovery,c='g',linestyle='-', marker='o', label='Recoveries')

plt.title('Number of Coronavirus Deaths and Recoveries Over Time')
plt.grid()
plt.yticks(np.arange(0,12001,2000))
plt.xticks(['2020-01-22','2020-01-25','2020-01-29','2020-02-01','2020-02-04','2020-02-08','2020-02-11','2020-02-14','2020-02-17'])
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend(loc='upper left')

plt.show()


# Top 10 most affected countries besides china
fig = plt.figure()

country = covid[['Country','Confirmed']].groupby('Country').sum().sort_values(by='Confirmed',ascending=False)
top10 = country.iloc[1:11,:]
top10.reset_index(level=0, inplace=True)


plt.bar(top10.Country,top10.Confirmed, align='center',color='steelblue')
plt.grid()
plt.title('Top 10 Countries (Other Than China) Affected by Coronavirus')
plt.xlabel('Countries')
plt.ylabel('Number of Confirmed Cases')
plt.yticks(np.arange(0,2001,500))
plt.show()