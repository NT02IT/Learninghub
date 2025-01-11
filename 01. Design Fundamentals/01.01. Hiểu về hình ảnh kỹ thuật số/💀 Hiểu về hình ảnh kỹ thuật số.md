---
created: 2025-01-11T18:16:00
tags:
  - Design
  - ImageProperties
not complete: true
---
## Hình ảnh kỹ thuật số (hình ảnh) là gì?

Hình ảnh kỹ thuật số hoặc thu thập hình ảnh kỹ thuật số là tạo ra các hình ảnh nhiếp ảnh, có thể là từ cảnh vật thực tế hoặc cấu trúc bên trong của một đối tượng. Thuật ngữ này thường bao gồm các bước xử lý như nén dữ liệu, lưu trữ, in ấn, và hiển thị hình ảnh.

Hình ảnh kỹ thuật số được phân loại dựa trên loại sóng điện từ hoặc các dạng sóng khác, phản xạ hoặc xuyên qua các đối tượng để truyền tải thông tin cấu thành hình ảnh. Trong tất cả các trường hợp, thông tin được cảm biến hình ảnh ghi nhận, chuyển đổi thành tín hiệu số, sau đó xử lý bằng máy tính để tạo ra hình ảnh có thể nhìn thấy.

Ví dụ:
- **Ánh sáng khả kiến:** Dùng trong nhiếp ảnh kỹ thuật số và quay phim kỹ thuật số với nhiều loại máy ảnh hoặc máy quay.
- **Tia X:** Dùng trong chụp X-quang kỹ thuật số, CT scan, hoặc quang tuyến.
- **Tia gamma:** Ứng dụng trong chẩn đoán hình ảnh như SPECT và PET.
- **Âm thanh:** Được sử dụng trong siêu âm y khoa hoặc thiết bị sonar.
- **Sóng vô tuyến:** Áp dụng trong radar để thu thập dữ liệu hình ảnh.

Hình ảnh kỹ thuật số không chỉ cho phép hiển thị hình ảnh mà còn tạo điều kiện phân tích bằng phần mềm. Ngoài ra, chúng có thể được chỉnh sửa hoặc thao tác để đạt được mục đích cụ thể.

## Cách tạo hình ảnh kỹ thuật số

Hình ảnh kỹ thuật số có thể được tạo theo hai cách chính:
1. **Chụp trực tiếp từ thực tế:** Một bức ảnh số có thể được tạo trực tiếp từ cảnh vật bằng máy ảnh, scanner hoặc thiết bị tương tự.
2. **Chuyển đổi từ hình ảnh khác:** Sử dụng máy quét ảnh hoặc các thiết bị tương tự để chuyển đổi ảnh chụp, phim ảnh, hoặc tài liệu in thành hình ảnh kỹ thuật số.

Ngoài ra, một số hình ảnh kỹ thuật số được tạo ra từ dữ liệu phức tạp không phải hình ảnh, ví dụ:
- Các thiết bị quét sonar hoặc kính viễn vọng vô tuyến.
- Bản đồ radar thời tiết, thường thấy trên các bản tin truyền hình.

Việc số hóa dữ liệu analog trong thế giới thực được gọi là số hóa, và bao gồm lấy mẫu (discretization) và lượng tử hóa. Chụp hình chụp cắt lớp kỹ thuật số có thể được thực hiện bằng máy dò tia X trực tiếp chuyển đổi hình ảnh sang định dạng số. Ngoài ra, việc chụp X quang phốt phát là nơi mà hình ảnh đầu tiên được chụp trên một tấm photpho phosphor (PSP) được quét bởi một cơ chế được gọi là phát quang phát quang.

Ngoài ra, hình ảnh kỹ thuật số còn có thể được **tính toán từ mô hình toán học** hoặc **mô phỏng hình học** – quá trình này thường được gọi là **rendering**.

## Raster và Vector

