---
created: 2025-01-07T22:10:00
tags:
  - Color
  - UI
  - Design
  - UIColor
  - NeutralColor
  - DesignSystem
  - ColorSystem
---
> Resources: File Figma màu sample: https://figmashort.link/Tzichj

## Hệ màu

Một vài hệ màu hay gặp (và cũng có trong Figma) như HEX, RGB, HSL, HSB:
- HEX: dùng 6 ký tự thập lục phân để diễn tả màu. RGB: hệ màu được kết hợp từ 3 màu Red, Green, Blue. Việc pick và điều chỉnh màu bằng Neutral bằng 2 hệ màu này gần như là không thể.    
- Có thể sử dụng 2 hệ màu HSL hoặc HSB.
- Vùng để chọn bảng màu là vùng đánh dấu trong hình, điều chỉnh giá trị tại kênh B = Brightness (mũi tên màu trắng) từ 0 (đen) đến 100 (trắng). Điều chỉnh các giá trị (không dùng chuột) để có độ chính xác tốt nhất.

![Hệ màu HSB và HSL trong Figma](https://i.imgur.com/6zpRf9c.jpeg)

## Các lớp màu Neutral trong UI design

Trước khi chọn màu cần phân tích các lớp màu trong một màn hình để biết thông thường sẽ cần bao nhiêu Styles / Variables cho bảng màu Neutral, đồng thời cũng biết được các màu Neutral sẽ được dùng ở đâu.

![Màn hình Vercel. Source: Mobbin](https://i.imgur.com/jHdlajt.jpeg)

![Màn hình Team management Dashboard - team Concepzilla](https://i.imgur.com/6Wiap2C.jpeg)

![Màn hình Contact management App - team Concepzilla](https://i.imgur.com/FByKY66.jpeg)

Ở đây chúng ta sẽ chia các lớp màu ra làm 3 nhóm chính: Nhóm màu nền, nhóm Border, nhóm Element.

### Nhóm màu Background

Nhóm này là các màu để làm Background, vị trí các mũi tên đánh số 1,2,3 trên hình. Lớp màu này có độ sáng cao nhất - đối với Light mode và tương ứng, tối nhất - đối với Dark mode.

Đối với đa số màn hình chỉ cần 3 lớp màu là có thể cover được khoảng 90% phần Background cho các dự án, cụ thể:
- **Surface - mũi tên số 1**: luôn làm lớp lót dưới cùng cho design, tạo Background để các Sections / Blocks / Cards được nổi bật, tách biệt với nền và với nhau.    
- **On-surface 1 - mũi tên số 2**: lớp này dùng làm Background cho các Sections / Blocks / Cards chứa thông tin. Lớp này thường nằm trên lớp Surface. Có thể dùng lớp màu này làm Background cho một màn hình nếu như trên màn hình không có quá nhiều Element cần phân cấp, hoặc màn hình đơn giản và Designers quyết định dùng Border / Divider để gom nhóm thông tin.    
- **On-surface 2 - mũi tên số 3**: lớp này dùng làm nền để highlight một vài Elements nhỏ, hoặc kích thước không quá lớn. Không khuyến khích dùng cho một vùng lớn vì nó sẽ làm cho màn hình tối hơn (hoặc sáng hơn với Dark mode), không được clean cho lắm.    

Đối với các dự án có nhiều data, cần phân cấp hơn nữa thì có thể chọn thêm 1 lớp màu nền nữa. Tuy nhiên trường hợp này trong thực tế mình thấy rất hiếm, Designers thường hay dùng Border / Divider để phân cấp chứ không dùng thêm lớp màu thứ 4. *(4 lớp màu Surface chồng lên nhau sẽ làm cho UI rối và mất đi sự mềm mại của Background)*

![Mô tả nguồn sáng lên các lớp màu nền](https://i.imgur.com/l1hRFXm.png)

Đặc điểm các lớp màu này là độ chênh lệch màu không quá lớn (nếu lớn quá sẽ làm cho độ chuyển giữa các lớp không mượt mà). Việc sắp xếp độ chênh sáng tối giữa Light và Dark mode cũng có chút khác biệt:

- Light mode:    
    - Lớp On-surface 1 sẽ gần với nguồn sáng hơn, sáng hơn Surface. Lớp On-surface 1 trong Light mode sẽ là lớp sáng nhất.        
    - Lớp On-surface 2 để highlight Elements, nên chọn màu bằng hoặc tối hơn lớp Surface một chút, đủ contrast để highlight.        
- Dark mode:    
    - Lớp On-surface 1 sẽ gần với nguồn sáng hơn, sáng hơn Surface. Lớp Surface trong Dark mode sẽ là lớp tối nhất.        
    - Lớp On surface 2 để highlight elements, đối với Dark mode nếu chọn tương ứng theo quy tắc của Light mode sẽ là tối bằng lớp Surface, như vậy các elements sẽ không nổi bật dược trên On surface 1 (sáng hơn), vì vậy màu On surface 2 sẽ là màu sáng nhất (Xem màn hình Contact management App - Concepzilla)        

Vậy:
- Độ sáng Light mode: On surface 1 > Surface ≥ On surface 2    
- Độ sáng Dark mode: On surface 2 > On surface 1 > Surface    

### Nhóm màu Stroke

Nhóm màu này dùng để làm Border và Divider. Tùy thuộc vào từng Direction / Style của dự án mà mình có thể chọn số lượng và đặc tính màu cho nhóm Border:

**Một màu cho Stroke**

- Một mã màu dùng cho cả dự án (màu Solid, không có Opacity)    
- Vì dùng chung trên nhóm các màu nền, nên chọn để độ tương phản lớn hơn, đảm bảo đối với lớp màu On-surface 2 sẽ vẫn có thể phân biệt được.    
- Cách setup và dùng đơn giản, thường được dùng đối với các dự án như CRM, CMS, Logistic, Chuyển đổi số, … (quan trọng hơn về business, dùng nội bộ, người dùng dùng màn hình phổ thông, …)    

**Hai màu cho Stroke**

- Màu Stroke Light: dùng làm Border và Divider trên nền màu Surface (Màn hình Team management Dashboard - Concepzilla - Mũi tên 4L)    
- Màu Stroke Bold: dùng làm Border và Divider trên nền màu On-surface 1 (Màn hình Team management Dashboard - Concepzilla - Mũi tên 4B)    
- Độ tương phản màu sắc k lệch nhau nhiều và đồng đều trên 2 lớp màu nền, màu sắc tổng thể sẽ “mượt” hơn một xíu. *(Sẽ giải thích kỹ hơn ở phần chọn màu bên dưới)*    
- Thường dùng ở các dự án Mobile (màn hình điện thoại độ tương phản màu sắc tốt và người dùng nhìn khoảng cách gần) hoặc dự án có yêu cầu thẫm mỹ hơn một chút.    

> [!Tip]
> Để giảm bớt contrast (vd làm divider nhạt đi) của divider, có thể dùng cách giảm weight của Border / Divider xuống nhỏ hơn 1 px. Cách này phù hợp đối với các thiết kế Mobile, đối với thiết kế trên màn hình desktop thì không nên dùng divider < 1px vì có trường hợp line nhỏ quá ⇒ bị mất do độ phân giải màn hình không tốt.

### Nhóm màu Element

Nhóm này là các màu dùng cho Text, Icon, Illustration.

- **Element Primary - mũi tên số 5**: dùng cho Heading, Title, các Elements ở trạng thái Active, Selected hoặc là các thông tin quan trọng. Màu này nổi bật nhất so với lớp màu làm Background.    
- **Element Secondary - mũi tên số 6**: dùng cho phần Text làm content, Support Text, Label, các Element ở trạng thái Idle / Default.    
- **Element Tertiary - mũi tên số 7**: dùng cho các Element ở trạng thái Disable. Màu này kém nổi bật nhất so với lớp màu làm Background, độ tương phản so với lớp Background nằm quanh vùng giá trị 3:1 (WCAG)    
- **Text on brand - mũi tên số 8**: dùng cho Text, Icon nằm trên các Element không đổi màu hoặc đổi ít khi chuyển giữa Light và Dark mode, vd màu text trên CTA button.    

Đặc điểm các lớp màu này là diện tích thể hiện màu không nhiều, cần độ chênh lệch màu lớn hơn để có thể phân cấp thông tin tốt.

![Diện tích thể hiện màu của Icon](https://i.imgur.com/t89DTEt.png)

![Độ chênh lệch màu (contrast) khi dùng cho lớp màu nền và Elements](https://i.imgur.com/05VWvof.png)

## Chọn màu Neutral

Chọn màu cho Light mode, Dark mode đa phần tương tự. 

```
Dùng hệ màu HSB, điều chỉnh tại kênh B = Brightness.
```

Chọn màu theo cách phân tích các lớp màu ở trên (sẽ điều chỉnh chi tiết ở bước “Test màu” để phù hợp với Direction / Style của dự án cũng như tiêu chuẩn tương phản màu sắc WCAG)

![Chọn màu Neutral](https://i.imgur.com/p5IryRS.jpeg)

### Chọn màu Background

```
Độ sáng Light mode: On surface 1 > Surface ≥ On surface 2
```

Bắt đầu với On Surface 01 - màu sáng nhất, B = 100, tương đương `#FFFFFF`.

Màu Surface: tối hơn một chút. Các màu ở nhóm màu Surface có độ lệch màu với nhau thấp. Chọn trong khoảng B = 94 - 97

Màu On-surface 2: trong khoảng từ B = 88-95 *(đậm hơn một tí để highlight Elements)*

### Chọn màu Stroke

Stroke về bản chất cũng là một Element nằm trên các lớp màu nền, tuy nhiên đây là Element để phân cấp thông tin nên sẽ không chọn màu có tương phản lớn *(so với lớp nền)* để tránh nổi bật hơn so với các Elements mang thông tin.

```
Độ sáng màu Stroke: Nhóm màu nền (sáng nhất) > Màu stroke (tối hơn) > Nhóm màu Elements (đậm nhất)
```

Đối với Stroke Light và Stroke Bold. Độ sáng của Stroke nằm trên lớp sáng hơn sẽ sáng hơn và độ sáng của Stroke nằm trên lớp tối hơn sẽ tối hơn.

![Màu Stroke trên 2 lớp nền](https://i.imgur.com/LR1me4K.png)

Với Light mode, chọn Stroke Light trong khoảng B = 75 - 85, Stroke Bold trong khoảng B = 80-90.

### Chọn màu Elements

Vì diện tích thể hiện màu của các Element nhỏ nên màu nhóm Elements có độ lệch màu với nhau lớn.

Màu Element Primary (màu đen) trên lớp nền sáng nhất (On surface 1) sẽ có contrast cao nhất, không nên chọn màu đen hoàn toàn `(#000000`) vì tương phản quá cao làm chói mắt người đọc, nhưng cũng không nên quá sáng *(hay chọn contrast ≥14:1)*

Màu sáng nhất trong nhóm màu này là Elemet Tertiary, màu này trên lớp nền tối nhất (ở đây là On-surface 2) phải đảm bảo tương phản lớn hơn tỉ lệ 3:1 (WCAG)

Màu Button tùy theo CTA để chọn, thường sẽ trùng với màu sáng nhất hoặc tối nhất trong bảng màu.

Với Light mode chọn Element Primary trong khoảng B = 4 - 15, Element Secondary B = 24 - 35, Element Tertiary B = 45 - 58

## Kiểm tra và cân chỉnh màu

Sau khi đã chọn được một bộ màu như trên *(tạm gọi là màu Raw Neutral)*, tiếp theo cần cân chỉnh màu sắc bằng cách đặt chúng vào một design / màn hình mẫu để test.

Dưới đây là một Design mẫu để kiểm tra các màu khi chúng kết hợp với nhau.

![Design sample để test màu](https://i.imgur.com/ZJ8teOI.png)

## Một số TIP nhỏ

1/ Màu của Background Figma cũng ảnh hưởng đến mắt khi cân chỉnh. Nên điều chỉnh Background Figma màu sáng khi chỉnh Light mode, Background Figma màu tối khi cân chỉnh Dark mode *(Optical illusion)*

![Hai hình vuông A và B có cùng mã màu `#808080`](https://i.imgur.com/80cqEoO.png)

2/ Để màu Neutral có chút shade của màu khác (hay gặp nhất là có shade của màu Primary brand) nhưng vẫn giữ nguyên tương phản thì điều chỉnh Hue của màu Neutral = Hue của màu Primary brand, Saturation chỉnh tăng dần để chọn lựa màu phù hợp.

3/ Sau khi Design được 2-3 màn hình / Flow đầu tiên, nên cân chỉnh màu một lần nữa cho chính xác (Vì lúc này Layout và Elements đã đúng với dự án, không phải là Design / màn hình mẫu để test. Lúc này team dev thường cũng trong giai đoạn setup, điều chỉnh cũng không mất nhiều thời gian)

4/ Màu Stroke sử dụng Opacity: Đối với các dự án có Background không phải Neutral (ví dụ một Section / Card / Block màu xanh), việc chọn màu Divider là Solid Neutral sẽ làm cho Divider bị bệch màu, không đẹp. Giải pháp là dùng màu có Opacity để Divider được hòa vào màu của Background.

![Màu Divider sử dụng Opacity](https://i.imgur.com/SZVabN1.png)

5/ Với hệ màu HSB, có thể chọn các Shade của màu Primary brand sáng thêm hoặc tối thêm một cách đơn giản. Hơn nữa, độ phân giải màu được 100 đơn vị, so với HSL chỉ có 50 đơn vị. Đây cũng chính là lý do mình sử dụng kênh HSB để chọn màu cho cả Neutral và các kênh màu khác.

- Điều chỉnh màu sáng hơn theo vùng được đánh dấu nằm ngang, càng sang trái (Saturation giảm) màu càng nhạt hơn    
- Điều chỉnh màu tối hơn theo vùng được đánh dấu nằm đứng, càng xuống dưới (Brightness giảm) càng đậm    
- Vùng chọn màu Primary nên chọn trong vùng dường Parabol hướng về phía góc trên bên phải.

![Đặc điểm hệ màu HSB](https://i.imgur.com/VxI9k4q.png)

---
## References:

[Chọn bảng màu Neutral trong UI design - Thien Nguyen](https://thiennguyen2409.substack.com/p/chon-bang-mau-neutral-trong-ui-design)