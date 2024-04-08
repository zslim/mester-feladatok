def parse_input(input_string):
    lines = input_string.split("\n")
    number_of_stamps, max_price = lines[0].split(" ")
    stamp_prices = lines[1].split(" ")
    assert number_of_stamps == len(stamp_prices)
    return max_price, stamp_prices


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


if __name__ == '__main__':
    input_message = """
    Please enter the number of stamps and the max price in the first line, then the stamp prices in the second line
    """
    task_input = input(input_message)
    max_price, stamp_prices = parse_input(task_input)
    result = calculate_max_needed_stamps(max_price, stamp_prices)
    print(result)
