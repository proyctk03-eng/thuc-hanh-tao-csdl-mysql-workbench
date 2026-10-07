-- =============================================================================
-- BÀI TẬP THỰC HÀNH: TẠO CSDL TRÊN MYSQL WORKBENCH
-- Cách 1: Mã SQL được sinh tự động bởi Trình hướng dẫn đồ họa (GUI Wizard)
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- Thao tác GUI:
-- 1. Click vào biểu tượng "Create a new schema in the connected server" trên thanh công cụ
-- 2. Nhập Schema Name: my_database1
-- 3. Chọn Character Set: utf8mb4, Collation: Default Collation
-- 4. Nhấn "Apply" -> MySQL Workbench sinh ra đoạn script sau:

CREATE SCHEMA `my_database1` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;

-- 5. Nhấn "Apply" tiếp theo để thực thi lên MySQL Server
-- 6. Nhấn "Finish" để hoàn tất.
