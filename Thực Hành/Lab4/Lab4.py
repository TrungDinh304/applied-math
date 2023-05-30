from matplotlib import pyplot as plt
import numpy as np
from sympy import Symbol
from sympy import symbols
from sympy import Matrix
from fractions import Fraction


def diem_dung(A,b):
    ATA = A.T @ A
    ATb = A.T @ b
    x = np.linalg.inv(ATA) @ ATb
    return x
def bieu_thuc(x, A, q, c):
    sobien = len(x)
    f = 0
    for i in range(sobien):
        f += x[i] * q[i]
        for j in range(sobien):
            f += x[i] * x[j] * A[i][j]
    f += c
    return f
#Bài 1:
#Kiểm tra tính lồi/lõm và tìm cực trị toàn cục nếu có của hàm f(x) = xT * A* x+ qT * x + 1 
# đạo hàm bậc 1: f'(x) = 2Ax + qT
# Đạo hàm bậc 2: f''(x) = 2A

# với ma trận A: |  1 -2 1  | ; x = (x1, x2, x3) ; q = (1, 2, -1)
#                |  -2 1 -2 |
#                |  1 -2 1  |

def xacDinh_loi_lom(A, q, c):
    gtri_rieng = np.linalg.eigvals(A)
    print(f'Các gái trị riêng: {gtri_rieng}')
    if all (gtri_rieng > 0):
        print('Do các giá trị riêng dương nên hàm xác định dương và f(x) là hàm lồi')
        qT = q.T
        qT = -1 * qT
        cucTieu = diem_dung(A,qT)
        print('Hàm f(x) có cực tiểu tại: x = ',cucTieu)
        fx = bieu_thuc(cucTieu,A,q,c)
        print(f'Với giá trị cực tiểu f(x) = {fx}')
    elif all(gtri_rieng >= 0):
        print('Do các giá trị riêng không âm nên hàm xác định nữa dương và f(x) là hàm lồi')
        qT = q.T
        qT = -1 * qT
        cucTieu = diem_dung(A,qT)
        print('Hàm f(x) có cực tiểu tại: x = ',cucTieu)
        fx = bieu_thuc(cucTieu,A,q,c)
        print(f'Với giá trị cực tiểu f(x) = {fx}')
    elif all(gtri_rieng < 0):
        print('Do các giá trị riêng âm nên hàm xác định âm và f(x) là hàm lõm')
        qT = q.T
        qT = -1 * qT
        cucDai = diem_dung(A,qT)
        print('Hàm f(x) có cực đại tại: x = ',cucDai)
        fx = bieu_thuc(cucDai,A,q,c)
        print(f'Với giá trị cực đại f(x) = {fx}')
    elif all(gtri_rieng <= 0):
        print('Do các giá trị riêng không dương nên hàm xác định nửa âm và f(x) là hàm lõm')
        qT = q.T
        qT = -1 * qT
        cucDai = diem_dung(A,qT)
        print('Hàm f(x) có cực đại tại: x = ',cucDai)
        fx = bieu_thuc(cucDai,A,q,c)
        print(f'Với giá trị cực đại f(x) = {fx}')
    else: 
        print('Hàm f(x) không xác định lồi cũng không xác định lõm')

# Bài: 2
def leastSquare(A,b):
    X = A.T @ A
    Y = A.T @ b
    coefficient = np.linalg.inv(X)@Y
    return coefficient

#Bài 3:
def fx_3(x,coefficient):
    return coefficient[0] + coefficient[1]*x + coefficient[2]*np.log(x**2+1)



