clientName = input("")
clientAge = int(input(""))
clientMonthlyIncome = float(input(""))

if clientAge <= 25:
    maximumLoanAmount = clientMonthlyIncome * 0.5
    print(f"{maximumLoanAmount:.2f}")
else:
    if(clientAge <= 35):
        maximumLoanAmount = clientMonthlyIncome * 0.75
        print(f"{maximumLoanAmount:.2f}")
    else:
        if(clientAge <= 45):
            maximumLoanAmount = clientMonthlyIncome * 1.00
            print(f"{maximumLoanAmount:.2f}")
        else:
            print("contatar gerente")