---
aliases:
  - CPM
  - Critical Path Method
  - Biểu đồ PERT
  - Biểu đồ mạng PERT
  - PERT
created: 2024-12-25T15:33:00
tags:
  - glossary
  - Chart
  - ProjectManagement
---
## Định nghĩa

"PERT" là viết tắt của "Program Evaluation and Review Technique", tạm dịch là "Kỹ thuật đánh giá và xem xét chương trình." PERT là một phương pháp quản lý dự án được sử dụng để xác định và lập kế hoạch cho các hoạt động dự án một cách hiệu quả. Phương pháp này thường được sử dụng để ước tính thời gian cần thiết để hoàn thành một dự án và xác định các công việc cần thực hiện theo trình tự nào.

Trong PERT, các công việc được biểu diễn bằng các mạng lưới (network) hoặc biểu đồ PERT để thể hiện sự phụ thuộc giữa các công việc và thời gian dự kiến hoàn thành. PERT thường sử dụng ba thời gian ước tính cho mỗi công việc: thời gian tối thiểu, thời gian trung bình và thời gian tối đa, để tạo ra một ước tính thời gian dự kiến chính xác hơn.

Phương pháp PERT thường được áp dụng trong các dự án lớn và phức tạp, như trong ngành xây dựng, công nghiệp sản xuất, và nghiên cứu phát triển sản phẩm.

![[Pasted image 20241225141835.png]]

Sơ đồ PERT biểu diễn các hoạt động trong dự án dưới dạng các đường thẳng (gọi là nhiệm vụ) được kết nối với nhau bởi các mũi tên (gọi là sự phụ thuộc giữa các nhiệm vụ). Một số thông tin có thể liên kết với mỗi nhiệm vụ, chẳng hạn như thời gian hoàn thành dự kiến ​​và thời gian bắt đầu dự kiến.

Sơ đồ mạng PERT thích hợp sử dụng trong các dự án lớn chứa hàng trăm, thậm chí là hàng ngàn hoạt động. Sơ đồ này nên được sử dụng khi nhà quản trị dự án cần:
- Xác định tiến trình quan trọng của dự án, đảm bảo mọi hoạt động đều đáp ứng đúng thời hạn.
- Biểu diễn rõ ràng về sự phụ thuộc lẫn nhau của các nhiệm vụ trong dự án.
- Xác định khoảng thời gian dự kiến cần thiết để hoàn thành dự án, chuẩn bị cho các dự án lớn và phức tạp hơn nhiều.

## 4 Yếu tố chủ chốt khi vẽ sơ đồ PERT

1. **Sự kiện:** Sự kiện là cột mốc đánh dấu khi mới bắt đầu hay kết thúc một hay nhiều nhiệm vụ nào đó trong dự án. Trong sơ đồ mạng lưới PERT, các sự kiện thường được thể hiện qua các hình tròn có đánh số, sự kiện đầu tiên mũi tên sẽ đi ra, các sự kiện ở giữa sẽ có cả dấu cung đi vào và đi ra, sự kiện kết thúc sẽ là cung đi vào.
2. **Công việc:** Công việc trong sơ đồ PERT đại diện cho nguồn lực như thời gian, nhân sự đảm nhiệm để tiến hành từ sự kiện này qua sự kiện tiếp theo. Yếu tố công việc được biểu diễn bằng các mũi tên chỉ hướng, độ dài của mũi tên thể hiện thời gian hoàn thành công việc.
3. **Thời gian dự trữ:** Thời gian dự trữ là khoảng thời gian dự phòng cho các công việc có thể bị chậm trễ. Tuy nhiên phải đảm bảo việc trì hoãn các công việc này không làm ảnh hưởng đến tiến độ chung của dự án. Đây là yếu tố quản lý rủi ro dự án được đánh dấu trên các đường cung chỉ hướng biểu diễn công việc. Nếu công việc được hoàn thành sớm hơn thời gian dự trữ, có thể đánh dấu lại bằng các chấm tròn nhỏ trên đường cung.
4. **Đường găng:** Đường găng là đường biểu diễn kết nối giữa các công việc. Đường găng dài nhất được tính từ điểm đầu đến điểm cuối của sơ đồ PERT. 

