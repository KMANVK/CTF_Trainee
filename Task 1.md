# ------ ***Task 1*** ------

# I.Khái Niệm Cơ Bản Về Forensics :
## _Computer Forensics hay còn gọi là điều tra số là công việc phát hiện, bảo vệ và phân tích thông tin được lưu trữ, truyền tải hoặc được tạo ra bởi một máy tính hoặc mạng máy tính. Nhằm đưa ra những suy luận hợp lý để tìm nguyên nhân, giải thích những hiện tượng trong suốt quá trình điều tra.
# II.Các Type of Foren : 
 ## 1.Image file format analysis : file image(file.png,file.jpg)
 * Một hình ảnh pháp y (forensic copy) là bản sao trực tiếp từng bit, từng khu vực của một thiết bị lưu trữ vật lý, bao gồm tất cả các tệp, thư mục và không gian chưa phân bổ,  trống và chùng . Hình ảnh pháp y không chỉ bao gồm tất cả các tệp hiển thị với hệ điều hành mà còn cả các tệp đã xóa và các phần tệp còn lại trong không gian trống và chùng.  

* Hình ảnh pháp y là một thành phần của  pháp y máy tính , là ứng dụng của các kỹ thuật điều tra và phân tích trên máy tính để thu thập bằng chứng phù hợp để trình bày trước tòa án.

* Không phải tất cả phần mềm chụp ảnh và  sao lưu đều  tạo ra hình ảnh pháp y. Ví dụ: sao lưu Windows tạo các bản sao lưu hình ảnh không phải là bản sao hoàn chỉnh của thiết bị vật lý. Hình ảnh pháp y có thể được tạo thông qua phần mềm pháp y chuyên dụng. Một số tiện ích hình ảnh đĩa không được bán trên thị trường để sử dụng pháp y cũng tạo ra  hình ảnh đĩa hoàn chỉnh .

* Trong trường hợp tội phạm mạng , bằng chứng bổ sung có thể được phát hiện ngoài những gì có sẵn thông qua hệ điều hành dưới dạng dữ liệu buộc tội đã bị  xóa  để ngăn chặn việc khám phá. Trừ khi dữ liệu được xóa và ghi đè một cách an toàn, dữ liệu thường có thể được khôi phục bằng phần mềm pháp y hoặc phần mềm khôi phục tệp.

