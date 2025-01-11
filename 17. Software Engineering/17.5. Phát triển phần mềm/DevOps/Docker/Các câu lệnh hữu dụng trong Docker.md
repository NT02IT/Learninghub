---
created: 2025-01-04T19:05:00
tags:
  - Docker
  - IT
  - DevOps
  - DockerPrompt
---

| Prompt                                 | Mục đích                                                                                                                                                                                                                                         |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `docker ps `                           | Liệt kê danh sách containers đang chạy                                                                                                                                                                                                           |
| `docker ps -a`                         | Liệt kê danh sách tất cả các container kể cả đã stop                                                                                                                                                                                             |
| `docker pull`                          | Tải một Docker image từ Docker Hub registry. Link của nó các bạn có thể vào Docker Hub để lấy. Hãy search từng image rồi vào chi tiết của chúng để xem.                                                                                          |
| `docker build`                         | Được dùng để tạo ra một image dựa trên một file Dockerfile. Thường dùng `docker build .` để build một image dựa trên Dockerfile trong thư mục hiện tại. `docker build -t "myimage:latest"` dùng để tạo một image và lưu image dưới tên được đặt. |
| `docker images` hoặc `docker image ls` | Hiển thị danh sách image ở máy bạn                                                                                                                                                                                                               |
| `docker run`                           | Chạy một container từ một image, i.e. `docker run myimage -it bash`. Nếu không có image nào được tìm thấy thì Docker run sẽ download nó tự động ở Docker hub.                                                                                    |
| `docker logs`                          | Hiển thị logs của một container mà bạn chỉ ra. Để tiếp tục show log được cập nhật thêm thì bạn chỉ cần dùng `docker logs -f mycontainer`                                                                                                         |
| `docker volume ls`                     | Hiển thị danh sách volumes, cái này dùng để lưu trữ dữ liệu trong container, tránh trường hợp restart container thì mất dữ liệu.                                                                                                                 |
| `docker network ls`                    | Liệt kê tất cả các network có sẵn.                                                                                                                                                                                                               |
| `docker network connect`               | Vào một network. Nó giúp container giao tiếp được với một container khác qua tên thay vì IP.                                                                                                                                                     |
| `docker rm`                            | Loại bỏ một hoặc nhiều container. Ví dụ: `docker rm mycontainer` nhưng chắc chắn là container đang không ở trạng thái running.                                                                                                                   |
| `docker rmi`                           | Xóa bỏ một hay nhiều image. `docker rmi myimage`, xóa image tên là myimage nhưng phải đảm bảo không có container nào đang chạy sử dụng image này.                                                                                                |
| `docker stop`                          | Stop một hay nhiều container. `docker stop mycontainer` stop 1 container trong khi `docker stop $(docker ps -a -q)` stop tất cả các container đang chạy.                                                                                         |
| `docker start`                         | Start một container đã được stop với trạng thái giữ nguyên.                                                                                                                                                                                      |
| `docker update --restart=no`           | Cập nhật một cài đặt container, nó đặc biệt hữu ích khi container của bạn lặp liên tục.                                                                                                                                                          |
| `docker cp`                            | Copy các file từ một container đang chạy ra ngoài host. `docker cp :/etc/file` để copy /etc/file ra thư mục hiện tại.                                                                                                                            |

## Một số kết hợp câu lệnh hữu ích

- Stop toàn bộ các container `docker kill $(docker ps -q)`
- Xóa toàn bộ các container `docker rm $(docker ps -a -q)`
- Xóa toàn bộ các image `docker rmi $(docker images -q)`
- Xóa và stop một container bị lặp vô tận `docker update --restart=no && docker stop`
- Chạy câu lệnh bên trong container `docker exec -i -t /bin/bash` – nếu không có bash thì dùng /bin/sh
- Chạy bash với user root nếu container đang chạy với một user khác `docker exec -i -t -u root /bin/bash`
- Xóa các image không được dùng bởi bất kỳ container nào và không được tag `docker image prune`
- Xóa toàn bộ các image không sử dụng `docker image prune -a`
- Xóa các container đã được tạo trong vòng 24h `docker image prune -a --filter "until=24h"`
- Xóa toàn bộ các container không chạy `docker container prune`

---
## References:

[Các câu lệnh hữu dụng trong Docker mà bạn cần nhớ](https://tedu.com.vn/kien-thuc/cac-cau-lenh-huu-dung-trong-docker-ma-ban-can-nho-295.html)