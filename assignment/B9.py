
# Bài 9 :
# Viết chương trình cho phép người dùng nhập 1 chuỗi (tối đa 50 kí tự).
# - Xóa hết tất cả kí tự khoảng trắng trong chuỗi '  ' và xuất chuỗi mới ra màn hình.
# VD: 	Nhập 	: S = Xin chao moi nguoi.
# 	Xuất	: S = Xinchaomoinguoi.


# Ham xoa khoang cach thua
def xoa_khoang_cach_thua(str):
    # Xoa khoang cach thua dau cua chuoi
    str = str.strip()
    # Xoa khoang cach thua o cac tu
    # Dung while lap cho den khi nao khong con '  ' nua thi dung
    while '  ' in str:
        # Thay '  ' thanh ' '
        str = str.replace('  ', '')
    while ' ' in str:
        str = str.replace(' ','')
    print(str)
str = input('Nhap ky tu can xu ly: ')
xoa_khoang_cach_thua(str)