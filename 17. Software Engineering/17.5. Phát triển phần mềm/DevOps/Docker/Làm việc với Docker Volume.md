---
aliases:
  - Docker Volume
created: 2025-01-06T00:05:00
tags:
  - Docker
  - IT
  - DevOps
---
**Docker Storage** là thành phần giúp lưu trữ bền vững các dữ liệu quan trọng ra bên ngoài `Docker Host` hoặc các phương thức lưu trữ khác.

Một số trường hợp sử dụng `volume`:
- Đưa cấu hình lưu trữ trên `docker host container`.
- Chia sẻ dữ liệu giữa `container` và `docker host`.
- Khi cần `backup`, `restore` hoặc `migrate` dữ liệu từ `docker host` sang `docker host`.

## Bind Mount

Với `bind mount`, `mount point` có thể nằm ở bất kỳ đâu trong **Docker Host**, tuy nhiên thành phần thư mục `mount point` này sẽ không được quản lý bởi **Docker**.

Cú pháp:

```bash
docker run --mount type=bind,src=<path_in_docker_host>,dst=<path_in_container> <image>
```

Cú pháp rút gọn:

```bash
docker run -v <path_in_docker_host>:<path_in_container> <image>
```

Ví dụ: Chạy `container centos` với `bind mount` giữa đường dẫn `file system`: `/opt/docker_host_folder` với đường dẫn trong `container` `/opt/mount_point`:

```bash
docker run --name bind-centos -itd -v /opt/docker_host_folder:/opt/mount_point centos
```

![](https://i.imgur.com/84ZcRLH.png)

Để kiểm tra tính đồng bộ dữ liệu giữa 2 thư mục trong và ngoài `container`, chúng ta sẽ ghi nội dung cho tệp tin trong thư mực `/opt/mount_point` của `container`:

```bash
docker exec bind-centos /bin/bash -c "echo 'new file' > /opt/mount_point/newfile.txt"
```

Tệp tin `newfile.txt` sẽ được lưu trữ hiện diện trên cả `filesystem` của **Docker Host**:

```bash
ls -al /opt/docker_host_folder
cat /opt/docker_host_folder/newfile.txt
```

![](https://i.imgur.com/wfrPCxa.png)

Ngược lại, chúng ta sẽ thử thêm mới tệp tin trên `filesystem` ở thư mực đã `mount` ra từ `container` `/opt/docker_host_folder`:

```bash
# Ở đây, bạn sẽ cần quyền của user root để ghi nội dung vào thư mục
sudo bash -c 'echo "I am in Filesystem" > /opt/docker_host_folder/message.txt'
```

Tệp tin `message.txt` sẽ xuất hiện ở trong `container` ? Hãy kiểm chứng bằng cách liệt kê các tệp tin ở `mount point` trong `container`:

```bash
docker exec bind-centos /bin/bash -c "ls -al /opt/mount_point"
```

![](https://i.imgur.com/en7xEpK.png)

## Volume Mount

Volume mount là chức năng ra đời muộn hơn so với `bind mount`, có những tính năng tốt hơn, thân thiện hơn về mặt quản lý `storage` của các `container` cho người dùng **Docker**. Bạn sẽ có một khu lưu trữ tập trung các `storage` này, và có thể đặt tên cũng như thêm các `label` cho chúng.

Về cú pháp, tương tự như với `bind mount` về phần `option` truyền vào lệnh `docker run`, điểm khác biệt nằm ở phần `mount point` trên `filesystem` của **Docker Host** sẽ được thay thế bởi tên của **Volume**.

```bash
docker run --mount type=volume,src=<volume_name>,dst=<container_path> <image>
# hoặc
docker run -v <volume_name>:<container_path> <image>
```

Ví dụ: Trước hết, chúng ta hãy tạo ra một `container` có sử dụng `volume mount` để đạt được tính bền vững lưu trữ dữ liệu:

```bash
docker run --name volume-centos -itd -v centos_volume:/opt/mount_point centos 
```

Khi `container` ở trạng thái `running`, `docker` đã tự động tạo `volume` `centos_volume` nếu nó không có trước. Bước tiếp chúng ta sẽ thêm tệp tin trong `mount point` của `container` và kiểm tra dữ liệu có được lưu trữ ra `docker volume` `centos_volume` hay không.

```bash
# Ghi file vào container
docker exec volume-centos /bin/bash -c "echo 'this is new file' > /opt/mount_point/test.txt"
```

Mặc định, khi cài đặt **Docker**, đường dẫn `var/lib/docker/volumes` là nơi lưu trữ các **Docker Volume**, hoặc bạn có thể sử dụng câu lệnh `inspect` để tìm kiếm về đường dẫn `volume` của `container`.

```bash
# Kiểm tra tệp tin trong centos_volume
sudo ls -al /var/lib/docker/volumes/centos_volume/_data
sudo cat /var/lib/docker/volumes/centos_volume/_data/test.txt
```

![](https://i.imgur.com/kF0qCP4.png)

Khi sử dụng **Docker Volume**, chúng ta cũng có thể đồng bộ các tệp tin thư mục theo 2 chiều từ ngoài vào trong hoặc từ trong ra ngoài **Container**. Tuy nhiên, **Docker** không khuyến khích việc ghi dữ liệu trực tiếp trên **Docker Volume**.

## Quản trị Volume

### Tạo mới Volume

Cú pháp:

```bash
docker volume create <volume_name>
```

Ví dụ: Tạo volume có tên my-volume

```bash
docker volume create my-volume
```

### Liệt kê Volume

Cú pháp:

```bash
docker volume ls
```

### Kiểm tra thông tin của Volume

Cú pháp:

```
docker volume inspect <volume>
```

![]()