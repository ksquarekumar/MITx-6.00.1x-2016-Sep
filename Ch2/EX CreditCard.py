import math as m

balance = float(input("Starting Loan ",))
annualInterestRate = float(input("Annual Rate % ",))/100
monthlyInterestRate = annualInterestRate/12
blc =1.0
lbal = balance / 20
ubal = balance / 10
payment = (ubal + lbal) / 2

def balcheck(balance, payment, monthlyInterestRate):
    for i in range (0,12,1):
        balance -= payment
        balance += balance*monthlyInterestRate
    return round(balance,2)


while (abs(blc) > 0.1):
    blc = balcheck(balance,payment, monthlyInterestRate)
    print(blc)
    if blc > 0:
        lbal = payment
        payment = (ubal + lbal) / 2
    elif blc < 0:
        ubal = payment
        payment = (ubal + lbal) / 2

print("Lowest Payment: "+str(round(payment,2)))
print("balance for " + str(payment)+ ":" + str(balcheck(balance,payment,monthlyInterestRate)))




