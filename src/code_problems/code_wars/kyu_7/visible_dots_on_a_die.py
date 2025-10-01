def total_amount_visible(top_num: int, num_of_sides):
    try:
        bottom_num = num_of_sides + 1 - top_num
        visible_dots = list(range(1, num_of_sides + 1))
        visible_dots.remove(bottom_num)
        return sum(visible_dots)
    except ValueError:
        return top_num, num_of_sides


def total_amount_visible_clever(top: int, sides):
    return (sides + 1) * (sides // 2) - (sides + 1 - top)