* Tạo và sao lưu hình ảnh pháp y giúp tránh mất dữ liệu do lỗi ổ đĩa gốc. Việc mất dữ liệu làm bằng chứng có thể gây bất lợi cho các trường hợp pháp lý. Hình ảnh pháp y cũng có thể ngăn chặn việc mất các tệp quan trọng nói chung.
### Một Số Dạng Về Image file format analysis: 
+ Dạng cat image: https://play.picoctf.org/practice/challenge/186?category=4&page=1 
+ Dạng bài Binwaik: https://ctflearn.com/challenge/108 
* Dùng Lệnh: binwalk --dd='.*' filename (will Extract type signatures, give the files an extension of ext, and execute cmd)
+ Dạng chỉnh sửa file image( hex.it):
* Dựa vào list of file signatures để chỉnh sửa file bằng hxd (https://en.wikipedia.org/wiki/List_of_file_signatures)

+ Dạng chỉnh độ dài và rộng của file image: 
   * Với file.png => Dùng tweak png để chỉnh sửa
   * Với file.jpg => Dùng hex.it để chỉnh sửa 
 ### * Tools : zsteg,steghide,Outguess,Strings,ExifTool,Stegsolve,Repair image online too,Foremost,Binwalk,hexed.it,pngcheck,file, grep, cat,Stegsnow,stegsekk,stegcracker.
 ## 2.Steganography : 
 * Kỹ thuật giấu tin hay kỹ thuật giấu thư, kỹ thuật ẩn mã là nghệ thuật và khoa học về việc viết và chuyển tải các thông điệp một cách bí mật, sao cho ngoại trừ người gửi và người nhận, không ai biết đến sự tồn tại của thông điệp, là một dạng của bảo mật bằng cách che giấu.
 * Việc sử dụng thuật ngữ này được ghi lại lần đầu tiên là vào năm 1499 bởi Johannes Trithemius trong tác phẩm Steganographia của ông , một chuyên luận về mật mã và kỹ thuật giấu tin, được cải trang thành một cuốn sách về phép thuật. Nói chung, các thông báo ẩn dường như là (hoặc là một phần của) thứ gì đó khác: hình ảnh, bài viết, danh sách mua sắm hoặc một số văn bản bìa khác. Ví dụ: thông điệp ẩn có thể được viết bằng mực vô hình giữa các dòng có thể nhìn thấy của một bức thư riêng. Một số triển khai của kỹ thuật giấu tin không có bí mật chung là các hình thức bảo mật thông qua che khuất và các sơ đồ giấu tin phụ thuộc vào khóa tuân thủ nguyên tắc của Kerckhoffs . 

* Ưu điểm của kỹ thuật giấu tin so với kỹ thuật mã hóa đơn thuần là thông điệp bí mật dự định không thu hút sự chú ý đến chính nó như một đối tượng để xem xét kỹ lưỡng. Các tin nhắn được mã hóa có thể nhìn thấy rõ ràng , cho dù chúng không thể phá vỡ được như thế nào, khơi dậy sự quan tâm và bản thân chúng có thể bị buộc tội ở các quốc gia nơi mã hóa là bất hợp pháp. 

* Trong khi mật mã là thực hành bảo vệ nội dung của một tin nhắn, thì kỹ thuật giấu tin liên quan đến việc che giấu sự thật rằng một tin nhắn bí mật đang được gửi và nội dung của nó.

* Steganography bao gồm việc che giấu thông tin trong các tập tin máy tính. Trong steganography kỹ thuật số, thông tin liên lạc điện tử có thể bao gồm mã hóa steganographic bên trong lớp vận chuyển, chẳng hạn như tệp tài liệu, tệp hình ảnh, chương trình hoặc giao thức. Các tệp phương tiện lý tưởng cho việc truyền dữ liệu ẩn vì kích thước lớn của chúng. Ví dụ: người gửi có thể bắt đầu với một tệp hình ảnh vô thưởng vô phạt và điều chỉnh màu của mỗi pixel thứ một trăm để tương ứng với một chữ cái trong bảng chữ cái. Sự thay đổi tinh tế đến mức một người không đặc biệt tìm kiếm nó khó có thể nhận thấy sự thay đổi.
* Các Kỹ Thuật Trong Steganography : 
* 1.Tin Nhắn Kỹ Thuật Số
* 2.Văn bản Kỹ Thuật Số
* 3.Ẩn hình ảnh trong tệp âm thanh 
* 4.Sử dụng câu đố
* 5.Mạng
* 6.Bản In
 ### Tools : Stegsnow,stegsekk,stegcracker,steghide và cx có thể dùng 1 số tool giống như các mảng khác
 ### Dạng Bài :
+ Dạng Bài Về Exiftool Và GPS : (challenge) https://www.root-me.org/en/Challenges/Steganography/EXIF-Metadata
* Dùng Lệnh : exiftool filename 
  ![exiftool](https://user-images.githubusercontent.com/94669750/217408069-9b289af9-9542-47fd-b99a-829fd04699ed.png)
* => t thấy được GPS của file và đưa lên https://www.gps-coordinates.net để kiếm vị trí và có flag
+ Dạng WAV - Noise analysis : (challenge) https://www.root-me.org/en/Challenges/Steganography/WAV-Noise-analysis
* Dùng Audacity để phân tích : giảm tốc độ phát lại xuống hết cỡ, sau đó chuyển sang hiệu ứng và phát ngược lại và chú ý nghe từng (chữ đó là cờ) 
  ![audacity](https://user-images.githubusercontent.com/94669750/217409860-7e317ec7-76c8-4ef5-a76e-05b502e3e779.png)
+ Dạng về whitespace : (challenge) https://www.root-me.org/en/Challenges/Steganography/Poem-from-Space
* Xem nội dung e nhận thấy có khác nhiều khoảng trắng trong bài thơ :
![image](https://user-images.githubusercontent.com/94669750/217411379-6f615d20-04ca-47ea-8afb-56f3b91a4171.png)
* E xóa tất cả các ký tự và để lại những khoảng trống sau những chữ cuối cùng của mỗi dòng và decode bằng wed on(https://www.dcode.fr/whitespace-lingu)
![decode](https://user-images.githubusercontent.com/94669750/217413432-9ec12db3-c608-4142-a4d5-eef1b74108ce.png)
+ Dạng tìm thông tin ẩn trong file PDF :(challenge) https://www.root-me.org/en/Challenges/Steganography/PDF-Embedded
* Dùng strings để đọc file thì nhận thấy vẫn còn nhiều file bị ẩn trong đó nên e quyết định giải nén file và gộp nó vào thành 1 file pdf bằng lệnh : 
***qpdf --stream-data=uncompress epreuve_BAC_2004.pdf uncompressed.pdf***
* Sau khi giải nén, e dùng trings đọc file vừa giải nén thì thấy mã base64 nhưng e nghĩ đây là tệp nhúng đc mã hóa base64 :
![image](https://user-images.githubusercontent.com/94669750/217417500-db42a6ea-7461-4d91-ae64-e5b267d1fe0a.png)
* => e decode mã đó ra bằng wed on(https://base64.guru/converter/decode/file) :
![image](https://user-images.githubusercontent.com/94669750/217417271-5cee6b43-2d60-4226-8bdf-39b813deda17.png)
* Và e nhận đc 1 file ảnh và chứa cờ.
+ Dạng Bài Về QSSTV :(challenge) https://play.picoctf.org/practice/challenge/26?category=4&page=3
* Đề bài cho mình 1 file wav và e dùng audacity và Sonic Visualiser để kiểm tra nhưng cũng ko phát hiện điều gì đặc biệt 
* Đọc kỹ đề bài cùng với gợi ý thì e nghĩ sẽ có một tool nào đó liên quan đến nó và tra gg e tìm được 1 tool đc gọi là QSSTV (tìm hiểu và đọc sơ lược qua 1 lần thì theo suy nghĩ đơn giản của e tool này dùng để decode file wav sang file image) 
* Và e bắt đầu cài đặt nó(https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04) và dùng 
![qsstv](https://user-images.githubusercontent.com/94669750/217425590-c739a6f3-00d9-4efa-a8ee-4309442171d2.png)
## 3. Network Forensics : 
* Pháp y mạng là một nhánh phụ của pháp y kỹ thuật số liên quan đến việc giám sát và phân tích lưu lượng mạng máy tính nhằm mục đích thu thập thông tin, bằng chứng pháp lý hoặc phát hiện xâm nhập. Không giống như các lĩnh vực pháp y kỹ thuật số khác, điều tra mạng xử lý thông tin biến động và năng động.
* Điều tra mạng là một danh mục con của điều tra kỹ thuật số, về cơ bản liên quan đến việc kiểm tra mạng và lưu lượng truy cập của mạng đi qua một mạng bị nghi ngờ có liên quan đến các hoạt động độc hại và điều tra mạng đó, chẳng hạn như một mạng đang phát tán phần mềm độc hại để đánh cắp thông tin đăng nhập hoặc để mục đích phân tích các cuộc tấn công mạng. Khi internet phát triển, tội phạm mạng cũng phát triển cùng với nó và tầm quan trọng của điều tra mạng cũng vậy, với sự phát triển và chấp nhận các dịch vụ dựa trên mạng như World Wide Web, e-mail và các dịch vụ khác.

* Với sự trợ giúp của điều tra mạng, toàn bộ dữ liệu có thể được truy xuất bao gồm tin nhắn, chuyển tệp, e-mail, lịch sử duyệt web và được xây dựng lại để hiển thị giao dịch ban đầu. Cũng có thể tải trọng trong gói lớp trên cùng có thể xuất hiện trên đĩa, nhưng các phong bì được sử dụng để phân phối nó chỉ được ghi lại trong lưu lượng mạng. Do đó, dữ liệu giao thức mạng kèm theo mỗi hộp thoại thường rất có giá trị.

* Để xác định các cuộc tấn công, điều tra viên phải hiểu các giao thức và ứng dụng mạng như giao thức web, giao thức Email, giao thức Mạng, giao thức truyền tệp, v.v.
* Các nhà điều tra sử dụng pháp y mạng để kiểm tra dữ liệu lưu lượng truy cập mạng được thu thập từ các mạng có liên quan hoặc bị nghi ngờ có liên quan đến tội phạm mạng hoặc bất kỳ loại tấn công mạng nào . Sau đó, các chuyên gia sẽ tìm kiếm dữ liệu hướng đến bất kỳ thao tác tệp nào, giao tiếp của con người, v.v. Với sự trợ giúp của pháp y mạng, nói chung, các nhà điều tra và chuyên gia tội phạm mạng có thể theo dõi tất cả các giao tiếp và thiết lập các mốc thời gian dựa trên các sự kiện mạng nhật ký được ghi lại bởi NCS.

* Các quy trình liên quan đến pháp y mạng:
* +Một số quy trình liên quan đến pháp y mạng được đưa ra dưới đây:

* 1. Nhận dạng: Trong quá trình này, các nhà điều tra xác định và đánh giá sự cố dựa trên các con trỏ mạng.
* 2. Bảo vệ: Trong quá trình này, các điều tra viên bảo quản và bảo mật dữ liệu để có thể ngăn chặn việc tiết lộ dữ liệu.
* 3. Tích lũy: Trong bước này, một báo cáo chi tiết về hiện trường vụ án được ghi lại và tất cả các mảnh bằng chứng kỹ thuật số đã thu thập được sao chép.
* 4. Quan sát: Trong quá trình này, tất cả dữ liệu hiển thị được theo dõi cùng với siêu dữ liệu.
* 5. Điều tra: Trong quá trình này, kết luận cuối cùng được rút ra từ các mảnh bằng chứng thu thập được.
* 6. Tài liệu: Trong quá trình này, tất cả các mẩu bằng chứng, báo cáo, kết luận đều được ghi lại và trình bày trước tòa.
* Những thách thức trong Network Forensics:  
* 1. Thách thức lớn nhất là quản lý dữ liệu được tạo ra trong quá trình này.
* 2. Ẩn danh nội tại của IP.
* 3. Giả mạo địa chỉ.
* +Thuận lợi:
* 1.Điều tra mạng giúp xác định các mối đe dọa và lỗ hổng bảo mật.
* 2.Nó phân tích và giám sát nhu cầu hiệu suất mạng.
* 3.Điều tra mạng giúp giảm thời gian chết.
* 4.Tài nguyên mạng có thể được sử dụng theo cách tốt hơn bằng cách báo cáo và lập kế hoạch tốt hơn.
* 5.Nó giúp tìm kiếm mạng chi tiết bất kỳ dấu vết bằng chứng nào còn sót lại trên mạng.
* +Điều bất lợi:
* Nhược điểm duy nhất của điều tra mạng là khó thực hiện.
### Tools : wireshark, tshark, tcpdump,Network Miner,Splunk,Snort(https://resources.infosecinstitute.com/topic/network-forensics-tools/)
### Dạng Bài : 
### + Dạng Phân tích bằng wireshark : 1 challenge e làm ở giải warnagame 2021
![challenge](https://user-images.githubusercontent.com/94669750/217436164-5ba35c07-d8c7-4f45-a54e-a966292fdaba.png)

* Sử dụng wireshark để phân tích thì e nhận thấy phần info có điều bất thường :vv
![image](https://user-images.githubusercontent.com/94669750/217436908-4586d4bb-fc77-4429-b2f9-2f2a7ac4e7c1.png)
* Dễ nhận thấy ID chỉ thay đổi 2 số đầu và vẫn giữ nguyên 2 số cuối là 57 và e sử dụng lệnh để kiểm tra nó : ***tshark -r Message.pcapng -Y “ip.dst==192.168.47.1” -T fields -e ip.id | cut -c 7-8 | xxd -p -r***
* Và e thấy mã base64 và nó đó là 1 tệp nhúng đã đc mã hóa bằng base64 
* E decode nó ra (https://base64.guru/converter/decode/file) và nhận đc 1 file zip
* Extract file e nhận đc 1 file flag.cpt
* Lúc đầu e cx ko bt file .cpt là gì nên đã tra gg và tìm đc nó là dạng Raster Image Files và em tiếp tục tìm kiếm cách để khai thác nó 
* Và e tìm thấy đc lệnh ccrypt có thể giải mã file đó ra và e đã sử dụng : ***ccrypt -d flag.cpt***
* Nhưng nó bắt nhập pass thì e lại quay đề để đọc 1 lần nx và thấy secret_message rất đang nghi ngờ nên đã nhập nó vào và đã đúng :)))
* Và e nhận đc 1 mã QR và quét nó e nhận đc flag.
### + Dạng Về sử lệnh tshark để phân tích dữ liệu : 1 challenge e chơi ở giải BlackHat Mea CTF 2022
![challenge](https://user-images.githubusercontent.com/94669750/217503693-8d562d4a-ad8f-4ac1-851f-166db740e96d.png)

* Ban đầu e sử dụng wireshark để phân tích thì thấy dữ liệu phân mobus.data có 2 thông số : 0000 và ff00 
![image](https://user-images.githubusercontent.com/94669750/217504333-144527a6-8bd5-4ad1-91da-abb6d83dfaa4.png)
![image](https://user-images.githubusercontent.com/94669750/217504504-53a601ac-17a4-4f2f-ac19-52caf1484c8a.png)
* => E liền liên tưởng đến một mã rất hay dùng đó là binary, nên e đã extract tất cả 2 thông số ở mobus.data đó có trong file ra thành 1 file.txt :
* E sử dụng câu lệnh : tshark -r file_name -T fields -e Thanh dữ liệu cần xuất -Y "điều kiện của dữ liệu" : ***tshark -r bus.pcap -T fields -e modbus.data -Y "modbus != 0 and tcp.dstport == 502" > binary.txt***
* Sau khi extract nó ra e dùng notepad để đổi 0000 -> 0 và ff00 -> 1 và decode binary ,cuối cùng e nhận đc cờ.
### Dạng Bài Về sử dụng wiresshark phân tích kết hợp crack file zip và dùng oletools : 1 challenge trong TTV KCSC 2023 vừa qua (challenge FINAL DESTINATION )
![challenge](https://user-images.githubusercontent.com/94669750/217521090-96e1ac33-c2a6-49e1-95b4-0232316a32c8.png)

* Dùng wireshark để phân tichs thì khi xem dữ liệu của protocol  thì e chú ý đến phần Data thì nhận thấy protocol SMB2 chiếm đến 85% nên e export :
![image](https://user-images.githubusercontent.com/94669750/217516453-f6faaec1-c876-4306-b87f-72f77739e6da.png)
![image](https://user-images.githubusercontent.com/94669750/217519198-fd3cc33a-eb15-48d9-a491-734ce9ff2abb.png)
* E nhận thấy có 1 file zip nhưng nó bắt nhập pass nên em nghĩ đến 1 tool crack pass zip rất tốt là : ***john ripper***
* ![image](https://user-images.githubusercontent.com/94669750/217890107-0c9d558a-34db-40c3-947a-c8abb80e28a8.png)
* Khi cat file thì e thấy cx ko có gì đặc biệt : 


![image](https://user-images.githubusercontent.com/94669750/217522850-9c22063c-263b-47ca-9666-1b90b20ab8b0.png)
* Sau đó e dùng hint thứ 2 là oletool , sau đó e tra gg và biết 1 công cụ trong oletool có liên quan đến file .rtf là : ***rtfobj*** dùng để trích xuất các đối tượng được nhúng từ các tệp RTF.
* Và e dùng lệnh : rtfobj file.rtf thì nhận đc 1 URL dẫn đến anotepad : 
![image](https://user-images.githubusercontent.com/94669750/217520379-303b4dd8-5939-49a6-836f-81647ed591b8.png)
* Và e nhận đc flag ở đó.
## 4. Disk Forensics :
* Điều tra đĩa là khoa học trích xuất thông tin điều tra từ phương tiện lưu trữ kỹ thuật số như Đĩa cứng, thiết bị USB, thiết bị Firewire, CD, DVD, ổ đĩa Flash, đĩa mềm, v.v. Quá trình điều tra đĩa là :
* 1.Xác định bằng chứng kỹ thuật số
* 2.Nắm bắt & thu thập bằng chứng
* 3.Xác thực bằng chứng
* 4.Bảo quản bằng chứng
* 5.Phân tích bằng chứng
* 6.Báo cáo kết quả
* Dữ liệu được khôi phục được phân tích bằng các công cụ pháp y mới nhất để đảm bảo rằng bằng chứng liên quan cụ thể cho trường hợp được khôi phục, phân tích và báo cáo phù hợp với yêu cầu của khách hàng.

* Việc kiểm tra, phân tích và báo cáo pháp y được thực hiện phù hợp với khả năng chấp nhận bằng chứng kỹ thuật số và mức độ phù hợp với các quy định pháp lý. Các dịch vụ hỗ trợ kiện tụng và lời khai của chuyên gia pháp y cũng được cung cấp theo yêu cầu.
tài liệu
### Tools : AccessData FTK Imager,Registry Viewer,Autopsy
### Dạng Bài :
### + Dạng Bài Strtings: (challenge) https://play.picoctf.org/practice/challenge/113?category=4&page=2
* Bài này theo đề bài thì e dùng lệnh đầu tiên sẽ là strings để xem nội dung và kèm theo đó là lệnh grep để tìm cụm từ mình muốn tìm : ***strings file_name | grep"pico"
![image](https://user-images.githubusercontent.com/94669750/217767818-241ab08f-0a93-4c59-b606-6caa5af767e4.png)
### + Dạng Bài Tìm Hostname và Time : Bài DIsk 1 (trong TTV KCSC 2023) :
![image](https://user-images.githubusercontent.com/94669750/217769582-26828620-c2b2-4504-b21e-42bbf775f968.png)
* Bài này lúc đầu e dùng accessData để xem thì phát hiện trong thùng rác có khác nhiều dữ liệu (tổng cộng có 7 file) và cộng thêm đề bài có đề cập đến xóa thư mục nên e đã xem từng file và phát hiện có 2 file chứa mã base64 
* Decode ra thì thấy 1 file dẫn về link nhạc còn 1 file là : ***Cause_I'd_die_for_you_You_know_I'd_still_die_for_you***
![image](https://user-images.githubusercontent.com/94669750/217773250-c06a8442-ef5b-4322-9c65-0f6863e65304.png)
* Đề bài có nói đến name file nên e có chú ý đến 1 file ở trong recycle bin : C:\Users\k137\Desktop\Kaceetce.txt
* => file name là Kaceetce.txt
![image](https://user-images.githubusercontent.com/94669750/217773903-ecd00797-7dfd-402a-9475-f12107604fef.png)
* Đề bài có hỏi host name của desktop nên e nghĩ có 1 subkey nào đó liên quan đến nó và e tìm thấy subkey đó là system ở access và export nó ra 
* E dùng Registy Viewer để xem subkey và theo đường dẫn ControlSet001/Control/ComputerName e lấy đc host name của nó : ***6MS14UO***
![image](https://user-images.githubusercontent.com/94669750/217776310-3d3c1ef8-6639-410b-8cc3-8d9cc038d2b0.png)
* Và Tương tự như cách tìm host name, em tìm đc time theo đường dẫn ControlSet001/Control/TimeZoneInformation : ***SE Asia standard time***
![image](https://user-images.githubusercontent.com/94669750/217777629-051994ca-43e8-4fbf-9e04-0bf261c37827.png)
* Kết hợp tất cả những ý trên và e có đc flag.
### + Dạng Bài Tìm Build Number và dựa vào brower history để tìm content : Bài Disk 2 :
![image](https://user-images.githubusercontent.com/94669750/217778587-6f170fbd-9250-4b0d-883a-e7900731a3f3.png)
* Đối với bài này lúc đầu e cx dùng acess để xem nhưng cx ko có gì đặc biết vì e cx ko hiểu gì về Build Number nên đã tra gg 
* Thì e tìm đc Subkey SOFTWARE cũng chứa một subkey Windows mô tả các chi tiết UI khác nhau của hệ điều hành, một subkey Classes nêu chi tiết những chương trình nào được liên kết với phần mở rộng file, v.v…(chi tiết : https://athena.edu.vn/tim-hieu-ve-hkey_local_machine-hklm-registry-hive/)
* Và e dùng access để kiếm subkey đó và export nó ra, mở bằng Registry Viewer
* Theo đường dẫn WOW6432Node->Microsoft->Windows NT->CurrentVersion -> e thấy được tên ver win là win 10 home single languge, với display ver là 21H1.
![image](https://user-images.githubusercontent.com/94669750/217783624-23b7a272-0475-4415-8c11-e003ba6ceed9.png)
* => find build number của máy tại đây :https://learn.microsoft.com/en-us/windows/release-health/release-information => 19043
![image](https://user-images.githubusercontent.com/94669750/217783772-4fc813bd-0af4-41d9-8212-1dda13a0e2d0.png)
* Dựa vào hint "Browser History", tra gg thì nó có liên quan tới Cache Data,e lại dùng access để tìm kiếm subkey về nó và theo đường dẫn root->user->k137->AppData->Local->Microsoft->Edge->User Data->Default->Cache->Cache_Data e đã tìm đc và đã export nó ra 
* Và tìm kiếm cộng cụ để xem đc nó thì có 1 công cụ là : ChromeCacheViewer 
* E thả vào đó và xem , xem 1 lúc e cx ko biết nó chưa gì trong đó vì có khác nhiều content type khác nhau nhưng đa số thì html chiếm ưu thế nên e đã xem nó và sau nhiều lú cái con mắt thì cuối cùng e cũng tìm đc 1 wed(text/html) dẫn đến 1 pastebin https://pastebin.com/XaxSi1c1
* E thấy trang chứa 4 file : ![image](https://user-images.githubusercontent.com/94669750/217786663-3308dde0-edd8-4284-9c0c-817d9e712a24.png)
* Đọc từng file thì e thấy có 2 file bắt nhập pass thì e nhớ lại ở thùng rác có 1 key ở đó :
![image](https://user-images.githubusercontent.com/94669750/217799182-2da26398-5ef9-4f73-b27d-6122b0830dea.png)
* Và e nhập pass vào thì nhận đc 1 mã base64 :
![image](https://user-images.githubusercontent.com/94669750/217799874-893f7523-1d9c-4cfa-bb9d-a4ed3f1a3169.png) 
* => decode nó ra và e nhận đc content 
* Ghép tất cả lại và e có đc flag
## 5.Memory Forensics (phần này e còn hơi yếu ạ): 
* Phân tích bộ nhớ hoặc Điều tra bộ nhớ là quá trình phân tích dữ liệu dễ bay hơi từ các kết xuất bộ nhớ máy tính. Với sự ra đời của phần mềm độc hại “fileless”, việc tiến hành phân tích pháp y kỹ thuật số ngày càng trở nên khó khăn hơn. Phân tích bộ nhớ không chỉ giúp giải quyết tình huống này mà còn cung cấp thông tin chi tiết độc đáo trong thời gian chạy hoạt động của hệ thống: kết nối mạng mở, các lệnh được thực thi gần đây và khả năng xem bất kỳ tệp độc hại nào đã được giải mã.
* Phần mềm độc hại Fileless :
* Bộ nhớ có thể được coi là hai loại, chính và phụ. Bộ nhớ chính không ổn định nghĩa là nó không giữ lại bất kỳ thông tin nào sau khi thiết bị tắt nguồn. Thiết bị bộ nhớ chính được biết đến nhiều nhất là bộ nhớ truy cập ngẫu nhiên (RAM). Bộ nhớ thứ cấp tham chiếu đến các thiết bị bộ nhớ lưu giữ thông tin mà không cần nguồn điện liên tục. Các thiết bị như ổ đĩa cứng (HDD) xuất hiện trong tâm trí. Phần mềm độc hại không có tệp lợi dụng các thuộc tính của bộ nhớ chính và tiến hành các hoạt động bên trong chúng, do đó chúng không có tệp vì chúng không được ghi vào bất kỳ thiết bị bộ nhớ thứ cấp nào. Fileless malware sử dụng các chiến thuật như Command and Scripting Interpreter (T1059) [4] thông qua việc sử dụng powershell, python, unix shell và visual basic để đạt được điều này. Các phương pháp pháp y kỹ thuật số truyền thống sẽ gặp khó khăn trong việc đánh giá loại phần mềm độc hại này.
### Tool : Volatility
### Dạng Bài :
* +Dạng Phân tích Bộ nhớ Bằng Volatility : 
* E thường sử dụng lệnh để xem thông tin máy chủ như : ***volatility -f file_name imageinfo***
* Sau khi biết đc thông tin của máy thì thường dùng đến profile và hivelist để biết thêm thông tin chi tiết (và hữu ích) về tổ chức đăng ký và vị trí trong RAM  : ***volatility -f file_name --profile=win_____ hivelist***



