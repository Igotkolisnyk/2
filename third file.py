time = int(input("enter the number of minutes:"))
if time < 0:
    print ("Eror, please enter correct time")
if time >= 0 and time <= 15:
    print ("firest quarter")
if time > 15 and time <= 30:
    print ("second quater")
if time > 30 and time <= 45:
    print ("third quater")
if time > 45 and time <= 60:
    print ("fourd quater")
if time > 60:
    print ("Eror, please enter correct time")
