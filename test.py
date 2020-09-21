import pandas as pd 

investment = pd.read_csv("./investment.csv") 

budget = pd.read_csv("./Budget.csv")
#print(budget)

budget.isnull() # to check if there are  null values 

budget.fillna(value='NO',inplace=True) # replacing null values with "NO"
#print(budget)



# now converting date to datetime format 
investment['Date'] = pd.to_datetime(investment.Date)
#print(investment.head(3))

investment['Year'] = investment.Date.dt.year #  column for year
investment['Month'] = investment.Date.dt.month # column for month 
investment['Day'] = investment.Date.dt.day # column for day
#print(investment.head(3))

# Utility "for" loop for budget.csv

for i,j in budget.iterrows():
    if (j['Sector']=='NO') and (j['Time Period']=='month'):
        amount = j['Amount']
    elif j['Sector']=='E-commerce' and j['Time Period']=='year':
        e_amount = j['Amount']
    elif j['Sector']=='Fintech' and j['Time Period']=='NO':
        f_amount = j['Amount']


# we can also have a utility 'for' loop for investment.csv but as data is small and for better understanding
#-- used seprate loops.

f_amt = 0
for x,y in investment.iterrows():
    if y['Sector']=='Fintech':
        f_amt = y['Amount'] + f_amt
        if f_amt > f_amount:
            break
print(y['ID'])         


 
month = 0
amnt=0
for x,y in investment.iterrows():
    if y['Sector']=='SaaS':
        month = y['Month'] - month
        amnt = y['Amount'] + amnt
        if month==0 and amnt > amount:
            break
print(y['ID'])            


year = 0
e_amnt = 0
for x,y in investment.iterrows():
    if y['Sector']=='E-commerce':
        year = y['Month'] - month
        e_amnt = y['Amount'] + e_amnt
        if year==0 and amnt > e_amount:
            break
print(y['ID'])            


        