Các loại và định dạng tệp hình ảnh được chia thành 2 loại chính: tệp hình ảnh raster (bitmap) và tệp hình ảnh vector.

### Hình ảnh Raster (hay Bitmap)

Đồ họa Raster (bitmap) là một tập hợp các điểm ảnh ([[Point vs Pixel|Pixel]]) nhỏ và lưu trữ thông tin về màu sắc và vị trí của từng điểm ảnh. Hình ảnh raster được tạo thành từ những pixels trên một lưới tĩnh. Trong đồ họa Raster (bitmap) mỗi pixel có thể được hiểu là một ô vuông mang màu sắc từ sự kết hợp đèn màu RGB (Đỏ, xanh lục, xanh lam) *(Cần phân biệt rõ Pixel trong Đồ họa Raster và Pixel nghĩa chung chung)*.

![](https://i.imgur.com/nAud3aI.jpeg)

Một tấm ảnh raster tương tự như một bức tranh khảm: nhìn gần chúng ta sẽ thấy tương tự như một loạt các hình vuông bằng nhau được xếp ngay ngắn, nhưng khi nhìn từ xa thì những ô vuông sẽ hòa vào nhau để tạo nên hình ảnh.

Bất cứ khi nào bạn bạn sử dụng cọ để vẽ một hình minh họa kỹ thuật số trong photoshop, mỗi nét cọ sẽ thêm các pixel dọc theo đường cọ. Số lượng pixel tùy thuộc vào kích thước file psd và bán kính cọ. 

Còn trong khi quay chụp, ống kính sẽ chuyển ánh sáng phản chiếu thành các pixel màu nhỏ kết hợp với nhau để tạo thành một hình ảnh kỹ thuật số thực tế.

Bởi vì mỗi pixel được chỉ định cho một không gian trên lưới, hình ảnh raster phụ thuộc vào độ phân giải. Càng nhiều pixel, chất lượng (hoặc độ phân giải) của hình ảnh càng cao, ít pixel hơn có nghĩa là một hình ảnh sẽ hiển thị dưới dạng nhỏ hoặc bị "vỡ ảnh".

Hình ảnh Raster thường gắn liền với các loại tệp như .BMP, .GIF, .JPEG, .PNG và .TIFF, .RAW, .PSD. Hầu hết tất cả hình ảnh bạn thấy trên Internet và hình ảnh được chụp bằng các thiết bị kỹ thuật số đều là hình ảnh raster.

#### Ưu điểm, hạn chế của Raster

**Ưu điểm:**
- Raster rất lý tưởng khi bạn muốn thể hiện chuyển màu và đổ bóng, chẳng hạn như khi vẽ minh họa hoặc chỉnh sửa hình ảnh
- Vì được cấu thành từ hàng ngàn Pixel nên đồ họa Raster có thể hiển thị vô số màu trong một hình ảnh và cho phép chỉnh sửa màu sắc chính xác hơn.
- Nhiều hiệu ứng ảnh chỉ hiển thị hoặc hiển thị tốt hơn bằng raster

**Nhược điểm:**
- Hình ảnh Raster không thể phóng lớn mà không bị mất chất lượng. 
- Phải xác định trước kích thước dự định của hình ảnh, điều này khiến bạn khó thích ứng nếu có sự thay đổi bất ngờ trong dự án.
- Hình ảnh Raster thường là tệp lớn, trong khi các hình ảnh vector tương đối nhẹ. 

> Raster là định dạng mặc định cho nhiếp ảnh, video và web. Khi nói đến hình ảnh minh họa, raster là lý tưởng cho hình ảnh bởi lượng màu phong phú mà nó thể hiện được. Nhưng ảnh raster không được dùng để tạo logo do quá phụ thuộc vào độ phân giải.

### Hình ảnh Vector

Hình ảnh Vector bao gồm các điểm neo (Anchor points), được nối với nhau bởi các đường thẳng và đường cong (các đường paths) dựa trên các phương trình toán học. Các thuật toán sẽ quyết định cách các đường tạo thành một hình dạng, và màu tô & màu viền của hình dạng là màu nào.

Một trong những điều tuyệt vời nhất về hình ảnh vector là bạn có thể thay đổi kích thước chúng lớn hơn hoặc nhỏ hơn vô hạn và chúng vẫn sẽ in ra rõ ràng như vậy, không tăng (hoặc giảm) kích thước tệp. 

Nếu bạn nhớ lại hình học trung học của mình, phương trình cho một vòng tròn có tâm $(h,k)$ và bán kính $r$ là $(x - h)^{2} + (y - k)^2 = r^2$. Nếu bạn muốn làm cho vòng tròn lớn hơn, bạn chỉ cần tăng giá trị của $r$ - thay vì phải theo dõi hàng tấn pixel mới, máy tính chỉ cần theo dõi một con số khác. Điều đó hầu như không chiếm dung lượng tệp nào cả.

![](https://i.imgur.com/XRaLPTW.jpeg)

Đồ họa Vector sẽ bao gồm ba thành phần chính: Điểm, Đường và đa giác. Một đồ họa Vector sẽ được tạo nên bởi vô số điểm (Point) kết nối với nhau. Các điểm này tuy vô hình nhưng bạn có thể sử dụng các công cụ trong phần mềm đồ họa để chỉnh sửa độ cong hay hình dáng của Vector. Đường (Path) là đường dẫn kết nối giữa các điểm, hay nói cách khác hai điểm nối với nhau sẽ tạo thành đường. Vì được tạo nên từ các điểm có thể chỉnh sửa nên các đường có thể mang nét cong, thẳng, chéo tùy ý theo cách sử dụng điểm của bạn. Ngoài ra bạn có thể thêm màu sắc, thay đổi kích cỡ của đường. Và cuối cùng là đa giác (Shape) hình thành khi được kết nối kín từ đường dẫn, hay hiểu đơn giản là các điểm sẽ kết nối với nhau và tạo thành hình hoàn chỉnh. Khi đã hoàn thành xong đa giác bạn có thể đổ màu vào hình đó.

Mặc dù đồ họa vector có thể được sử dụng để mô phỏng hình ảnh, tuy nhiên chúng phù hợp nhất cho các thiết kế sử dụng màu sắc đơn giản và đồng nhất. Hình ảnh vector được tạo thành từ các hình dạng, mỗi hình dạng có một màu riêng; do đó, vector không thể tạo ra các dải màu, bóng đổ và sự chuyển màu phức tạp như hình ảnh raster (có thể mô phỏng các hiệu ứng này, nhưng sẽ cần phải raster hóa một phần hình ảnh – điều này đồng nghĩa với việc nó sẽ không còn là vector thực sự). 

Các hình ảnh ảnh raster thường có các định dạng sau: PDF, EPS,AI, SVG,...

#### Ưu điểm, hạn chế của Vector

**Ưu điểm:**
- Có thể được thu phóng đến bất kỳ kích thước nào mà không làm giảm chất lượng.
- Đồ họa Vector giúp bạn tạo ra các đường thẳng, đường cong tuyệt đối. Thích hợp với kiểu thiết kế gọn gàng.
- Dung lượng của đồ hoạ Vector cũng thấp hơn so với Raster.

**Nhược điểm:**
- Đồ họa Vector không mạnh trong khoản tạo ra các hiệu ứng đổ bóng thực tế hay tổ hợp màu gradient đẹp mắt. Vì vậy nó thường được dùng để thiết kế ở dạng phẳng (flat design).
- Dù mang lại sự chính xác cao trong các đường nét, nhưng điều này cũng khiến đồ họa Vector khó có thể tạo ra các nét tự nhiên như nét vẽ tay.

> Đồ họa vector rất thích hợp cho thiết kế in ấn vì không phải phụ thuộc vào độ phân giải. Khả năng thu phóng tự do và hình học đơn giản hóa cũng là một lý do mà logo được thiết kế trên nền tảng này vì logo là một đối tượng thiết kế được sử dụng trên đa nền tảng đa kích thước cũng như có thể dễ dàng thay đổi, chỉnh sửa. Vector có thể được sử dụng để minh họa và mặc dù bị hạn chế về mặt phong cách, chúng có khả năng chính xác hình học cao. 
> Điều quan trọng cần lưu ý là, ngoại trừ định dạng SVG, các vector phải được rasterized trước khi chúng có thể được sử dụng trên web.

### Sự khác nhau giữa Raster và Vector

| Tiêu chí            | Vector                                                                                           | Raster                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cấu thành           | Được tạo từ các điểm, đường và đa giác bằng các phương trình toán học                            | Được tạo từ các điểm ảnh xếp trên lưới                                                                                                                                                    |
| Tính linh hoạt      | Có thể thu phóng vô hạn mà không làm giảm chất lượng                                             | Bị "vỡ ảnh" khi phóng to ảnh so với kích thước ban đầu, tuy nhiên có thể giữ chất lượng hình ảnh khi thu nhỏ bằng cách tăng độ phân giải theo tỉ lệ.                                      |
| Kích thước          | Nhẹ hơn nhiều so với raster, đặc biệt là với những file Raster có kích thước và độ phân giải lớn | Càng chứa nhiều thông tin, ảnh sẽ càng nặng                                                                                                                                               |
| Khả năng hiển thị   | Bị hạn chế khi hiển thị các dải màu gradient, hiệu ứng đặc biệt như đổ bóng,...                  | Hiển thị vô số màu trong một hình ảnh và cho phép chỉnh sửa màu sắc chính xác hơn.                                                                                                        |
| Khả năng chuyển đổi | Có thể dễ dàng chuyển đổi sang Raster bằng cách export                                           | Có thể sử dụng AI hoặc các tính năng thông minh có sẵn trong các ứng dụng chỉnh sửa vector để chuyển ảnh bitmap thành vector, tuy nhiên kết quả không phải lúc nào cũng tốt và chính xác. |
| Khả năng tiếp cận   | Chỉ có thể mở và chỉnh sửa bằng các phần mềm chỉnh sửa vector chuyên dụng                        | Phổ biến và dễ nhận biết bởi các phần mềm hỗ trợ hình ảnh thông dụng. Ngoài ra, hầu hết các hình ảnh kỹ thuật số trên web đều là ảnh bitmap.                                              |
| Ứng dụng            | Thiết kế Logo, Font chữ, Thiết kế đồ họa vector, In ấn, Trò chơi điện tử,...                     | Nhiếp ảnh, Thiết kế đồ họa, In ấn, Đồ họa máy tính và Trò chơi, Truyền thông và Thiết kế đa phương tiện, Ảnh trên Website, Hình ảnh Y khoa,...                                            |
| Định dạng phổ biến  | .AI, .CDR, .DAE, .EMF, .SVG, .EPS, .PDF,...                                                      | .BMP, .GIF, .JPEG, .PNG và .TIFF, .RAW, .PSD, .EPS, .PDF,...                                                                                                                              |
| Phần mềm chỉnh sửa  | Adobe Illustrator, CorelDraw, InkScape,...                                                       | Adobe Photoshop, GIMP, Adobe Lightroom, Corel PaintShop Pro,...                                                                                                                           |

## Kích thước ảnh hoạt động ra sao trên màn hình

Kích thước của ảnh rất quan trọng vì nó quyết định những gì chúng ta có thể làm với ảnh khi ở trên máy tính. Một ảnh rất nhỏ sẽ chỉ đẹp trên màn hình, và sẽ không đẹp nếu in ra. Kích thước của ảnh được đo bằng:
1. **MB (megabytes)**, nó chiếm bao nhiêu dung lượng trên bộ nhớ máy tính
2. **[[Point vs Pixel|Pixel]]**, hoặc **yếu tố hình ảnh (picture elements)**, là bao nhiêu chấm vuông nhỏ tạo nên ảnh, cho biết độ chi tiết của ảnh.

#NotComplete 

## Kích thước của ảnh hoạt động như thế nào khi in ra

Các máy in có hệ thống ấn định kích thước ảnh khác nhau khi in ra. Ảnh có thuộc tính gọi là **[[DPI vs PPI|DPI]]**, viết tắt của **chấm trên in (dots per inch)**. Nó đơn giản có nghĩa là có bao nhiêu chấm mực xuất hiện trên một đường thẳng dài một in. Hầu hết ảnh chụp trên điện thoại thông minh đều có 120 DPI, và ảnh chụp từ máy ảnh kỹ thuật số cao cấp sẽ có 300 DPI.

Khi một DPI cao được kết hợp với số lượng pixel cao, có nghĩa là ảnh có thể in ra rất lớn và với chất lượng cao. DPI thấp sẽ không làm cho ảnh nhỏ hơn khi in ra, chỉ là chất lượng thấp hơn.

## Ảnh đã chỉnh sửa có thể giảm chất lượng

Nếu thay đổi kích thước một tấm ảnh, sau đó lưu nó ở định dạng JPG, sau đó chỉnh sửa lại tấm ảnh mới, lần sau khi lưu, nó có thể trông thậm chí còn tệ hơn. 

> Nếu đã chỉnh sửa ảnh và không thích kết quả, tốt nhất nên quay lại ảnh gốc để làm lại, tránh làm mất chất lượng hơn nữa.

Sử dụng định dạng tệp BMP sẽ giúp tránh giảm chất lượng. Cách này chiếm nhiều dung lượng nhất trên máy tính, nhưng khi chỉnh sửa xong, có thể lưu kết quả cuối cùng dưới dạng JPG để chia sẻ qua email hoặc truyền thông xã hội.

## Tại sao các thiết bị cũ chụp ảnh kém hơn

Chất lượng ban đầu của một tấm ảnh kỹ thuật số phụ thuộc vào máy móc, hay phần cứng, trong máy ảnh hoặc thiết bị chụp nó. Cảm biến của máy ảnh có một số pixel, thể hiện tấm ảnh lớn nhất mà máy ảnh có thể chụp. Ống kính máy ảnh quyết định chất lượng của bức ảnh. Máy ảnh cũ có cảm biến nhỏ hơn với ít pixel hơn, và một số có ống kính kém hơn.

Một chiếc điện thoại thông minh mới hơn sẽ chụp ảnh đẹp hơn nhiều so với một chiếc quá cũ, và một chiếc máy ảnh nhỏ gọn mới thậm chí có thể chụp những tấm ảnh đẹp hơn một chiếc máy ảnh DSLR cũ. Cách dễ nhất để có được những tấm ảnh chất lượng tốt hơn là mua một chiếc điện thoại thông minh hoặc máy ảnh kỹ thuật số mới hơn, tốt hơn. 

---
## References:

[Hiểu các thuộc tính của ảnh](https://beconnected.esafety.gov.au/pluginfile.php/76370/mod_resource/content/2/Understanding%20image%20properties%20t32%20c2%20VIE.html#)
[Hình ảnh kỹ thuật số - Phần 1](https://thietbikhoahoccongnghe.com.vn/hinh-anh-ky-thuat-so-phan-1.html)
[Phân Biệt Hình Ảnh Vector Và Raster Trong Thiết Kế Đồ Họa](https://atomisystems.com/blog-vi/elearning-vi/phan-biet-hinh-anh-vector-va-raster/)
[Sự khác biệt giữa Vector và Raster trong thiết kế đồ họa](https://gitiho.com/blog/su-khac-biet-giua-vector-va-raster-trong-thiet-ke-do-hoa-1.html)

