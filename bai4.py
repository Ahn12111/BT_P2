def sotien(km):
    if (km > 120):
        return ((km - 5) * 3500 + 4500 * 4 + 5000) * 1 / 10
    elif (5 < km <= 120):
        return ((km - 5) * 3500 + 4500 * 4 + 5000)
    elif (km > 1):
        return ((km - 1) * 4500 + 5000)
    elif (km == 1):
        return 5000
    else:
        return "Khong hop le"

km = float(input("Nhập số km bạn đã đi: "))
print("So tin ban phai tra la: ", sotien(km))
