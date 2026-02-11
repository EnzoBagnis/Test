def average():
    total = 0
    count = 0
    while True:
        try:
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == 'done':
                break
            total += float(num)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    if count > 0:
        print(f"The average is: {total / count}")
    else:
        print("No numbers were entered.")