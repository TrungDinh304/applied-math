import numpy as np


# các hàm phụ trợ
#=========================================================================================================
# in list ma trận
def print_matrix_list(A):
    r = len(A)
    for i in range(r):
        print(A[i])
# nhân vector với 1 hằng số
def multiplyScalarVector(scalar, A):
    result = [0 for _ in range(len(A))]
    for i in range(len(A)):
        result[i] = A[i]*scalar
    return result
# cộng 2 vector
def cong_vector(a,b):
    if(len(a)!= len(b)):
        print('======================================================================================')
        print('|Tham số truyền vào không hợp lệ do 2 vector truyền vào có chiều dài không giống nhau|')
        print('======================================================================================')
        exit()
    result = [0 for _ in range(len(a))]
    for i in range(len(a)):
        result[i] = a[i]+b[i]
    return result
# chuyển vị 1 ma trận
def transpose(A):
    #Khoi tao ma tran ket qua
    AT = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    m=len(A)#Cho biet so dong cua A
    n=len(A[0])#Cho biet so cot cua A
    for i in range(m):
        for j in range(n):
            AT[j][i]=A[i][j]    
    return AT


#hàm tính độ dài vector
def module(v):
    result=0
    for i in range(len(v)):
        result += v[i]**2
    result = result**(1/2)
    return result
#đưa cá giá trị xấp xỉ 0 về 0 để tiện cho việc biểu diễn 
def xuli0(A):
    r = len(A)
    c = len(A[0])
    for i in range(r):
        for j in range(c):
            if abs(A[i][j])<1e-10:
                A[i][j] = 0.
# làm tròn các giá trị trong ma trận với A là ma trận cần làm tròn, n là số thập phân muốn làm tròn
def round_n(A,n):
    A = [[round(A[i][j],n) for j in range(len(A[0]))] for i in range(len(A))]
    return A
#======================================================================================================

#hàm theo yêu cầu đề bài:
#tính giá trị tích vô hướng 2 vector
def innerproduct(v1, v2):
    l1=len(v1)
    l2=len(v2)
    if(l2!=l1):#kiểm tra 2 vector có đủ điều kiện để thực hiện phép tính hay không
        print('======================================================================================')
        print('|Tham số truyền vào không hợp lệ do 2 vector truyền vào có chiều dài không giống nhau|')
        print('======================================================================================')
        exit()
    result = 0.
    for i in range(l1):
        result += v1[i] * v2[i]
    return result



# nhân 2 ma trận
def nhanmatran(A,B):
    rowsa = len(A)
    colsa = len(A[0])
    rowsb = len(B)
    colsb = len(B[0])
    if(colsa != rowsb ):
        print('======================================================================================')
        print('|Tham số truyền vào không hợp lệ do số cột của A khác sô hàng của B                  |')
        print('======================================================================================')
        exit()
    result = [[0 for _ in range(colsb)] for _ in range(rowsa)]
    temp = transpose(B)
    for i in range(rowsa):
        for j in range(colsb):
            result[i][j]=innerproduct(A[i],temp[j])
    return result


#thuật toán GramSchmidt để tìm ta ma trận Q
def GramSchmidtProcess(A):
    rows = len(A)
    cols = len(A[0])
    temp = transpose(A)
    result = temp
    print 
    for i in range(cols):
        for j in range(0,i):
            if(module(result[j])**2!=0):
                hs = -1.*innerproduct(result[j],temp[i])/(module(result[j])**2)
                vt = multiplyScalarVector(hs,result[j])
                result[i] = cong_vector(result[i],vt)
    for i in range(cols):
        if(module(result[i])**2 !=0 ):
            result[i] = multiplyScalarVector(1./module(result[i]),result[i])
    result=transpose(result)
    xuli0(result)
    return result

#hàm theo yêu cầu đề bài:
# Trả về ma trận phân rã Q, R
def QR_factorization(A):
    Q = GramSchmidtProcess(A)
    R = nhanmatran(transpose(Q),A)
    xuli0(R)
    return (Q, R)




def main():
    #đọc ma trận từ file input
    A = np.loadtxt('INPUT.txt')
    A = A.tolist() # chuyển ma trận về dạng list 
    print('Ma Trận A đọc được: ')
    print_matrix_list(A)
    print('--------------------------')
    Q,R = QR_factorization(A)
    print('Ma trận phân rã QR của A: A=QR')
    print('========Q========')
    
    print_matrix_list(round_n(Q,2))
    print('========R========')
    print_matrix_list(round_n(R,2))
main()


