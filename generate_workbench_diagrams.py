import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_paths = [
        r"C:\Windows\Fonts\segoeui.ttf" if not bold else r"C:\Windows\Fonts\segouib.ttf",
        r"C:\Windows\Fonts\calibri.ttf" if not bold else r"C:\Windows\Fonts\calibrib.ttf",
        r"C:\Windows\Fonts\arial.ttf" if not bold else r"C:\Windows\Fonts\arialbd.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def render_gui_creation():
    w, h = 1400, 850
    img = Image.new("RGB", (w, h), "#0F172A")
    draw = ImageDraw.Draw(img)

    f_title = get_font(24, bold=True)
    f_body = get_font(15, bold=False)
    f_body_b = get_font(15, bold=True)
    f_code = get_font(17, bold=True)
    f_small = get_font(13, bold=False)

    # Workbench Top App Bar
    draw.rectangle([0, 0, w, 40], fill="#020617")
    draw.text((20, 10), "MySQL Workbench - [Local instance 3306 - localhost:3306] - Cach 1: Tao CSDL bang GUI (Schemas Wizard)", fill="#F8FAFC", font=f_body_b)

    draw.rectangle([w - 45, 0, w, 40], fill="#EF4444")
    draw.text((w - 28, 10), "X", fill="#FFFFFF", font=f_body_b)

    draw.rectangle([0, 40, w, 75], fill="#1E293B")
    menus = ["File", "Edit", "View", "Query", "Database", "Server", "Tools", "Scripting", "Help"]
    mx = 20
    for m in menus:
        draw.text((mx, 48), m, fill="#94A3B8", font=f_small)
        mx += 65

    draw.rectangle([0, 75, w, 115], fill="#334155")
    draw.rounded_rectangle([25, 80, 260, 110], radius=5, fill="#1D4ED8", outline="#60A5FA", width=1)
    draw.text((35, 86), "[+] Create a new schema (Icon)", fill="#FFFFFF", font=f_body_b)

    draw.rounded_rectangle([270, 80, 420, 110], radius=5, fill="#475569")
    draw.text((280, 86), "> Execute Query", fill="#CBD5E1", font=f_small)

    draw.rectangle([0, 115, 300, h - 35], fill="#020617")
    draw.rectangle([0, 115, 300, 150], fill="#0F172A")
    draw.text((20, 122), "Navigator: SCHEMAS", fill="#F8FAFC", font=f_body_b)
    draw.text((260, 122), "[R]", fill="#60A5FA", font=f_body_b)

    schemas = [
        ("[-] sys", False),
        ("[-] sakila", False),
        ("[-] world", False),
        ("[*] my_database1 (Dang tao...)", True)
    ]
    sy = 165
    for s_name, is_target in schemas:
        if is_target:
            draw.rectangle([5, sy - 4, 295, sy + 28], fill="#1E3A8A")
            draw.text((15, sy), s_name, fill="#38BDF8", font=f_body_b)
        else:
            draw.text((15, sy), s_name, fill="#94A3B8", font=f_body)
        sy += 38

    draw.rectangle([300, 115, w, h - 35], fill="#090D16")
    
    draw.rectangle([300, 115, 540, 150], fill="#1E293B", outline="#334155")
    draw.text((315, 122), "new_schema - Schema  [X]", fill="#F8FAFC", font=f_body_b)

    form_box = [330, 175, w - 30, 470]
    draw.rounded_rectangle(form_box, radius=8, fill="#1E293B", outline="#475569", width=1)

    draw.text((360, 195), "Buoc 1 & 2: Thiet Lap Thong So Co So Du Lieu Moi (New Schema)", fill="#60A5FA", font=f_title)
    
    draw.text((360, 250), "Name:", fill="#F8FAFC", font=f_body_b)
    draw.rounded_rectangle([480, 240, 920, 285], radius=4, fill="#0F172A", outline="#3B82F6", width=2)
    draw.text((495, 250), "my_database1", fill="#38BDF8", font=f_code)

    draw.text((360, 310), "Charset:", fill="#F8FAFC", font=f_body_b)
    draw.rounded_rectangle([480, 300, 920, 345], radius=4, fill="#0F172A", outline="#475569", width=1)
    draw.text((495, 310), "utf8mb4 (Ho tro tieng Viet Unicode day du)", fill="#E2E8F0", font=f_body)

    draw.text((360, 370), "Collation:", fill="#F8FAFC", font=f_body_b)
    draw.rounded_rectangle([480, 360, 920, 405], radius=4, fill="#0F172A", outline="#475569", width=1)
    draw.text((495, 370), "Default Collation (utf8mb4_unicode_ci)", fill="#E2E8F0", font=f_body)

    draw.rounded_rectangle([w - 180, 420, w - 60, 455], radius=4, fill="#2563EB", outline="#60A5FA", width=1)
    draw.text((w - 145, 427), "Apply >>", fill="#FFFFFF", font=f_body_b)

    draw.rounded_rectangle([w - 300, 420, w - 200, 455], radius=4, fill="#334155")
    draw.text((w - 275, 427), "Revert", fill="#94A3B8", font=f_body)

    pw_box = [450, 485, 1250, 775]
    draw.rounded_rectangle(pw_box, radius=8, fill="#020617", outline="#3B82F6", width=2)
    draw.rectangle([450, 485, 1250, 525], fill="#1E3A8A")
    draw.text((470, 495), "Apply SQL Script to Database (Review Script Wizard)", fill="#F8FAFC", font=f_body_b)

    draw.text((475, 540), "SQL Script sinh tu dong boi MySQL Workbench khi nhan Apply:", fill="#94A3B8", font=f_small)
    sql_review_box = [475, 565, 1225, 705]
    draw.rectangle(sql_review_box, fill="#0F172A", outline="#334155")
    draw.text((490, 595), "CREATE SCHEMA `my_database1` DEFAULT CHARACTER SET utf8mb4 ;", fill="#22C55E", font=f_code)
    draw.text((490, 635), "-- Nhan Apply tiep theo de thuc thi len MySQL Server", fill="#64748B", font=f_small)

    draw.rounded_rectangle([1110, 720, 1220, 760], radius=4, fill="#16A34A")
    draw.text((1140, 730), "Apply [OK]", fill="#FFFFFF", font=f_body_b)

    draw.rounded_rectangle([980, 720, 1090, 760], radius=4, fill="#334155")
    draw.text((1010, 730), "Cancel", fill="#CBD5E1", font=f_body)

    draw.rectangle([0, h - 35, w, h], fill="#020617")
    draw.text((20, h - 26), "Ready. Connected to MySQL 8.0 on port 3306. | Cach 1: Tao CSDL bang GUI thanh cong 100% | Tac gia: Nguyen Tuan Dat (proyctk03-eng)", fill="#22C55E", font=f_small)

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-csdl-mysql-workbench\mysql_workbench_gui_create_schema.png"
    img.save(out_file)
    print("Saved clean:", out_file)

def render_sql_creation():
    w, h = 1400, 850
    img = Image.new("RGB", (w, h), "#0F172A")
    draw = ImageDraw.Draw(img)

    f_title = get_font(24, bold=True)
    f_body = get_font(15, bold=False)
    f_body_b = get_font(15, bold=True)
    f_code = get_font(18, bold=True)
    f_small = get_font(13, bold=False)

    draw.rectangle([0, 0, w, 40], fill="#020617")
    draw.text((20, 10), "MySQL Workbench - [Local instance 3306 - localhost:3306] - Cach 2: Su dung cau lenh SQL", fill="#F8FAFC", font=f_body_b)
    draw.rectangle([w - 45, 0, w, 40], fill="#EF4444")
    draw.text((w - 28, 10), "X", fill="#FFFFFF", font=f_body_b)

    draw.rectangle([0, 40, w, 75], fill="#1E293B")
    menus = ["File", "Edit", "View", "Query", "Database", "Server", "Tools", "Scripting", "Help"]
    mx = 20
    for m in menus:
        draw.text((mx, 48), m, fill="#94A3B8", font=f_small)
        mx += 65

    draw.rectangle([0, 75, w, 115], fill="#334155")
    draw.rounded_rectangle([25, 80, 240, 110], radius=5, fill="#1D4ED8", outline="#60A5FA", width=1)
    draw.text((35, 86), "[+] New Query Tab (Ctrl+T)", fill="#FFFFFF", font=f_body_b)

    draw.rounded_rectangle([250, 80, 420, 110], radius=5, fill="#16A34A", outline="#4ADE80", width=1)
    draw.text((260, 86), "> Execute (Ctrl+Enter)", fill="#FFFFFF", font=f_body_b)

    draw.rectangle([0, 115, 300, h - 35], fill="#020617")
    draw.rectangle([0, 115, 300, 150], fill="#0F172A")
    draw.text((20, 122), "Navigator: SCHEMAS", fill="#F8FAFC", font=f_body_b)
    draw.text((260, 122), "[R]", fill="#60A5FA", font=f_body_b)

    schemas = [
        ("[-] sys", False),
        ("[-] sakila", False),
        ("[-] world", False),
        ("[V] my_database1 (Vua tao xong)", True)
    ]
    sy = 165
    for s_name, is_target in schemas:
        if is_target:
            draw.rectangle([5, sy - 4, 295, sy + 28], fill="#065F46")
            draw.text((15, sy), s_name, fill="#4ADE80", font=f_body_b)
        else:
            draw.text((15, sy), s_name, fill="#94A3B8", font=f_body)
        sy += 38

    draw.rectangle([300, 115, w, 520], fill="#0F172A")
    
    draw.rectangle([300, 115, 480, 150], fill="#1E293B")
    draw.text((315, 122), "Query 1  [X]", fill="#38BDF8", font=f_body_b)

    draw.rectangle([300, 150, 350, 520], fill="#020617")
    for l_num in range(1, 10):
        draw.text((320, 160 + (l_num - 1) * 36), str(l_num), fill="#475569", font=f_small)

    editor_x = 370
    draw.text((editor_x, 160), "-- ===========================================================", fill="#64748B", font=f_code)
    draw.text((editor_x, 196), "-- BAI TAP: TAO CSDL BANG CAU LENH SQL TREN MYSQL WORKBENCH", fill="#64748B", font=f_code)
    draw.text((editor_x, 232), "-- ===========================================================", fill="#64748B", font=f_code)
    
    draw.rectangle([editor_x - 10, 268, w - 30, 312], fill="#1E293B", outline="#3B82F6", width=1)
    draw.text((editor_x, 276), "CREATE DATABASE `my_database1`;", fill="#38BDF8", font=f_code)
    draw.text((editor_x + 360, 276), "<-- CAU LENH YEU CAU DE BAI", fill="#FBBF24", font=f_body_b)

    draw.text((editor_x, 340), "-- Kiem tra co so du lieu vua tao:", fill="#94A3B8", font=f_code)
    draw.text((editor_x, 376), "SHOW DATABASES;", fill="#F43F5E", font=f_code)
    draw.text((editor_x, 412), "USE `my_database1`;", fill="#A855F7", font=f_code)

    draw.rectangle([300, 520, w, h - 35], fill="#020617")
    draw.rectangle([300, 520, w, 555], fill="#1E293B")
    draw.text((315, 526), "Action Output", fill="#F8FAFC", font=f_body_b)

    draw.rectangle([300, 555, w, 585], fill="#0F172A")
    draw.text((320, 560), "Status", fill="#94A3B8", font=f_small)
    draw.text((400, 560), "Time", fill="#94A3B8", font=f_small)
    draw.text((490, 560), "Action", fill="#94A3B8", font=f_small)
    draw.text((820, 560), "Message", fill="#94A3B8", font=f_small)
    draw.text((1150, 560), "Duration / Fetch", fill="#94A3B8", font=f_small)

    # Row 1: CREATE DATABASE
    draw.rectangle([300, 585, w, 625], fill="#064E3B")
    draw.text((320, 595), "[OK]", fill="#4ADE80", font=f_body_b)
    draw.text((400, 595), "16:08:12", fill="#E2E8F0", font=f_small)
    draw.text((490, 595), "CREATE DATABASE `my_database1`", fill="#FFFFFF", font=f_body_b)
    draw.text((820, 595), "1 row(s) affected", fill="#4ADE80", font=f_body_b)
    draw.text((1150, 595), "0.015 sec / 0.000 sec", fill="#CBD5E1", font=f_small)

    # Row 2: SHOW DATABASES
    draw.rectangle([300, 625, w, 665], fill="#020617")
    draw.text((320, 635), "[OK]", fill="#4ADE80", font=f_body_b)
    draw.text((400, 635), "16:08:14", fill="#E2E8F0", font=f_small)
    draw.text((490, 635), "SHOW DATABASES", fill="#E2E8F0", font=f_body)
    draw.text((820, 635), "5 row(s) returned", fill="#94A3B8", font=f_small)
    draw.text((1150, 635), "0.000 sec / 0.000 sec", fill="#CBD5E1", font=f_small)

    # Row 3: USE my_database1
    draw.rectangle([300, 665, w, 705], fill="#0F172A")
    draw.text((320, 675), "[OK]", fill="#4ADE80", font=f_body_b)
    draw.text((400, 675), "16:08:15", fill="#E2E8F0", font=f_small)
    draw.text((490, 675), "USE `my_database1`", fill="#E2E8F0", font=f_body)
    draw.text((820, 675), "0 row(s) affected", fill="#94A3B8", font=f_small)
    draw.text((1150, 675), "0.000 sec / 0.000 sec", fill="#CBD5E1", font=f_small)

    draw.rectangle([0, h - 35, w, h], fill="#020617")
    draw.text((20, h - 26), "Query completed successfully. Database `my_database1` is ready to use. | Tac gia: Nguyen Tuan Dat (proyctk03-eng)", fill="#22C55E", font=f_small)

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-csdl-mysql-workbench\mysql_workbench_sql_query_create_database.png"
    img.save(out_file)
    print("Saved clean:", out_file)

def render_table_query():
    w, h = 1400, 850
    img = Image.new("RGB", (w, h), "#0F172A")
    draw = ImageDraw.Draw(img)

    f_title = get_font(22, bold=True)
    f_body = get_font(15, bold=False)
    f_body_b = get_font(15, bold=True)
    f_code = get_font(17, bold=True)
    f_small = get_font(13, bold=False)

    # App bar
    draw.rectangle([0, 0, w, 40], fill="#020617")
    draw.text((20, 10), "MySQL Workbench - [Local instance 3306] - Ket qua mo rong: Tao bang & Truy van du lieu mau", fill="#F8FAFC", font=f_body_b)
    draw.rectangle([w - 45, 0, w, 40], fill="#EF4444")
    draw.text((w - 28, 10), "X", fill="#FFFFFF", font=f_body_b)

    # Menu bar
    draw.rectangle([0, 40, w, 75], fill="#1E293B")
    menus = ["File", "Edit", "View", "Query", "Database", "Server", "Tools", "Scripting", "Help"]
    mx = 20
    for m in menus:
        draw.text((mx, 48), m, fill="#94A3B8", font=f_small)
        mx += 65

    # Navigator with expanded tree
    draw.rectangle([0, 75, 320, h - 35], fill="#020617")
    draw.rectangle([0, 75, 320, 110], fill="#0F172A")
    draw.text((20, 85), "SCHEMAS Navigator (Expanded)", fill="#38BDF8", font=f_body_b)

    tree_items = [
        ("[-] my_database1", "#38BDF8", True),
        ("    [v] Tables (3 bang)", "#F8FAFC", True),
        ("        * departments", "#94A3B8", False),
        ("        * students", "#22C55E", True),
        ("        * courses", "#94A3B8", False),
        ("    [>] Views (0)", "#64748B", False),
        ("    [>] Stored Procedures (0)", "#64748B", False),
        ("    [>] Functions (0)", "#64748B", False),
        ("[-] sys", "#64748B", False),
        ("[-] sakila", "#64748B", False),
        ("[-] world", "#64748B", False)
    ]
    ty = 125
    for t_text, t_color, is_bold in tree_items:
        draw.text((20, ty), t_text, fill=t_color, font=f_body_b if is_bold else f_body)
        ty += 32

    # Query Editor (Upper right)
    draw.rectangle([320, 75, w, 320], fill="#0F172A")
    draw.rectangle([320, 75, 520, 110], fill="#1E293B")
    draw.text((335, 85), "Query 2 - SELECT *  [X]", fill="#38BDF8", font=f_body_b)

    draw.text((345, 130), "USE `my_database1`;", fill="#F43F5E", font=f_code)
    draw.text((345, 170), "SELECT s.`student_code`, s.`full_name`, s.`email`, d.`dept_name`", fill="#E2E8F0", font=f_code)
    draw.text((345, 210), "FROM `students` s", fill="#E2E8F0", font=f_code)
    draw.text((345, 250), "JOIN `departments` d ON s.`dept_id` = d.`dept_id`;", fill="#38BDF8", font=f_code)

    # Result Grid (Lower right)
    draw.rectangle([320, 320, w, h - 35], fill="#020617")
    draw.rectangle([320, 320, w, 360], fill="#1E293B")
    draw.text((335, 330), "Result Grid (3 rows returned in 0.002 sec)", fill="#22C55E", font=f_body_b)

    # Table Headers
    cols = [
        ("Mã SV", 120),
        ("Họ Và Tên", 260),
        ("Email", 280),
        ("Khoa / Bộ Môn", 320)
    ]
    cx = 330
    draw.rectangle([320, 360, w, 400], fill="#334155")
    for col_name, c_w in cols:
        draw.text((cx + 10, 370), col_name, fill="#F8FAFC", font=f_body_b)
        draw.line([cx + c_w, 360, cx + c_w, 400], fill="#475569", width=1)
        cx += c_w

    # Table Rows
    data_rows = [
        ("SV001", "Nguyen Tuan Dat", "proyctk03@gmail.com", "Bo Mon Ky Thuat Phan Mem"),
        ("SV002", "Tran Thi Mai", "maitt@codegym.vn", "Khoa Cong Nghe Thong Tin"),
        ("SV003", "Le Hoang Nam", "namlh@codegym.vn", "Bo Mon He Thong Thong Tin")
    ]
    ry = 400
    for r_idx, row in enumerate(data_rows):
        bg = "#0F172A" if r_idx % 2 == 0 else "#020617"
        draw.rectangle([320, ry, w, ry + 42], fill=bg)
        cx = 330
        for val, (_, c_w) in zip(row, cols):
            draw.text((cx + 10, ry + 12), val, fill="#38BDF8" if val.startswith("SV") else "#E2E8F0", font=f_body)
            draw.line([cx + c_w, ry, cx + c_w, ry + 42], fill="#1E293B", width=1)
            cx += c_w
        ry += 42

    # Bottom Status Bar
    draw.rectangle([0, h - 35, w, h], fill="#020617")
    draw.text((20, h - 26), "Database & Table verification successful. Full Integrity Checked. | Tac gia: Nguyen Tuan Dat (proyctk03-eng)", fill="#22C55E", font=f_small)

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-csdl-mysql-workbench\mysql_workbench_schemas_and_table_query.png"
    img.save(out_file)
    print("Saved clean:", out_file)

if __name__ == "__main__":
    render_gui_creation()
    render_sql_creation()
    render_table_query()
