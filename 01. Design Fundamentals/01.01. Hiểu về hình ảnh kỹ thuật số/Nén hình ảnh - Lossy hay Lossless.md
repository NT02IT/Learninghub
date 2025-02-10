---
aliases:
  - Lossy
  - Lossless
created: 2025-01-11T19:25:00
tags:
  - Design
  - Image
---
**Nén hình ảnh** là một kỹ thuật nén dữ liệu nhằm giảm dung lượng lưu trữ hoặc chi phí truyền tải của hình ảnh kỹ thuật số. Các thuật toán nén tận dụng khả năng cảm nhận thị giác của con người và các đặc tính thống kê của dữ liệu hình ảnh, mang lại hiệu quả cao hơn so với các phương pháp nén thông thường.

## 1. Phân loại nén ảnh: Lossy và Lossless 

### 1.1. Lossy: Nén mất dữ liệu

> Nén mất dữ liệu là một phương pháp mã hóa dữ liệu giúp giảm kích thước tệp bằng cách loại bỏ các chi tiết không cần thiết. Nén hình ảnh mất dữ liệu sẽ loại bỏ vĩnh viễn dữ liệu ít cần thiết hơn.

Nén mất dữ liệu là cách hiệu quả nhất để quản lý hình ảnh kỹ thuật số. Điều này đặc biệt đúng đối với việc sử dụng web, có thể giảm kích thước tệp lên đến 90% trong khi vẫn duy trì giao diện chất lượng cao.

#### Nén Lossy hoạt động như thế nào

Nén hình ảnh mất dữ liệu đòi hỏi phải giảm dữ liệu cẩn thận và duy trì chất lượng. Quy trình kỹ thuật này hoạt động:

