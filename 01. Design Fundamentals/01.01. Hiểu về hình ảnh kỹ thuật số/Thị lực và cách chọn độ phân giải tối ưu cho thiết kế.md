---
created: 2025-01-14T14:42:00
tags:
  - Design
  - Image
  - Guide
---
Việc đánh giá độ phân giải của tệp in nên được liên kết với khoảng cách mà bản in của bạn sẽ được xem. Để mắt bạn không còn phân biệt các chấm mực cách nhau gần nhau trong bản in và để hình ảnh không bị coi là bị vỡ hoặc mờ, người ta ước tính rằng khoảng cách xem ít nhất phải là 25cm đối với tệp ban đầu có độ phân giải 300dpi.

300 DPI, mà chúng ta đã quen sử dụng trong thiết kế in ấn, không nhất thiết phải thiết cho tất cả các hình ảnh cách mắt nhìn lớn hơn 25 cm.

## Lựa chọn độ phân giải

Có 2 lựa chọn độ phân giải: **Độ phân giải danh nghĩa** (The nominal resolution) và **Độ phân giải cần và đủ** (Necessary and sufficient resolution).

### Độ phân giải danh nghĩa

> Độ phân giải danh nghĩa dành cho các bản in nhỏ, được xem kỹ.  
  
Đối với lý do danh nghĩa, tệp nên được chuẩn bị ở độ phân giải 300dpi, tương ứng với thị lực trung bình ở khoảng cách 25cm.  
  
Theo nguyên tắc chung, khoảng cách xem thoải mái là 1,5 x kích thước đường chéo. Chúng ta tiến gần hơn trong trường hợp muốn xem kỹ chi tiết.

### Độ phân giải cần và đủ

> Độ phân giải cần và đủ (hoặc 'tối ưu') dành cho các bản in được xem từ xa. Hình ảnh càng được xem xa, độ phân giải của nó sẽ càng thấp.

## Thị lực dưới góc nhìn toán học

Số megapixel cần thiết để in một cái gì đó, hoặc xem tivi cuối cùng được xác định bởi thị lực của mắt người và khoảng cách mà đối tượng được nhìn thấy. Đối với một người có thị lực trung bình (tức là 20/20), độ nhạy của họ sẽ được định nghĩa là một _phút cung_, hoặc 1/60 độ. Để so sánh, một mặt trăng tròn trên bầu trời xuất hiện khoảng 31 phút cung (1/2 độ) ngang.

