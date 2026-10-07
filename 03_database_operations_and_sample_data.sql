-- =============================================================================
-- BÀI TẬP THỰC HÀNH: TẠO CSDL TRÊN MYSQL WORKBENCH
-- Phần 3: Tạo Bảng, Khóa Chính, Khóa Ngoại & Thao Tác Dữ Liệu Thực Nghiệm
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- Chọn CSDL đã tạo ở Bước 2
USE `my_database1`;

-- 1. Tạo bảng `departments` (Phòng ban / Khoa chuyên môn)
CREATE TABLE IF NOT EXISTS `departments` (
    `dept_id` INT AUTO_INCREMENT PRIMARY KEY,
    `dept_code` VARCHAR(20) NOT NULL UNIQUE,
    `dept_name` VARCHAR(100) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Tạo bảng `students` (Sinh viên / Học viên)
CREATE TABLE IF NOT EXISTS `students` (
    `student_id` INT AUTO_INCREMENT PRIMARY KEY,
    `student_code` VARCHAR(20) NOT NULL UNIQUE,
    `full_name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `phone` VARCHAR(15),
    `gender` ENUM('Nam', 'Nữ', 'Khác') DEFAULT 'Nam',
    `birth_date` DATE,
    `dept_id` INT,
    `is_active` BOOLEAN DEFAULT TRUE,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT `fk_students_department` 
        FOREIGN KEY (`dept_id`) REFERENCES `departments` (`dept_id`) 
        ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Tạo bảng `courses` (Khóa học / Học phần)
CREATE TABLE IF NOT EXISTS `courses` (
    `course_id` INT AUTO_INCREMENT PRIMARY KEY,
    `course_code` VARCHAR(20) NOT NULL UNIQUE,
    `course_name` VARCHAR(150) NOT NULL,
    `credits` INT NOT NULL DEFAULT 3,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Thêm dữ liệu mẫu vào bảng `departments`
INSERT INTO `departments` (`dept_code`, `dept_name`) VALUES
('CNTT', 'Khoa Công Nghệ Thông Tin'),
('KTPM', 'Bộ Môn Kỹ Thuật Phần Mềm'),
('HTTT', 'Bộ Môn Hệ Thống Thông Tin')
ON DUPLICATE KEY UPDATE `dept_name`=VALUES(`dept_name`);

-- 5. Thêm dữ liệu mẫu vào bảng `students`
INSERT INTO `students` (`student_code`, `full_name`, `email`, `phone`, `gender`, `birth_date`, `dept_id`) VALUES
('SV001', 'Nguyễn Tuấn Đạt', 'proyctk03@gmail.com', '0912345678', 'Nam', '2003-05-15', 2),
('SV002', 'Trần Thị Mai', 'maitt@codegym.vn', '0987654321', 'Nữ', '2003-08-20', 1),
('SV003', 'Lê Hoàng Nam', 'namlh@codegym.vn', '0901234567', 'Nam', '2002-12-10', 3)
ON DUPLICATE KEY UPDATE `full_name`=VALUES(`full_name`);

-- 6. Thêm dữ liệu mẫu vào bảng `courses`
INSERT INTO `courses` (`course_code`, `course_name`, `credits`) VALUES
('CSDL101', 'Cơ Sở Dữ Liệu Quan Hệ & MySQL', 3),
('GIT101', 'Quản Lý Mã Nguồn Với Git & GitHub', 2),
('FED101', 'Thiết Kế Web & Giao Diện Người Dùng', 3)
ON DUPLICATE KEY UPDATE `course_name`=VALUES(`course_name`);

-- 7. Truy vấn kiểm tra dữ liệu kết hợp JOIN
SELECT 
    s.`student_code` AS `Mã SV`,
    s.`full_name` AS `Họ Và Tên`,
    s.`email` AS `Email`,
    s.`gender` AS `Giới Tính`,
    COALESCE(d.`dept_name`, 'Chưa phân bổ') AS `Khoa / Bộ Môn`
FROM `students` s
LEFT JOIN `departments` d ON s.`dept_id` = d.`dept_id`
ORDER BY s.`student_id` ASC;
