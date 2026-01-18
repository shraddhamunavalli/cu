def main(num):
    num = float(num)
    cube = num ** 3
    return f"Cube of {num} is {cube}"

if __name__ == "__main__":
    n = input("Enter a number: ")
    print(main(n))
