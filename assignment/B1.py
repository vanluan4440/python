#Bài 1 :
# Viết chương trình với các yêu cầu sau.
# -	Cho phép người sử dụng nhập vào một số nguyên có 3 chữ số
# -	In ra màn hình chữ số hằng trăm, hàng chục và hàng đơn vị tương ứng của số vừa nhập.

def functionInput():
   n = str(input("Nhập số nguyên n gồm ba chữ số: "))
   if len(n) > 3:
       n = str(input("Nhập số nguyên n gồm ba chữ số: "))
   return int(n)
def main():
    n = functionInput()
    a=n//100 #trăm
    b=(n%100)//10 #chục
    c=n%10 # đơn vị
    print("Chữ số hàng trăm", a)
    print("Chữ số hàng chục", b)
    print("Chữ số hàng đơn vị", c)
main()
   
