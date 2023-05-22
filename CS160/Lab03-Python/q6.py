PI = 3.14159;

def main():
    radius = float(input("Enter raidus of cylinder: "));
    height = float(input("Enter height of cylinder: "));

    volume = PI * (radius ** 2) * height;

    print("\nThe volume is " + format(volume, '.1f') + " cubic inches");

main();