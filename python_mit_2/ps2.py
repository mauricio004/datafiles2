def paytheminimum(balance, annualInterestRate, monthlyPaymentRate):
    monthlyRate = annualInterestRate / 12.0
    payment = balance * monthlyPaymentRate
    unpaidBalance = balance - payment
    totalPaid = 0.0
    for i in range(1, 13):
        payment = balance * monthlyPaymentRate
        unpaidBalance = balance - payment
        balance = unpaidBalance + (monthlyRate * unpaidBalance)
        print('Month: ' + str(i))
        print('Minimum monthly payment: ' + str(round(payment, 2)))
        print('Remaining balance: ' + str(round(balance, 2)))
        totalPaid += payment
    print('Total paid: ' + str(round(totalPaid, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))


def paytheminimum2(balance, annualInterestRate, monthlyPaymentRate):
    monthlyRate = annualInterestRate / 12.0
    remainingBalance = balance
    totalPaid = 0
    for i in range(1, 13):
        balance = remainingBalance
        payment = balance * monthlyPaymentRate
        unpaidBalance = balance - payment
        interest = unpaidBalance * monthlyRate
        remainingBalance = unpaidBalance + interest
        print('Month: ' + str(i))
        print('Minimum monthly payment: ' + str(round(payment, 2)))
        print('Remaining balance: ' + str(round(remainingBalance, 2)))
        totalPaid += payment
    print('Total paid: ' + str(round(totalPaid, 2)))
    print('Remaining balance: ' + str(round(remainingBalance, 2)))


def payingdebtinoneyear(balance, annualInterestRate):
    monthlyRate = annualInterestRate / 12.0
    remainingBalance = balance
    original_balance = balance
    payment = 0
    while remainingBalance > 0:
        balance = original_balance
        remainingBalance = balance
        payment += 10
        for i in range(1, 13):
            balance = remainingBalance
            unpaidBalance = balance - payment
            interest = unpaidBalance * monthlyRate
            remainingBalance = unpaidBalance + interest
    print('Lowest Payment: ' + str(payment))


def bisectionsearch(balance, annualInterestRate):
    monthlyRate = annualInterestRate / 12.0
    remainingBalance = balance
    original_balance = balance
    totalPaid = 0
    lower_bound = balance / 12.0
    upper_bound = (balance * (1 + monthlyRate) ** 12) / 12.0
    payment = (lower_bound + upper_bound) / 2.0
    while remainingBalance < -0.1 or remainingBalance > 0.1:
        print('Lower bound = ' + str(round(lower_bound, 2)) + ' Upper bound = ' + str(round(upper_bound, 2))
              + ' Payment = ' + str(round(payment, 2)))
        balance = original_balance
        remainingBalance = balance
        payment += 0.01
        for i in range(1, 13):
            balance = remainingBalance
            unpaidBalance = balance - payment
            interest = unpaidBalance * monthlyRate
            remainingBalance = unpaidBalance + interest
        remainingBalance = round(remainingBalance, 1)
        if remainingBalance < 0:
            upper_bound = payment
        else:
            lower_bound = payment
        payment = (lower_bound + upper_bound) / 2.0
    print('Lowest Payment: ' + str(payment))


def test():
    return


def main():
    ##paytheminimum2(4213, 0.2, 0.04)
    ##payingdebtinoneyear(4773, 0.2)
    bisectionsearch(320000, 0)
if __name__ == '__main__':
    main()