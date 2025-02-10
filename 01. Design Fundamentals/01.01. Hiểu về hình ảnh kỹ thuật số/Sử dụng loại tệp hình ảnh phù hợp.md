---
created: 2025-01-14T14:03:00
tags:
  - Design
  - FileFormat
  - Guide
---
## Tiêu chí đánh giá định dạng tệp hình ảnh

Trước khi chọn định dạng tệp, điều quan trọng là phải hiểu các loại tệp hình ảnh khác nhau. Có một số danh mục xác định khả năng của tệp hình ảnh:

### [[Hiểu về hình ảnh kỹ thuật số - Raster vs Vector|Vector hay Raster]]

- **Vector:** Lý tưởng để thay đổi kích thước hình ảnh, vì chúng có thể scale tùy thích. Tỷ lệ hình ảnh được tính toán và tự động điều chỉnh bằng toán học, giúp dễ dàng sửa đổi hình ảnh mà không ảnh hưởng đến kích thước tệp hoặc độ rõ nét của hình ảnh.
- **Raster:** Các tệp hình ảnh raster dựa trên pixel. Hình ảnh raster không thể thay đổi kích thước mà không ảnh hưởng đến chất lượng hình ảnh. Tuy nhiên hình ảnh Raster lại thích hợp để lưu trữ các hình ảnh cần sự trung thực về màu sắc và các đường nét tự nhiên.

### [[Nén hình ảnh - Lossy hay Lossless]]

- **Nén Lossy:** Làm giảm kích thước tệp bằng cách xóa vĩnh viễn một số dữ liệu hình ảnh. Quá trình này dẫn đến kích thước tệp nhỏ hơn, lý tưởng cho các ứng dụng như trang web nơi thời gian tải nhanh hơn là rất quan trọng. Tuy nhiên, sự đánh đổi là chất lượng hình ảnh giảm nhẹ, có thể đáng chú ý hoặc không, tùy thuộc vào mức độ nén được áp dụng.
- **Nén Lossless:** Giữ nguyên tất cả dữ liệu hình ảnh gốc. Điều này có nghĩa là không có sự giảm chất lượng khi nén tệp. Mặc dù điều này dẫn đến kích thước tệp lớn hơn so với các định dạng mất dữ liệu, nhưng lợi ích là không có chi tiết nào bị mất, điều này rất cần thiết cho công việc chuyên nghiệp hoặc chi tiết như logo hoặc hình ảnh dựa trên vector.

### [[DPI vs PPI|Độ phân giải]]

Độ phân giải càng cao thì hình ảnh sẽ càng sắc nét và chi tiết hơn (điều này không phải lúc nào cũng đúng). Điều này là do số lượng pixel trên mỗi inch (PPI) hoặc số chấm trên mỗi inch (DPI) tăng lên, giúp hiển thị các chi tiết nhỏ và các đường nét rõ ràng hơn. Hình ảnh có độ phân giải cao thường được sử dụng trong in ấn và các ứng dụng yêu cầu chất lượng hình ảnh cao.

Tuy nhiên, độ phân giải cao cũng đồng nghĩa với kích thước tệp lớn hơn, có thể ảnh hưởng đến tốc độ tải và lưu trữ. Ảnh độ phân giải thấp có thể sẽ phù hợp hơn để lưu hình ảnh xem trước (preview), thumbnail, ảnh demo,... để tiết kiệm dung lượng cũng như tránh việc bị mang đi sử dụng trước khi hoàn thành.

### [[Color bit depth]]

Độ sâu màu (color bit depth) càng cao thì hình ảnh có thể hiển thị nhiều màu sắc hơn và chi tiết hơn. Điều này có nghĩa là hình ảnh sẽ trông mượt mà hơn, với các chuyển màu tự nhiên và ít hiện tượng dải màu (banding) hơn. Độ sâu màu cao cũng giúp cải thiện khả năng hiển thị các chi tiết nhỏ và các vùng tối sáng trong hình ảnh.

