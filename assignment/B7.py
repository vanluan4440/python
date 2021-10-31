'''
Bài 7 :
-	Viết chương trình cho phép nhập 1 chuỗi có (tối đa) 10 phần tử. Hiển thị chuỗi vừa nhập ra màn hình.
- 	In ra màn hình các giá trị sau: chiều dài của chuỗi, số lượng kí tự là dấu '  ' (khoảng trắng) trong chuỗi. 
-	Chuyển chuỗi sang chữ HOA và xuất ra màn hình

'''
def viet_hoa(s):
    if len(s) == 0:
        return ''
    if s[0].islower():
        s = s.upper()
    elif s[0].isupper():
        s = s.upper()
    return s
s = input('Nhập chuỗi tối đa 10 kí tự: ')
print("Do dai chuoi:", len(s))
print("Chuoi vua nhap:", s)
print(viet_hoa(s))      

