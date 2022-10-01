# leap year
year = int(input("enter your year for checking leap year "))

if year%400==0 :
    print('its leap year')
elif year %200==0 :
    print('its leap year')
elif year %4==0 :
    print("its a leap year")

else :
    print("its not leap year")