![](https://i.imgur.com/aWZymg8.png)

Một số mô tả bỏ qua từ nói về phút cung đến mô tả cách khoảng cách giữa người quan sát và một vật thể có thể được tính toán với độ phân giải của vật thể. Ví dụ, khoảng cách (tính bằng inch) mà mắt đạt đến giới hạn độ phân giải thường được tính bằng:

$$min\_dpi = \frac{3438}{h}$$

Trong đó, h là độ phân giải và có thể là **ppi** cho màn hình và **dpi** cho bản in. Vì vậy, nếu h = 300, thì d = 11.46 inch. Bây giờ để tính toán khoảng cách xem tối ưu liên quan đến một con số kỳ diệu - 3438. Con số này đến từ đâu? Rất ít mô tả thực sự cung cấp bất kỳ thông tin chi tiết nào, nhưng chúng ta có thể bắt đầu với một số lượng giác cơ bản. Hãy xem xét sơ đồ trong hình dưới, trong đó h là _cao độ pixel_, d là khoảng cách nhìn và θ là góc nhìn.

![](https://i.imgur.com/84j7eWk.png)

Bây giờ chúng ta có thể sử dụng phương trình cơ bản để tính góc θ, với chiều dài của các cạnh đối và cạnh kề:

$$
tan(θ) = \frac{opposite}{adjacent}
$$

Áp dụng vào hình trên ta có:

$$
tan(θ/2) = \frac{h/2}{d} \implies h=tan(θ/2)*2d
$$

Bây giờ nếu chúng ta sử dụng thị lực là 1 phút cung (1/60 độ), điều này tương đương với 0,000290888 radian. Do đó:

$$
h = 2d*tan(0.000290888/2) 
  = 2d*0.000145444
$$

Vì vậy, đối với d = 24 inch thì h = 0,00698 inch. Để chuyển đổi điều này thành PPI / DPI, chúng ta chỉ cần lấy nghịch đảo, vì vậy 1 / 0,00698 = 143ppi. Làm thế nào để chúng ta biến phương trình này thành một phương trình có giá trị 3438 trong đó? Chà, cho rằng độ phân giải có thể được tính bằng cách lấy nghịch đảo, chúng ta có thể sửa đổi phương trình trước đó:

```
min_dpi = 1/(2d * 0.000145444)
  = 1/d * 1/2 * 1/0.000145444
  = 1/d * 1/2 * 6875.49847
  = 1/d * 3437.749
  = 3438/d
```

Ví dụ, hãy xem xét Apple Watch Series 8, có màn hình có độ phân giải 326ppi. Thực hiện phép tính cho d=3438/326=10.55 inch. Vì vậy, đồng hồ nên được giữ cách mặt 10.55 inch. Đối với áp phích in ở 300dpi, d=11.46 inch và đối với áp phích in ở 180dpi, d=19.1 inch. Điều này không phụ thuộc vào kích thước của áp phích, chỉ có độ phân giải in và đại diện cho độ phân giải tối thiểu ở một khoảng cách cụ thể - chỉ khi bạn di chuyển đến gần hơn, bạn mới cần độ phân giải cao hơn. Đây là lý do tại sao biển quảng cáo có thể được in ở độ phân giải thấp, thậm chí 1dpi, bởi vì khi nhìn từ xa, độ phân giải thấp đến mức nào không thực sự quan trọng.

Lưu ý rằng có nhiều biến số khác khi nói đến sự nhạy bén của mắt. Những tính toán này cung cấp kịch bản trường hợp đơn giản nhất. Đối với những đôi mắt nằm ngoài phạm vi bình thường, thị lực sẽ khác đi, dẫn đến thay đổi trong phép tính (thay đổi θ). Cuối cùng, cần nói thêm rằng các tính toán độ nhạy này chỉ tính đến những gì ngay trước mắt chúng ta, tức là tầm nhìn hẹp, sắc nét, do [foveola](https://pixelcraft.photo.blog/2022/05/16/the-human-visual-system-focus-and-acuity/) trong mắt cung cấp - tất cả các phần khác của cảnh (tầm nhìn ngoại vi), sẽ có độ nhạy thấp hơn một chút di chuyển ra khỏi điểm trung tâm này.

![](https://i.imgur.com/OMRNnme.png)

## [[Key note]]

Việc lựa chọn độ phân giải tệp để in nên được xem xét liên quan đến cách nó sẽ được cảm nhận sau đó, tùy thuộc vào:
- Khoảng cách xem
- Sự cần thiết phải đọc kỹ hoặc xem chi tiết hay không
- Độ phân giải tối đa mà thiết bị hiển thị có thể hiển thị
- Độ phân giải tối đa mà máy in có thể in

Nếu bản in được xem ở cự ly gần: yêu cầu 300 dpi.  
  
Nếu bản in dự định được xem từ xa: số dpi có thể được giảm để tăng dung lượng của nó trong kích thước in, tùy thuộc vào khoảng cách xem. `min_dpi=3438/d`
  
Khoảng cách xem để xem thoải mái ước tính là 1,5 x kích thước đường chéo của bản in.

---
## References:

[Picto Online - Khoảng cách xem](https://www.pictoonline.fr/en/help/resolution-distance)
[The math behind visual acuity | Crafting Pixels](https://pixelcraft.photo.blog/2022/10/24/the-math-behind-visual-acuity/)