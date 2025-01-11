---
aliases:
  - Docker Container
created: 2025-01-05T23:24:00
tags:
  - Docker
  - IT
  - DevOps
---
Container là một môi trường chạy thực, nơi ứng dụng được đóng gói và khởi động ở bên trong. Ở góc độ người dùng, `container` cũng giống như một máy ảo, cũng cần được cung cấp tài nguyên `CPU`, `RAM`, `Network`, ổ đĩa lưu trữ, biến môi trường,…

- Với `network`: `container` nằm trong một mạng lưới độc lập so với `internet` cũng như mạng `local` trên máy tính. Nên để truy cập vào ứng dụng trong `container`, chúng ta sẽ cần tạo kết nối từ máy tính vào trong `container`.
- `CPU` và `RAM` được cung cấp dựa theo yêu cầu sử dụng của ứng dụng trong `container`.
- Ổ đĩa lưu trữ cũng được cung cấp tạm thời, sẽ bị mất đi nếu không sử dụng cơ chế `volume/bind mount` của Docker để đồng bộ dữ liệu trong `container` ra ngoài máy tính.
- Biến môi trường: khi tạo ra `container`, chúng ta có thể thêm vào `container` các biến môi trường cần thiết.

## Tạo container từ image

Cú pháp:

```bash
docker run [options] <image>
```

Một số `option` thông dụng
- `--name <name>` tên container
- `-d` đưa container xuống chạy ngầm
- `-p <host_port>:<container_port>` mapping port
- `-v` tạo kết nối storage giữa host với container
    - `-v <host_path>:<container_path>` Kiểu gán thư mục với thư mục
    - `-v <volume>:<container_path>` Kiểu gán volume (do docker quản lý) với thư mục
- `-e <key>:<value>` Thiết lập biến môi trường cho ứng dụng trong container

Ví dụ đơn giản:

```bash
docker run nginx 
```

Sử dụng các `option` trong câu lệnh `docker run`:

```bash
docker run -d -p 80:80 docker/getting-started
```

![](https://i.imgur.com/3poP75p.png)

### Ví dụ: Khởi chạy ứng dụng cơ sở dữ liệu `mysql` với các yêu cầu

- Đưa `container` xuống chạy ngầm
- Mở cổng kết nối: 80 trên `host` → 80 trên `container`
- Thêm biến môi trường: `password` cho `user root`. Tên biến “MYSQL_ROOT_PASSWORD”, giá trị “mypassword”
- Đặt tên container là “mysql-4”
- Sử dụng image là “mysql:5.7”
- Kết nối `storage` giữa `host` với `container` sử dụng `volume` có tên “mysql_data”, kết nối vào trong `container` ở thư mục “/var/lib/mysql”

```bash
docker run -itd -e MYSQL_ROOT_PASSWORD=mypassword -v mysql_data:/var/lib/mysql --name mysql-4 -p 13307:3306 mysql:5.7
```

![](https://i.imgur.com/lXRwxj7.png)

## Liệt kê các container

Cú pháp:

```bash
docker container ls 
# hoặc 
docker ps
```

![](https://i.imgur.com/tBvKda7.png)

Cú pháp trên sẽ hiển thị các container ở trạng thái `running`, còn các `image` ở trạng thái khác sẽ cần tới `option -a` trong câu lệnh để hiển thị lên kết quả câu lệnh.

```bash
docker container ls -a
# hoặc
docker ps -a
```

![](https://i.imgur.com/YXOa2Os.png)

Các thành phần trong `Docker` được quản lý bởi định danh, các định danh này chính là một chuỗi các ký tự không trùng khớp nhau. Ngoài ra, bạn cũng cần để ý tới trạng thái của `container`, `running` hay `exit`?

Trong phần này, quy ước `<container>` trong các câu lệnh được hiểu là `<container_id>` hoặc `<container_name>`.

## Kiểm tra thông tin của container

Cú pháp:

```bash
docker container inspect <container>
# Hoặc
docker inspect <container>
```

Đọc các thông tin, những thông tin này là hữu ích trong quá trình `debug`, tìm ra lỗi sai của `container`.

Ví dụ:

```bash
docker inspect mysql-4 
```

![](https://i.imgur.com/TPtEJnJ.png)

## Kiểm tra log ứng dụng

Cú pháp:

```bash
docker container logs <container>
docker logs <container>
```

Ví dụ

```bash
docker logs -f mysql-4
```

![](https://i.imgur.com/EepU4Bn.png)

## Truy cập vào trong container

Cú pháp:

- Tương tác một lệnh:

```bash
docker container exec <container> <command>
# hoặc 
docker exec <container> <command>
```

- Mở `shell` kết nối tới `container`, sử dụng thêm `option -it` và truyền vào `shell` sử dụng (`sh` hoặc `bash`)

```bash
docker container exec -it <container_id> <shell>
# hoặc 
docker exec -it <container_id> <shell> 
```

Ví dụ:

```bash
docker exec -it mysql-4 sh
```

![](https://i.imgur.com/uZpifhR.png)

## Trạng thái của container

Dưới đây mô tả các trạng thái của một `container` có thể có:
- `docker create [options] <image>` : đưa container tới trạng thái `created`
- `docker start <container>` : khởi động `container` từ trạng thái `created` sang `running` hoặc từ `stopped` sang `running`
- `docker run [options] <image>` : Tạo mới `container` từ `image`
- `docker pause <container>` : tạm dừng hoạt động của `container`
- `docker unpause <container>` : chuyển đổi trạng thái cho `container` từ `paused` sang `running`
- `docker stop <container>` : tương tự như hành động `shutdown` máy tính.
- `docker rm <container>` : dùng để xóa `container`, tương tự như hành động vất máy tính vào thùng rác.

Container là một môi trường chạy ứng dụng cách ly, cung cấp các tài nguyên cần thiết như `CPU`, `RAM`, `Network`, ổ đĩa lưu trữ và biến môi trường. Các `container` được quản lý thông qua `Docker`, cho phép tạo, chạy, dừng, và xóa các `container` một cách hiệu quả. Việc sử dụng `container` mang lại lợi ích về tính linh hoạt, khả năng mở rộng, và quản lý tài nguyên, giúp tối ưu hóa việc triển khai và vận hành ứng dụng. Với kiến thức cơ bản về `Docker`, `Linux`, và `Git`, bạn có thể dễ dàng tạo và quản lý các container để phục vụ cho nhu cầu phát triển và triển khai ứng dụng của mình.

---
## References:

[Tìm hiểu Docker Container](https://tedu.com.vn/kien-thuc/bai-3-tim-hieu-docker-container-389.html)