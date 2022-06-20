import unittest
from math import sin, cos, tan, log

from hypothesis import given
import hypothesis.strategies as st
from MathExpTree import MathExpTree


class MathTest(unittest.TestCase):

    def test_sin_func(self):
        i = MathExpTree('sin(0)+func(5)*(5-1)')
        i.convert()
        self.assertEqual(i.evaluate(func=lambda x: x * 42), 840)
        i.visualize(1)

    def test_cos_pow(self):
        i = MathExpTree('cos(0)+func(5)+pow(2,2)')
        i.convert()
        self.assertEqual(i.evaluate(func=lambda x: x + 2), 12.0)
        i.visualize(3)

    def test_cos_func(self):
        i = MathExpTree('12-(cos((3-a)*b)+(func(c)+3))')
        i.convert()
        self.assertEqual(i.evaluate(a=3, b=5, c=7, func=lambda x: x / 2), 4.5)
        i.visualize(4)

    def test_func_add(self):
        i = MathExpTree('func1(1,2)+func2(3,4,5)')
        i.convert()
        def f1(x, y): return x + y
        def f2(x, y, z): return max(x, y, z)
        self.assertEqual(i.evaluate(func1=f1, func2=f2), 8.0)
        i.visualize(5)

    def test_mul_dev(self):
        i = MathExpTree('(4+14-(2*3))/2')
        i.convert()
        self.assertEqual(i.evaluate(), 6.0)
        i.visualize(6)

    def test_run_time_error(self):
        i = MathExpTree('2+2/0')
        i.convert()
        i.visualize(8)
        self.assertEqual(False, i.evaluate())

    @given(a=st.integers(min_value=10, max_value=20),
           b=st.integers(min_value=10, max_value=20),
           c=st.integers(min_value=10, max_value=20),
           d=st.integers(min_value=10, max_value=20))
    def test_pow_log(self, a, b, c, d):
        i = MathExpTree(
            'pow(' +
            str(a) +
            ',' +
            str(b) +
            ')*log(' +
            str(c) +
            ',' +
            str(d) +
            ')')
        i.convert()
        i.visualize(7)
        self.assertEqual(i.evaluate(), pow(a, b) * log(c, d))

    @given(a=st.integers(min_value=0, max_value=100),
           b=st.integers(min_value=0, max_value=100),
           c=st.integers(min_value=0, max_value=100),
           d=st.integers(min_value=0, max_value=100))
    def test_add_minus(self, a, b, c, d):
        i = MathExpTree('' + str(a) + '+' + str(b) +
                        '+(' + str(c) + '-' + str(d) + ')')
        i.convert()
        self.assertEqual(i.evaluate(), a + b + (c - d))
        i.visualize(2)


if __name__ == '__main__':
    unittest.main()
