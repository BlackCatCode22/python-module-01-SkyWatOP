import time

def main():

    t = time.localtime()
    cur = int(time.strftime( "%H", t))

    name = input("What is your name?: ")

    # if time is less than 12 then it is morning,
    if cur < 12:
        print("Good morning, "+name)
    # if time is between 12 and 18 it is afternoon
    elif 12 <= cur < 18:
        print("Good afternoon, "+name)
    # if time is greater than 18 it is night
    elif cur > 18:
        print("Good evening, "+name)

main()