---
aliases:
  - Độ sâu màu
created: 2025-01-14T14:21:00
tags:
  - Design
  - ImageProperties
  - Image
  - Color
---
## Color bit depth là gì?

_Độ sâu bit_ chỉ định lượng thông tin màu có sẵn cho mỗi pixel trong hình ảnh. Nhiều bit thông tin trên mỗi pixel dẫn đến nhiều màu sắc hơn và thể hiện màu sắc chính xác hơn trong hình ảnh, do đó ảnh hưởng đến kích thước hình ảnh. Nói một cách đơn giản, kích thước tệp của hình ảnh tăng theo độ sâu bit vì nhiều thông tin màu sắc được lưu trữ trên mỗi pixel trong hình ảnh có độ sâu bit cao hơn.

![](https://i.imgur.com/nsx6uPd.jpeg)

Ví dụ:
- Hình ảnh với bit depth là 1 có các pixel với hai giá trị khả dĩ: đen và trắng.
- Hình ảnh với bit depth là 8 có $2^8$, tức 256, giá trị khả dĩ.    
- Hình ảnh ở chế độ Grayscale với bit depth là 8 có 256 giá trị xám khả dĩ.    
- Hình ảnh ở chế độ RGB được tạo thành từ ba kênh màu. Hình ảnh RGB với 8 bit trên mỗi kênh có 256 giá trị khả dĩ cho mỗi kênh, nghĩa là có hơn 16 triệu giá trị màu khả dĩ.    

![](https://i.imgur.com/TfPQr9k.png)

Hình ảnh RGB với 8 bit trên mỗi kênh (Bits/Channel hoặc bpc) đôi khi được gọi là hình ảnh 24 bit (8 bit x 3 kênh = 24 bit dữ liệu cho mỗi pixel). Ngoài hình ảnh 8 Bits/Channel, Photoshop còn có thể làm việc với hình ảnh chứa 16 hoặc 32 Bits/Channel. Hình ảnh với 32 Bits/Channel còn được gọi là hình ảnh dải động cao (HDR).

## Độ sâu màu cao hơn nghĩa là có nhiều màu hơn

Độ sâu màu càng cao, càng nhiều màu có thể được hiển thị. Trong thế giới thực, độ sâu màu cao hơn sẽ có nghĩa là hình ảnh đẹp hơn, vì sẽ có nhiều sắc thái đỏ, xanh lục và xanh lam hơn để lựa chọn và hiển thị. 

Sự khác biệt về độ sâu màu có thể dễ dàng nhận thấy khi bạn nhìn vào “độ dốc” của một màu, chẳng hạn như bầu trời trong hình ảnh bên dưới.

![](https://i.imgur.com/J5LvKU0.jpeg)

### Tại sao nên sử dụng độ sâu màu cao

Có nhiều lý do và trường hợp sử dụng cần phải chuyển sang độ sâu màu cao hơn. Trong số đó có việc tránh hiện tượng sọc màu (color banding) và hiện tượng posterization, hình ảnh dải động cao (high dynamic range - HDR) và cũng để duy trì chất lượng khi hình ảnh được xử lý qua giai đoạn hậu kỳ.
#### Banding

Sọc màu (banding) xảy ra khi độ sâu màu quá thấp, khiến mắt người có thể nhìn thấy sự thay đổi màu sắc rõ ràng thay vì thấy một sự chuyển đổi mượt mà giữa các sắc độ. Những sự khác biệt này thường xuất hiện dưới dạng các dải màu chạy qua hình ảnh - do đó có tên gọi là banding. Dưới đây là một ví dụ về một bức ảnh được tái tạo ở độ sâu màu quá thấp để có thể tái hiện chính xác sự chuyển đổi màu sắc trong các sắc độ xanh của bầu trời:

![Bức ảnh trên thể hiện hiện tượng banding trong bầu trời do độ sâu màu không đủ để tái hiện chính xác sự chuyển đổi màu sắc.](https://i.imgur.com/PxyGoJN.jpeg)

#### Posterization

Posterization thực chất là vấn đề tương tự như banding, nhưng có tên gọi khác vì một số hình ảnh không có các gradient lớn dẫn đến việc phân tách thành những "dải màu" gọn gàng. Thay vào đó, một số hình ảnh sẽ phân tách thành các mẫu hình trừu tượng hơn. Vấn đề vẫn là giống nhau – thay vì có những sắc thái màu sắc chuyển tiếp mượt mà, mắt người có thể nhận thấy rõ ràng điểm dừng của màu sắc này và điểm bắt đầu của màu sắc khác.

![Ví dụ về posterization, nơi sự phân tách màu sắc có thể thấy rõ trong nền cây cối.](https://i.imgur.com/tLGeMIB.jpeg)

Trong hình ảnh trên, hiện tượng posterization có thể thấy rõ ở khu vực nền, nơi sự mờ dần của nét ảnh. Một hiện tượng thú vị về posterization là các khu vực có chi tiết và độ tương phản cao (tần số không gian cao) không bị ảnh hưởng nhiều về mặt cảm quan. Lấy ví dụ, cây ở phần bên phải, nơi có độ nét - nếu không có nền, sẽ rất khó để nhận ra rằng độ sâu bit thấp đang ảnh hưởng tiêu cực đến hình ảnh này. Điều này là vì ở những khu vực có tần số không gian cao, màu sắc giới hạn được sử dụng thay đổi và bị cắt ra nhanh chóng hơn, khiến mắt chúng ta không thể nhận diện những khu vực đáng ra phải có các chuyển sắc mượt mà hơn.

Mặt khác, các khu vực có tần số không gian thấp (chẳng hạn như những vùng ngoài tiêu điểm hoặc cảnh có độ tương phản thấp) dễ dàng xuất hiện hiện tượng posterization hơn. Điều này là vì các vùng lớn có khả năng bị giảm xuống thành một màu duy nhất, khiến chúng dễ dàng nhận diện hơn bằng mắt.

#### HDR (High Dynamic Range) và Dải Màu Sắc Rộng (Wide Color Gamuts)  

Một lĩnh vực khác đã thúc đẩy việc chuyển sang độ sâu bit cao là sự xuất hiện của High Dynamic Range (HDR) và các dải màu sắc rộng hơn đang được đưa vào thị trường tiêu dùng. Cả HDR và dải màu sắc rộng có tiềm năng làm trầm trọng thêm vấn đề banding và posterization vì chúng yêu cầu độ sâu bit để thể hiện cả nhiều màu sắc hơn và cũng phải thể hiện một dải màu sắc và bóng tối sáng hơn. Điều này có nghĩa là về bản chất, độ sâu bit phải được kéo dài hơn so với trước đây và sẽ bắt đầu tạo ra banding ở những khu vực mà trước đây có thể không thấy được trong dải động tiêu chuẩn (Standard Dynamic Range).

Do đó, các TV Ultra-High Definition (UHD) đã chuyển sang hỗ trợ HDR phải có khả năng tái tạo ít nhất 10 bit mỗi kênh để tránh gây ra banding cho nội dung. Dolby Vision (tiêu chuẩn HDR của Dolby) còn đi một bước xa hơn và yêu cầu nội dung Dolby Vision phải được mã hóa với 12 bit mỗi kênh nhằm bảo vệ tương lai và giảm thiểu bất kỳ vấn đề tiềm ẩn nào.

##### Vậy tại sao chúng ta lại cần nhiều hơn 12-bit mỗi kênh nếu nó có thể xử lý nội dung HDR và Dải Màu Sắc Rộng mà không gặp vấn đề gì? 

Mặc dù đúng là độ sâu màu này gần như đã vượt quá khả năng thị giác của con người khi giám sát, nhưng độ sâu bit cao hơn rất thường được yêu cầu trong quá trình hậu kỳ. Điều này là vì hậu kỳ thường liên quan đến việc kéo và đẩy màu sắc mạnh mẽ, tương đương với việc kéo dài độ sâu bit được mã hóa trong một hình ảnh. Khi bạn bắt đầu nhìn thấy banding hoặc posterization, bạn đã đạt đến giới hạn của thông tin độ sâu màu, điều này làm hạn chế khả năng sáng tạo của các chuyên gia chỉnh màu, compositors và VFX.

Một ứng dụng khác của độ sâu bit cao là mã hóa thông tin phơi sáng bổ sung có thể được truy xuất sau này. Ví dụ, công việc hiệu ứng hình ảnh (VFX) thường được render ở độ sâu 32-bit mỗi kênh sử dụng giá trị Ánh sáng Tuyến tính (Linear Light). Điều này cho phép các điểm trắng sáng (giá trị trắng vượt quá điểm mã hóa bình thường) được lưu trữ và sau đó có thể được chỉnh sửa thêm sau này. Ví dụ, một compositor ghép các vụ nổ render ở độ sâu 32-bit có thể bắt đầu điều chỉnh độ phơi sáng để khớp nó vào cảnh của mình và lấy lại chi tiết từ các vùng trắng mà trước đó có vẻ như đã bị cắt và mất đi.

## Ứng dụng trong thực tế

Qua ví dụ trên thì chắc chắn ai cũng nghĩ rằng, ảnh 16 Bits chắc chắn sẽ tốt hơn ảnh 8 Bits, vì gồm nhiều bước màu hơn hẳn, giúp cho ảnh 'mượt' hơn và đẹp hơn? Không hoàn toàn như vậy. Theo như các nhà khoa học, thì mắt người chỉ có thể phân biệt 2 màu khác nhau khi chúng đủ khác nhau.

![](https://i.imgur.com/GylDimp.jpeg)

Ví dụ như ở 16 Bits, 2 màu đỏ cách nhau 256 giá trị thì chỉ cách nhau trên bảng màu 8 Bits có 1 giá trị duy nhất mà thôi. Màu đỏ R:225 (trái) và đỏ R:254 (phải) khác nhau quá ít, trong đa phần trường hợp mọi người sẽ không thể phân biệt được. Hơn nữa, gần như toàn bộ màn hình hiện nay cũng chỉ có khả năng hiển thị 8 Bits, những màn hình cao cấp chuyên cho mục đích đồ họa có thể lên tới 10 Bits, nhưng có giá bán đắt và rất ít được hỗ trợ bởi thành phần đồ họa (GPU).

![](https://i.imgur.com/HJMDwUd.jpeg)

Ảnh 16 Bits hữu ích nhất ở công đoạn chỉnh sửa, khi người dùng sẽ 'kéo dãn' bức ảnh về những giá trị màu khác nhau, làm cho hệ màu 8 Bits bị phân mảnh và dẫn tới hiện tượng kẻ sọc (banding). Thế nhưng một khi đã chỉnh sửa xong, thì người dùng hoàn toàn có thể lưu ảnh ở màu 8 Bits, không cần thiết phải lưu cao hơn.

Hầu hết các mẫu TV màn hình hiện nay chỉ có khả năng hiển thị hình ảnh 8 bit. Tuy nhiên cũng có không ít model cao cấp mới nhất sử dụng tấm nền 10 bit. Cá biệt, đã có một vài tấm nền hỗ trợ độ sâu màu 12 bit, nhưng hiện tại, có rất ít nội dung để thưởng thức trên chúng. Không giống như bước nhảy từ 8 bit lên 10 bit, sự khác biệt giữa 10 bit và 12 bit là không thực sự rõ rệt.

**Vậy ta có thể khẳng định lại được một điều đã cũ nhưng vẫn hay bị hiểu nhầm:** số Bits hoàn toàn có ảnh hưởng tới chất lượng ảnh, nhưng sau 8 Bits thì độ khác nhau đã vượt quá khả năng thu nhận của mắt người rồi, nên không cần thiết nữa. Ảnh có Bit Depth cao chỉ có giá trị trong chỉnh sửa, còn trong việc lưu trữ hoặc đăng tải thì luôn luôn thừa.

Việc chọn bit depth phù hợp cho hình ảnh của bạn là quan trọng để đảm bảo chất lượng màu sắc và chi tiết tốt nhất, đồng thời cân nhắc đến kích thước tệp và khả năng xử lý của hệ thống.

## [[Key note]]

- Ảnh export luôn ở 8-bit để tiết kiệm dung lượng, vì mắt người không thể phân biệt được các màu gần nhau ở độ sâu màu cao hơn
- Ảnh có độ sâu màu cao hơn sẽ giảm được các hiện tượng Banding, Posterization; phù hợp để hậu kỳ, chỉnh sửa màu nâng cao, vì vậy nếu có thể hãy quay chụp ở độ sâu màu cao
- Mã màu hex chỉ có thể biểu diễn màu trong không gian 8-bit
- Khi chuyển file từ n-bit sang m-bit thì dung lượng file sẽ giảm $1-\frac{m}{n}$ dung lượng gốc. Ví dụ chuyển từ 16-bit sang 8-bit thì, dung lượng file giảm $1-\frac{8}{16}=50\%$


---
## References:

['Giải ngố' khái niệm độ sâu bit (Bit Depth) được dùng trong nhiếp ảnh](https://genk.vn/giai-ngo-khai-niem-do-sau-bit-bit-depth-duoc-dung-trong-nhiep-anh-20190724210627819.chn)
[Độ sâu màu là gì? Có ý nghĩa thế nào trong công nghệ hiển thị?](https://quantrimang.com/cong-nghe/do-sau-mau-la-gi-182177)
[Unravel | Understanding Bit Depth](https://www.unravel.com.au/understanding-bit-color-depth)