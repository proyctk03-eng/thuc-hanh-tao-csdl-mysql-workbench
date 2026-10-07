-- =============================================================================
-- BÀI TẬP THỰC HÀNH: TẠO CSDL TRÊN MYSQL WORKBENCH
-- Cách 2: Tạo CSDL sử dụng câu lệnh SQL trực tiếp trên MySQL Workbench Query Editor
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- Bước 1: Mở New Query Tab bằng tổ hợp phím (Ctrl + T) hoặc icon '+' trên Workbench
-- Bước 2: Nhập và thực thi câu lệnh tạo cơ sở dữ liệu theo đúng yêu cầu đề bài:

CREATE DATABASE `my_database1`;

-- =============================================================================
-- MỞ RỘNG NÂNG CAO (BEST PRACTICES TRONG MÔI TRƯỜNG DỰ ÁN THỰC TẾ)
-- =============================================================================

-- 1. Câu lệnh chuẩn phòng ngừa lỗi trùng lặp (Error 1007: Can't create database; database exists)
-- và cấu hình bảng mã tiếng Việt Unicode đầy đủ (utf8mb4 hỗ trợ cả emoji và ký tự đặc biệt):
CREATE DATABASE IF NOT EXISTS `my_database1`
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- 2. Kiểm tra danh sách các cơ sở dữ liệu hiện có trên máy chủ MySQL
SHOW DATABASES;

-- 3. Xem chi tiết cú pháp và thiết lập định dạng của cơ sở dữ liệu vừa tạo
SHOW CREATE DATABASE `my_database1`;

-- 4. Kích hoạt và chọn CSDL `my_database1` để làm việc (tương đương double click trên Schemas)
USE `my_database1`;

-- 5. Xác nhận CSDL đang được chọn hiện tại
SELECT DATABASE() AS `current_database`;
