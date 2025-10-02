def red_knight(knight_row, pawns_col):
    caught_col = pawns_col * 2

    def _are_both_odd_or_even(term, term_2):
        return (
            term % 2 == 0
            and term_2 % 2 == 0
            or term % 2 == 1
            and term_2 % 2 == 1
        )

    color = (
        'White' if _are_both_odd_or_even(knight_row, pawns_col) else 'Black'
    )
    return color, caught_col


def red_knight_clever(knight_row, pawns_col):
    return 'White' if pawns_col % 2 == knight_row else 'Black', pawns_col * 2


def red_knight_clever_2(knight_row, pawns_col):
    return ['White', 'Black'][(knight_row + pawns_col) % 2], pawns_col * 2
