#W2A1
print("Hello World!")
#W2A2
name = input("Nhập tên của bạn: ")
print("Xin chào", name + "!")
#W2A3
a, b = map(int, input("Nhập a b: ").split())
print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)
print("Phần nguyên:", a // b)
print("Phần dư:", a % b)
print("Chia thực:", format(a / b, ".2f"))
#W2A4
a1, b1, c1, a2, b2, a3 = map(float, input().split())
tb = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
print(format(tb, ".1f"))
#W2A5
a, b = map(int, input().split())
print(a ** b)
#W2A6
ch = input("Nhập 1 kí tự thường: ")
print("Mã Unicode:", ord(ch))
print("Kí tự hoa:", ch.upper())
#W2A7
A = ((13 ** 2) * 3) + 5
B = 13 ** 2 * 3 + 5
print("A =", A)
print("B =", B)
#w2A8
C = float(input("Nhập nhiệt độ C: "))
F = 9/5 * C + 32
print(format(F, ".2f"))
#W2A9
x = float(input("Giá đồng hồ (USD): "))
total = x + 10
total = total * 1.3 * 1.1
print(format(total, ".2f"))
#W2A10
a, b, c = input("Nhập tên 3 người: ").split()
print(f"Hi {c}, {b} and {a}.")
#W2A11
h, m = map(int, input().split())
seconds = h * 3600 + m * 60
print(seconds)
#W2A12
n = int(input())
print(6 * n * n)
#W2A13
a, b = map(int, input().split())
print((a * b) % 10)
#W2A14
a, b = map(int, input().split())
a, b = b, a
print(a, b)
#W2A15
n = int(input())
star_number = 6 * n * (n - 1) + 1
print(star_number)
#W2A16
print("Spring")
print("Summer")
print("Autumn")
print("Winter")
#W2A17
print("*")
print("***")
print("*****")
#W2A18
print("### # #     ### ###")
print(" #    #    #    #    #")
print(" #    #     #   #    #")
print(" #    #    #    #    #")
print(" #    # #       #    #")
#W2A19
print("Monday")
print("Tuesday")
print("Wednesday")
print("Thursday")
print("Friday")
print("Saturday")
print("Sunday")
#W2A20
print("January")
print("February")
print("March")
print("April")
print("May")
print("June")
print("July")
print("August")
print("September")
print("October")
print("November")
print("December")
#W2A21
for _ in range(10):
    print("Hello, world")
