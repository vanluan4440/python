'''
Bài 11 :
-	Viết chương trình cho phép người dùng nhập một giá trị số nguyên, nếu nhập sai định dạng yêu cầu nhập lại giá trị.
- 	Tạo một List (danh sách) với các phần tử là số nguyên (giá trị tuân theo quy luật của dãy số Fibonacci) và số lượng phần tử bằng với giá trị vừa nhập.
- Hiển thị danh sách vừa nhập ra màn hình.
- In ra màn hình tất cả các giá trị là số nguyên tố có trong danh sách vừa nhập.

'''

def nhap_so():
        try:
            number = input('Nhập dãy số nguyên dương: ').split()
            number = list(map(int,number))
            return number
        except:
            print ('dữ liệu đầu vào không hợp lệ, nhập lại: ')
        
def nguyen_to(number):
    nguyenTo = []
    for i in number:
        if i <= 0:
            return 'Bạn cần nhập số nguyên dương'
    else:
        for i in number:
            check = True
            for j in range(2,i):
                if i == 1:
                    check = True
                elif i % j == 0:
                    check = False
            if check:
                nguyenTo.append(i)
    return nguyenTo

if __name__ == '__main__':
    print('Dãy số nguyên tố là: {}'.format(nguyen_to(nhap_so())))