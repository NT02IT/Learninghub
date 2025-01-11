---
aliases:
  - Docker là gì?
  - Docker
created: 2025-01-04T18:41:00
tags:
  - DevOps
  - IT
  - Docker
  - glossary
---
## Docker là gì?

Docker là một công nghệ containerization. Nó cho phép chúng ta đóng gói toàn bộ phần mềm thành 1 khối bao gồm **mã nguồn** phần mềm đã biên dịch, các **thành phần kèm theo** (depedencies) và **môi trường thực thi**. Điều này giúp giảm rủi ro trong việc deployment đó là sự khác nhau giữa các môi trường thực thi. Ngày xưa chúng ta phải quan tâm đến việc đó, còn giờ thì đã có Docker lo.

![Virtual Machines vs Containers](https://i.imgur.com/ugDjxqm.jpeg)

Có thể thấy, ở công nghệ ảo hóa bên trái chúng ta chỉ dùng chung một máy thật cài hệ điều hành và cần có một bộ ảo hóa (Hypervisor) để giúp chúng ta cài thêm các con máy ảo, và chúng độc lập với nhau ở mức hệ điều hành. 

Còn với container chúng ta sử dụng chung 1 hệ điều hành và chạy chung trên 1 Docker Engine, ở đây Docker Engine sẽ giúp làm vệc và adapt với các sự khác nhau giữa các hệ điều hành. Ví dụ một ứng dụng chạy trên Windows chúng ta sẽ có Docker trên Windows và chạy trên Linux sẽ có Docker cho Linux lo việc đó.

Vậy chốt lại là ủy quyền việc thích nghi môi trường cho Docker lo, chúng ta chỉ cần đóng gói toàn bộ đồ đạc lại thành 1 bộ duy nhất và mang đi bất cứ đâu mà chúng ta muốn.

## Docker Image

Vậy thứ mà chúng ta đóng lại gọi là gì? Nó là Docker Image, dịch ra thì cũng không ổn lắm nhưng nó là một bộ cài của ứng dụng của chúng ta bao gồm các mã nguồn đã đóng gói, các depedencies (ví dụ là các packages chúng ta sử dụng khi lập trình) và đóng gói luôn cả các cấu hình cũng như môi trường chạy.

![What is docker image?](https://i.imgur.com/DnLzgla.png)

Ở đây chúng ta cần tư duy theo hướng layer, một Docker Image sẽ có thể dùng các image khác để build lên nó, ví dụ khi chúng ta build một ứng dụng ASP.NET Core đương nhiên chúng ta cần thư viện của .NET Core. Vậy Base image sẽ là image của .NET Core, trên nó mới là layer code của ứng dụng của chúng ta. Cứ như vậy 1 image được xây lên từ nhiều lớp giống như xây nhà vậy. Hàng gạch từ dưới cùng là hàng gạch móng chính là base image được Microsoft phát hành. Trên nó sẽ là các image của chúng ta xây dựng. Chồng 2 lớp đó lên chúng ta sẽ có một image ứng dụng hoàn chỉnh.

## Docker Container

Ok vậy khi đã có một bộ cài rồi thì chúng ta có thể mang nó đi bất cứ đâu để cài, cái này làm mình nhớ đến cái đĩa Ghost Windows mà bạn nào học IT cũng có thời ngồi vọc đúng không? Chính cái bản ghost đó đóng gói luôn cả bộ Windows và các phần mềm trong đó và cả các driver nữa. File ghost đó cũng giống như một Docker image vậy. Vậy là mang ra máy nào cũng chỉ cần bung bản ghost đó ra là xong. Docker cũng vậy, ta có image rồi vậy chỉ cần mang nó lên bất cứ máy nào bạn run image đó nó sẽ chạy như là bạn đã cài đặt nó trên máy của mình vậy. Và khi image được chạy nó sẽ chạy trong một container, container giống như thùng chứa, ứng dụng chúng ta sẽ chạy trong nó và đưa thông tin ra ngoài, nó hoàn toàn độc lập với môi trường xung quanh.

![](https://i.imgur.com/AVGsZOY.jpeg)

Trong thực tế khi có nhiều loại hàng hóa khác nhau với kích thước khối lượng khác nhau thì rất khó để chúng ta đóng gói và vận chuyển vì các phương tiện vận chuyển không biết thiết kế và xếp như thế nào. Người ta đã nghĩ ra một loại chuẩn để đóng gói hàng hóa giúp thuận tiện vận chuyển đó là Container. Tương tự như thế với thế giới IT, nó cũng được sử dụng để deploy các ứng dụng khác nhau, môi trường khác nhau và phần cứng khác nhau.

![](https://i.imgur.com/wn4hZbT.jpeg)

## Docker Registry

Docker Registry nó giống như một thư viện chứa image, các image cần chia sẻ giữa các nơi sẽ được đưa lên đó, và các nơi khác nhau sẽ có thể lấy về để chạy, nó giống như một ổ đĩa chia sẻ trên mạng. Docker các bạn có một nơi chia sẻ rất nổi tiếng các image có sẵn là [https://hub.docker.com/](https://hub.docker.com/) bạn có thể tìm bất cứ Docker image public có sẵn nào trên đó để lấy về dùng. Bạn cũng có thể đưa các image của mình lên đó với tài khoản của bạn.

Đối với doanh nghiệp của bạn, nếu không dùng một public registry, bạn có thể tự cài cho mình một private registry để lưu trữ và quản lý image version của riêng mình.

Sơ đồ tương quan giữa các thành phần

![](https://i.imgur.com/Kv64saq.jpeg)

Các image sẽ được để lên Docker registry (private hoặc public) sau đó bất cứ ai có thể truy cập đều lấy được image về và run trên Docker Deamon để chạy ứng dụng trong Container. Container sẽ được tạo ra khi chúng ta run image.

Cái mà chúng ta cài bao gồm Docker Client và Docker Deamon, Docker deamon chính là engine giúp quản lý và chạy Container và tương tác với OS. Nó là trái tim của Docker Engine.

---
## References:

[Tìm hiểu về các khái niệm trong Docker](https://tedu.com.vn/kien-thuc/tim-hieu-ve-cac-khai-niem-trong-docker-196.html)