# Dinh nghia ham tra ve chuoi HOA hoac thuong
def chuoi_hoa_thuong(str):
    if len(str) == 0:
        print()
    else:
        # Neu ky tu dau tien la chu thuong
        if str[0].islower():
            # Hien thi chuoi toan chu thuong
            print(str.lower())
        # Neu ky tu dau tien la chu hoa
        elif str[0].isupper():
            # Hien thi chuoi toan chu hoa
            print(str.upper())
        else:
            # Truong hop gap ky tu dac biet thi in chuoi nhu cu
            print(str)
str = input('Nhap chuoi can xu ly: ')
chuoi_hoa_thuong(str)