Tuy nhiên, độ sâu màu cao hơn cũng đồng nghĩa với việc kích thước tệp lớn hơn, vì mỗi pixel cần nhiều bit hơn để lưu trữ thông tin màu sắc. Điều này có thể ảnh hưởng đến hiệu suất xử lý và lưu trữ, đặc biệt là khi làm việc với các tệp hình ảnh lớn hoặc phức tạp.

## Hướng dẫn sử dụng tệp hình ảnh phù hợp nhu cầu

### 1. Hậu kỳ, chỉnh sửa (Working file)

| Nén                     | Độ phân giải                                 | Độ sâu màu                                      | Dung lượng         | Khả năng tương thích                                |
| ----------------------- | -------------------------------------------- | ----------------------------------------------- | ------------------ | --------------------------------------------------- |
| Không nén hoặc Lossless | Càng cao càng tốt (≥ độ phân giải cần thiết) | Càng cao càng tốt (phù hợp với tính chất dự án) | Không thành vấn đề | Chuyên nghiệp hóa (Có thể cần phần mềm chuyên dụng) |

**Ảnh chụp:** .RAW > .HEIF > .TIFF > .JPEG
**Vector Art (Logo, Icon, Illustration,...):** Native format (.AI, .CDR,...)
**Image edit:** Native format (.PSD, .LRCAT, .XCF,...)
**Dàn trang/ Collection:** Native format (.INDD, .LRCAT,...) > .HEIF, .TIFF
**Print after:** .TIFF > .PNG > .JPEG

### 2. Website (Final file)

| Nén                 | Độ phân giải                                                     | Độ sâu màu     | Dung lượng                                                 | Khả năng tương thích                   |
| ------------------- | ---------------------------------------------------------------- | -------------- | ---------------------------------------------------------- | -------------------------------------- |
| Lossless hoặc Lossy | Web chỉ quan tâm kích thước ảnh chứ không quan tâm độ phân giải. | 8-bit/ channel | Càng nhỏ càng tốt (Với chất lượng hình ảnh chấp nhận được) | Hỗ trợ rộng rãi bởi tất cả trình duyệt |

**Ảnh bitmap không có nền:** .WebP > .PNG
**Ảnh động:** .WebP > .GIF
**Ảnh bitmap có nền với kích thước lớn:** .WebP > .JPG
**Ảnh bitmap có nền với nhiều nét mảnh (line, type, sơ đồ, biểu đồ...):** .WebP > .PNG
**Ảnh bitmap có nền với kích thước nhỏ (icon, favicon,...):** .WebP > .PNG
**Vector assets (Logo, Icon,...):** .SVG > .WebP > .PNG

> [!Tip] Tip
> Để giải quyết vấn đề về khả năng tương thích, có thể sử dụng thẻ `picture` thay cho thẻ `img` để cung cấp ảnh dự phòng khi ảnh trước đó không tương thích. Thẻ `picture` cùng với thuộc tính `srcset` giúp cung cấp nhiều phiên bản của cùng một hình ảnh, cho phép trình duyệt chọn phiên bản phù hợp nhất dựa trên khả năng hỗ trợ và độ phân giải màn hình.

### 3. In ấn (Final file)
| Nén                 | Độ phân giải                                                                                            | Độ sâu màu       | Dung lượng         | Khả năng tương thích                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ | -------------------------------------------------------------- |
| Lossless hoặc Lossy | Độ phân giải phù hợp với dự án (xét trên các tiêu chí: chất liệu in, kỹ thuật in, khoảng cách nhìn,...) | ≥ 8-bit/ channel | Không thành vấn đề | Chuyên nghiệp hóa (Có thể cần phần mềm chuyên dụng hoặc không) |

**Ảnh chụp/ Bitmap image:** .TIFF > .PNG > .JPEG
**Dàn trang/ Collection:** .PDF
**Vector Art:** .EPS > .PDF 

