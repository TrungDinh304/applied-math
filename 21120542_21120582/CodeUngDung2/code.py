import matplotlib.pyplot as plt
from skimage import io, img_as_ubyte,img_as_float32
from sklearn import decomposition
from skimage.util import random_noise
import os

def read_image(image_path):
    try:
        input_image =  io.imread(image_path, as_gray=True) 
        return input_image
    except (FileNotFoundError, IOError) as e:
        raise Exception("Lỗi không thể đọc file:",str(e))

#=============== I. NHỮNG HÀM XỬ LÝ VỚI NOISE IMAGE (ẢNH NHIỄU) ============================================== 
#1.1 Hàm tạo noise_image
def create_noise_image(input_image):
    #Thêm nhiễu vào input_image (ảnh gốc đọc vào)
    noise_image = random_noise(input_image, mode='gaussian', var=0.05)
    return noise_image

#1.2 Hàm lưu noise_image     
def save_noise_image(noise_image, noise_pic_path):
    # Chuyển đổi về định dạng uint8
    noise_image = img_as_ubyte(noise_image)
    
    # Lưu ảnh noise (màu của ảnh là gray)
    io.imsave(noise_pic_path, noise_image)
    
    #In thông báo:
    print('Đã lưu noise_image tại ', noise_pic_path)
    
#=============== II. NHỮNG HÀM XỬ LÝ VỚI PCA_RECONS_IMAGE (ẢNH TÁI TẠO LẠI SAU KHI SỬ DỤNG PCA) =============== 
#2.1 Hàm tạo pca_recons_image    
def create_pca_recons_image(noise_image):
    #Áp dụng PCA với số thành phần chính = 50
    pca = decomposition.PCA(n_components= 50)
    
    #Khớp lại dữ liệu
    pca.fit(noise_image)
    pcaFace = pca.transform(noise_image)
    pca_recons_image = pca.inverse_transform(pcaFace)
    
    return pca_recons_image

#2.2 Hàm lưu pca_recons_image
def save_pca_recons_image(pca_recons_image, pca_pic_path):
    # Chuẩn hóa giá trị của image_recons về trong đoạn [0,1] ([black,white]). Phải chuẩn hóa thì mới lưu ảnh được
    pca_recons_image = img_as_float32(pca_recons_image)
    pca_recons_image = (pca_recons_image - pca_recons_image.min()) / (pca_recons_image.max() - pca_recons_image.min())
    
    # Chuyển đổi về định dạng uint8
    pca_recons_image = img_as_ubyte(pca_recons_image)
    
    #Lưu ảnh PCA (màu của ảnh là gray)
    io.imsave(pca_pic_path, pca_recons_image)
    
    #In thông báo
    print('Đã lưu pca_recons_image tại ', pca_pic_path)

#===================================================== HÀM MAIN =============================================== 

if __name__ == "__main__":
    # Xóa màn hình trước đó, để khi xuất các dòng xử lý của chương trình ra sẽ dễ nhìn hơn
    os.system("cls")
    
    # Lấy đường dẫn thư mục đang làm việc
    file_path=os.path.dirname(__file__)
    
    # Nhập vào tên file ảnh (vd: input_picture1.jpg)
    image_name = str(input('Hãy nhập vào tên file ảnh: '))
    
    # Lấy đường dẫn file ảnh input
    image_path = file_path.replace("\\",'/') + '/' + image_name
    
    # Đọc ảnh từ file:
    try:
        input_image = read_image(image_path)
    except Exception as e:
        print(str(e))
        print ('== Kết thúc chương trình ==')
        exit(1)
    print('Đọc file thành công')
    print('******************************************************************************************')
    
    #Tạo ảnh noise_image (ảnh nhiễu)
    noise_image = create_noise_image(input_image)
    
    # Khai báo đường dẫn file ảnh noise
    noise_pic_path = file_path.replace("\\",'/') + '/noise_picture.jpg'
    
    # Lưu ảnh noise_image
    save_noise_image(noise_image, noise_pic_path)
    
    print('******************************************************************************************')
    
    #Tạo ảnh pca_recons_image (ảnh tái tạo lại sau khi sử dụng pca)
    pca_recons_image = create_pca_recons_image(noise_image)
    
    # Khai báo đường dẫn file ảnh PCA
    pca_pic_path =  file_path.replace("\\",'/') + '/pca_picture.jpg'
    
    # Lưu ảnh pca_recons_image
    save_pca_recons_image(pca_recons_image, pca_pic_path)
    
    print('******************************************************************************************')
    
    #== (Trong trường hợp thầy muốn xem luôn mà ko cần mở các file được lưu) ==
    # Hiển thị các ảnh lên màn hình, màu của các ảnh đều là gray 
    '''fig, axes = plt.subplots(1, 3, figsize=(15, 6))

    axes[0].imshow(input_image, cmap='gray')
    axes[0].set_title('input_picture')
    axes[0].axis('off')

    axes[1].imshow(noise_image, cmap='gray')
    axes[1].set_title('noise_picture')
    axes[1].axis('off')

    axes[2].imshow(pca_recons_image, cmap='gray')
    axes[2].set_title('pca_picture')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()'''
    print ('== Kết thúc chương trình ==')