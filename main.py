def parse_input(input_string):
    lines = input_string.split("\n")
    number_of_stamps, max_price = lines[0].split(" ")
    stamp_prices = lines[1].split(" ")
    assert number_of_stamps == len(stamp_prices)
    return max_price, stamp_prices


def calculate_max_needed_stamps(max_price, stamp_prices):
    # elosztom a legnagyobb értékűvel, aztán a maradékot a második legnagyobbal
    pass


def get_max_needed_stamps(price, stamp_prices):
    prices_sorted = sorted(stamp_prices, reverse=True)
    remaining_price = price
    number_of_stamps = 0

    for stamp in prices_sorted:
        number_of_stamps += remaining_price // stamp
        remaining_price = remaining_price % stamp

    return number_of_stamps
