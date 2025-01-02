def calculate_max_needed_stamps(max_price, stamp_prices):
    max_number_of_stamps = 1
    for price in range(1, max_price + 1):
        number_of_stamps = get_max_needed_stamps(price, stamp_prices)
        if number_of_stamps > max_number_of_stamps:
            max_number_of_stamps = number_of_stamps
    return max_number_of_stamps


def get_max_needed_stamps(price, stamp_prices):
    prices_sorted = sorted(stamp_prices, reverse=True)
    remaining_price = price
    number_of_stamps = 0

    for stamp in prices_sorted:
        number_of_stamps += remaining_price // stamp
        remaining_price = remaining_price % stamp

    return number_of_stamps


def main():
    input_line_1 = input("Please enter the number of stamps and the maximum price: ")
    number_of_stamps, max_price = [int(number) for number in input_line_1.split(" ")]
    input_line_2 = input("Please enter the stamp prices: ")
    stamp_prices = [int(number) for number in input_line_2.split(" ")]
    assert number_of_stamps == len(stamp_prices)
    result = calculate_max_needed_stamps(max_price, stamp_prices)
    print(result)


if __name__ == '__main__':
    main()
