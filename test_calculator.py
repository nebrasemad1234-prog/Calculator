import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        print("اختبار الجمع: 2 + 3 =", result)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(5, 3)
        print("اختبار الطرح: 5 - 3 =", result)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = multiply(4, 3)
        print("اختبار الضرب: 4 × 3 =", result)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = divide(10, 2)
        print("اختبار القسمة: 10 ÷ 2 =", result)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        print("اختبار القسمة على صفر: يجب أن يظهر خطأ")
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
