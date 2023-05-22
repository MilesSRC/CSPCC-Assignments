def main():
    num = int(input("Enter a number to get a multication table of: "));
    print("\n")

    for index in range(0, 10):
        times = index + 1
        result = times * num;

        print(str(times) + " * " + str(num) + " = " + str(result));

main();