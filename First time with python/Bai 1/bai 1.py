def count_digits(n):
    # Sử dụng hàm str để chuyển số thành chuỗi, sau đó sử dụng len để đếm số chữ số
    return len(str(n))

# Nhập vào số nguyên dương n từ người dùng
n = int(input("Nhập vào số nguyên dương n: "))

# Đếm số chữ số của n
result = count_digits(n)

print(f"Số nguyên {n} có {result} chữ số.")