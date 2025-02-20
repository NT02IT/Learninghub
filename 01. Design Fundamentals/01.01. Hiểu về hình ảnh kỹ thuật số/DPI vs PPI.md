---
aliases:
  - DPI
  - PPI
  - Độ phân giải
created: 2024-12-12T03:18:00
tags:
  - Design
  - Unit
  - Resolution
  - Printing
  - Screen
  - DPI
  - PPI
  - Compare
---
Khi nói đến in qua máy in laser, DPI là một phép đo quan trọng để mô tả mật độ của các chấm (dot) hiển thị trên trang in. Dots không nhất thiết phải tròn và chúng có thể chồng lên nhau, tạo ra hiệu ứng bão hòa. Mặt khác, pixel hoàn toàn không chồng chéo.

Trước thời kỳ máy tính và thậm chí ngày nay trong việc sử dụng in offset, thuật ngữ được sử dụng để chỉ việc in ấn là lines per inch (LPI), đề cập đến số dòng halftone, được tạo thành từ một lưới các dots, nằm trong một inch không gian. Thông thường, đối với các ấn phẩm như tạp chí, chúng sẽ có tỷ lệ 2:1 giữa line và dot, vì vậy một tạp chí in ở 300dpi sẽ in ở khoảng 150lpi.

![](https://img.playbook.com/zbZInFZbdURIkDt62F_Kxk4bwUqRtTtwJACCr5ivKKU/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzk1YjhmZmRj/LWE3YmItNGM2NC04/NDk1LWIzODJjMmI2/ZjZiNQ)

Ảnh chụp màn hình của Mario, như bạn thấy, các pixel không chồng lên nhau!

Nhưng vấn đề là khi bạn chuyển những chấm đó sang màn hình LCD, thuật ngữ sẽ thay đổi. Độ phân giải lúc này đề cập đến mật độ của picture element (pixel) trên màn hình. Độ phân giải dots-per-inch (DPI) của một hình ảnh có thể khớp với độ phân giải pixels-per-inch (PPI) của màn hình, nhưng chúng không đề cập đến cùng một khái niệm. Dot (chấm) về cơ bản đề cập đến mật độ mực in, trong khi pixel đề cập đến mật độ hình ảnh trên màn hình. 

Tuy nhiên, nhiều người vẫn cố gắng điều chỉnh ảnh của họ ở 72 dpi. Quá trình điều chỉnh kích thước ảnh cho web thường bị hiểu sai. DPI không áp dụng trong việc thiết kế bố cục web. Khi ai đó chuyển đổi một hình ảnh sang 72 DPI, họ đang thêm một bước thừa thãi mà không mang lại lợi ích gì. Các trang web được đo bằng pixel, không phải các đơn vị thực tế như inches.

Khi ai đó yêu cầu bạn một hình ảnh web có kích thước, ví dụ, 2 inches chiều rộng, họ đang ước tính cách hình ảnh đó sẽ xuất hiện trên màn hình của chính họ. Tuy nhiên, nếu không thay đổi kích thước pixel của hình ảnh, thì hình ảnh đó sẽ xuất hiện lớn hơn hoặc nhỏ hơn trên các màn hình khác nhau — và thậm chí sẽ trông khác trên cùng một màn hình nhưng ở các cài đặt độ phân giải khác nhau.

## Có rất nhiều lý do khiến điều này dễ gây nhầm lẫn. Một trong số đó liên quan đến sự khác biệt quan trọng trong cách Windows và Mac OS hoạt động.

Trong những ngày đầu của ngành máy tính, vào năm 1984, khi Apple chuẩn bị giới thiệu máy tính Macintosh đầu tiên. Giao diện của Mac được thiết kế để giúp mọi người liên hệ máy tính với thế giới thực. Các kỹ sư phần mềm đã sử dụng phép ẩn dụ về một chiếc bàn làm việc để mô tả hoạt động bí ẩn của máy tính, cho đến các biểu tượng "giấy", "thư mục" và "thùng rác". Steve Jobs và nhóm phát triển Macintosh đã quyết định đặt độ phân giải của giao diện đồ họa (GUI) ở mức 72ppi, để phù hợp với kích thước điểm chữ tiêu chuẩn của văn bản và các tài liệu in ấn khác. Mỗi pixel trên màn hình 9 inch (đường chéo) và 512 x 342 pixel của máy Mac gốc được đo chính xác 1 x 1 point. Đặt thước vào màn hình, và bạn sẽ thấy rằng 72 pixel thực sự sẽ lấp đầy 1 inch. Bằng cách này, nếu bạn in một hình ảnh hoặc đoạn văn bản và giữ nó bên cạnh màn hình, cả hình ảnh và bản cứng sẽ có cùng kích thước. Điều này rất hữu ích cho những người làm công việc xuất bản trên máy tính để bàn (desktop publishing), vì họ muốn kích thước văn bản trên màn hình khớp với kích thước khi in ra.

Nhưng những bức ảnh kỹ thuật số ban đầu rất rườm rà và lởm chởm. Khi công nghệ màn hình và bộ nhớ được cải thiện, máy tính có thể hiển thị nhiều pixel hơn trên cùng một màn hình kích thước. Việc khớp bản in với màn hình thậm chí còn kém chắc chắn hơn khi các ứng dụng raster và vector cho phép người dùng phóng to và kiểm tra pixel chặt chẽ. 

Microsoft, với cách tiếp cận riêng của mình, lại có suy nghĩ khác khi phát triển Windows. Họ cho rằng khoảng cách xem từ màn hình lớn hơn khoảng cách đọc sách in, do đó cần một mật độ pixel khác. Vào giữa những năm 1990, Microsoft Windows đã chuyển đổi từ 72 thành 96ppi. Điều này làm cho kích thước phông chữ nhỏ hơn dễ đọc hơn vì có nhiều pixel hơn trên mỗi point, nhưng lại tạo ra sự không đồng nhất với các hệ thống máy tính khác. Đặc biệt, văn bản trên Mac sẽ nhỏ hơn so với Windows khi so sánh cùng một kích thước điểm (point).

<center>Mac 72ppi => 1pt = 1/72 inch = 1px</center>
<center>Win 96ppi => 1pt = 1/72 inch = 96/72 >1px</center>

![](https://img.playbook.com/Kz3EhX7IF9B1Nfs-EqvPFL82yW999wIW_kwmDi1Edog/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzM5YjE3ZDli/LTk4OTctNGRiMi1i/MjhlLTNiZjUwZWVj/NjBhYg)

Cuối cùng Microsoft đã cho phép người dùng tự thay đổi cài đặt DPI.

Mặc dù độ phân giải ngày càng tăng đã thay đổi tình trạng này theo thời gian, nhưng nó không làm giảm bớt sự nhầm lẫn xung quanh thuật ngữ DPI, vốn thường bị sử dụng sai khi nói về mật độ pixel. *Thêm vào đó là sự nhầm lẫn do Photoshop gây ra, vì phần mềm này làm việc với DPI, mặc dù thực tế bạn đang thao tác với pixel.* Tuy nhiên, nếu bạn dự định in ấn, thì DPI lại trở nên quan trọng hơn.

*Sự nhầm lẫn này cũng mở rộng sang lĩnh vực web, nơi mà các trình duyệt web về cơ bản phớt lờ DPI.*

[Một bài viết năm 2010 trên Web Designer Depot](https://webdesignerdepot.com/the-myth-of-dpi/) cho biết rằng các trình duyệt web thường phớt lờ thiết lập dots-per-inch (DPI), ít nhất là đối với hình ảnh. Mặc dù các định dạng JPG và PSD hỗ trợ DPI một cách tự nhiên, nhưng các định dạng tập trung vào kỹ thuật số như GIF và PNG thì không.

Điều này có nghĩa là, về mặt kỹ thuật, bạn có thể đặt một bức ảnh ở mức 300dpi và tải nó lên một trang web, nhưng điều đó sẽ không có ý nghĩa gì trừ khi ảnh đó được in ra.

Trong hầu hết các trường hợp, độ phân giải 300ppi được khuyến nghị, nhưng có những trường hợp ngoại lệ, khi đó độ phân giải cao hơn được khuyến nghị dựa trên mức độ chi tiết của đối tượng. Những khuyến nghị này đôi khi làm dấy lên mối lo ngại từ một số người cho rằng 300ppi là quá thấp, nhất là khi ngày nay nhiều smartphone đã hỗ trợ màn hình có độ phân giải vượt quá 300ppi.

> [!NOTE] Lưu ý: 
> Bạn cũng có thể nghe thấy thuật ngữ "samples per inch" (SPI) khi nói về quét ảnh. Mặc dù việc sử dụng PPI không sai, nhưng theo công ty tư vấn in ấn IDEAS, SPI là thuật ngữ chính xác hơn về mặt kỹ thuật, vì nó phản ánh cách máy quét lấy mẫu hình ảnh.

## Pixel Size phụ thuộc vào ngữ cảnh

Một [[Point vs Pixel|Pixel]] là đơn vị nhỏ nhất trên một lưới hiển thị hình ảnh số. DPI đo kích thước của các pixel, hoặc chấm, khi chúng được in ra.

### Resizing làm thay đổi Pixel Sizes; Resampling làm thay đổi số lượng Pixel

Có hai cách để phóng to một hình ảnh: thêm nhiều pixel hoặc làm cho các pixel lớn hơn. Tương tự, bạn có thể giảm kích thước của hình ảnh bằng cách cắt bớt pixel hoặc thu nhỏ pixel. Tuy nhiên, thu nhỏ và cắt bớt là hai quá trình khác nhau.

**Resizing** chỉ thay đổi kích thước của các pixel, chứ không thay đổi số lượng pixel. Chúng ta không tăng hoặc giảm số lượng pixel, chỉ thay đổi kích thước của các pixel khi in ra. Đây là một mối quan hệ ngược lại: các hình ảnh có pixel lớn hơn sẽ có mật độ pixel thấp hơn (ít pixel trong cùng một số inch) khi in.

Điều này có nghĩa là khi bạn phóng to hình ảnh mà không thay đổi số lượng pixel, các pixel sẽ trở nên lớn hơn, làm cho hình ảnh ít chi tiết hơn khi in ra, vì mật độ pixel thấp hơn.

**Resampling** *(Thay đổi mẫu)* và **Interpolation** *(Nội suy)* thay đổi kích thước của hình ảnh bằng cách tăng hoặc giảm số lượng pixel. Các pixel bổ sung có thể được tạo ra một cách nhân tạo thông qua một quá trình gọi là 'nội suy', trong đó máy tính phân tích các pixel ban đầu và tạo ra những pixel mới dựa trên những gì nó nghĩ sẽ có ở đó. Hình ảnh có nhiều pixel hơn sẽ chứa nhiều thông tin hơn và thường tạo ra đồ họa phong phú hơn. Ví dụ: nếu bạn có một pixel màu xanh lam nằm bên cạnh một pixel màu vàng và muốn tăng dpi của hình ảnh một cách giả tạo, máy tính sẽ sử dụng nội suy để thêm một pixel màu xanh lá cây ở giữa hai pixel.

Nội suy hiệu quả cho phép bạn tăng kích thước của hình ảnh, trong khi vẫn giữ nguyên dpi, do đó tránh được bất kỳ vấn đề pixel nào. Điều này nghe có vẻ là giải pháp hoàn hảo về mặt lý thuyết, tuy nhiên không hợp lý khi mong đợi máy tính tạo ra một ước tính hoàn toàn chính xác về các pixel bị thiếu và quá trình này nên được sử dụng một cách có cân nhắc.

Khi bạn tăng số lượng pixel, bạn có thể làm cho hình ảnh chi tiết hơn, nhưng nếu làm không đúng cách, hình ảnh có thể trở nên mờ hoặc bị vỡ nét. Ngược lại, khi giảm số lượng pixel, bạn sẽ làm giảm chi tiết và chất lượng của hình ảnh, giúp nó phù hợp với các yêu cầu về kích thước nhỏ hơn hoặc giảm dung lượng.

Mặc định, nên tránh **Resampling** nếu có thể, vì bạn có thể mất độ rõ nét và sắc nét trong hình ảnh. Bạn vẫn có thể sử dụng Undo, nhưng có thể hữu ích nếu giữ một bản sao của hình ảnh gốc, trong trường hợp bạn vô tình lưu phiên bản độ phân giải thấp và mất tất cả các chi tiết đó.

#### Resizing và Resampling trong Photoshop

Panel Image Size trong Photoshop điều khiển cả việc thay đổi kích thước  (resizing) và thay đổi mẫu (resampling) của hình ảnh.

![](https://img.playbook.com/H7XDDZwjZWIlOY7Z2DZhLCVwcLuc6pHoFKR__lJnREQ/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzhkNmU5OTU5/LWMzZjktNDNlNy1i/NWVlLWU0ZDYyN2Q0/NzM2MA)

Hộp kiểm "Resample" thay đổi số lượng pixel trong một inch tuyến tính—tức là số pixel trên mỗi inch. Nếu bạn tắt resampling, Photoshop chỉ làm duy nhất một việc để thay đổi kích thước hình ảnh là phóng to các pixel để in ra.

![](https://img.playbook.com/HBtipe5-Cl229-uKaXuTH2BtzK5MrC-GfXZNuo3lzdQ/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2Q1NDAzZmY4/LWEzM2QtNGFhYy1h/ZTRlLTdjMjU4YTgz/MWQxNQ)

Khi hộp kiểm resampling không được đánh dấu, việc thay đổi hộp "resolution" sẽ thay đổi kích thước vật lý của hình ảnh khi in ra, nhưng không làm thay đổi số lượng pixel trong hình ảnh. Khi in, hình ảnh sẽ xuất hiện lớn hơn hoặc nhỏ hơn tùy thuộc vào độ phân giải được đặt. Tuy nhiên, trên một trang web, hình ảnh sẽ vẫn giữ nguyên kích thước vì web chỉ quan tâm đến số lượng pixel của hình ảnh, không phải độ phân giải khi in ra.
### Bạn càng ở gần một thứ gì đó, bạn sẽ cần mật độ pixel hoặc chấm càng cao

Mặc dù có thể gây nhầm lẫn, nhưng mật độ pixel và mật độ chấm thường có khá nhiều điểm tương đồng.

Hãy quay lại với iPhone X mà chúng ta đã nhắc đến ở đầu bài viết. Bạn sẽ thường xuyên nhìn gần màn hình, đúng không? Điều này thực sự khá hữu ích, vì với độ phân giải 458ppi, iPhone X cho phép hiển thị nhiều chi tiết hơn mà bạn có thể nhận thấy nhờ vào việc bạn gần màn hình.

Bây giờ, so sánh điều đó với những thứ khác mà bạn thường xuyên nhìn thấy, chủ yếu dưới dạng in ấn. Một tờ báo, thông thường, sẽ có mật độ chấm từ 150dpi đến 200dpi, không chi tiết bằng nhưng vẫn đủ để phục vụ cho mục đích sử dụng của nó — in thông tin nhanh chóng trên giấy rẻ tiền.

Mặt khác, một tờ glossy magazine chất lượng cao sẽ thường in với độ phân giải 300dpi, độ phân giải này cho phép tái tạo chi tiết tốt và sẽ trông rất đẹp khi nhìn gần, nhưng có thể không đạt đến mức độ chi tiết của một bản in ảnh chất lượng cao.

(Và cần phải nhấn mạnh một lần nữa rằng, đối với in ấn offset, LPI có thể là thuật ngữ được ưa chuộng tùy thuộc vào tình huống, mặc dù nếu bạn đang in từ máy in laser, thì thường bạn đang nói về DPI.)

**Còn khi nói đến biển quảng cáo (billboards):**
Bạn đã bao giờ nhìn gần một biển quảng cáo chưa? Dĩ nhiên là bạn chưa — thường thì chúng cách bạn hàng trăm feet, xa tầm mắt của bạn khi di chuyển nhanh. Và điều đó có nghĩa là độ phân giải cần thiết để in biển quảng cáo thực tế là khá khiêm tốn.

![](https://i.imgur.com/49Pmk8a.png)

Clear Channel Advertising cho biết, đối với mỗi ô vuông rộng nửa inch trong các tệp số của một biển quảng cáo in ấn, nó sẽ được in ra với kích thước 1 foot vuông (144 inch² ~ 12x12inch), tức gấp 24 lần.

Với tỷ lệ này, một thiết kế 7x24 inch sẽ phù hợp với biển quảng cáo 168x576 inch. Nếu thiết kế rộng 24 inch này được gửi đến Clear Channel với độ phân giải 300dpi, điều đó có nghĩa là thiết kế bạn thấy trên biển quảng cáo thực tế sẽ chỉ hiển thị với độ phân giải 12.5dpi (300dpi/24) — mặc dù bạn sẽ không nhận ra điều đó, vì bạn sẽ nhìn từ cách xa hàng trăm feet.

Digital billboards có kích thước hơi khác biệt—chúng thường được gửi cho công ty với độ phân giải 72dpi, nhưng cũng được thay đổi kích thước để phù hợp với các kích thước lớn hơn.

## Pixels per Inch trên màn hình

DPI không ảnh hưởng đến cách hiển thị hình ảnh trên màn hình web, nhưng PPI (pixels per inch) là yếu tố quan trọng khi nói đến cách hiển thị hình ảnh trên màn hình. Màn hình máy tính có thể được đo đạc về mặt vật lý bằng inch, và mỗi màn hình sẽ hiển thị một số pixel nhất định. 

### PPI cao hơn có nghĩa là Legibility (tính dễ đọc) tốt hơn ở Point size nhỏ hơn

Màn hình có PPI cao hơn rất dễ đọc. Nhiều pixel trên mỗi inch làm cho các mẫu chữ dễ đọc hơn vì sắc nét hơn. Nó cũng có nghĩa là hình ảnh và văn bản phải lớn hơn (tính bằng pixel) để có thể đọc được.

![](https://img.playbook.com/G3HABugCQVkJYk4IlVHjXS8hn-dqWKSbA4xzdLPcPYE/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzY2YzBiZjFh/LTM1ZTgtNDFlZS04/MjYzLTY1YTYxOWYz/MDJmOQ)

Nếu bạn cầm một chiếc thước đo màn hình, bạn sẽ thấy rằng kích thước của biểu tượng và cửa sổ có tỷ lệ nghịch với số lượng pixel hiển thị. Nhiều pixel hơn có nghĩa là biểu tượng nhỏ hơn; ít pixel hơn có nghĩa là biểu tượng lớn hơn. Nhiều pixel trên cùng một màn hình sẽ cung cấp mật độ pixel cao hơn; ít pixel hơn có mật độ thấp hơn.

Sự khác biệt trở nên đáng chú ý hơn với các loại màn hình khác nhau:
- Một digital billboard có kích thước 47 x 12 feet có thể chỉ sử dụng 888 x 240 pixel (khoảng 1,6 PPI). 
- Màn hình iPhone ngày nay có kích thước 2 x 3 inch và chứa 320 x 480 pixel (khoảng 160 PPI).

Một tệp PNG đơn lẻ có kích thước 100 x 100 pixel có thể được đặt trên digital billboard và màn hình iPhone trên. Tuy nhiên, tệp PNG này sẽ xuất hiện lớn hơn rất nhiều trên bảng quảng cáo vì pixel của bảng quảng cáo lớn gấp 100 lần so với pixel của iPhone (1.6 PPI so với 160 PPI). Điều này là do mật độ pixel (PPI) của màn hình càng cao, các đối tượng và hình ảnh trên màn hình càng nhỏ và chi tiết hơn, trong khi màn hình có mật độ pixel thấp sẽ hiển thị các đối tượng lớn hơn, nhưng kém sắc nét hơn​.

## [[Key note]]
- Khoảng cách từ mắt đến 1 vật càng gần thì cần DPI càng cao để mắt không nhận ra sự vỡ hạt pixel.
- Tránh Resize ảnh gốc về size nhỏ hơn, nếu bắt buộc hãy lưu 1 bản sao cho size ban đầu để giữ lại chi tiết ảnh. Ở điều kiện bình thường, nên để layer ảnh về smart layer để link đến ảnh gốc thay vì sử dụng trực tiếp ảnh đó.
- **Lưu ý với thiết kế web:**
	- DPI và PPI không có ý nghĩa đối với website, nó chỉ thực sự có ý nghĩa khi được in ra.
	- Cùng 1 kích thước màn hình vật lý, 1px trên màn hình có PPI cao hơn trông sẽ nhỏ hơn.
	- Kích thước của 1 đối tượng trên màn hình đối với mắt người sẽ phụ thuộc vào nhiều yếu tố hơn là pixel, như: OS DPI, Kích thước màn hình, Screen Scale, Application Scale, Zoom Scale,...
	- Với thiết kế web responsive cần tính toán đến các trường hợp ảnh co giãn lớn hơn kích thước thực sự của nó (bằng thuộc tính max width, max height). Ngoài ra còn có thể kiểm soát thay đổi kích thước ảnh theo breakpoint để tối ưu tốc độ tải trang.
- **Lưu ý khi in ấn:** 
	- Khi gửi ảnh để in, nên sử dụng độ phân giải 300dpi, nhưng tùy thuộc vào chất lượng của hình ảnh và kích thước đang in, có thể sử dụng dpi thấp hơn. Hình ảnh ảnh A3 có thể trông ổn với độ phân giải 150dpi.
	- Tỉ lệ thu phóng thường dùng cho Billboard ngoài trời cỡ lớn thường là 24x. Tức chỉ cần thiết kế ở kích thước nhỏ hơn kích thước thật 24 lần ở 300dpi là đủ.
- **Lưu ý khi làm việc với Pixel art:**
	- Đối với pixel art, nên xuất ảnh theo đúng kích thước lưới thiết kế gốc để giữ nguyên độ sắc nét của các đường viền và chi tiết. Khi xuất với kích thước lưới gốc, mỗi pixel sẽ là một khối vuông sắc nét, không bị làm mờ. Nếu cần tính linh hoạt để dùng cho nhiều kích thước khác nhau, thì vẫn nên xuất với lưới gốc và phóng to sau, giữ đúng bội số nguyên để không bị nhòe.
	- Khi bạn phóng to hình ảnh mà không đúng tỷ lệ lưới, trình duyệt hoặc phần mềm hiển thị sẽ cố làm "mượt" các đường nét bằng phương pháp khử răng cưa (anti-aliasing), dẫn đến hiệu ứng nhòe.
	- Nếu cần sử dụng ảnh lớn hơn, nên phóng to ảnh theo tỷ lệ bội số nguyên của lưới gốc. Đừng phóng to theo tỷ lệ lẻ (ví dụ 1.5x hay 3.2x) vì điều này sẽ tạo ra các điểm ảnh trung gian, gây hiệu ứng mờ nhòe.
	- Tắt tính năng khử răng cưa *(anti-aliasing)* khi xuất ảnh
	- Nên lưu ở PNG thay vì JPEG vì PNG là định dạng ảnh giữ nguyên độ sắc nét, không nén mất dữ liệu *(lossless)*.

---
## References
[Why Dots Per Inch Isn't Pixels Per Inch](https://tedium.co/2018/01/18/dots-per-inch-pixels-per-inch/)
[The Myth of DPI | Web Designer Depot](https://webdesignerdepot.com/the-myth-of-dpi/)
[The ultimate guide to image resolution | Creative Bloq](https://www.creativebloq.com/graphic-design/what-is-dpi-image-resolution-71515673)
[Image_resolutions.pdf](https://cft.vanderbilt.edu/wp-content/uploads/sites/59/Image_resolutions.pdf)