Nhà quản lý dự án có thể nhìn vào đường găng để theo dõi biểu đồ tiến độ công việc. Nếu có bất trì sự chậm trễ nào trong quá trình thực hiện các sự kiện trên đường găng có nghĩa là công việc đang bị chậm tiến độ so với kế hoạch.

## Vẽ sơ đồ mạng lưới PERT

### Bước 1. Xác định nhiệm vụ dự án

Thu thập thông tin và xác định các nhiệm vụ cần thực hiện trong dự án. Xây dựng một kế hoạch chi tiết để đảm bảo sự chuẩn bị đầy đủ cho các bước tiếp theo.
### Bước 2. Sắp xếp thứ tự ưu tiên cho các nhiệm vụ

Xác định thứ tự ưu tiên của các nhiệm vụ dự án dựa trên mức độ ưu tiên và phụ thuộc giữa chúng.
### Bước 3. Kết nối các nhiệm vụ dự án

Bắt đầu kết nối các nhiệm vụ bằng cách sử dụng mũi tên để đại diện cho các nhiệm vụ và các nút để đại diện cho các sự kiện hoặc cột mốc quan trọng trong dự án.
### Bước 4. Ước tính khung thời gian của dự án

Cần 3 ước lượng thời gian cho mỗi công việc. Kết hợp lại để có con số cuối cùng:
- Ước lượng lạc quan nhất (MO - Most Optimistic): Thời gian cần để hoàn thành công việc trong điều kiện "tốt nhất" hay "lý tưởng" (không có trở ngại nào)
- Ước lượng khả dĩ nhất (ML - Most Likely): Thời gian cần để hoàn thành công việc trong điều kiện "bình thường" hay "hợp lý"
- Ước lượng bi quan nhất (MP - Most Pessimistic): Thời gian cần để hoàn thành công việc một cách "tồi nhất" (đầy trở ngại)

**Ước lượng cuối cùng được tính theo công thức:**
$$EST=\frac{MO + 4*ML + MP}{6}$$

#### Ví dụ: Các công việc liên quan đến lắp mạng nội bộ cho cơ quan

| Tên công việc                                       | MO  | ML  | MP  | EST |
| --------------------------------------------------- | --- | --- | --- | --- |
| Vẽ sơ đồ và khoan tường                             | 2   | 3   | 5   | 3.2 |
| Lắp các ống gen                                     | 1   | 2   | 4   | 2.2 |
| Đi dây                                              | 1   | 2   | 4   | 2.2 |
| Lắp các hộp nối                                     | 0.5 | 1   | 2   | 1   |
| Lắp các máy tính, máy chủ, Hub                      | 2   | 3   | 3   | 2.8 |
| Kết nối các máy tính, máy chủ vào hệ thống dây mạng | 1   | 2   | 4   | 2.2 |
| Thử xem mạng đã thông chưa                          | 0.5 | 1   | 10  | 2.4 |
| Tổng thời gian                                      | 8   | 14  | 32  | 16  |
Sau đó tăng "một ít thời gian" cho mỗi công việc (thời gian tiêu phí giữa chừng). Thông thường tăng thêm 7-10%

| Tên công việc                                       | EST | %   | Final EST |
| --------------------------------------------------- | --- | --- | --------- |
| Vẽ sơ đồ và khoan tường                             | 3.2 | 10% | 3.52      |
| Lắp các ống gen                                     | 2.2 | 10% | 2.42      |
| Đi dây                                              | 2.2 | 10% | 2.42      |
| Lắp các hộp nối                                     | 1   | 10% | 1.1       |
| Lắp các máy tính, máy chủ, Hub                      | 2.8 | 10% | 3.08      |
| Kết nối các máy tính, máy chủ vào hệ thống dây mạng | 2.2 | 10% | 2.42      |
| Thử xem mạng đã thông chưa                          | 2.4 | 10% | 2.64      |
| Tổng thời gian                                      | 16  | 10% | 17.6      |

### Bước 5. Thiết lập đường găng phù hợp

