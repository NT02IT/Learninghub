---
created: 2024-12-28T19:34:00
tags:
  - IT
  - SoftwareEngineering
  - Java
  - Spring
---
## Cài đặt môi trường Spring
### Cài đặt JDK (Java Development Kit)

JDK, viết tắt của Java Development Kit, là một bộ phần mềm cung cấp môi trường phát triển cho ứng dụng Java. JDK bao gồm cả Java Runtime Environment (JRE), giúp lập trình viên có thể chạy thử và kiểm tra ứng dụng trong quá trình phát triển.

**Bước 1**: Truy cập trang web của Oracle để tải JDK. Chọn phiên bản 1.8 trở lên để đảm bảo tương thích với Spring.

![[Pasted image 20241228193547.png]]

**Link tải**: [https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)

**Bước 2**: Sau khi tải xong, bạn cài đặt JDK bằng cách chạy tệp cài đặt.

**Bước 3**: Để kiểm tra cài đặt thành công, mở Command Prompt (hoặc Terminal trên macOS) và nhập lệnh sau:

```
java -version
```

Nếu thấy thông tin về phiên bản JDK hiển thị, điều này có nghĩa cài đặt đã thành công.

### Cài đặt Apache Tomcat (hoặc Glassfish)

Apache Tomcat là một máy chủ web HTTP được phát triển bởi Apache Software Foundation, dành cho việc phát triển ứng dụng Java Servlet, JavaServer Pages (JSP), Java EL và WebSocket.

**Bước 1**: Truy cập trang web của Apache Tomcat để tải phiên bản mới nhất.

![[Pasted image 20241228193930.png]]

**Link tải**: [https://tomcat.apache.org/download-80.cgi](https://tomcat.apache.org/download-80.cgi)

**Bước 2**: Tải tệp cài đặt và chạy tệp đó để cài đặt Apache Tomcat.

**Bước 3**: Kiểm tra cài đặt bằng cách mở trình duyệt và truy cập địa chỉ sau: `http://localhost:8080/`. Nếu bạn thấy trang quản trị của Tomcat, cài đặt đã thành công.

### Cài đặt IDE IntelliJ (hoặc Eclipse)

IDE (Integrated Development Environment) là môi trường phát triển tích hợp, giúp bạn dễ dàng phát triển ứng dụng Spring.

**Bước 1**: Truy cập trang web của IntelliJ để tải phiên bản Community hoặc đăng ký tài khoản Jetbrains để sử dụng bản Ultimate miễn phí trong 1 năm.

![[Pasted image 20241228194037.png]]

**Link tải**: [https://www.jetbrains.com/idea/download/#section=windows](https://www.jetbrains.com/idea/download/#section=windows)

**Bước 2**: Tải tệp cài đặt và chạy tệp đó để cài đặt IntelliJ.

**Bước 3**: Mở IntelliJ và tạo một dự án mới để bắt đầu phát triển ứng dụng Spring.

## Chạy chương trình spring đầu tiên

Trong lập trình Spring Boot, Annotation `@Component` và `@Autowired` là hai trong những khái niệm quan trọng giúp quản lý và tiêm các thành phần (component) vào ứng dụng của bạn.

### Giới thiệu

Trước khi tìm hiểu về `@Component` và `@Autowired`, nên nắm vững hai khái niệm quan trọng sau đây:
1. **[[Khái niệm tight-coupling và cách loosely coupled|Tight coupling (liên kết ràng buộc) và loose coupling (liên kết lỏng lẻo)]]**: Tight coupling là sự phụ thuộc mạnh giữa các thành phần trong ứng dụng, trong khi loose coupling là sự phụ thuộc yếu hoặc không phụ thuộc giữa các thành phần.
2. **Dependency Injection (DI) và Inversion of Control (IoC)**: DI là một nguyên tắc trong lập trình, nói rằng các thành phần không nên tạo ra các đối tượng phụ thuộc của chúng, mà nên nhận chúng từ bên ngoài. IoC là một nguyên tắc quản lý và cung cấp các đối tượng phụ thuộc.

### Cài đặt

Trước tiên, bạn cần cài đặt các gói thư viện của Spring Boot trong Maven. Để làm điều này, bạn cần thêm `spring-boot-starter-parent` là parent của project và thêm dependency `spring-boot-starter-web` cho việc lập trình web hoặc server side. Dưới đây là ví dụ cấu hình `pom.xml`:

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.0.5.RELEASE</version>
    <relativePath /> <!-- lookup parent from repository -->
</parent>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

### Cách chạy ứng dụng Spring Boot

Trong Spring Boot, để chạy ứng dụng, bạn cần chỉ cho Spring Boot biết nơi ứng dụng bắt đầu. Điều này được thực hiện bằng cách thêm annotation `@SpringBootApplication` trên class chính và gọi `SpringApplication.run(App.class, args);` để khởi tạo ứng dụng. Ví dụ:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class App {
    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(App.class, args);
    }
}
```

Trong ví dụ trên, chúng ta đã tạo một ứng dụng Spring Boot và khởi tạo `ApplicationContext`, container chứa toàn bộ các dependency trong ứng dụng.

### Annotation `@Component` trong Spring Boot

`@Component` là một annotation đánh dấu trên các class để cho biết chúng là các bean được quản lý bởi Spring Boot. Điều này có nghĩa là Spring Boot sẽ tạo và quản lý các instance của các class được đánh dấu `@Component`.

Ví dụ:

```java
import org.springframework.stereotype.Component;

@Component
public class Bikini implements Outfit {
    @Override
    public void wear() {
        System.out.println("Mặc bikini");
    }
}
```

Trong ví dụ trên, `Bikini` được đánh dấu là một `@Component`, nên Spring Boot sẽ tạo một instance của `Bikini` và quản lý nó.

### Annotation `@Autowired` trong Spring Boot

`@Autowired` được sử dụng để tiêm (inject) các dependency vào các thành phần khác. Khi bạn đánh dấu một thuộc tính bằng `@Autowired`, Spring Boot sẽ tự động tiêm một instance của dependency tương ứng vào thuộc tính đó.

Ví dụ:

```java
import org.springframework.beans.factory.annotation.Autowired;

@Component
public class Girl {

    @Autowired
    Outfit outfit;

    // Các getter và setter
}
```

Trong ví dụ trên, `Girl` có một thuộc tính `outfit` được đánh dấu bằng `@Autowired`. Khi Spring Boot tạo một instance của `Girl`, nó sẽ tiêm một instance của `Outfit` (trong trường hợp này là `Bikini`) vào thuộc tính `outfit`.

### Singleton

Một điều đặc biệt là các bean trong Spring Boot được quản lý bởi `ApplicationContext` đều là singleton. Điều này có nghĩa là chỉ có một instance duy nhất của mỗi bean và nó được chia sẻ giữa các thành phần khác nhau. Điều này có thể thấy từ ví dụ sau:

```java
ApplicationContext context = SpringApplication.run(App.class, args);

Outfit outfit = context.getBean(Outfit.class);
Girl girl = context.getBean(Girl.class);

System.out.println("Outfit Instance: " + outfit);
System.out.println("Girl Outfit: " + girl.outfit);
```

Cả `outfit` và `girl.outfit` đều trỏ vào cùng một instance của `Bikini`.