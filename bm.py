age = input("please enter your age   ")
weight = input("please enter your weight:.")
height = input("please enter your height:.")
BMI = float(weight) / float(height) * float(height)
if BMI < 18.5:
    print("you are under weight")
elif BMI < 24.9:
    print("you have a normal weight")
elif BMI < 29.9:
    print("you are over weight")
else:
    print("you are obese")
