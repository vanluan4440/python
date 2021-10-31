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
    for i in range(0,n-1):
        for j in range(i+1,n):
            if l[i]<l[j]:
             tg=l[i]
             l[i]=l[j]
             l[j]=tg
    print("Mảng sắp xếp lại là")
def nhapN():
    n=int(input("Nhập n="))
    while n<0:
        n=int(input("Nhập sai nhập lại ="))
    return n
def xuat(l):
    print(l)
def main():
    l=[]
    n=nhapN()
    nhap(l,n)
    xuat(l)
main()