def main():
    # Bài 1:
    print('==================BÀI 1========================')   
    A = np.array([[1, -2, 1],
                [-2, 1, -2],
                [1, -2, 1]])

    print(f'Ma trận A:\n {A}')

    x1,x2,x3 = symbols('x1,x2,x3') 
    x = np.array([x1,x2,x3])
    print(f'X = {x}')

    q = np.array([1,2,-1])
    print(f'vector q = {q}')
    sotudo = -1

    # A = np.array([[3,-1,1],
    #               [-1,1,0],
    #               [1,0,1]])
    # print(f'Ma trận A:\n {A}')

    # x1,x2,x3 = symbols('x1,x2,x3') 
    # x = np.array([x1,x2,x3])
    # print(f'X = {x}')

    # q = np.array([0,0,0])
    # print(f'vector q = {q}')

    # sotudo = 0

    f = bieu_thuc(x,A,q, sotudo)
    print(f'Hàm số: f({x}) = {f}')
    xacDinh_loi_lom(A,q,sotudo)

    #bài 2
    print('=======================BÀI 2=========================')
    data = np.array([[0, 10], 
                     [1, 8], 
                     [2, 7], 
                     [3, 5], 
                     [4, 2]])
    rows,cols = data.shape
    A = np.zeros([rows,cols])
    b = np.zeros([rows,1])
    for i in range(rows):
            A[i][1] = 1
            A[i][0] = data[i][0]
            b[i][0] = data[i][1]
    # tính các hệ số a, b qua phương pháp bình phương tối tiểu
    coefficient = leastSquare(A,b)
    print(coefficient)
    print('Phương trình tuyến tính thể hiện lượng thuốc giảm theo thời gian: ')
    print('y = ', coefficient[0], ' x + ',coefficient[1])

    # khai báo 2 biểu đồ trên cùng một bảng để vẽ biểu đồ cho cả bài 2 và bài 3
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4), sharey=True, dpi=120)

    # Định nghĩa biểu đồ bài 2
    ax1.set_title('Bài 2:\n Đường tuyến tính thể hiện\n lượng thuốc giảm theo thời gian:')
    ax1.set_xlabel('Thời Gian (giờ)')
    ax1.set_ylabel('Lượng Thuốc còn tồn lại')

    #vẽ các điểm từ dữ liệu thực tế
    ax1.plot(data.T[0],data.T[1],'bo--', label = 'dữ liệu thực tế')

    # tạo list các điểm thuộc đưởng thẳng khớp với mô hình để vẽ đồ thị
    x_sample = np.linspace(min(data.T[0]),max(data.T[0]),10)
    y_sample = [coefficient[0] * x + coefficient[1] for x in x_sample]
    ax1.plot(x_sample,y_sample,'r', label = f'y = {coefficient[0]}x + {coefficient[1]}')
    ax1.legend(loc = 'best')

    #Bài 3:
    print('================================== Bài 3 ===============================')
    ax2.set_title('Bài 3-b:\nTrọng lượng của hợp chất \ntheo thời gian khi tiếp xúc với không khí')
    ax2.set_xlabel('Thời Gian (năm)')
    ax2.set_ylabel('Trọng Lượng (gram)')
    data3 = np.array([  [-2,-1],
                        [0,1.5],
                        [1,3.1],
                        [2,6.3],
                        [4,11.1]])
    
    print('\tCâu a:')
    #Câu a:
    rows,cols = data3.shape
    A3 = np.zeros([rows,3])
    b3 = np.zeros([rows,1])
    # mô hình hóa dữ liệu thực
    for i in range(rows):
        A3[i][0] = 1
        A3[i][1] = data3[i][0]
        A3[i][2] = np.log(data3[i][0]**2 + 1)
        b3[i][0] = data3[i][1]
    
    coefficient_3 = leastSquare(A3,b3)
    print('Phương trình theo mô hình: ')
    print(f'y = {coefficient_3[0]} + {coefficient_3[1]}x + {coefficient_3[2]}ln(x^2 + 1)')
   
    # Câu b
    print('\tCâu b:')
    # dự đoán y với x = 6.5
    print(f'[Với x = 6.5, y được dự đoán: {fx_3(6.5,coefficient_3)} gram.]')

    #Vẽ biểu đồ so sánh dữ liệu thực với mô hình
    ax2.plot(data3.T[0],data3.T[1],'ro--', label = 'dữ liệu thực tế') # vẽ đồ thị dữ liệu thực tế
    
    # tạo list các điểm thuộc đưởng thẳng khớp với mô hình để vẽ đồ thị
    x_sample = np.linspace(min(data3.T[0]),max(data3.T[0]),50)
    y_sample = [fx_3(x,coefficient_3)  for x in x_sample]
    
    # vẽ đường thể hiện phương trình theo mô hình 
    ax2.plot(x_sample,y_sample,'g', label = f'y = {coefficient_3[0].round(2)} + {coefficient_3[1].round(2)}x + {coefficient_3[2].round(2)}ln(x^2 + 1)')
    ax2.legend(loc='upper left')
    plt.show()

    # câu c
    print("\tCâu c: ")
    # thử với mô hình  y = a + bx + cln(x) 
    print('--------------------------------------------------')
    try:
        print('Thử mô hình y = a + bx + cln(x)')
        A3c = np.zeros([rows,3])
        b3c = np.zeros([rows,1])
        # mô hình hóa dữ liệu thực
        for i in range(rows):
            A3c[i][0] = 1
            A3c[i][1] = data3[i][0]
            A3c[i][2] = np.log(data3[i][0])
            b3c[i][0] = data3[i][1]
    except:
        print('In ln x must be positive.')
        print('Vì vậy không nên dùng mô hình y = a + bx + cln(x) để xấp xỉ dữ liệu trên.')
    
    # thử với mô hình  y = a + bx + c/x
    print('--------------------------------------------------')
    try:
        print('Thử mô hình y = a + bx + c/x')
        A3c = np.zeros([rows,3])
        b3c = np.zeros([rows,1])
        # mô hình hóa dữ liệu thực
        for i in range(rows):
            A3c[i][0] = 1
            A3c[i][1] = data3[i][0]
            A3c[i][2] = 1/data3[i][0]
            b3c[i][0] = data3[i][1]
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        print('Vì vậy không nên dùng mô hình y = a + bx + c/x để xấp xỉ dữ liệu trên.')
    
    print('--------------------------------------------------')
    print("Do dữ liệu thực trong bài này có giá trị x âm và x = 0 nên: ")
    print("Không thể sử dụng mô hình y = a + bx + cln(x) hay y = a + bx + c/x để xấp xỉ vì:")
    print("\t+ Trong ln(x) thì x bắt buộc phải dương.")
    print("\t+ Trong 1/x thì x bắt buộc phải khác 0.")


if __name__ =="__main__":
    main()
