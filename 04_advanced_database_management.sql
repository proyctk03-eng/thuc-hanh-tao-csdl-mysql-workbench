-- =============================================================================
-- BÀI TẬP THỰC HÀNH: TẠO CSDL TRÊN MYSQL WORKBENCH
-- Phần 4: Các Thao Tác Quản Trị CSDL Nâng Cao (Alter, Drop, Character Set)
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- 1. Xem cấu hình bảng mã (Character Set) và quy tắc đối chiếu (Collation) của server và CSDL
SELECT 
    SCHEMA_NAME AS `Tên CSDL`,
    DEFAULT_CHARACTER_SET_NAME AS `Bảng Mã`,
    DEFAULT_COLLATION_NAME AS `Collation`
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = 'my_database1';

-- 2. Thay đổi bảng mã và collation của CSDL (ALTER DATABASE)
ALTER DATABASE `my_database1`
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

-- 3. Kiểm tra danh sách bảng và dung lượng trong CSDL
SELECT 
    TABLE_NAME AS `Tên Bảng`,
    ENGINE AS `Storage Engine`,
    TABLE_ROWS AS `Số Bản Ghi`,
    ROUND(((DATA_LENGTH + INDEX_LENGTH) / 1024), 2) AS `Dung Lượng (KB)`
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'my_database1';

-- 4. Cú pháp xóa CSDL an toàn (chỉ thực hiện khi muốn dọn dẹp môi trường thử nghiệm)
-- DROP DATABASE IF EXISTS `my_database1`;
