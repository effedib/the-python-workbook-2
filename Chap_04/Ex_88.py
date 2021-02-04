# Median of Three Values

# This function takes three numbers as parameters and returns the median value as its result.

# @return the median of values num1, num2 and num3
def Median(num1: float, num2: float, num3: float) -> float:
    nums = (num1, num2, num3)
    median = sum(nums) - max(nums) - min(nums)

    return median

def main():
    a, b, c = input("Enter 3 number divided by space: ").split()
    a, b, c = (float(a), float(b), float(c))
    med     = Median(a, b, c)
    print("The median number is {:.2f}".format(med))

if __name__ == "__main__":
    main()