### 4. Trung gian chuyển đổi (Intermediate file)
| Nén                 | Độ phân giải      | Độ sâu màu        | Dung lượng         | Khả năng tương thích                       |
| ------------------- | ----------------- | ----------------- | ------------------ | ------------------------------------------ |
| Lossless hoặc Lossy | Dựa trên file gốc | Dựa trên file gốc | Không thành vấn đề | Tương thích với nhiều phần mềm tương đương |

**Ảnh chụp/ Bitmap image:** .TIFF > .PNG > .JPEG
**Vector Art:** .EPS > .SVG

### 5. Xem trước (Preview file)

| Nén   | Độ phân giải                          | Độ sâu màu        | Dung lượng        | Khả năng tương thích                                 |
| ----- | ------------------------------------- | ----------------- | ----------------- | ---------------------------------------------------- |
| Lossy | Càng thấp càng tốt (đảm bảo đọc được) | Dựa trên file gốc | Càng nhỏ càng tốt | Tương thích tốt với tất cả trình duyệt, hệ điều hành |

**Ảnh chụp/ Bitmap image:** .JPEG
**Ảnh có nền trong suốt:** .PNG
**Dàn trang/ Collection:** .PDF
**Ảnh động:** .GIF

> [!Tip] Tip
> Với ảnh preview ngoài giảm chất lượng hình ảnh, còn có thể gắn thêm watermark hoặc các dấu hiệu đặc biệt đã đánh bản quyền tác giả cũng như đánh dấu việc chưa thanh toán và không công khai rộng rãi.

### 6. Lưu trữ (Storage file)

> [!Tip] Tip
> Trong tất cả các dự án hãy cố gắng lưu trữ đầy đủ Working file và Intermediate file sau khi đã đóng dự án. 
> Nên lưu trữ các file dự án cũ ít nhất 1 năm bằng 1 nền tảng lưu trữ cloud hoặc ổ cứng. Để tiết kiệm chi phí, nền tảng lưu trữ không cần tốc độ cao chỉ cần không gian lưu trữ lớn là đủ (vì các file lưu trữ thường ít được truy cập lại).

### 7. Chia sẻ (Sharing file)

| Nén                 | Độ phân giải             | Độ sâu màu        | Dung lượng        | Khả năng tương thích                                 |
| ------------------- | ------------------------ | ----------------- | ----------------- | ---------------------------------------------------- |
| Lossless hoặc Lossy | Tùy theo nhu cầu chia sẻ | Dựa trên file gốc | Càng nhỏ càng tốt | Tương thích tốt với tất cả trình duyệt, hệ điều hành |

**Ảnh chụp/ Bitmap image với kích thước nhỏ:** .PNG
**Ảnh chụp/ Bitmap image với kích thước lớn:** .JPEG
**Ảnh có nền trong suốt:** .PNG
**Dàn trang/ Collection:** .PDF
**Ảnh động:** .GIF

### 8. Sử dụng cho mục đích đặc biệt (Special file)

**Windows Icon:** .ICO
**Lưu trữ Database:** 
- BLOB (Base64) - đối với file nhỏ/ số lượng file ít
- URL - đối với file lớn/ số lượng file nhiều
**Ảnh với hệ sinh thái Apple:** .HEIF

## Một vài cách để giảm kích thước tệp mà vẫn tối ưu trải nghiệm xem

- Xóa bớt metadata nếu không cần thiết.
- Thử giảm độ sâu màu nếu chất lượng màu không thay đổi quá nhiều thì có thể cân nhắc.
- Với những ảnh như grayscale nên sử dụng 8-bit màu thay vì 24-bit hay cao hơn hoặc chọn đúng Color Mode là Grayscale ngay lúc tạo file (nếu có thể).
- Thay đổi kích thước hình ảnh theo kích thước chính xác mà nó sẽ được hiển thị.
- Sử dụng định dạng tệp hình ảnh được tối ưu hóa cho mục đích sử dụng. Nếu hình ảnh sẽ được hiển thị trên nhiều phương tiện, hãy chọn định dạng tối ưu cho từng phương tiện riêng lẻ (Sử dụng theo `picture` cùng với `media query`.