# '''Bài 5 : Viết chương trình tính tiền cước taxi với bảng giá như sau :
# •	2  km đầu tiên  : 20.000 đ.
# •	8  km tiếp theo : 7.000đ/km.
# •	10 km tiếp theo : 5.000đ/km.
# •	Từ km thứ 21 	  : 3.000đ/km.
# Dựa trên các thông số trên, viết chương trình có các chức năng sau :
# •	Cho phép người sử dụng nhập vào các số km đi được.
# •	Xuất ra màn hình tiền cước.'''
def main():
    #Nhập số km và khai báo kiểu giá trị
    km=float(input("Nhập số km"))
    tien=float
    #dùng if elif else để đưa ra số tiền cần trả
    if km<=2:
        print("số tiền là=", 20000)
    elif km>2 and km<=10:
        print("Số tiền là =",(km-2)*7000+1*20000)
    elif km>10 and km <21:
        print("Số tiền là =", 1*20000+(km-10)*5000+8*7000)
    else:
        print("Số tiền là =", 1*20000+(km-21)*3000+8*7000+10*5000)
main()
