import unittest
from contextlib import redirect_stdout
from io import StringIO

from fizzbuzz import fizzbuzz, main


class FizzBuzzTests(unittest.TestCase):
    def test_number(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(98), "98")

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(99), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(100), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(90), "FizzBuzz")

    def test_output(self):
        output = StringIO()
        with redirect_stdout(output):
            main()

        lines = output.getvalue().splitlines()
        self.assertEqual(len(lines), 100)
        self.assertEqual(lines[:15], [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
            "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
        ])
        self.assertEqual(lines[-1], "Buzz")
        self.assertEqual(lines.count("Fizz"), 27)
        self.assertEqual(lines.count("Buzz"), 14)
        self.assertEqual(lines.count("FizzBuzz"), 6)


if __name__ == "__main__":
    unittest.main()
