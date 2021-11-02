# Bài 3: Viết chương trình nhập vào giá trị điện dung C, điện cảm L và tần số f. Tính và in ra tổng trở Z của mạch. Cho biết:
import time
def inputFunction(string):
    data= int(input(string))
    return data
def Z(C,L,f):
    pi=3.14
    resultZ = (2*pi*f*L) -(1/(2*pi*f*C))
    return resultZ
def main():
    C = inputFunction('Nhập giá trị điện dung C: ')
    L = inputFunction('Nhập giá trị điện cảm L: ')
    f = inputFunction('Nhập giá trị tần số f: ')
    print('đang tính toán ....')
    time.sleep(2)
    print("Tổng trở Z của mạch là: {}  Ω".format(Z(C, L, f)))
main()