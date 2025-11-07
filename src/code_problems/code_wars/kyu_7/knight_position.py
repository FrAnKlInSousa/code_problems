def possible_positions(pos: str):
    row, col = list(pos)
    row = ord(row)
    col = int(col)

    def valid_pos(row, col):
        if any([row < 97, row > 104, col < 1, col > 8]):  # noqa PLR2004
            return
        return f'{chr(row)}{col}'

    positions = [
        [row + 2, col + 1],
        [row + 2, col - 1],
        [row - 2, col + 1],
        [row - 2, col - 1],
        [row + 1, col + 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row - 1, col - 2],
    ]
    final = [move for pos in positions if (move := valid_pos(*pos))]

    return sorted(final)
