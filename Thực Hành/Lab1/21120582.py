import numpy as np


def read_file_txt(filename):
    a = np.loadtxt(filename)
    return a

def save_matrix_toTXT(filename, matrix):
    np.savetxt(filename, matrix)
 


def swap_row(arr,a,b):
    arr[a]=arr[a]+arr[b]
    arr[b]=arr[a]-arr[b]
    arr[b]=arr[a]-arr[b]


#bài 1:
def Gauss_elimination(arr):
    rows, cols = arr.shape
    t=0
    #đi từng cột của ma trận
    for i in range(cols):
        if(i>=rows):
            break
        if(i+t>cols):
            break
        # kiểm tra xem cột có full 0 hay không
        all0 = False
        #kiểm tra giá trị đầu cột có bằng 0 hay không nếu bằng 0
        # thì hoán vị dòng với bất kì dòng nào khác 0
        if(arr[i+t][i] == 0):
            for j in range(i+t,rows):
                if(arr[j][i]!=0):
                    swap_row(arr,i+t,j)
                    break
                if(j==rows-1):
                    all0=True
        # nếu cột full 0 thì bỏ qua cột và nhảy qua duyệt cột kế tiếp
        if(all0==True):
            t=t-1
            continue
        # thực hiện quá trình cộng trừ nhân chia để bán chuẩn dòng i+t
        a = arr[i+t]/arr[i+t][i]
        for j in range(i+1+t,rows):
            arr[j]=arr[j]-a*arr[j][i]
    # đưa các phần tử có sai số rất nhỏ so với 0 về 0 do đang tính trên số thực
    for i in range(rows):
        for j in range(cols):
            if abs(arr[i][j]) < 1e-10:
                arr[i][j]=0

# hàm hỗ trợ để tìm nghiệm của hệ phương trình
#Gauss jordan 
def Gauss_jordan_elimination(A):
    Gauss_elimination(A)
    rows,cols=A.shape

    for i in range(rows):
        for j in range(cols):
            if(A[i][j]!=0):
                A[i] = A[i]/A[i][j]
                break
    #tinh rank cua ma tran he so
    rank_heso=rows
    for i in range(rank_heso):
        count=0
        for j in range(cols):
            if(abs(A[i][j])<1e-10):
                count=count+1
        if(count >= cols - 1):
            swap_row(A,i,rank_heso-1)
            rank_heso=rank_heso-1
    for i in range(rank_heso):
        flag = np.zeros(rows)
        for j in range(cols-1):
            a=np.zeros(cols)
            for k in range(rows-1,i,-1):
                if A[k][j] != 0 and flag[k] == 0:
                    a = A[k]
                    flag[k] = 1
                    break
            A[i]= A[i]-a*A[i][j]
    for i in range(rows):
        for j in range(cols):
            if abs(A[i][j]) < 1e-10:
                A[i][j]=0


#bài 2:
def back_substitution(A):
    #đưa ma trận đầu vào về dạng bậc thang
    Gauss_elimination(A)
    
    rows,cols=A.shape
    for i in range(rows):
        for j in range(cols):
            if(A[i][j]!=0):
                A[i] = A[i]/A[i][j]
                break
    #tìm rank của ma trận mở rộng
    # đồng thời dồn các dòng full 0 xuống đáy ma trận
    rank=rows
    for i in range(rank):
        count=0
        for j in range(cols):
            if(A[i][j]==0):
                count=count+1
        if(count==cols):
            swap_row(A,i,rank-1)
            rank=rank-1
    
    #tinh rank cua ma tran he so
    rank_heso=rows
    for i in range(rank_heso):
        count=0
        for j in range(cols):
            if(A[i][j]==0):
                count=count+1
        if(count >= cols - 1):
            swap_row(A,i,rank_heso-1)
            rank_heso=rank_heso-1
    # nếu rank của ma trận mở rộng lớn hơn rank của ma trận hệ số thì hệ vô nghiệm
    if(rank > rank_heso):
        print("He phuong trinh vo nghiem: ")
        return
    # nếu rank của ma trận hệ số bằng rank của ma trận mở rộng và 
    # có giá trị bằng số biến của hệ thì hệ có 1 nghiệm duy nhất
    elif(rank_heso == cols -1):
        
        result = np.zeros(cols-1)
        # duyệt từ dưới lên để tìm nghiệm của từng biến
        for i in range (rank-1,-1,-1):
            result[i]=result[i] + A[i][cols-1]
            for k in range(i,cols-2):
                result[i]=result[i]+-1*A[i][k+1]*result[k+1]
        print('He co nghiem duy nhat: ')
        print(result)
        return result
    # nếu rank của ma trận hệ số bằng rank của ma trận mở rộng và 
    # rank ma trận hệ số < số nghiệm của hệ thì hệ có vô số nghiệm với 
    # số vector cơ sở tập nghiệm = số nghiệm của hệ - rank ma trận hệ số với số chiều = số biến của hệ 
    elif(rank==rank_heso and rank_heso<cols-1):
        # chuẩn hóa ma trận bậc thang
        Gauss_jordan_elimination(A)
        # tìm số vector cơ sở của tập cơ sở tập nghiệm
        Sovt_coso = cols-1 - rank_heso
        # khởi tạo ma trận cơ sở
        coso_tapno = np.zeros([Sovt_coso,cols-1])
        # khởi tạo mảng lưu cờ để đánh dấu các biến phụ thuộc
        bacthang = np.zeros(cols-1)
        # khởi tạo mảng lưu vị trí dòng của các biến phụ thuộc
        dong_bacth = np.zeros(cols-1)
        # đặt cờ và tìm dòng của các biến phụ thuộc
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    bacthang[j] = 1
                    dong_bacth[j]=i
                    break
        t = 0
        # lần lượt gán các giá trị tự cho cho các biến tự do 
        for i in range(cols-1):
            if bacthang[i] == 0:
                coso_tapno[t][i] = 1
                t = t + 1
        # 2 lớp for ngoài để duyệt từng phần tử của ma trận cơ sở tập nghiệm duyệt từng phần tử của 
        for i in range(cols-1):
            if bacthang[i] == 1:
                for j in range(Sovt_coso):
                    vitribien = int(dong_bacth[i])
                    coso_tapno[j][i] = A[vitribien][cols-1]
                    for k in range(cols-1):
                        if bacthang[k] == 0:
                            coso_tapno[j][i] = coso_tapno[j][i] - coso_tapno[j][k]*A[vitribien][k]

        print('He co vo so nghiem co tap co so la:')
        print(coso_tapno)
        return coso_tapno
        

def main():
    A=read_file_txt("matrix.txt")
    print('ma tran doc duoc\n',A)
    print('=========')
    Gauss_elimination(A)
    print('MA TRAN BAC THANG CUA MA TRAN VUA DOC DUOC: \n',A)
    print('=====================================')
    back_substitution(A)
main()




