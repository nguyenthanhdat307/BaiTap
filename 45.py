import subprocess

# Định nghĩa lệnh cần thực thi
lenh = "ls -l"  # Ví dụ: lệnh để liệt kê các tệp trong thư mục hiện tại

# Thực thi lệnh và in ra kết quả
try:
    ket_qua = subprocess.check_output(lenh, shell=True, text=True)
    print("Kết quả của lệnh:")
    print(ket_qua)
except subprocess.CalledProcessError as loi:
    print(f"Lỗi khi thực thi lệnh: {loi}")