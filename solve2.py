from PIL import Image

# Kích thước của mỗi ảnh và kích thước của ảnh đầu ra
image_width = 32
image_height = 32
output_width = image_width * 32  # Số ảnh theo chiều ngang
output_height = image_height * 32  # Số ảnh theo chiều dọc

# Tạo ảnh đầu ra mới
output_image = Image.new('RGB', (output_width, output_height))

# Đường dẫn đến thư mục chứa 1024 file ảnh PNG
images_folder = 'C:/Users/Bui Duyet/Dropbox/PC/Desktop/Digital Dragons CTF/Ransom/secret-2'

for i in range(1,1025,1):
    # Đọc ảnh từ thư mục
    image_path = f'{images_folder}/{i}.png'
    img = Image.open(image_path)

    # Tính toán vị trí của ảnh trong ảnh đầu ra
    row = i // 32
    col = i % 32
    left = col * image_width
    top = row * image_height

    # Đặt ảnh vào vị trí tương ứng trên ảnh đầu ra
    output_image.paste(img, (left, top))

# Lưu ảnh đầu ra
output_image.save('C:/Users/Bui Duyet/Dropbox/PC/Desktop/Digital Dragons CTF/Ransom/anh_32x32.png')
