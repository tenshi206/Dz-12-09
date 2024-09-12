a= int(input("введите координату x1:"))
b= int(input("введите координату y1:"))
c= int(input("введите координату x2:"))
d= int(input("введите координату y2:"))

if not 1 <= a <= 8 or not 1 <= b <= 8 or not 1 <= c <= 8 or not 1 <= d <= 8:
    print("не правильно")
elif int(c-a) ==1 and int(d-b) ==2:
    print("да")
elif int(c-a) ==2 and int(d-b) ==1:
    print("да")
else:
    print("нет")
