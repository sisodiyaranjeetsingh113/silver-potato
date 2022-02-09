try:
   days=int(input("how many working day you have :"))
except Exception as e:   
    print(e)
else:
    try:
        if(days>30 or days<0):
            raise ValueError
        else:
            payment=500*days
            print("your payment  is:",payment)
    except ValueError:
            print("please check the day you Enter....!!!!")
finally:
    print("------------thanks for visit--------------")




