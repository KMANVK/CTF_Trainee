# Đề Bài : Fix ảnh và xem được (Bai1.png)

## Giải : 

### Em fix lại như sau : 
+ 1.Signature: CF 50 22 26 0D 6D 61 72 -> 89 50 4E 47 0D 0A 1A 0A
+ 2.Chunk IHDR : 49 78 44 20 -> 49 48 44 52
+ 3.Chunk IDAT đầu tiên : 49 44 41 0B -> 49 44 41 54
![image](https://user-images.githubusercontent.com/94669750/219335627-db9fea29-b0c7-4ea8-b7ae-da23c0f4303e.png)
+ 4.Trailer: 49 45 7A 2A AE 42 04 82 -> 49 45 4E 44 AE 42 60 82
![image](https://user-images.githubusercontent.com/94669750/219336796-df2496a6-e716-4d59-b664-c0259570c030.png)

### Và xem được ảnh : 
![Bai1](https://user-images.githubusercontent.com/94669750/219337161-723ed01c-de97-4ba5-b68f-63cecd93341f.png)