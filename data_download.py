import requests
import csv
response = requests.get('https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=S4&ps=2018, 2017, 2016, 2015, 2014&r=498&p=all&rg=all&cc=AG1&uitoken=74aec4a8cf3b14ceaeb1915c0252305b&fmt=csv')
response_2 = requests.get('https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=S4&ps=2013, 2012, 2011, 2010, 2009&r=498&p=all&rg=all&cc=AG1&uitoken=74aec4a8cf3b14ceaeb1915c0252305b&fmt=csv')
with open('comtrade_data.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow
        writer.writerow(line.decode('utf-8').split(','))
    
    for line in response_2.iter_lines():
        writer.writerow
        writer.writerow(line.decode('utf-8').split(','))