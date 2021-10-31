def f(n): #gắn hàm để xuất dãy số Fibonacci
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)
n=int(input("Nhập số n: "))
values = [str(f(x)) for x in range(0, n+1)] #vòng lập để chạy lại giá trị
print (",".join(values)) #in ra màn hình kết quả


