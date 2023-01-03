import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cashBackNoPrime = 0.03 # CashBack amount in decimal form for no Amazon Prime
cashBackYesPrime = 0.05 # CashBack amount in decimal form with Amazon Prime
amazonPrimeCost = 16.23 # Cost of amazon prime monthly with tax
amazonYearlyPrimeCost = 12.54 # Cost of amazon prime per month with taxif you bought the year plan
amazonStudentMonthlyPrimeCost = 8.11 # Cost of amazon prime monthly with tax as a student
amazonStudentYearlyPrimeCost = 6.23 # Cost of amazon prime per month with tax if you bought the year plan as a student.

#Function for defining the equation to calculate cash back.
def AmazonCashBack(moneySpent, cashBack, primeCost):
    return ((moneySpent * cashBack) - primeCost)

# Function to calculate the intercept of two linear lines
def calculateIntercept(a,b,c1,c2):
    return ((c1 - c2) / (a - b))

cashSpentList = np.arange(0,20001,1) #Total Money Spent

# Line equation for no amazon prime with a 3 % card
noPrimeCashBack = AmazonCashBack(cashSpentList,cashBackNoPrime, 0)
# Line equation for paying Amazon Prime with Amazon's 5% cash back card
yesPrimeCashBack = AmazonCashBack(cashSpentList, cashBackYesPrime, amazonPrimeCost)
# Line equation for paying Amazon Prime Yearly plan with Amazon's 5% cash back card
yesPrimeCashBackYearly = AmazonCashBack(cashSpentList, cashBackYesPrime, amazonYearlyPrimeCost)
# Line equation for paying Amazon Prime Monthly plan as a student with Amazon's 5% cash back card
yesPrimeCashBackMonthlyStudent = AmazonCashBack(cashSpentList, cashBackYesPrime, amazonStudentMonthlyPrimeCost)
# Line equation for paying Amazon Prime Yearly plan as a student with Amazon's 5% cash back card
yesPrimeCashBackYearlyStudent = AmazonCashBack(cashSpentList, cashBackYesPrime, amazonStudentYearlyPrimeCost)

# Calculate the intercept of the two points, x and y value, of monthly Prime cashback and 3% cashback
xinterceptValue = round(calculateIntercept(cashBackNoPrime,cashBackYesPrime,0,amazonPrimeCost),2)
yinterceptValue = AmazonCashBack(xinterceptValue,cashBackNoPrime, 0)
# Calculate the intercept of the two points, x and y value, of Yealy Prime cashback and 3% cashback
xinterceptValueYearly = round(calculateIntercept(cashBackNoPrime,cashBackYesPrime,0,amazonYearlyPrimeCost),2)
yinterceptValueYearly = AmazonCashBack(xinterceptValueYearly,cashBackNoPrime, 0)
# Calculate the intercept of the two points, x and y value, of monthly Prime cashback as a student and 3% cashback
xinterceptValueMonthlyStudent = round(calculateIntercept(cashBackNoPrime,cashBackYesPrime,0,amazonStudentMonthlyPrimeCost),2)
yinterceptValueMonthlyStudent = AmazonCashBack(xinterceptValueMonthlyStudent,cashBackNoPrime, 0)
# Calculate the intercept of the two points, x and y value, of Yealy Prime cashback as a student and 3% cashback
xinterceptValueYearlyStudent = round(calculateIntercept(cashBackNoPrime,cashBackYesPrime,0,amazonStudentYearlyPrimeCost),2)
yinterceptValueYearlyStudent = AmazonCashBack(xinterceptValueYearlyStudent,cashBackNoPrime, 0)

# Calculating the the upper limits of the graphs
upperxLimit = (round(xinterceptValue/5)*5)*1.5 # calculating an upper x axis limit
upperyLimit = (round(yinterceptValue/5)*5)*1.5 # calculating an upper y axis limit

# Generate graph 
plt.plot(cashSpentList,noPrimeCashBack,label="3% CashBack No Prime")
plt.plot(cashSpentList,yesPrimeCashBack,label="5% CashBack w/Prime Monthly")
plt.plot(cashSpentList,yesPrimeCashBackYearly,label="5% CashBack w/Prime Yearly")
plt.plot(cashSpentList,yesPrimeCashBackMonthlyStudent,label="5% CashBack w/Prime Monthly as a Student")
plt.plot(cashSpentList,yesPrimeCashBackYearlyStudent,label="5% CashBack w/Prime Yearly as a Student")
plt.plot(xinterceptValue,yinterceptValue,marker="o", markersize=5, markerfacecolor="green")#,label="Intercept Point")
plt.annotate(('$%.2f' % xinterceptValue), xy=(xinterceptValue, yinterceptValue), textcoords = "offset points", xytext=(10, -3), ha='left')
plt.plot(xinterceptValueYearly,yinterceptValueYearly,marker="o", markersize=5, markerfacecolor="pink",label="Yearly Intercept Point")
plt.annotate(('$%.2f' % xinterceptValueYearly), xy=(xinterceptValueYearly, yinterceptValueYearly), textcoords = "offset points", xytext=(10, -3), ha='left')
plt.plot(xinterceptValueMonthlyStudent,yinterceptValueMonthlyStudent,marker="o", markersize=5, markerfacecolor="darkgreen",label="Monthly Student Intercept Point")
plt.annotate(('$%.2f' % xinterceptValueMonthlyStudent), xy=(xinterceptValueMonthlyStudent, yinterceptValueMonthlyStudent), textcoords = "offset points", xytext=(10, -3), ha='left')
plt.plot(xinterceptValueYearlyStudent,yinterceptValueYearlyStudent,marker="o", markersize=5, markerfacecolor="lime",label="Yearly Student Intercept Point")
plt.annotate(('$%.2f' % xinterceptValueYearlyStudent), xy=(xinterceptValueYearlyStudent, yinterceptValueYearlyStudent), textcoords = "offset points", xytext=(10, -3), ha='left')
plt.title("Cashback")
plt.xlim(0,upperxLimit)
plt.xlabel("Money Spent ($)")
plt.ylim(0,upperyLimit)
plt.ylabel("Cash Back Earned ($)")
plt.legend()
plt.show()
