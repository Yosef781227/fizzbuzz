def fizzbuzz(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def main() -> None:
    for number in range(1, 101):
        print(fizzbuzz(number))


if __name__ == "__main__":
    main()
