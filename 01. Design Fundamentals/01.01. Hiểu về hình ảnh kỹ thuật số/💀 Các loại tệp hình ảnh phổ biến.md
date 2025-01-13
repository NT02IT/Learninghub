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

### JPEG (JPG) — Joint Photographic Experts Group

| Image type | Compress | Color depth | Browsers               | Use cases                                             |
| ---------- | -------- | ----------- | ---------------------- | ----------------------------------------------------- |
| Raster     | Lossy    | upto 24-bit | Tất cả các trình duyệt | Ảnh tĩnh;<br>Web Images;<br>Ảnh xem trước;<br>Chia sẻ |
Tùy theo sở thích, bạn có thể để format này ở dạng ‘JPEG’ hoặc ‘JPG’ – cả hai đều là dạng viết tắt chấp nhận được của cùng một định dạng – [Joint Photographic Experts Group](https://en.wikipedia.org/wiki/JPEG).

![Tiger Image JPEG Format](https://i.imgur.com/sHX8Sfr.jpeg)

JPEG là định dạng tệp hình ảnh raster sử dụng phương pháp nén [[Nén hình ảnh Lossy và Lossless|Lossy]], hỗ trợ lên đến 24 bit màu phù hợp để chia sẻ hình ảnh. Định dạng JPEG còn cho phép bạn lựa chọn linh hoạt độ nén của ảnh – từ 0% (nén nặng nhất) đến 100% (không nén). Nhìn chung, độ nén ở khoảng 60%-75% sẽ giảm thiểu dung lượng khá khá, trong khi vẫn đảm bảo chất lượng trên đa số màn hình.

Tuy JPEG phù hợp cho việc nén và render ảnh chụp, đây lại là dạng nén khá lỏng lẻo, không tiện cho việc chỉnh sửa chuyên sâu. Sau mỗi lần export ảnh JPEG, chất lượng sẽ bị giảm đi một tý. Vì lý do này, nhiều nhiếp ảnh gia thường chụp ở chuẩn RAW Lossless.

Dù vậy JPEG vẫn là một trong những loại tệp hình ảnh được sử dụng nhiều nhất mà bạn sẽ thấy trên internet vì khả năng nén và hỗ trợ hầu hết các trình duyệt/hệ điều hành phổ biến.

**Ưu điểm và nhược điểm:**
- Được hỗ trợ kể từ phiên bản 1.0 của tất cả các trình duyệt chính (Chrome, Firefox, Safari, v.v.)
- Được hỗ trợ theo mặc định bởi tất cả trình xem và trình chỉnh sửa hình ảnh của tất cả các hệ điều hành chính.
- Kích thước tệp khá nhỏ.
- Nén hình ảnh mất dữ liệu có thể dẫn đến khả năng đọc văn bản kém.

**Use cases:**
- Lựa chọn tốt cho hình ảnh blog và bài viết
- Không sử dụng JPEG cho đồ họa thông tin có nhiều văn bản nhỏ hoặc ảnh chụp màn hình hướng dẫn mà văn bản là cực kỳ quan trọng.

### HEIF — High Efficiency Image Format
| Image type | Compress                   | Color bit depth | Browsers                 | Use cases                                                                                            |
| ---------- | -------------------------- | --------------- | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| Raster     | Lossy (Nén nâng cao H.265) |                 | Không hỗ trợ trình duyệt | Ảnh tĩnh;<br>Bộ sưu tập ảnh, ảnh liên tục;<br>Lưu trữ (Chất lượng cao hơn nhưng chiếm ít bộ nhớ hơn) |
![JPEG vs HEIF format](https://i.imgur.com/TEUqGga.jpeg)

HEIF, viết tắt của High Efficiency Image File Format, là định dạng hình ảnh do nhóm phát triển định dạng video MPEG phát triển để trở thành đối thủ cạnh tranh trực tiếp với JPEG. Về lý thuyết, khả năng nén hiệu quả gần gấp đôi JPEG, tạo ra hình ảnh có chất lượng gấp đôi với kích thước tệp giống hệt nhau.

Đây là định dạng hình ảnh raster, dựa trên ánh xạ pixel, nghĩa là bạn không thể phóng to hình ảnh mà không làm giảm chất lượng.

**Ưu điểm và nhược điểm:**
- Không được hỗ trợ bởi bất kỳ trình duyệt chính nào.
- Hỗ trợ gốc trong macOS Sierra và iOS 11 trở lên, nhưng không có trong phiên bản Safari tương ứng của chúng.
- Tỷ lệ chất lượng/kích thước tệp tuyệt vời.

**Use cases:**
- Được một số điện thoại và thiết bị mới hơn sử dụng để lưu trữ ảnh có chất lượng cao hơn tệp JPEG.

### PNG — Portable Network Graphics
| Image type | Compress | Color bit depth            | Browsers               | Use cases                                                                                 |
| ---------- | -------- | -------------------------- | ---------------------- | ----------------------------------------------------------------------------------------- |
| Raster     | Lossless | RGB 24-bit <br>RGBA 32-bit | Tất cả các trình duyệt | Ảnh có nền trong suốt;<br>Ảnh có nhiều nội dung văn bản;<br>Ảnh chụp màn hình;<br>Chia sẻ |
![Kinsta’s resource center .png image file](https://i.imgur.com/EmCzuMj.png)

PNG là định dạng đồ họa raster hỗ trợ nén [[Nén hình ảnh Lossy và Lossless|Lossless]], duy trì chi tiết và độ tương phản giữa các màu. Đặc biệt, PNG cung cấp khả năng đọc văn bản tốt hơn nhiều so với JPEG.

Điều này khiến PNG trở thành lựa chọn phổ biến hơn cho infographics, banner, ảnh chụp màn hình và các đồ họa khác bao gồm cả hình ảnh và văn bản.

**Ưu điểm và nhược điểm:**
- Được hỗ trợ bởi tất cả các trình duyệt chính (Chrome, Edge, Firefox, Internet Explorer, Opera, Safari).
- Được hỗ trợ bởi tất cả các hệ điều hành chính và trình chỉnh sửa hình ảnh tiêu chuẩn của chúng.
- Hình ảnh chất lượng cao hơn *(Lossless)* và văn bản hiển thị rõ ràng.
- Kích thước tệp lớn hơn có thể làm chậm trang web của bạn nếu sử dụng quá mức *(đặc biệt là hình ảnh có độ phân giải cao)*.

**Use cases:**
- Lựa chọn tốt cho infographics, banner, ảnh blog, ảnh chụp màn hình và các hình ảnh trực quan khác có chứa văn bản.

### TIFF — Tagged Image File Format

| Image type | Compress           | Color bit depth | Browsers     | Use cases                                                   |
| ---------- | ------------------ | --------------- | ------------ | ----------------------------------------------------------- |
| Raster     | Lossy <br>Lossless | 1 to 24-bit     | Không hỗ trợ | Lưu trữ;<br>In ấn & Xuất bản;<br>Scanner;<br>Bộ sưu tập ảnh |
TIFF, viết tắt của Tagged Image File Format, là định dạng hình ảnh raster thường được sử dụng nhất để lưu trữ và chỉnh sửa hình ảnh sẽ được sử dụng sau này để in.

Mặc dù nó vẫn có hỗ trợ nén Lossy, nhưng nó thường được sử dụng như một định dạng hình ảnh Lossless. Hơn nữa, hầu hết các ứng dụng đồ họa chuyên nghiệp hỗ trợ TIFF (Photoshop, Illustrator, v.v.) đều không sử dụng nén. Các tệp TIFF cũng hỗ trợ nhiều lớp và trang. Do đó, hình ảnh TIFF thường có kích thước tệp lớn.

**Ưu điểm và nhược điểm:**
- Không có trình duyệt chính nào có thể hiển thị tệp TIFF mà không có add-ons hay extensions.
- Chủ yếu có sẵn dưới dạng định dạng export trong các công cụ chỉnh sửa và xuất bản hình ảnh chuyên nghiệp.
- Chất lượng cao hoàn hảo để lưu trữ hoặc xuất bản in.
- Kích thước tệp lớn do không nén *(Lossless)*.

**Use cases:**
- Lưu trữ và chuẩn bị hình ảnh và đồ họa để xuất bản/ in ấn.
- Được nhiều máy quét sử dụng để bảo quản chất lượng của tài liệu hoặc hình ảnh được quét.

### WebP
| Image type | Compress           | Color bit depth | Browsers                                                                                                  | Use cases                                              |
| ---------- | ------------------ | --------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Raster     | Lossy <br>Lossless |                 | Google Chrome (Phiên bản 17+ cho Desktop, 25+ cho Mobile)<br>Firefox (65+)<br>Edge (18+) và Opera (11.0+) | Ảnh trong suốt;<br>Hoạt ảnh;<br>Lưu trữ;<br>Web images |
![WebP image example](https://i.imgur.com/MASa1iR.jpeg)

WebP là định dạng hình ảnh được phát triển đặc biệt để cung cấp khả năng nén Lossless và Lossy nâng cao. Việc chuyển từ JPEG và PNG sang WebP có thể giúp tiết kiệm dung lượng đĩa máy chủ và băng thông đáng kể, với các tệp hình ảnh nhỏ hơn tới 35% nhưng vẫn có chất lượng giống hệt nhau.

**Ưu điểm và nhược điểm:**
- Google Chrome (Phiên bản 17+ cho Desktop, 25+ cho Mobile), Firefox (65+), Edge (18+) và Opera (11.0+) hỗ trợ WebP. 
- Định dạng này vẫn chưa được hầu hết các trình chỉnh sửa hình ảnh gốc của hệ điều hành hỗ trợ, nhưng các tùy chọn chuyên nghiệp như Photoshop hỗ trợ WebP.
- Các tệp nhỏ hơn cho chất lượng hình ảnh tương đương hoặc tốt hơn.
- Không được hỗ trợ bởi tất cả các trình duyệt và trình chỉnh sửa hình ảnh.

**Use cases:**
- Thay thế các tệp JPEG và PNG để tiết kiệm băng thông và tăng tốc trang web của bạn. Khi sử dụng WebP nên cung cấp thêm các định dạng khác cho các trình duyệt cũ.

### GIF — Graphics Interchange Format
| Image type | Compress | Color bit depth | Browsers               | Use cases                                     |
| ---------- | -------- | --------------- | ---------------------- | --------------------------------------------- |
| Raster     | Lossless | 8-bit           | Tất cả các trình duyệt | Hoạt ảnh;<br>Flat Design;<br>Chia sẻ;<br>Meme |
![Example of a gif image](https://i.imgur.com/AuTy1jx.gif)

GIF là một loại tệp hình ảnh khác nằm trong định dạng raster. GIF sử dụng nén [[Nén hình ảnh Lossy và Lossless|Lossless]] nhưng “hạn chế” hình ảnh ở mức 8 bit cho mỗi pixel và bảng màu giới hạn là 256 màu.

Định dạng GIF nổi tiếng nhất *(và được sử dụng nhiều nhất)* cho hình ảnh động vì giới hạn 8 bit của nó giúp giữ kích thước tệp hình ảnh động nhỏ và thân thiện với internet.

**Ưu điểm và nhược điểm:**
- Được hỗ trợ bởi tất cả các trình duyệt chính (Chrome, Edge, Firefox, Internet Explorer, Opera, Safari).
- Được hỗ trợ bởi tất cả các hệ điều hành chính và trình chỉnh sửa hình ảnh tiêu chuẩn của chúng.
- Kích thước tệp nhỏ.
- Hỗ trợ hoạt ảnh.
- Giới hạn 8 bit dẫn đến chất lượng hình ảnh hạn chế.

**Use cases:**
- Sử dụng GIF cho hoạt ảnh.
- Không sử dụng nếu bạn cần hình ảnh màu lớn hơn 8 bit.

### SVG — Scalable Vector Graphics
| Image type | Compress | Color bit depth | Browsers               | Use cases                                                                        |
| ---------- | -------- | --------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Vector     | None     |                 | Tất cả các trình duyệt | Vector Artwork (Logo, Icon, Vector Illustrations,...);<br>Lưu trữ;<br>Web Images |
![SVG logo](https://i.imgur.com/ebaAnWD.png)

Định dạng tệp Scalable Vector Graphics, thường được gọi là SVG, được W3C phát triển như một ngôn ngữ đánh dấu để hiển thị hình ảnh hai chiều ngay trong trình duyệt. Định dạng này không dựa vào pixel như định dạng raster mà sử dụng văn bản XML để phác thảo hình dạng và đường thẳng theo cách tương tự như cách các phương trình toán học tạo ra đồ thị.

Khi được viết theo markup gốc XML, file SVG của bạn sẽ có thể được edit trong mọi text editor và được modify bằng JavaScript hoặc CSS. Vì có thể giữ lại chất lượng ở mọi kích thướng ảnh, vector rất lý tưởng cho thiết kế responsive.

Tuy SVG về bản chất là dạng vector, nhưng bạn vẫn có thể (thậm chí còn rất thường thấy) embed thành phần hình ảnh bitmap ngay trong fiel SVG – giống y như cách bạn embed JPEGs vào HTML.

Bạn có thể làm được điều này bằng cách liên kết URL nguồn ảnh (giống cách bạn link JPG lên webpage) hoặc bằng cách chuyển đổi hình ảnh pixel sang dạng Data URI. Như bạn thấy, SVG nhờ điểm này mà có được sức mạnh và sự linh hoạt không sao bì được.

> [!NOTE] 
> Nếu bạn cần giảm kích thước tệp của SVG (ví dụ: để chia sẻ trực tuyến dễ dàng hơn), bạn có thể xuất tệp đó dưới dạng tệp [.svgz](https://fileinfo.com/extension/svgz). Khi đó hình ảnh sẽ được nén bởi gzip và giảm kích thước tệp của nó từ 50 đến 80%.

**Ưu điểm và nhược điểm:**
- Được hỗ trợ bởi tất cả các trình duyệt chính (Chrome, Edge, Firefox, Internet Explorer, Opera, Safari).
- Các trình chỉnh sửa hình ảnh mặc định có xu hướng không hỗ trợ SVG (vì nó không phù hợp với ảnh chụp), nhưng hầu hết các phần mềm minh họa đều hỗ trợ xuất SVG.

**Use cases:**
- SVG là định dạng lý tưởng cho logo, biểu tượng, hình minh họa đơn giản hay bất kỳ thứ gì khác mà bạn muốn có thể tự do scale.

### EPS — Encapsulated Postscript
| Image type | Compress | Color bit depth | Browsers     | Use cases                                                                                             |
| ---------- | -------- | --------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| Vector     | None     |                 | Không hỗ trợ | Vector Artwork (Logo, Icon, Vector Illustrations,...);<br>Lưu trữ;<br>In ấn;<br>Trung gian chuyển đổi |
Về bản chất, tệp EPS (Encapsulated PostScript) là tệp hình ảnh vector được sử dụng để lưu trữ hình minh họa trong Adobe Illustrator và các phần mềm minh họa khác như CorelDraw.

Giống như tệp SVG, EPS thực chất là một tài liệu dạng văn bản phác thảo hình dạng và đường thẳng bằng mã, thay vì ánh xạ pixel và màu sắc. Do đó, tệp EPS cũng hỗ trợ tính năng Lossless scaling.

**Ưu điểm và nhược điểm:**
- EPS không phải là định dạng tệp hình ảnh web chuẩn và không được bất kỳ trình duyệt chính nào hỗ trợ.
- Lossless scaling

**Use cases:**
- Chủ yếu được sử dụng để lưu trữ, lưu lại và in hình minh họa khi làm việc với Adobe Illustrator hoặc phần mềm khác.

### PDF — Portable Document Format
| Image type | Compress | Color bit depth | Browsers | Use cases                                                                                                     |
| ---------- | -------- | --------------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| Vector     | None     |                 |          | Vector Artwork (Logo, Icon, Vector Illustrations);<br>Lưu trữ;<br>In ấn;<br>Chia sẻ;<br>Tài liệu có tương tác |
Tệp PDF là một loại tài liệu được sử dụng rộng rãi để duy trì bố cục và định dạng ban đầu trên các thiết bị và hệ điều hành khác nhau. Nó thường được sử dụng để chia sẻ tài liệu, chẳng hạn như báo cáo, hợp đồng, hướng dẫn sử dụng hoặc biểu mẫu, đảm bảo rằng nội dung xuất hiện giống nhau cho tất cả người dùng. Các tệp PDF có thể bao gồm văn bản, hình ảnh, chú thích và thậm chí cả các yếu tố tương tác (ví dụ: nút và hộp kiểm) và người dùng thường tạo chúng từ các định dạng tệp khác, chẳng hạn như tài liệu Word .DOCX, Excel . Bảng tính và hình ảnh XLSX.

Bạn có thể gặp các tệp PDF theo nhiều cách khác nhau, cho dù tải xuống tài liệu từ trang web hay nhận tài liệu từ đồng nghiệp hoặc bạn bè dưới dạng tệp đính kèm email. Các tệp PDF cũng giữ nguyên phông chữ và định dạng điện tử trên nhiều nền tảng và xuất hiện giống nhau trên màn hình như khi in trên giấy.

Đây là định dạng được lựa chọn để lưu trữ hình minh họa, bìa tạp chí và nhiều thứ khác để in ấn.

**Ưu điểm và nhược điểm:**
- Được hỗ trợ bởi tất cả các trình duyệt chính.
- Được hỗ trợ dưới dạng định dạng bởi hầu hết các trình chỉnh sửa tài liệu chuẩn (như MS Word hoặc Google Docs) và phần mềm minh họa (AI, Inkscape) nhưng không được hỗ trợ bởi phần mềm chỉnh sửa hình ảnh.
- Văn bản có thể lập chỉ mục và tìm kiếm được làm cho nó hoàn hảo cho đồ họa thông tin hoặc báo cáo chuyên sâu.
- Có thể bao gồm các liên kết, nút CTA và các thành phần tương tác khác.
- Lossless scaling

**Use cases:**
- PDF là lựa chọn tốt nhất nếu bạn muốn tạo báo cáo trực quan tương tác hoặc đồ họa thông tin bổ sung cho nội dung của mình.

### Raw Image File Types
| Image type | Compress | Color bit depth | Browsers     | Use cases                        |
| ---------- | -------- | --------------- | ------------ | -------------------------------- |
| Raster     | Lossless | -               | Không hỗ trợ | Nhiếp ảnh;<br>Hậu kỳ;<br>Lưu trữ |
Định dạng ảnh thô là loại tệp mà máy ảnh kỹ thuật số sử dụng để lưu trữ hình ảnh chất lượng đầy đủ cho quá trình hậu kỳ và chỉnh sửa sau này.

Các loại tệp ảnh thô chính theo hãng sản xuất máy ảnh:
- Kodak: CR, K25, KDC
- Canon: CRW CR2 CR3
- Epson: ERF
- Nikon: NEF NRW
- Olympus: ORF
- Pentax: PEF
- Panasonic: RW2
- Sony: ARW, SRF, SR2

Tệp RAW cung cấp tới 16.384 sắc thái trên mỗi kênh màu (14 bit) trong một hình ảnh duy nhất. Điều đó giúp bạn linh hoạt hơn khi tinh chỉnh màu sắc và độ tương phản trong quá trình hậu xử lý. 

**Ưu điểm và nhược điểm:**
- Hình ảnh thô không dành cho web hoặc chia sẻ và không được bất kỳ trình duyệt hoặc trình xem hình ảnh chính nào hỗ trợ.
- Hình ảnh chất lượng cao hơn với nhiều màu sắc đa dạng hơn.
- Tệp hình ảnh khổng lồ (tệp thô có thể dễ dàng lên tới 20 đến 40MB).

**Use cases:**
- Lưu ảnh ở chất lượng cao nhất có thể để xử lý hậu kỳ và chỉnh sửa.

### Bảng tóm tắt và so sánh

| Format                                       | File extensions                                                                                                                                                                                                                | Compress             | Best For                                                               | Special Attributes                                                                                                            | Limit                                    |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **JPEG** (Joint Photographic Experts Groups) | [.jpg](https://fileinfo.com/extension/jpg), [.jpeg](https://fileinfo.com/extension/jpeg)                                                                                                                                       | Lossy                | Web Images, In không chuyên nghiệp, E-Mail, Powerpoint                 | Có thể chọn lượng nén khi lưu trong các chương trình chỉnh sửa hình ảnh                                                       | Giảm chất lượng sau mỗi lần Export       |
| **HEIF** (High Efficiency Image Format)      | [.heif](https://fileinfo.com/extension/heif)                                                                                                                                                                                   | Lossy - nén nâng cao | Lưu trữ, Hậu kỳ                                                        | Có thể gói một loạt hình ảnh vào 1 file duy nhất;<br>Save Transparency                                                        | Trình duyệt hỗ trợ hạn chế               |
| **PNG** (Portable Network Graphics)          | [.png](https://fileinfo.com/extension/png)                                                                                                                                                                                     | Lossless             | Web Images                                                             | Save Transparency                                                                                                             |                                          |
| **TIFF** (Tagged Image File Format)          | [.tif](https://fileinfo.com/extension/tif), [.tiff](https://fileinfo.com/extension/tiff)                                                                                                                                       | Lossless             | Lưu trữ, Hậu kỳ, Artwork, Bản in chất lượng cao, Ấn phẩm chuyên nghiệp | Save Transparency                                                                                                             | Trình duyệt hỗ trợ hạn chế               |
| **WEBP**                                     | [.webp](https://fileinfo.com/extension/webp)                                                                                                                                                                                   | Lossy and Lossless   | Blogger, Web Images                                                    | Nén tốt, cho ra chất lượng ảnh tốt hơn cả PNG và JPEG trong khi dung lượng nhỏ hơn;<br>Save Transparency; <br>Can be Animated | Không tương thích với một số trình duyệt |
| **GIF** (Graphics Interchange Format)        | [.gif](https://fileinfo.com/extension/gif)                                                                                                                                                                                     | Lossless             | Web Images, Animated, Flat Design                                      | Có thể lưu hình ảnh có nền trong suốt; Có thể lưu hoạt ảnh (animated)                                                         | Chỉ hỗ trợ 8bit (256 màu)                |
| **SVG** (Scalable Vector Graphics)           | [.svg](https://fileinfo.com/extension/svg)                                                                                                                                                                                     | None                 | Lưu trữ, Vector Artwork, Logo, Illustrations                           | Embed bitmap                                                                                                                  |                                          |
| **EPS** (Encapsulated PostScript)            | [.eps](https://fileinfo.com/extension/eps)                                                                                                                                                                                     | None                 | Lưu trữ, Vector Artwork, Illustrations                                 | Lưu thông tin vector                                                                                                          |                                          |
| **RAW** Image Files                          | [.raw](https://fileinfo.com/extension/raw), [.cr2](https://fileinfo.com/extension/cr2), [.nef](https://fileinfo.com/extension/nef), [.orf](https://fileinfo.com/extension/orf), [.sr2](https://fileinfo.com/extension/sr2),... | None                 | Lưu trữ, Hậu kỳ, Photography                                           | Lưu metadata, nhiều thông tin thô chưa qua xử lý                                                                              |                                          |
| **PDF** (Portable Document Format)           | [.pdf](https://fileinfo.com/extension/pdf)                                                                                                                                                                                     | Lossless             | Lưu trữ, Printing                                                      | Có thể chứa các yếu tố tương tác như liên kết, Bảo vệ dữ liệu bằng mật khẩu                                                   | Khó chỉnh sửa                            |

## Hướng dẫn chọn loại tệp phù hợp (Recommend)

### Các loại tệp cho hình ảnh là gì?

Các định dạng tệp hình ảnh phổ biến bao gồm JPEG, PNG, GIF, TIFF, WebP, SVG, BMP và HEIF. Mỗi loại đều có điểm mạnh riêng: **JPEG** rất phù hợp cho ảnh, **PNG** lý tưởng cho hình ảnh có độ trong suốt, **GIF** hỗ trợ hoạt ảnh đơn giản, **TIFF** được sử dụng cho các bản in chất lượng cao, các loại tệp ảnh **WebP và AVIF** cung cấp khả năng nén hiệu quả, **SVG** là định dạng vector có thể mở rộng, **BMP** là định dạng không nén và **HEIF** là định dạng mới hơn cung cấp chất lượng tốt hơn **JPEG** ở kích thước nhỏ hơn.
### Định dạng tệp hình ảnh nào tốt hơn để sử dụng và tại sao?

Định dạng hình ảnh tốt nhất phụ thuộc vào nhu cầu của bạn. WebP rất phù hợp để sử dụng web, cung cấp độ nén cao với mức giảm chất lượng tối thiểu, mặc dù nó không được hỗ trợ bởi tất cả các trình duyệt. JPEG lý tưởng cho ảnh, cân bằng chất lượng và kích thước tệp. PNG hoàn hảo cho các loại hình ảnh có văn bản, logo hoặc độ trong suốt, nhưng nó dẫn đến kích thước tệp lớn hơn.

### Định dạng hình ảnh tốt nhất cho chất lượng là gì?

Để có định dạng hình ảnh chất lượng tốt nhất với kích thước tệp nhỏ hơn, **WebP** là một lựa chọn tuyệt vời, cung cấp khả năng nén tuyệt vời trong khi vẫn duy trì chất lượng hình ảnh cao. Đối với chất lượng không mất dữ liệu, **PNG** hoạt động tốt, đặc biệt là đối với hình ảnh có độ trong suốt. Nếu bạn cần chất lượng hàng đầu cho mục đích in ấn hoặc lưu trữ, **TIFF** là lý tưởng, nhưng đối với hầu hết các mục đích sử dụng web, **WebP** và **PNG** là định dạng ảnh phù hợp.

### Loại dữ liệu phù hợp nhất cho trường tệp hình ảnh trong form là gì? ⇒ BLOB (Mã nhị phân) 

Kiểu dữ liệu phù hợp nhất cho trường tệp hình ảnh thường là **BLOB** (Binary Large Object). Nó cho phép lưu trữ các tệp hình ảnh trực tiếp trong cơ sở dữ liệu dưới dạng dữ liệu nhị phân, giúp dễ dàng quản lý và truy xuất. Tuy nhiên, đối với hình ảnh lớn hơn hoặc hiệu suất tốt hơn, lưu trữ tệp hình ảnh trên máy chủ và lưu đường dẫn tệp hoặc URL trong cơ sở dữ liệu thường hiệu quả hơn.

[[Updating...]]

---
## References:

[Image File Formats - All About Images - Research Guides at University of Michigan Library](https://guides.lib.umich.edu/c.php?g=282942&p=1885348)
[9 Best Image File Types [+ Pros, Cons and the Best Use Cases] - ShortPixel Blog](https://shortpixel.com/blog/best-image-file-types/)
[15 Best Image File Types (Pros vs Cons of Each Format)](https://kinsta.com/blog/image-file-types/)