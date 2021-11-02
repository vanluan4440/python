# Bài 13: Viết chương trình tạo 1 danh sách 2 chiều (lưu dữ liệu dạng: 3 hàng 2 cột). Cho phép người sử dụng nhập các giá trị phần tử từ bàn phím.
# a/ Hiển thị danh sách vừa nhập ra màn hình.
# b/ Cho phép người sử dụng nhập vào giá trị cần tìm kiếm. Nếu tìm thấy có phần tử thỏa mãn yêu cầu tìm kiếm, in ra màn hình vị trí (hàng, cột) của phần tử đó. Nếu không tìm thấy yêu cầu nhập lại giá trị tìm kiếm khác.


def main():
    rowNum=3
    colNum=2
    list = []
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    for row in range(rowNum):
        for col in range(colNum):
            a = int(input('Nhập giá trị [{} ;{}]: '.format(row,col)))
            multilist[row][col] = a
    print (multilist)
    find = int(input('Nhập giá trị cần kiếm: '))
    for row in range(rowNum):
        for col in range(colNum):
            if multilist[row][col] == find:
                list.append([row,col])
    print('Kiếm quả tìm kiếm: ', list)
main()