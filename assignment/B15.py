'''

Bài 15: Viết câu lệnh xây dựng hàm Arange(A) với A là 1 danh sách (list).
-	Hàm trả về 1 danh sách với các phần tử đã được sắp xếp theo thứ tự từ lớn đến bé và giá trị số chẵn đứng trước, số lẻ đứng sau.
VD: A = [1,6,2,7,1,9,4]  sẽ thành [6,4,2,9,7,1,1]

'''
def nhap(l,n):
    for i in range(n):
        # j=random.randint(0,10000)
        j=int(input("a["+str(i)+"]="))
        l.append(j)
def checkArray(list, evenArray,oddArray):
    for i in list:
        if i % 2 == 0:
            evenArray.append(i)
        else:
            oddArray.append(i)
def nhapN():
    n=int(input("Nhập n="))
    while n<0:
        n=int(input("Nhập sai nhập lại ="))
    return n
def xuat(l):
    print('Mảng cũ...')
    print(l)
def main():
    l=[]
    even =[]
    odd = []
    n=nhapN()
    nhap(l,n)
    xuat(l)
    checkArray(l, even, odd)
    print('mảng mới...')
    even.sort(reverse=True)
    odd.sort(reverse=True)
    print(even + odd)
main()