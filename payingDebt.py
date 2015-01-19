"""paying-debt-off-in-a-year
calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months."""

import time
start_time = time.clock()       #begining of calculating seconds till end of calculating
balance = 3329	#original credit card balance
initialBalance = balance	#assigning balance to cosntant initialBalance 
annualInterestRate = 0.2	#constant annualInterestRate for each month
monthlyPayment = 10		#begining value for monthlyPayment
monthlyInterestRate = annualInterestRate / 12.0		#constant monthlyInterestRate
totalPaid = 0.0
count = 1		#for the begining of loop
ans = 0			#final answer for the lowest payment
interest = (monthlyInterestRate * balance)	#interest for each month

while True:		#loop true until remainingBalance <= 0
    for count in range(0, 12):		#calculate (remainingBalance & totalPaid) after one year
        monthlyUnpBalance = balance - monthlyPayment		#unpaid balance after each month
        interest = (monthlyInterestRate * monthlyUnpBalance)	#interest after each month
        remainingBalance = monthlyUnpBalance + interest		#remainingBalance after each month
        balance = remainingBalance		#let the remaining balance is the new balance for next month
        totalPaid = totalPaid + monthlyPayment		#totalPaid of the whole month

    if remainingBalance > 0:		#if remainingBalance > 0 
        balance = initialBalance	#assign remaining balance to original balance
        monthlyPayment += 10		#and change monthlyPayment by 10$ then checking remaining balance again
        
    else:				#if remainingBalance <= 0
        ans = monthlyPayment		#assign monthlyPayment to answer
        break				#end looping and print the 

print 'Total Paid: ' + str(totalPaid)
print 'Lowest Payment: ' + str(ans)
print time.clock() - start_time, ' seconds'
