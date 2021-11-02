# Bài 10 :
# -	Viết chương trình cho phép người dùng nhập lần lượt các giá trị (số nguyên) cho 1 List có 5 phần tử:
# - Hiển thị danh sách vừa nhập ra màn hình.
# - In ra màn hình các giá trị: lớn nhất, nhỏ nhất, giá trị trung bình các phần tử của danh sách.
def inputList():
    len = 5
    list=[]
    for x in range(0, len, 1):
        data = int(input('Nhập giá trị cho phần tử {} : '.format(x)))
        list.append(data)
   
    return list
def average(list):
    sum = 0
    for i in list:
        sum+=int(i)
    return sum/len(list)
def main():
   list = inputList()
   list.sort()
   minNumber = list[4]
   maxNumber = list[0]
   averageNumber = average(list)
   print("số nhỏ nhất: {} \nsố lớn nhất: {} \ngiá trị trung bình: {}".format(minNumber,maxNumber,averageNumber))

main()
