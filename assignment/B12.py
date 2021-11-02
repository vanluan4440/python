# Viết chương trình theo yêu cầu sau :
# - Tạo sẵn 1 danh sách 2 chiều (danh sách lồng ghép) có 5 phần tử (mỗi phần tử có 3 giá trị: tương ứng – Họ tên, MSSV, Điểm).
# - Hiển thị danh sách vừa nhập ra màn hình.
# - Cho phép người dùng nhập vào MSSV (hoặc Họ tên). In điểm số tương ứng ra màn hình
import time
#danh sách sinh viên
def data():
    list = [
        ['Nguyễn Văn A',123456,9],
        ['Nguyễn Thị B',123478,6],
        ['Nguyễn Thị C',455555,7]

    ]
    return list
#function nhập 
def inputFunction():
    choose = str(input('Chọn họ tên để In điểm: nhấm A:\nChọn mssv để in điểm chọn B: '))
    print('---------------------------------------------------------------------------')
    if choose == 'a':
        name = str(input('Mời nhập họ tên sinh viên: '))
        return name
    if choose == 'b':
        Id = str(input('Mời nhập mã số sinh viên: '))
        if len(Id) == 6:
            return Id
        else:
            Id = str(input('Mời nhập mã số sinh viên: [có 6 số]: '))
            return Id
#function kiếm theo Tên
def findStudentByName(value):
    list = data()
    student = []
    for i in list:
        if i[0] == value:
           student = i
    return student
  #function kiếm theo ID       
def findStudentByID(value):
    list = data()
    student = []
    for i in list:
        if i[1] == value:
           student = i
    return student  
#fuction main   
def main():
    findInput = inputFunction()
    #Kiếm theo mã số
    if findInput.isdigit():
        print('Đang tìm mã số sinh viên....')
        print('----------------------------------------------------------------------')
        time.sleep(2)
       
        if len(findStudentByID(int(findInput))) == 0:
            print('Không tìm mã số sinh viên : {}'.format(findInput))
        else:
           print('Sinh viên: {}\nMSSV:{}\nĐiểm:{}'.format(findStudentByID(int(findInput))[0],findInput,findStudentByID(int(findInput))[2]))
    #Kiếm theo tên
    else:
        print('Đang tìm tên sinh viên....')
        print('----------------------------------------------------------------------')
        time.sleep(2)
        if len(findStudentByName(findInput)) == 0:
            print('Không tìm thấy sinh viên tên: {}'.format(findInput))
        else:
            print('Sinh viên: {} \nCó điểm: {}'.format(findInput,findStudentByName(findInput)[2]))
main()
    
