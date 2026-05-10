temprature = int(input("please enter the temprature      "))

if temprature > 50:
    print("hot")
elif temprature > 30:
    print("warm")
elif temprature > 15:
    print("normal")
elif temprature > 5:
    print("cold")
else:
    print("very cold")