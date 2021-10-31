'''
Viết chương trình với các yêu cầu sau.
-	Cho phép người sử dụng nhập vào ngày tháng năm sinh theo định dạng : ‘d:m:yyyy’
-	Tách và in riêng giá trị: ngày, tháng, năm

'''
class c_Date:
    #Phương thức khai báo hàm khởi tạo
    def __init__(self,ngay,thang,nam):
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
    # hàm điều kiện

    def normalize(self):
        if self.d < 1 or self.maxday() < self.d:
            self.d = 1

    def maxday(self):
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.kt_nhuan() == True:
            days[2] = 29
        if self.kt_nhuan() == False:
            days[2] = 28
        return days[self.m]

    def kt_nhuan(self):
        if self.y % 4 == 0:
            return True
        if self % 4 != 0:
            return False

    # thay đổi là lấy giá trị thuộc tính của

    def __set__(self, d):
        self.d = d

    def __get__(self, d):
        return self.d

    def __set__(self, m):
        self.m = m

    def __get__(self, m):
        return self.m

    def __set__(self, y):
        self.y = y

    def __get__(self, y):
        return self.y

    # hàm nhập và xuất kết quả

    def __str__(self):
        return '{}/{}/{}'.format(self.d, self.m, self.y)

def main():
    ngay=int(input("Nhập ngày là: "))
    thang=int(input("Nhập tháng là: "))
    nam=int(input("Nhập năm là: "))
main()