def parse_input(input_string):
    lines = input_string.split("\n")
    number_of_stamps, max_price = lines[0].split(" ")
    stamp_prices = lines[1].split(" ")
    assert number_of_stamps == len(stamp_prices)
    return number_of_stamps, max_price, stamp_prices


def calculate_max_needed_stamps(number_of_stamps, max_price, stamp_prices):
    pass
