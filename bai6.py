def kt(thang):
    if (1 <= thang <= 3):
        print("Thang ", thang, " thuoc mua xuan")
    elif (4 <= thang <= 6):
        print("Thang ", thang, " thuoc mua he")
    elif (7 <= thang <= 9):
        print("Thang ", thang, " thuoc mua thu")
    elif (10 <= thang <= 12):
        print("Thang ", thang, " thuoc mua dong")
    else:
        print("Khong hop le")

thang = int(input("Nhap thang: "))
kt(thang)