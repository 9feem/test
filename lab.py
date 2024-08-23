def o():
    return "----------------------"
def p(name):
    print(f"-{name}-")

def get_input(prompt, valid_options=None, is_int=False):
    while True:
        user_input = input(prompt)
        if is_int:
            try:
                user_input = int(user_input)
            except ValueError:
                print("กรุณาใส่หมายเลขที่ถูกต้อง.")
                continue
        if valid_options and user_input not in valid_options:
            print("เลือกไม่ถูกต้อง, กรุณาลองใหม่.")
        else:
            return user_input

# กำหนดตัวแปรต่างๆ
shop = "ร้าน ซี-ฟี ฟาร์ม"
s = {"1": "ไข่ไก่บ้าน", "2": "ไข่ไก่ฟาร์ม"}
b = [0, 1, 2, 3, 4]
money = {"1": "ปลายทาง", "2": "พร้อมเพย์"}

# เริ่มโค้ด
print(f"{o()}{shop}{o()}")
user = input("ป้องชื่อ : ")
p("เลือกประเภทไข่")
for i, name in s.items():
    print(f"{i}: {name}")

num1 = get_input("กรุณาเลือกหมายเลขประเภทไข่: ", valid_options=s.keys())
selected_egg_type = s[num1]

p("เลือกเบอร์ไข่")
print("0 : เบอร์ 0\n1 : เบอร์ 1\n2 : เบอร์ 2\n3 : เบอร์ 3\n4 : เบอร์ 4")
num2 = get_input("กรุณาเลือกหมายเลขเบอร์ไข่: ", valid_options=b, is_int=True)

quantity = get_input("จำนวนที่ต้องการกี่แผง: ", is_int=True)

p("เลือกช่องทางจ่ายเงิน")
for i, method in money.items():
    print(f"{i}: {method}")

num3 = get_input("กรุณาเลือกหมายเลขช่องทางจ่ายเงิน: ", valid_options=money.keys())

address_and_phone = input("ที่อยู่และเบอร์: ").strip()

# แสดงข้อมูลที่เลือก
print(f"{o()}สรุปการสั่งซื้อ{o()}")
print(f"สวัดดีคุณ : {user}")
print(f"ประเภทไข่ที่เลือก: {selected_egg_type}")
print(f"หมายเลขเบอร์ไข่ที่เลือก: {num2}")
print(f"จำนวนที่ต้องการ: {quantity} แผง")
print(f"ช่องทางการจ่ายเงิน: {money[num3]}")
print(f"ที่อยู่และเบอร์: {address_and_phone}")
print(f"{o()}ขอบคุณที่ใช่บริการ{o()}")
