# imports
from scripts.rule import Rule


def main():
    upper_bound = int(input())
    print(Rule(upper_bound).collatz_sequence())


if __name__ == "__main__":
    print("Hello there! Please insert the upper bound of the numbers to be plotted: ")
    main()
