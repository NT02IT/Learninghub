---
aliases:
  - Pixel
  - Point
created: 2024-12-11T14:26:00
tags:
  - Design
  - Unit
  - Compare
---
## Image Pixel (px)

**Pixel *(picture element)* là phần tử nhỏ nhất trong hình ảnh điện tử.** Số lượng pixel mà máy ảnh sử dụng để chụp ảnh càng lớn thì chất lượng hình ảnh càng tốt. Độ phân giải của máy ảnh kỹ thuật số dao động từ khoảng 4 triệu đến hơn 16 triệu pixel (MP - million pixels).

> [!NOTE] Lưu ý
> Pixel không phải là một hình vuông nhỏ.
> Pixel là 1 mẫu điểm (point sample). Đối với ảnh màu, một pixel thực sự có thể chứa ba mẫu, một mẫu cho mỗi màu cơ bản đóng góp vào hình ảnh tại điểm lấy mẫu. Chúng ta vẫn có thể coi đây là một mẫu điểm của một màu. Nhưng chúng ta không thể nghĩ về một pixel như một hình vuông – hoặc bất cứ thứ gì khác ngoài một điểm.
> Một ảnh (theo nghĩa image-base graphic) là một lưới các pixel (point sample).
> Đọc thêm: [A Pixel Is Not A Little Square](http://alvyray.com/Memos/CG/Microsoft/6_pixel.pdf)

Mặc dù pixel hình vuông là phổ biến trong các thiết bị hiển thị do tính đơn giản và khả năng ghép nối dễ dàng mà không có khoảng trống, nhưng có thể sử dụng các dạng khác như hình lục giác, tròn hoặc thậm chí đa giác cho một số ứng dụng đặc biệt.

Tìm hiểu thêm: [What is the Shape of a Pixel?](https://blogs.mathworks.com/steve/2018/03/16/what-is-the-shape-of-a-pixel/#27191473-0165-46fd-a8a4-272a6d026587)
## Point (pt)

**Point là một đơn vị đo chiều dài, point chủ yếu được sử dụng khi bạn muốn đo chiều cao của một phông chữ.** Nhưng khi nói về mặt kỹ thuật, point có thể được sử dụng để đo bất kỳ chiều dài nào. 

Trong bất kỳ ứng dụng nào, 1 point chính xác bằng 1/72 inch. Chúng ta hãy so sánh nó với Pixel, các pixel của một điểm phụ thuộc vào độ phân giải của hình ảnh của bạn. Ví dụ, nếu độ phân giải của hình ảnh của bạn là 72 pixel/inch (ppi) thì 1 point bằng 1 Pixel.

![](https://img.playbook.com/fJ7D6RdeqZkwKl7h7fb8JkwWC2q_suKeShh2DcFlShI/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzY2Yjg2OTRl/LTUxMmUtNDhkYi04/NTg5LTU4YWJiOTVh/ZjBmMQ)

## Vậy màn hình thông thường so với màn hình retina và màn hình siêu retina hoạt động như thế nào?

Khi Steve Jobs ra mắt iPhone 4, và cùng với đó là màn hình Retina đầu tiên, ông đã mô tả nó như một màn hình có rất nhiều điểm ảnh được đóng gói rất gần nhau (được đánh giá là 326ppi) đến mức mắt người không thể nhận thấy chúng ở khoảng cách 12 inch. Bạn sẽ không nhìn thấy từng điểm ảnh riêng lẻ: bạn chỉ nhìn thấy hình ảnh mà các điểm ảnh đó tạo ra.

**Một số thiết bị có mật độ điểm ảnh lớn hơn 326ppi, một số thì ít hơn. Làm sao tất cả chúng đều có thể được gọi là Retina?**

Bởi vì có hai yếu tố quan trọng quyết định xem điểm ảnh có thể nhận biết được hay không: **mật độ** và **khoảng cách**. Mắt bạn càng xa màn hình thì mật độ điểm ảnh cần thiết để khiến các điểm ảnh 'biến mất' càng thấp. Nói chung, màn hình càng lớn thì mắt bạn càng có khả năng cách xa màn hình và do đó mật độ điểm ảnh cần thiết để 'đủ điều kiện' là màn hình Retina càng thấp.

![](https://img.playbook.com/sbAaI3FAauiYwQBCOCv0Nu2dQ_gFsSu82x8och8yAZw/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzJkYTgyZDI5/LWQzOGQtNGZiYi04/MjhlLTQ5Mjg1MTli/MDg0Yw)

Ví dụ, iPhone 4, 5, 6, 7 và 8 đều có màn hình với mật độ điểm ảnh là 326ppi, trong khi các phiên bản Plus có mật độ cao hơn là 401ppi. iPhone X, XS và XS Max có mật độ điểm ảnh là 458ppi.

Tuy nhiên, hãy nhìn vào MacBook Pro 13in, màn hình của nó chỉ có mật độ 227ppi. Nhưng nó đủ điều kiện là Retina vì bạn ngồi xa màn hình máy tính xách tay hơn.

![](https://img.playbook.com/vw9RDDr5OE7gfm7CTTXO_6kvVES5BIdJxA2mX-V1m60/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2JkZjQwMmRk/LTBjMjItNDFhZS1h/NWFhLWM2ZWJiNTIx/NDc3Mg)

## [[Key note]]
- Pixel là phần tử nhỏ nhất trong hình ảnh điện tử; Point là một đơn vị đo chiều dài, 1 point chính xác bằng 1/72 inch. ⇒ Ở độ phân giải 72ppi thì 1pt=1px
- 1 Point có thể được biểu diễn trên màn hình bởi nhiều pixel tùy theo PPI.
- Image Pixel và Screen Pixel là khác nhau. Image Pixel là đơn vị nhỏ nhất trong một bức ảnh số hoặc hình ảnh kỹ thuật số. Một pixel trong hình ảnh chứa thông tin về màu sắc và độ sáng của một điểm ảnh trong ảnh. Screen Pixel là đơn vị cơ bản của độ phân giải trên màn hình hiển thị (ví dụ: trên điện thoại, máy tính). Một pixel trên màn hình có thể phát sáng hoặc không và có thể chứa nhiều màu sắc.
- Screen Pixel trước khi tái tạo và Screen Pixel sau khi tái tạo là khác nhau. Sau khi được hệ điều hành tái tạo 1px có thể nhiều hơn 1px trên tấm nền màn hình (Đổi độ phân giải xuống thấp hơn).
- Khi đổi độ phân giải màn hình xuống thấp hơn độ phân giải gốc sẽ làm cho 1px trở nên to hơn nhưng đồng thời cũng làm cho tổng thể ít sắc nét hơn vì tổng số pixel trên màn hình hiển thị bị ít lại.

---
## References
[Difference between the PIXEL and POINT | by Ashihaldia | Medium](https://ashihaldia.medium.com/difference-between-the-pixel-and-point-7d02d5354bbb)
[What is a Pixel? (and what is a point sample)](https://pages.graphics.cs.wisc.edu/559-f14/2014/08/29/what-is-a-pixel-and-what-is-a-point-sample/)