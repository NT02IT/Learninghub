---
created: 2025-01-12T03:59:00
tags:
  - Design
  - Image
  - FileFormat
  - Compare
---
## Native File Formats

Không chỉ có định dạng hình ảnh mà nhiều ứng dụng có định dạng tệp gốc của riêng chúng. Điều quan trọng là phải hiểu rằng có sự khác biệt giữa loại tệp gốc và loại tệp hình ảnh.

Một ví dụ về loại tệp gốc là .PSD viết tắt của Photoshop Document. Tệp này chỉ được tạo bởi Adobe Photoshop và có thể giữ lại thông tin như lớp, điều chỉnh, mặt nạ và các điều chỉnh Photoshop khác.

Bạn nên lưu một phiên bản của hình ảnh ở định dạng gốc nếu bạn định thực hiện các chỉnh sửa trong tương lai đối với hình ảnh, vì định dạng tệp gốc sẽ giữ tất cả thông tin chỉnh sửa.

### Image Editors

Adobe Photoshop - [(.PSD)](http://www.fileinfo.com/extension/psd)
GIMP - [(.XCF)](http://www.fileinfo.com/extension/xcf)

### Illustration/Vector Art

Adobe Illustrator - [(.AI)](http://www.fileinfo.com/extension/ai)
CorelDRAW - [(.CDR)](http://www.fileinfo.com/extension/cdr)

## Common Image File Formats

Có rất nhiều loại tệp hình ảnh nên rất khó để biết loại tệp nào phù hợp nhất với nhu cầu sử dụng của bạn. Một số loại hình ảnh như TIFF rất phù hợp để in trong khi những loại khác, như JPG hoặc PNG, tốt nhất cho đồ họa web.

Danh sách dưới đây phác thảo một số loại tệp phổ biến hơn và cung cấp mô tả ngắn gọn, cách sử dụng tệp tốt nhất và bất kỳ thuộc tính đặc biệt nào mà tệp có thể có.

| Format                                       | File extensions                                                                                                                                                                                                                | Compress             | Best For                                                           | Special Attributes                                                                                                            | Limit                                    |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **JPEG** (Joint Photographic Experts Groups) | [.jpg](https://fileinfo.com/extension/jpg), [.jpeg](https://fileinfo.com/extension/jpeg)                                                                                                                                       | Lossy                | Web Images, In không chuyên nghiệp, E-Mail, Powerpoint             | Có thể chọn lượng nén khi lưu trong các chương trình chỉnh sửa hình ảnh                                                       | Giảm chất lượng sau nhiều lần chỉnh sửa  |
| **HEIF** (High Efficiency Image Format)      | [.heif](https://fileinfo.com/extension/heif)                                                                                                                                                                                   | Lossy - nén nâng cao |                                                                    | Có thể gói một loạt hình ảnh vào 1 file duy nhất;<br>Save Transparency; <br>16-bit color depth                                | Trình duyệt hỗ trợ hạn chế               |
| **PNG** (Portable Network Graphics)          | [.png](https://fileinfo.com/extension/png)                                                                                                                                                                                     | Lossless             | Web Images                                                         | Save Transparency                                                                                                             |                                          |
| **TIFF** (Tagged Image File Format)          | [.tif](https://fileinfo.com/extension/tif), [.tiff](https://fileinfo.com/extension/tiff)                                                                                                                                       | Lossless             | Artwork, Bản in chất lượng cao, Ấn phẩm chuyên nghiệp, Bản sao lưu | Save Transparency                                                                                                             | Khó chia sẻ, trình duyệt hỗ trợ hạn chế  |
| **WEBP**                                     | [.webp](https://fileinfo.com/extension/webp)                                                                                                                                                                                   | Lossy and Lossless   | Blogger                                                            | Nén tốt, cho ra chất lượng ảnh tốt hơn cả PNG và JPEG trong khi dung lượng nhỏ hơn;<br>Save Transparency; <br>Can be Animated | Không tương thích với một số trình duyệt |
| **GIF** (Graphics Interchange Format)        | [.gif](https://fileinfo.com/extension/gif)                                                                                                                                                                                     | Lossless             | Web Images                                                         | Có thể lưu hình ảnh có nền trong suốt; Có thể lưu hoạt ảnh (animated)                                                         | Chỉ hỗ trợ 8bit (256 màu)                |
| **EPS** (Encapsulated PostScript)            | [.eps](https://fileinfo.com/extension/eps)                                                                                                                                                                                     | None                 | Vector artwork, illustrations                                      | Lưu thông tin vector                                                                                                          |                                          |
| **RAW** Image Files                          | [.raw](https://fileinfo.com/extension/raw), [.cr2](https://fileinfo.com/extension/cr2), [.nef](https://fileinfo.com/extension/nef), [.orf](https://fileinfo.com/extension/orf), [.sr2](https://fileinfo.com/extension/sr2),... | None                 | Photography                                                        | Lưu metadata, nhiều thông tin thô chưa qua xử lý                                                                              |                                          |
| **PDF** (Portable Document Format)           | [.pdf](https://fileinfo.com/extension/pdf)                                                                                                                                                                                     | Lossless             | Printing                                                           | Có thể chứa các yếu tố tương tác như liên kết, Bảo vệ dữ liệu bằng mật khẩu                                                   | Khó chỉnh sửa                            |

## Hướng dẫn chọn loại tệp phù hợp (Recommend)

### Các loại tệp cho hình ảnh là gì?

Các định dạng tệp hình ảnh phổ biến bao gồm JPEG, PNG, GIF, TIFF, WebP, SVG, BMP và HEIF. Mỗi loại đều có điểm mạnh riêng: **JPEG** rất phù hợp cho ảnh, **PNG** lý tưởng cho hình ảnh có độ trong suốt, **GIF** hỗ trợ hoạt ảnh đơn giản, **TIFF** được sử dụng cho các bản in chất lượng cao, các loại tệp ảnh **WebP và AVIF** cung cấp khả năng nén hiệu quả, **SVG** là định dạng vector có thể mở rộng, **BMP** là định dạng không nén và **HEIF** là định dạng mới hơn cung cấp chất lượng tốt hơn **JPEG** ở kích thước nhỏ hơn.
### Định dạng tệp hình ảnh nào tốt hơn để sử dụng và tại sao?

Định dạng hình ảnh tốt nhất phụ thuộc vào nhu cầu của bạn. WebP rất phù hợp để sử dụng web, cung cấp độ nén cao với mức giảm chất lượng tối thiểu, mặc dù nó không được hỗ trợ bởi tất cả các trình duyệt. JPEG lý tưởng cho ảnh, cân bằng chất lượng và kích thước tệp. PNG hoàn hảo cho các loại hình ảnh có văn bản, logo hoặc độ trong suốt, nhưng nó dẫn đến kích thước tệp lớn hơn.

### Định dạng hình ảnh tốt nhất cho chất lượng là gì?

Để có định dạng hình ảnh chất lượng tốt nhất với kích thước tệp nhỏ hơn, **WebP** là một lựa chọn tuyệt vời, cung cấp khả năng nén tuyệt vời trong khi vẫn duy trì chất lượng hình ảnh cao. Đối với chất lượng không mất dữ liệu, **PNG** hoạt động tốt, đặc biệt là đối với hình ảnh có độ trong suốt. Nếu bạn cần chất lượng hàng đầu cho mục đích in ấn hoặc lưu trữ, **TIFF** là lý tưởng, nhưng đối với hầu hết các mục đích sử dụng web, **WebP** và **PNG** là định dạng ảnh phù hợp.

### Loại dữ liệu phù hợp nhất cho trường tệp hình ảnh trong form là gì? ⇒ BLOB (Mã nhị phân) 

Kiểu dữ liệu phù hợp nhất cho trường tệp hình ảnh thường là **BLOB** (Binary Large Object). Nó cho phép lưu trữ các tệp hình ảnh trực tiếp trong cơ sở dữ liệu dưới dạng dữ liệu nhị phân, giúp dễ dàng quản lý và truy xuất. Tuy nhiên, đối với hình ảnh lớn hơn hoặc hiệu suất tốt hơn, lưu trữ tệp hình ảnh trên máy chủ và lưu đường dẫn tệp hoặc URL trong cơ sở dữ liệu thường hiệu quả hơn.

---
## References:

[Image File Formats - All About Images - Research Guides at University of Michigan Library](https://guides.lib.umich.edu/c.php?g=282942&p=1885348)
[9 Best Image File Types [+ Pros, Cons and the Best Use Cases] - ShortPixel Blog](https://shortpixel.com/blog/best-image-file-types/)
