import numpy as np
import scipy.linalg
import math
import matplotlib.pyplot as plt

#đọc và lưu ma trận từ file .txt vào kiểu dữ liệu numpy array
def readfile_txt():
    a=np.loadtxt('data.txt')
    return a

# chuẩn hóa sang dạng mô hình Log10(N) ~ a(t - 1970) + b
def log10_model(a):
    rows,cols = a.shape
    for i in range(rows):
        modelling_vector(a[i])
    A = np.zeros([rows,cols])
    B = np.zeros([rows,1])
    for i in range(rows):
        A[i][1] = 1
        A[i][0] = a[i][0]
        B[i][0] = a[i][1]
    # Đặt Log(N) = y, a(t - 1970) = x
    #Lúc này mô hình có dạng y = ax + b
    # trong đây ma trận A là ma trận hệ số của a và b tức là các vector (x, 1)
    # ma trận B vector cột các giá trị y
    # từ đó đưa bài toán tìm hệ số về dạng AX =B với nghiệm X là nghiệm bình phương tối tiểu X = (a,b)
    return A, B

def modelling_vector(vt):
    if vt[1] != 0:
        vt[1] = math.log10(vt[1])
    vt[0] = vt[0] - 1970
    return vt

#tìm ma trận giả nghịch đảo cho ma trận truyền vào
def find_A_plus(A):
    rows, cols = A.shape
    U, D, VT = scipy.linalg.svd(A)
    sigma = np.zeros([rows,cols])
    for i in range(len(D)):
        sigma[i][i] = D[i]
    sigma_plus = sigma.T
    for i in range(len(D)):
        sigma_plus[i][i] = 1/sigma_plus[i][i]
    #ma trân giả nghịch đảo A+
    A_plus = VT.T @ sigma_plus @ U.T
    return A_plus

#tìm giá trị của y theo mô hình
def tinh_y(x,a,b):
    return a*x+b

# tìm hệ số cho đường thẳng gần với số liệu đọc được
def least_square_solution(A, B):
    #nghiệm bình phương tối tiểu của phương trình Ax = b:
    A_plus = find_A_plus(A)
    x = A_plus @ B
    return x

def main():
    # đọc dữ liệu từ file data.txt
    a = readfile_txt()
    print('Dữ liệu đọc được: ')
    print(a)
    rows, cols = a.shape
    #Chuẩn hóa dữ liệu theo mô hình Log10(N) ~ a(t - 1970) + b
    A, B = log10_model(a)

    print('Câu a:')
    # mục địch chính cần tìm ở câu a là tìm hệ số a, b của mô hình
    coefficient = least_square_solution(A, B)
    print('nghiệm bình phương tối tiểu của hệ phương trình Ax = B:')
    print(coefficient.round(2))
    print('Phương trình đường thẳng khớp với mô hình có dạng: y = ', coefficient[0], 'x + ', coefficient[1])
    
    print('Câu b:')
    #Nối tiếp dữ liệu năm 2015 vào bảng dữ liệu và mô hình hóa nó
    a = np.append(a ,[[2015 - 1970, math.log10(4.0e+09)]], axis = 0)
    # tạo list các điểm thuộc đưởng thẳng khớp với mô hình để vẽ đồ thị
    dotx = np.zeros([rows + 1,cols])
    for i in range(rows + 1):
        dotx[i][0] = a[i][0]
        dotx[i][1] = tinh_y(dotx[i][0],coefficient[0],coefficient[1])
        
    #dự đoán số bóng bán dẫn trong bộ vi xử lí vào năm 2015:
    print('Số bóng bán dẫn trong bộ vi xử lí được dự đoán vào năm 2015: ', 10**(tinh_y((2015 - 1970), coefficient[0], coefficient[1])))
    print('Với độ chênh lệch với dữ liệu thực tế là: ',10**tinh_y((2015 - 1970), coefficient[0], coefficient[1]) - (4.0e+09),' bóng bán dẫn.')
    #vẽ đồ thị cho đường thẳng gần với số liệu nhận được
    plt.plot(dotx.T[0],dotx.T[1], label = 'Đường thẳng khớp với mô hình')
    # vẽ đồ thị nối các điểm từ số liệu nhận được
    plt.plot(a.T[0],a.T[1], label = 'Các điểm của mô hình')
    plt.show()
main()