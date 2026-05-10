percentage = int(input("please enter your percentage   "))

if percentage > 98:
    print("grade = outstanding")
elif percentage > 92:
    print("grade = A+")
elif percentage > 80:
    print("grade = A")
elif percentage > 65:
    print("grade = B ")
elif percentage > 55:
    print("grade = C ")
elif percentage > 40:
    print("grade = D ")
else:
    print("grade = F ")