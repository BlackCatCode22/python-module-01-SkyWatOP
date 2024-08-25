def main():

    # ask user for hourly rate and pay
    hourlyPay = float(input("What is your hourly pay?: "))
    hours = float(input("How many hours did you work?: "))
    pay = 0

    if hours > 40:
        over = hours - 40
        over = over * 1.5 * hourlyPay
        pay = (hourlyPay * 40) + over
        print("Your overtime pay is: " +str(over))
        print("Your overall gross pay is " +str(pay))

    else:
        pay = hourlyPay * hours
        print("Your overall gross pay is " +str(pay))

main()