![](https://i.imgur.com/PThdGZL.jpeg)

**Bước 1:** Ban đầu, thuật toán lossy quét hình ảnh để tìm dữ liệu có thể sử dụng, tập trung vào các biến thể màu sắc mà bạn không thể nhìn thấy bằng mắt thường. Sau đó, quá trình lượng tử hóa (quantization) nhóm các giá trị tương tự để đơn giản hóa dữ liệu.

**Bước 2:** Bước tiếp theo mã hóa dữ liệu đơn giản hóa, sử dụng các thuật toán như DCT để loại bỏ dư thừa dữ liệu. Các kỹ thuật như biến đổi không gian màu YCbCr và DCT thể hiện dữ liệu hình ảnh một cách hiệu quả.

**Bước 3:** Hình ảnh nén cuối cùng nhỏ hơn nhiều, nhưng nó vẫn có chất lượng đủ tốt cho hầu hết các mục đích sử dụng, đặc biệt là đối với đồ họa web và phương tiện kỹ thuật số.

Hãy nhớ rằng, dữ liệu nén hình ảnh mất dữ liệu là không thể đảo ngược và nén quá mức có thể dẫn đến giảm chất lượng đáng kể. Nó có lợi khi ưu tiên hiệu quả lưu trữ và băng thông hơn nhu cầu về độ trung thực của hình ảnh hoàn hảo.

#### Một số thuật toán nén Lossy

- **Giảm không gian màu:** Chỉ giữ lại các màu phổ biến nhất, dùng bảng màu để tham chiếu, kết hợp dithering để tránh hiệu ứng phân tầng màu (posterization).
- [**Chroma Subsampling**](https://www.educative.io/blog/chroma-subsampling): Giảm dữ liệu màu sắc, tận dụng đặc điểm mắt người nhạy với độ sáng hơn là màu sắc.
- **Mã hóa bằng chuyển đổi:**
    - **Biến đổi Cosine rời rạc (DCT):** Rất phổ biến, dùng trong JPEG.
    - **Biến đổi sóng (Wavelet Transform):** Dùng trong JPEG 2000, nén mạnh hơn DCT.
- [**Fractal Image Compression**](https://users.cs.northwestern.edu/~agupta/_projects/image_processing/web/FractalImageCompression/index.html): Sử dụng các mẫu tự tương tự (fractals) trong hình ảnh để giảm kích thước của chúng bằng cách tìm và mã hóa các mẫu này xuất hiện nhiều lần.

#### Các loại tệp hình ảnh nén Lossy

**JPEG:** Lý tưởng cho những bức ảnh nhiều màu sắc, hỗ trợ hàng triệu màu sắc và có khả năng nén có thể điều chỉnh. JPEG cân bằng chất lượng hình ảnh và kích thước tệp cho các trang web, mạng xã hội và email.

**WebP:** Hình ảnh web do Google phát triển này vượt trội hơn PNG và JPEG về độ trong suốt và hoạt ảnh. Nó được xây dựng để tăng tốc độ tải hình ảnh web và nén hình ảnh trong khi vẫn duy trì chất lượng hình ảnh.

**HEIC:** Được sử dụng trong các thiết bị Apple mới hơn, nó cung cấp hình ảnh chất lượng cao với kích thước tệp nhỏ để lưu trữ ảnh hiện đại. Nó hỗ trợ các tính năng nâng cao như ảnh trực tiếp và bản đồ độ sâu.

**TIFF:** Mặc dù TIFF được biết đến với khả năng nén không mất dữ liệu, nhưng biến thể mất dữ liệu của nó rất hữu ích trong đồ họa và xuất bản cho các lớp và trang phức tạp. Nó có thể lưu trữ nhiều lớp và trang để chỉnh sửa hình ảnh chi tiết.

#### Ưu và nhược điểm của Nén Lossy

**Ưu điểm của nén mất dữ liệu:**
- **Giảm kích thước:** Kỹ thuật nén mất dữ liệu giúp giảm kích thước tệp hình ảnh một cách hiệu quả và cải thiện hiệu quả dung lượng lưu trữ.
- **Hiệu quả băng thông:** Nén mất dữ liệu làm giảm kích thước tệp và sử dụng băng thông, lý tưởng cho việc duyệt web khi băng thông bị hạn chế.
- **Tải nhanh hơn:** Tải trang nhanh hơn và trải nghiệm người dùng tốt hơn do kích thước hình ảnh nhỏ hơn.
- **Trường hợp sử dụng linh hoạt:** Nén mất dữ liệu phù hợp với ảnh, video và tệp âm thanh có thể chấp nhận được sự giảm chất lượng nhỏ.
- **Nén tùy chỉnh:** Bạn có thể chọn mức nén, cân bằng kích thước tệp và chất lượng hình ảnh dựa trên yêu cầu của mình.

**Nhược điểm của nén mất dữ liệu:**
- **Mất chất lượng:** Nén mất dữ liệu có thể làm giảm chất lượng hình ảnh và gây ra các đối tượng, đặc biệt là ở tỷ lệ nén cao. Nó trở nên tồi tệ hơn khi bạn chỉnh sửa hình ảnh nén mất dữ liệu.
- **Mất dữ liệu vĩnh viễn:** Nếu bạn nén hình ảnh bằng nén mất dữ liệu, bạn không thể lấy lại dữ liệu bị mất. Nó đã biến mất vĩnh viễn.
- **Kém chuyên nghiệp:** Nén mất dữ liệu có thể không đáp ứng các tiêu chuẩn có độ trung thực cao của các nhà thiết kế đồ họa, nghệ sĩ và nhiếp ảnh gia do chất lượng hình ảnh bị ảnh hưởng.

### 1.2. Lossless: Nén không mất dữ liệu

Nén không mất dữ liệu là một phương pháp nén giúp làm cho các tệp nhỏ hơn mà không làm mất dữ liệu. Nó tái tạo hoàn hảo dữ liệu gốc từ dữ liệu nén.

Khi bạn cần những thứ như hình ảnh y tế hoặc bản vẽ kỹ thuật, chính xác là nén không mất dữ liệu là điều cần thiết vì nó giữ được tất cả các chi tiết ban đầu.

#### Nén Lossless hoạt động như thế nào

![](https://i.imgur.com/MmcFVbA.png)

Nén không mất dữ liệu loại bỏ các yếu tố hình ảnh trùng lặp thống kê khỏi các tệp hình ảnh và tạo ra các yếu tố mới nhỏ hơn. Giữ các yếu tố cốt lõi để duy trì chất lượng hình ảnh.

**Bước 1:** Chương trình nén không mất dữ liệu ban đầu xem xét dữ liệu để tìm các mẫu và các bộ phận lặp lại. Nó quét các yếu tố hoặc trình tự lặp lại để xác định và loại bỏ.

**Bước 2:** Sau khi tìm thấy các mẫu này, chương trình sử dụng các phương pháp nén dữ liệu như Huffman hoặc Lempel-Ziv-Welch. Nó cung cấp các mã ngắn của các phần tử dữ liệu phổ biến và các phần tử hiếm có mã dài hơn. Nó làm cho dữ liệu nhỏ hơn nhưng vẫn giữ được chất lượng.

**Bước 3:** Nén không mất dữ liệu có thể khôi phục dữ liệu gốc từ các tệp nén. Điều đó có thể xảy ra do quá trình tạo tệp có thể đảo ngược. Khi bạn mở rộng nó một lần nữa, tệp chứa mọi thứ cần thiết để khôi phục dữ liệu gốc.

#### Một số thuật toán nén Lossless

- **Huffman Coding**: [Thuật toán nén Mã hóa Huffman](https://www.101computing.net/lossless-compression-huffman-coding-algorithm/) giảm kích thước tệp bằng cách sử dụng mã ngắn hơn cho các phần tử dữ liệu thường xuyên xuất hiện. Nó được sử dụng rộng rãi ở các định dạng tệp ZIP và để nén văn bản.
- **Lempel-Ziv-Welch (LZW)**: Thuật toán nén LZW được sử dụng rộng rãi ở các định dạng GIF và TIFF do tính đơn giản và hiệu quả của nó. Nó tiết kiệm không gian bằng cách sử dụng các mã đơn lẻ thay vì các chuỗi ký tự dài hơn.
- **Run-Length Encoding (RLE):** Thuật toán RLE sử dụng số lượng và giá trị thay vì các chuỗi dài của các phần tử lặp lại để tiết kiệm dung lượng trong khi nén. Nó được sử dụng trong hình ảnh bitmap.
- **Deflate**: Deflate là sự kết hợp của mã hóa LZ77 và Huffman. Nó được sử dụng ở các định dạng PNG và ZIP vì nó nhanh và nén tệp tốt.

#### Các loại tệp hình ảnh nén Lossless

**PNG:** Định dạng hình ảnh được sử dụng rộng rãi sử dụng tính năng nén không mất dữ liệu, lý tưởng cho logo, biểu tượng và đồ họa trang web chất lượng cao. PNG hỗ trợ độ trong suốt và chất lượng trong hình ảnh có văn bản và cạnh sắc nét.

**BMP:** BMP là một định dạng hình ảnh lý tưởng cho đồ họa độ phân giải cao với đủ chi tiết. Bạn có thể sử dụng các tệp hình ảnh BMP cho nghệ thuật kỹ thuật số và thiết kế chuyên nghiệp vì chúng nén hình ảnh mà không làm giảm chất lượng.

**RAW:** Các nhiếp ảnh gia chuyên nghiệp thích RAW để chụp tất cả dữ liệu cảm biến để xử lý hậu kỳ linh hoạt. Lưu ảnh ở định dạng RAW. Nó bảo quản dữ liệu hình ảnh mà không làm giảm chất lượng, lý tưởng để lưu trữ.

**GIF:** Bạn có thể sử dụng hình ảnh GIF để tạo hoạt ảnh ngắn và meme trực tuyến. Nhờ sự hỗ trợ của họ cho nhiều khung hình trong một tệp duy nhất. GIF hoạt động tốt cho các nút và biểu ngữ trang web do kích thước tệp nhỏ và không mất dữ liệu.

#### Ưu và nhược điểm của nén không mất dữ liệu

**Ưu điểm của nén không mất dữ liệu**:
1. **Chất lượng gốc**: Nén không mất dữ liệu đảm bảo không làm giảm chất lượng và duy trì tiêu chuẩn ban đầu của tệp hình ảnh.
2. **Có thể đảo ngược**: Bạn có thể tái tạo hoàn hảo tệp gốc từ tệp nén, khiến nó trở nên lý tưởng để lưu trữ.
3. **Hình ảnh chất lượng cao**: Lý tưởng cho âm thanh và hình ảnh chất lượng cao, chẳng hạn như chụp ảnh hoặc in ấn chuyên nghiệp, trong đó độ chính xác của hình ảnh là rất quan trọng.
4. **Chỉnh sửa linh hoạt**: Bạn có thể chỉnh sửa hình ảnh nén không mất dữ liệu mà không làm giảm chất lượng tổng thể.
5. **Các định dạng được hỗ trợ:** Nó hỗ trợ các định dạng hình ảnh phổ biến như PNG và GIF cho hình ảnh và FLAC cho âm thanh, được chấp nhận rộng rãi và dễ làm việc.

**Nhược điểm của nén không mất dữ liệu**:
1. **Kích thước tệp lớn hơn**: Nén không mất dữ liệu dẫn đến kích thước tệp lớn hơn nén mất dữ liệu. Nó ảnh hưởng đến lưu trữ và băng thông.
2. **Không thân thiện với web:** Các tệp hình ảnh không mất dữ liệu có thể làm chậm thời gian tải trang web do kích thước lớn hơn, ảnh hưởng đến trải nghiệm người dùng và SEO.
3. **Nén hạn chế**: Nén ít hơn các phương pháp mất dữ liệu hạn chế khả năng giảm kích thước tệp.

## 2. Lossy và Lossless khi nào nên sử dụng cái nào?

### Khi nào nên sử dụng nén Lossy?

**Lý tưởng để sử dụng web:** Nén mất dữ liệu giúp giảm kích thước tệp và lý tưởng cho các trang web có nhiều hình ảnh như cửa hàng trực tuyến và blog. Bạn có thể cải thiện thời gian tải trang, trải nghiệm người dùng và SEO bằng cách sử dụng nén mất dữ liệu. Các trang web tải nhanh hơn giữ chân khách truy cập, giảm tỷ lệ thoát và tăng chuyển đổi.

**Kiểm soát chất lượng so với kích thước**: Nén mất dữ liệu cho phép bạn kiểm soát sự cân bằng giữa chất lượng hình ảnh và kích thước tệp. Bạn có thể sử dụng các công cụ tối ưu hóa hình ảnh để chọn mức nén lý tưởng của mình, cho phép một cách tiếp cận cân bằng mà không ảnh hưởng quá nhiều đến chất lượng hình ảnh của bạn.

**Phương tiện truyền thông xã hội và chia sẻ trực tuyến**: Nén mất dữ liệu là lựa chọn tốt nhất để chia sẻ hình ảnh trên mạng xã hội hoặc qua email khi thời gian tải lên và tải xuống nhanh chóng quan trọng hơn chất lượng hình ảnh hoàn hảo.

**Khi không gian lưu trữ là ưu tiên**: Nếu tiết kiệm ổ đĩa hoặc dung lượng lưu trữ đám mây quan trọng hơn chất lượng hình ảnh, thì nén mất dữ liệu là lựa chọn phù hợp. Nó có lợi cho việc giảm kích thước hình ảnh hoặc tệp khi chất lượng được ưu tiên thấp.

### Khi nào nên sử dụng nén không mất dữ liệu?

**Lưu trữ**: Nén không mất dữ liệu giữ nguyên chất lượng hình ảnh có độ phân giải cao ban đầu cho các nhiếp ảnh gia, nhà thiết kế đồ họa và nghệ sĩ chuyên nghiệp giới thiệu tác phẩm của họ trực tuyến.

**Hình ảnh y tế và kỹ thuật**: Nén không mất dữ liệu là cần thiết cho các ngành dựa vào hình ảnh chính xác, như bản vẽ kỹ thuật và hình ảnh y tế. Nó đảm bảo phân tích và chẩn đoán chính xác bằng cách lưu giữ tất cả các chi tiết.

**Ứng dụng chuyên nghiệp**: Các nhà thiết kế đồ họa, nghệ sĩ và nhiếp ảnh gia sử dụng nén không mất dữ liệu để duy trì công việc của họ. Các bản in, ấn phẩm và màn hình kỹ thuật số chất lượng cao yêu cầu chất lượng hình ảnh phù hợp để duy trì hiệu quả và giá trị thẩm mỹ.

---
## References:

[Nén hình ảnh](https://thietbikhoahoccongnghe.com.vn/nen-hinh-anh.html)
[Lossy vs Lossless Compression: Comprehensive Analysis - ShortPixel Blog](https://shortpixel.com/blog/lossy-vs-lossless/)