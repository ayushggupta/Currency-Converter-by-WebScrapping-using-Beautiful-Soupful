import bs4
import requests
res= requests.get('https://www.x-rates.com/table/?from=USD&amount=1')
import lxml
import pandas as pd
bsoup=bs4.BeautifulSoup(res.text,'html')
table_required= bsoup.find("table",{"class":"tablesorter ratesTable"})
import csv
with open('mycsv.xlsx','w',newline='') as f:
    thewriter =csv.writer(f)
        thewriter.writerow(['currency_of_country','in_1_USD'])
    
    for move in table_required.findAll('tbody'):
        listnew=[]
        for row in move.findAll('tr'):
            inside_list=[]
            currency_of_country=row.td.text
            cell2=row.findAll("td",{"class":"rtRates"})[0].text
            inside_list.append(currency_of_country)
            inside_list.append(cell2)
            listnew.append(inside_list)
    for x in listnew:
        thewriter.writerow(x)
    
    
    

with open('mycsv.xlsx','r',newline='') as f:
    lines =f.readlines()
    def Convert(lst): 
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
        return res_dct 
    c={}
    for list in listnew:
        d=Convert(list)
        c.update(d)
    amount= int(input("Enter Amount : \n"))
    print("Enter the name of currency you want to convert this amount to ? Available Options:\ n")
    [print(item)for item in c.keys()]
    currency_to_convert= input('\nEnter the currency to be converted\n')
    currency_in_which_to_convert= input("\nEnter the currency in which it to get coverted \n")
    temp_1=float(c[currency_to_convert])
    temp=float(c[currency_in_which_to_convert])
    print(amount ,currency_to_convert," in ",currency_in_which_to_convert,' = ',temp*amount/temp_1)
  
