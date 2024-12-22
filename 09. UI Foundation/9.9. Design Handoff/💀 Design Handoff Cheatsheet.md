---
aliases:
  - Design Handoff
created: 2024-12-21T06:44:00
tags:
  - Handoff
  - Design
  - UID
  - UI/UX
not complete: true
---
## Design Hand-off là gì?

Design Hand-off là giai đoạn chuyển giao thiết kế từ Designer sang các [[💀 Stakeholders]]. Đây là một bước quan trọng trong quy trình phát triển sản phẩm, đảm bảo rằng giải pháp thiết kế được hiện thực hóa một cách chính xác. Quá trình này không chỉ dừng lại ở việc chia sẻ file thiết kế, mà còn đòi hỏi Designer cung cấp đầy đủ thông tin, tài liệu và hướng dẫn để các Stakeholders dễ dàng hiểu và triển khai.

*Vậy làm thế nào để quá trình này diễn ra hiệu quả và giảm thiểu sai sót?*

## I. Xác định Đối tượng nhận bàn giao thiết kế

Để quá trình Hand-off hiệu quả, cần hiểu rõ đối tượng sẽ nhận thiết kế:
- **Nếu là Developer front-end:** bạn hãy tập trung vào giao diện, cách sử dụng component, và tài nguyên cần export và tối ưu performance.
- **Nếu là Developer back-end:** bạn hãy nhấn mạnh luồng dữ liệu, các trạng thái và logic liên quan đến chức năng.
- **Nếu là QA:** bạn hãy cung cấp các trường hợp kiểm thử và ghi chú những điểm cần kiểm tra kỹ lưỡng.
Tất nhiên còn nhiều đối tượng khác nhau trong tổ chức/đội nhóm sản phẩm, hãy tùy vào từng đối tượng mà bàn giao cho phù hợp. 

## II. Sắp xếp các Thành phần, Màn hình và Luồng rõ ràng

### 2.1. Với các Thành phần (Component)

Các thành phần thiết kế nhỏ lẻ như nút bấm, input, checkbox, hay card cần được tập trung và quản lý một cách khoa học. Điều này không chỉ giúp Developer dễ dàng truy cập mà còn đảm bảo sự nhất quán khi tái sử dụng các thành phần này.
- **Tách biệt component:** Đặt tất cả các component trong một trang riêng hoặc khu vực cụ thể. Điều này giúp Developer nhanh chóng nhận diện các thành phần cần dùng trong file thiết kế.
- **Sử dụng Design System:** Nếu có thể, xây dựng một Design System hoàn chỉnh. Một Design System giúp quản lý các component và quy tắc thiết kế ở một nơi, dễ dàng cập nhật và áp dụng trên toàn dự án.

### 2.2. Với Màn hình và Luồng

Mỗi dự án đều có nhiều màn hình và luồng tính năng khác nhau. Nếu không được sắp xếp hợp lý, file thiết kế sẽ trở nên rối rắm, gây khó khăn cho Developer.
- **Không dồn tất cả vào một file duy nhất:** Hãy tách riêng các chức năng hoặc luồng phức tạp thành từng module nhỏ. Ví dụ: nếu bạn thiết kế một hệ thống thanh toán, hãy tách các bước thanh toán ra từng module như: chọn phương thức thanh toán, xác nhận đơn hàng, hoặc thông báo giao dịch thành công.
- **Sắp xếp logic và trực quan:** Đặt các màn hình theo thứ tự luồng công việc, chẳng hạn từ màn hình chính, đăng nhập, đến các tính năng chi tiết. Điều này giúp Developer dễ hình dung luồng người dùng và kiểm tra tính liên kết giữa các màn hình.

## III. Kiểm tra Tài nguyên thiết kế trước khi gửi đi

### 3.1. Đảm bảo Tài nguyên đầy đủ và đúng định dạng

**Export đúng format:** Các tài nguyên cần được export theo định dạng mà các Stakeholders yêu cầu, như PNG, SVG, hoặc JSON cho hình ảnh và icon.
**Tối ưu performance:** Tránh sử dụng hình ảnh dung lượng lớn, gây chậm hiệu suất ứng dụng. Sử dụng các công cụ nén hình ảnh như TinyPNG/iLoveIMG hoặc ImageOptim để tối ưu hóa file.

### 3.2. Kiểm tra Thông số kỹ thuật

Font chữ, màu sắc, kích thước, và spacing cần phải được kiểm tra kỹ lưỡng trước khi gửi đi. Hãy đảm bảo chúng tuân thủ quy chuẩn thiết kế đã đề ra.
Đối với các hiệu ứng phức tạp *(như shadow, gradient)*, hãy chắc chắn rằng Developer hiểu rõ cách triển khai chúng trong code.

## IV. Đính kèm Tài liệu thiết kế chi tiết và Hướng dẫn

File thiết kế không đủ để truyền đạt ý đồ thiết kế, nhất là khi dự án có nhiều màn hình và tính năng phức tạp. Vì vậy, hãy cung cấp tài liệu bổ sung để hỗ trợ Developer:
- **Mô tả chức năng:** Giải thích ý nghĩa và mục tiêu của từng màn hình hoặc tính năng.
- **Hướng dẫn sử dụng Component:** Làm rõ cách các component được sử dụng, vị trí và trạng thái của chúng.
- **Quy chuẩn thiết kế:** Bao gồm thông tin về grid, spacing, màu sắc, font chữ, và các quy tắc khác mà Developer cần tuân theo.

**Tài liệu có thể dưới dạng nào?**
- Tài liệu viết tay (Google Docs, Notion).
- File chú thích trong file thiết kế (Figma).
- Video ngắn hoặc xây dựng một bản prototype nhằm giải thích các luồng thiết kế phức tạp.

## V. Kiểm tra Tính khả thi và Giới hạn của thiết kế

### 5.1. Đánh giá tính khả thi

**Trước khi gửi, hãy tự hỏi:**
- Thiết kế này có thực sự khả thi về mặt kỹ thuật không?
- Có vấn đề nào mà Developer có thể gặp phải khi triển khai không?

Hãy trao đổi trực tiếp với Developer nếu có những phần thiết kế phức tạp *(như animation hoặc hiệu ứng đặc biệt)* để đảm bảo họ hiểu rõ cách thực hiện.

### 5.2. Hiểu rõ giới hạn kỹ thuật

Một số thiết kế có thể đẹp về mặt giao diện nhưng không khả thi hoặc quá phức tạp để triển khai. Hãy làm rõ các giới hạn này trước khi gửi file. 

Ví dụ:
- Một số hiệu ứng hover không thể hiện thực trên mobile.
- Một số font chữ không hỗ trợ đầy đủ các ngôn ngữ.

---
## References:
[Figma UIUX VN | Facebook](https://www.facebook.com/groups/112822915025011?multi_permalinks=448684208105545&hoisted_section_header_type=recently_seen)