Khi đã xác định được các sự kiện cụ thể và thời gian cần thiết thì bước cuối cùng là thiết lập đường găng đi qua các sự kiện. Điều kiện cần và đủ để đường găng đi qua là tất cả sự kiện quan trọng và dài nhất.

### Bước 6: Tính phương sai $σ^2$ của các thời gian hoạt động

Đặc biệt, phương sai này có mối liên quan với ET và được tính:
$$σ^2={\frac{{MP-MO}}{6}}^2$$

### Bước 7: Xác định xác suất hoàn thành dự án với thời gian đã cho, dựa vào ứng dụng phân phối chuẩn bình thường. 

Một đặc trưng của việc dùng ước lượng 3 loại thời gian là nó cho phép các nhà phân tích đánh giá tác động của sự không chắc chắn đến thời gian hoàn thành dự án. Cơ chế để tính xác suất này như sau:
a. Tính tổng giá trị phương sai đối với những hoạt động trên đường găng.
b. Thay số vào công thức biến đổi tìm Z-score như sau:
$$Z=\frac{D-T_{E}}{\sqrt{ \sum{σ_{cp}^2} }}$$
	Trong đó:
	$D$: Thời gian hoàn thành dự án theo mong muốn
	$T_{E}$: Thời gian kỳ vọng sẽ hoàn thành dự án (có được sau khi đã vẽ biểu đồ PERT)
	$\sum{σ_{cp}^2}$: Tổng các phương sai thuộc đường găng

- **Z>0:** Thời gian mục tiêu D lớn hơn thời gian kỳ vọng T_E​, bạn đang tìm xác suất để hoàn thành trong thời gian dài hơn.
- **Z<0:** Thời gian mục tiêu D nhỏ hơn thời gian kỳ vọng T_E​, bạn đang tìm xác suất để hoàn thành nhanh hơn.

c. Tính giá trị Z, là số độ lệch chuẩn mà dự án tới hạn so với thời gian kỳ vọng hoàn thành
d. Dùng giá trị Z, tìm xác suất đáp ứng thời hạn dự án (tìm trong bảng phân phối chuẩn - Standard Normal Distribution Table). Thời điểm hoàn thành kỳ vọng là thời điểm bắt đầu cộng với tổng thời gian của các hoạt động trên đường găng

### Ví dụ

Một dự án được xác định gồm các hoạt động sau, tính xác suất dự án hoàn thành trong 35 tuần?

![[Pasted image 20241225144731.png]]

<u>Giải:</u>
![[Pasted image 20241225144953.png]]
![[Pasted image 20241225145021.png]]
Đường găng: 
- A – C – F – G
- A – B – D – F – G

*Xác định xác suất hoàn thành dự án trong 35 tuần*
Có 2 đường găng của sơ đồ mạng, chúng ta phải quyết định dùng phương sai của đường găng nào để tính xác suất đáp ứng yêu cầu. Theo phương pháp bảo thủ là dùng đường có tổng phương sai lớn nhất để tập trung sự chú ý của ban quản trị đến các hoạt động dễ xảy ra. 

Do đó, sẽ dùng các hoạt động A, C, F, G để tìm xác suất hoàn thành
$$
\sum{σ_{cp}^2}=9+2\frac{7}{9}+\frac{1}{9}+0=11.89
$$

$$
Z=\frac{D-T_{E}}{\sqrt{ \sum{σ_{cp}^2} }}=\frac{35-38}{\sqrt{ 11.89 }}=-0.87
$$
Trang bảng phân phối chuẩn, ta thấy giá trị Z = -0.87 tạo ra xác suất 0.1922, nghĩa là nhà quản trị dự án chỉ có khoảng 19% cơ hội hoàn thành dự án trong 35 tuần.

---
## References:

[Sơ đồ PERT là gì? Hướng dẫn các bước vẽ sơ đồ PERT](https://www.pace.edu.vn/tin-kho-tri-thuc/so-do-pert)
[507f9950-e446-4eaa-96fa-1f61e2afca48_cpmcouocluongthoigianhoatdong.docx](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fkqtkd.duytan.edu.vn%2Fupload%2Ffile%2F507f9950-e446-4eaa-96fa-1f61e2afca48_cpmcouocluongthoigianhoatdong.docx&wdOrigin=BROWSELINK)