# Ransom_DigitalDragonsCTF_2023
***
## Description: Hacker lỏd nào đó đã upload lên website những tài liệu đen mà hắn hack được, hãy tìm ra chúng và thưởng thức. (Đề bài tự bịa)
- format: có 2 flag trong bài có dạng flag{}, tìm cả 2 flag để hoàn thành.
- link: [Ransom](https://drive.google.com/file/d/11El0CR1B3O95Cs2nfndQz3lX3csyCagM/view?usp=sharing)

1. Theo như đề bài, hacker đã upload một số tài liệu lên trên mạng nên mình check phần export xem có gì đặc biệt
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/42bbeddc-9c04-4353-82ca-ccbf920e5ace)
2. Trong phần export http mình thấy có khá nhiều file trong đó, thử export ra để kiểm tra
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/4d8d2356-a4b9-430b-a548-350c57e02032)
3. Do là đang kiểm tra upload nên mình check các file upload trước xem có thông tin gì hữu ích không
4. Ở file upload(3).php - mới được upload gần đây nhất
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/ce304541-a426-42b2-8305-8b872b4c84ad)
5. Check tiếp file upload(2).php
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/28cf122e-e6b2-45d2-8d94-2a932b2dd50e)
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/d30f2ba3-c416-46a1-908a-40c270fbd73c)
6. Nhận thấy đây là một chuỗi hex encoded, mỗi cặp ký tự hex biểu diễn một byte (8 bit) dữ liệu. Để phân tích nó, chúng ta có thể giải mã từng byte, để giải mã nhanh chóng, ta cần chuyển đổi chuỗi hex này sang các byte dữ liệu gốc. Trong Python, có thể sử dụng hàm bytes.fromhex() để thực hiện việc này:
---- file encode pdf
7. Và đây là kết quả khi ta encode được:
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/279eade3-3bb2-4146-952b-89804ef2e463)
---- Chèn thêm file encode
8. Còn flag 2 ta check tiếp file upload(1).php
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/213ae06e-19a8-4dea-aecb-b3d6fe219059)
  Cũng vẫn là 1 file đã được upload
9. Ở file upload.php, có vẻ đây là một file chứa data, thử extract nó ra bằng "binwalk -e upload"
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/c4ee19f7-eba7-4aeb-b1f0-9729f5fab5f6)
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/b90b816d-2995-4483-9a46-3f2a97921998)
10. Được một folder secret-2
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/a580d50a-936d-487a-bb1f-3033fedd37bc)
11. Trong folder này chứa 1024 ảnh được đánh số từ 1 -> 1024, và mỗi bức ảnh chỉ chứa những đường trắng đen, nghi ngờ đây là một file ảnh được tách thành 1024 mảnh ghép, giờ ta chỉ cần code một đoạn code để có thể ghép 1024 ảnh lại với nhau
---- code ghép ảnh
![anh_32x32](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/29014d9c-74b8-4b74-a75e-2cdcb1b3cd4d)
![image](https://github.com/BuiDuyet/ransom_DigitalDragonsCTF_2023/assets/135353207/78eed17f-a91e-4cd6-9721-a1fd926cf1ed)
End.




