class NumberChecker:
    def __init__(self, number):
        self.number = number

    def check_odd_even(self):
        if self.number % 2 == 0:
            return "Even"
        else:
            return "Odd"


# Example use
num = int(input("Enter a number: "))
checker = NumberChecker(num)
print(f"The number is {checker.check_odd_even()}.")
