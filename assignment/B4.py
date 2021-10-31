'''Bài 4:  Viết chương trình nhập vào một giá trị số nguyên a. In ra màn hình tất cả số nguyên tố nằm trong khoảng [0,a].'''
#Nhập số nguyên dương n
def so_ngto(n): #gọi hàm kiểm tra số nguyên tố
    dem=0
    for i in range(1,n+1):
        if n % i==0:
            dem=dem+1
    if dem==2:
        return 1
    else:
        return 0
n=int(input("Nhập n="))
for i in range(1,n+1):
    if so_ngto(i)==1:
        print(i)