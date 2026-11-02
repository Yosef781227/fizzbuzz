import unittest
from contextlib import redirect_stdout
from io import StringIO

from fizzbuzz import fizzbuzz, main


class FizzBuzzTests(unittest.TestCase):
    def test_rules(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_output(self):
        output = StringIO()
        with redirect_stdout(output):
            main()
        lines = output.getvalue().splitlines()
        self.assertEqual(len(lines), 100)
        for number, line in enumerate(lines, start=1):
            expected = ""
            if number % 3 == 0:
                expected += "Fizz"
            if number % 5 == 0:
                expected += "Buzz"
            with self.subTest(number=number):
                self.assertEqual(line, expected or str(number))


if __name__ == "__main__":
    unittest.main()
