# Cấu Trúc Chuẩn của file .PNG :
## Một tệp PNG bao gồm một tiêu đề chữ ký 8 byte, theo sau là bất kỳ số khối nào chứa dữ liệu điều khiển/siêu dữ liệu/dữ liệu hình ảnh. Mỗi đoạn chứa ba trường tiêu chuẩn – độ dài 4 byte, mã loại 4 byte, CRC 4 byte – và các trường bên trong khác nhau phụ thuộc vào loại đoạn.
## 1.PNG file signature :
+ Tám bytes đầu tiên của tệp PNG luôn chứa các giá trị sau:
+ (hệ 16)           89  50  4e  47  0d  0a  1a  0a
  (ASCII)         \211   P   N   G  \r  \n \032 \n
+ 2 bytes đầu : (89 50) phân biệt các tệp PNG trên các hệ thống
+ Byte Đầu Tiên : (89) để giảm khả năng tệp văn bản có thể bị nhận dạng sai thành tệp PNG
+ Byte 2 -> 4 : là tên định dạng tệp PNG
##  2.Chunk IHDR:

+ Là chunk đầu tiên của 1 ảnh PNG.

+ Bắt đầu chunk IHDR là tên của nó : 49 48 44 52

+ 4 bytes tiếp theo : thể hiện chiều rộng của ảnh. (pixel)

+ 4 bytes tiếp theo : thể hiện chiều dài của ảnh. (pixel)
## 3.chunk IDAT :
+ Chứa data của ảnh.

+ các chunk IDAT phải liên tục và không bị chunk khác gián đoạn.

+ Chunk IDAT dù chỉ có 1 byte hay chẳng có gì thì vẫn tính là hợp lệ.
## 4.Trailer(Chunk IEND) :
+ Bắt đầu và kết thúc của chunk này là 49 45 4E 44 AE 42 60 82
