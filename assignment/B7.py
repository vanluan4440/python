def viet_hoa(s):
    if len(s) == 0:
        return ''
    if s[0].islower():
        s = s.upper()
    elif s[0].isupper():
        s = s.upper()
    return s
s = input('Nhập chuỗi tối đa 10 kí tự: ')
while (s>10):
    s= str(input("Nhập dư xin mời nhập lại: "))
print(viet_hoa(s))      