def calculate(selected_drink, selected_payment):
    return selected_payment - drink[selected_drink]

drink = {"cola"     :1200,
         "water"    :1000,
         "sprite"   :1100,
         "milk"     :1300,
         "juice"    :1400}

print("<Drink List") 

for key in drink.keys():
    print(str(key) + ":" + str(drink[key]))

# variable
drink_name  = input("What do you want?(Drink name): ")
payment     = input("How much do you pay?")

result_payment = calculate(drink_name, int(payment))

if(result_payment > 0):
    print("change:" + str(result_payment))
    print("get a " + str(drink_name))
elif(result_payment == 0):
    print("get a " + str(drink_name))
else:
    print(drink_name + " is " + str(drink_name) + ", but you paid " + payment)
    agreed = input("please pay " + str(-result_payment) + "(Do you agree? Y/N : ")
    if agreed == "Y":
        print("get a " + drink_name)
    else:
        print("return" + payment)

