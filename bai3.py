def xuly(a, b, c):
    if((a + b <= c) or (a + c <= b) or (b + c <= a)):
        print("{}, {}, {} khong phai ba canh cua mot tam giac".format(a, b, c))
    else:
        if (a == b == c):
            print("Day la tam giac deu")
        elif (a == b or b == c or a == c):
            if ((a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b)):
                print("Day la tam giac vuong can")
            else:
                print("Day la tam giac can")
        elif((a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b)):
            print("Day la tam giac vuong")
        else:
            print("Day la tam giac thuong")

print("Nhap do dai ba canh" )
a = float(input())
b = float(input())
c = float(input())
xuly(a, b, c)