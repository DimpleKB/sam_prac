import numpy as np
week_spendings=np.array([150,120,30,40,200,90,300])
highest_spending=week_spendings[0]
index=1
for i in range(len(week_spendings)):
    if week_spendings[i]>highest_spending:
        highest_spending=week_spendings[i]
        index=i
days={1:'mon',2:'tue',3:'wed',4:'thurs',5:'fri',6:'sat',7:'sun'}
print(highest_spending,days[index])