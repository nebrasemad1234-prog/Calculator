

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("لا يمكن القسمة على صفر")
    return a / b

# الجزء الخاص بالتشغيل من المستخدم
if __name__ == "__main__":
    print("آلة حاسبة بسيطة")
    print("اختر العملية:")
    print("1 - جمع")
    print("2 - طرح")
    print("3 - ضرب")
    print("4 - قسمة")

    choice = input("أدخلي رقم العملية (1/2/3/4): ")

    try:
        num1 = float(input("أدخلي الرقم الأول: "))
        num2 = float(input("أدخلي الرقم الثاني: "))

        if choice == '1':
            print("الناتج =", add(num1, num2))
        elif choice == '2':
            print("الناتج =", subtract(num1, num2))
        elif choice == '3':
            print("الناتج =", multiply(num1, num2))
        elif choice == '4':
            print("الناتج =", divide(num1, num2))
        else:
            print("اختيار غير صحيح")
    except ValueError as e:
        print("خطأ:", e)
