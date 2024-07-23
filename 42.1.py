import platform

# Xác định kiến trúc của Python
architecture = platform.architecture()[0]

if architecture == '32bit':
    print("Python đang thực thi ở chế độ 32-bit")
elif architecture == '64bit':
    print("Python đang thực thi ở chế độ 64-bit")
else:
    print("Không thể xác định được kiến trúc của Python")