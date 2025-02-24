import pandas as pd
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
df=pd.read_excel("C:\\Users\\DIMPLE K B\\Documents\\Book1.xlsx",parse_dates=["date"])

#the best month to offer discount

df["date"]=pd.to_datetime(df["date"],format="mixed")
df["Month"]=df["date"].dt.strftime("%Y-%m")
monthly_sales=df.groupby("Month")["amount"].sum().reset_index()

min_sales_value = monthly_sales["amount"].min()
min_sales_month=monthly_sales[monthly_sales["amount"]==min_sales_value]["Month"].tolist()
print(f"the best month to offer discount is : {min_sales_month}")



#the best month when we can bring surchange 

max_sales_value = monthly_sales["amount"].max()
max_sales_month=monthly_sales[monthly_sales["amount"]==max_sales_value]["Month"].tolist()
print(f"the best month when we can bring surchange : {max_sales_month}")


#give a coupon to the valuable customer who did not turn up since over 2 months

customer_spending=df.groupby("customer")["amount"].sum().reset_index()
valuable_customer=customer_spending[customer_spending["amount"]>=customer_spending["amount"].quantile(0.75)]
last_visit=df.groupby("customer")["date"].max().reset_index()
valuable_last_visit=pd.merge(valuable_customer,last_visit,on="customer")
cutoff_date=datetime.today()-timedelta(days=30)
customer_for_coupon=valuable_last_visit[valuable_last_visit["date"]<cutoff_date]
if not customer_for_coupon.empty:
    print("customer eligible for a coupon:")
    for index,row in customer_for_coupon.iterrows():
        print(f"customer {row['customer']} (last visit : {row['date'].date()}, total spend:{row['amount']})-coupon awarded")
else:
    print("no valuable customer have been inactive for over 2 months.")
    
    
#display the monthly sales of a year

plt.figure(figsize=(10,6))
bars=plt.bar(monthly_sales["Month"],monthly_sales["amount"],color="blue",alpha=0.7,label="sales per month")
for bar,month,sales in zip(bars,monthly_sales["Month"],monthly_sales["amount"]):
    if sales==min_sales_value:
        bar.set_color("red")
    elif sales==max_sales_value:
        bar.set_color("green")
plt.xlabel("Month")
plt.ylabel("total sales")
plt.title("monthly sales trend")
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.legend()
plt.show()

#divide the day into 4 parts and display the sales using pie chart

def get_time_slot(hour):
    if 6<= hour < 12:
        return "Morning"
    elif 12<=hour<18:
        return "Afternoon"
    elif 18<=hour<24:
        return "Evening"
    else:
        return "Night"

df["time slot"]=df["date"].dt.hour.apply(get_time_slot)
time_slot_sales=df.groupby("time slot")["amount"].sum()
plt.figure(figsize=(8,8))
colors=['gold','lightcoral','lightskyblue','lightgreen']
plt.pie(time_slot_sales,labels=time_slot_sales.index,autopct="%1.1f%%",colors=colors,startangle=90)
plt.title("sales distribution by time of day")
plt.show()