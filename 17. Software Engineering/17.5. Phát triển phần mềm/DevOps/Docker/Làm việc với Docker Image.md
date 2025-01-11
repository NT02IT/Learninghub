---
aliases:
  - Docker Image
created: 2025-01-05T22:53:00
tags:
  - IT
  - DevOps
  - Docker
---
Image là thành phần quan trọng của Docker. Các lệnh trong Docker Engine được thực hiện thông qua CLI, nó như là 1 API tương tác các câu lệnh nhập của chúng ta từ bàn phím. Làm việc với Image chúng ta có các lệnh thao tác như: `xem`, `pull`, `push`, `save`, `load`, `delete`.

## Cấu trúc và quy ước

Cấu trúc của một Image:
- `Image name`: tên của `image`
- `Image tag`: `tag` của một `image`
- `Image digest`: chuỗi ký tự định danh cho một `image`, giá trị này là duy nhất cho một `image`

`Image` có thể viết ở các dạng sau:
- `Image` không `tag` và `digest`: `<image_name>` , vd: `mysql`
- `Image` bao gồm `tag`: `<image_name>:<image_tag>` , vd: `mysql:5.7`
- `Image` bao gồm `digest`: `<image_name>@<image_digest>` , vd: `mysql@sha256:aaa1374f1e6c24d73e9dfa8f2cdae81c8054e6d1d80c32da883a9050258b6e83`

Câu lệnh sau đây sẽ đưa ra thông tin về cách sử dụng của lệnh `docker image` để tương tác và quản lý `image`:

```bash
docker image --help
```

## Login docker hub

Đầu tiên, chúng ta sẽ vào https://hub.docker.com/ để tạo tài khoản. Sau đó vào `cmd` nhập lệnh để đăng nhập:

```bash
docker login
```

## Liệt kê danh sách image

Câu lệnh liệt kê các `image` có trên `Docker Host`:

```bash
docker image ls 
```

Hoặc câu lệnh rút gọn:

```bash
docker images
```

## Pull image

Cú pháp:

```bash
docker image pull <image>
```

Hoặc, cú pháp rút gọn:

```bash
docker pull <image>
```

Bạn sẽ tải về những `image` đầu tiền:

```bash
docker pull mysql:8.0
```

> [!NOTE] Lưu ý:
> - Khi không chỉ định image_tag, image sẽ được `Docker` mặc định gán cho `tag latest` để tìm kiếm và tải về.
> - Với `Docker`, có thể bỏ qua phần chỉ định `host` ở phía trước của `image`. Nhưng nếu tải về từ các `Docker Registry` khác, bạn sẽ cần chỉ định rõ ràng `host` của `registry` đó ở phía trước của `image_name`, hay nói cách khác, `image_name` bao gồm cả phần `host` của `registry`.

Bạn hãy tìm kiếm các image liên quan tới các môi trường chạy ứng dụng và tải chúng về `Docker Host`, hãy thử cả trường hợp không chỉ định `tag` và chỉ định `tag` (tùy ý) cho `image` tải về, tối thiểu tải về 5 `image`:
- openjdk
- node
- python

## Tag image

Tạo mới `image_tag` cho một `image`, đây là quá trình đặt tên mới(`image_name`, `image_tag`) cho một image, tuy nhiên `image` sẽ không thay đổi về `digest string`, bởi đây là giá trị cố định, giống như `UserID` của `user` trong `Linux`, mã căn cước của công dân Việt Nam.

```bash
# đầy đủ
docker image tag <image_name_src>:<image_tag_src>  <image_name_dst>:<image_tag_dst>
# rút gọn:
docker tag <image_name_src>:<image_tag_src>  <image_name_dst>:<image_tag_dst>
```

Ví dụ:

```bash
docker image tag mysql:8.0 my-mysql:v1
```

## Push image

Cú pháp:

```bash
docker image push <image>
```

Cú pháp rút gọn:

```bash
docker push <image> 
```

Hãy thử `push image` bất kỳ:

```bash
docker push mysql:5.7
docker push my-mysql:v1
```

> [!NOTE]
> Câu lệnh `push` này sẽ không được thực hiện thành công, vì bạn không có quyền cho những `image` và `repository` này. Bạn chỉ có quyền cho `repository` cá nhân của mình trên `Docker Hub`, bởi vậy chúng ta cần 1 bước trước khi thực hiện `push image` tới tài khoản cá nhân.

B1. Đánh tag cho image về repo cá nhân, ở đây image mới sẽ có dạng `<username>/<image_name>:<image_tag>`

```bash
docker tag mysql:5.7 <username>/my-mysql:v1
# ví dụ: $ docker tag mysql:5.7 orezfu/my-mysql:v1
```

B2. Push image lên Docker Hub như thông thường

```bash
docker push my-mysql:v1
```

## Save image

Lưu trữ image về dạng filesystem

```bash
docker image save <image1> [<image2> ...] -o <file_name>
```

Ví dụ:

```bash
docker image save nginx:1.23.4 -o nginx.tar
docker image save  mysql:5.7  -o database.tar
```

## Load image

Đảo ngược của quá trình save image, tải file image vào Docker Host từ filesystem trên Linux

```bash
docker image load -i <file_name>
```

Ví dụ:

```bash
docker image load -i nginx.tar
docker image load -i database.tar  
```

## Delete image

Để xóa một image sẽ sử dụng câu lệnh sau:

```bash
docker image rm <image>
```

Hoặc, rút gọn câu lệnh:

```bash
docker rmi <image>
```

Ví dụ:

```bash
docker image rm nginx:1.23.4
docker rmi mysql:5.7
```

> [!NOTE]
> Có một điểm cần lưu ý, nếu có nhiều image cùng trỏ tới cùng một image_digest, tức là image đó có nhiều tag, câu lệnh xóa image sẽ chỉ xóa tag - tức là xóa tên của image, tới khi xóa image với tag cuối cùng trỏ tới digest thì mới thực sự xóa image khỏi Docker Host. Ví dụ, có 2 image `nginx:v1` và `nginx:v1.2` được tag từ `nginx:v1`, 2 image này sẽ có cùng digest `sha256:adfjiser...`, khi bạn xóa image `nginx:v1` , image thực sự vẫn tồn tại trên Docker Host, tuy nhiên bạn chỉ thấy còn tồn tại `nginx:v1.2` , tới khi bạn xóa `nginx:v1.2` thì image sẽ thực sự bị xóa khỏi Docker Host.

---
## References:

[Làm việc với Docker Image](https://tedu.com.vn/kien-thuc/bai-2-lam-viec-voi-docker-image-388.html)