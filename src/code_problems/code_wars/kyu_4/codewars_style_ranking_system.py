class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.valid_ranks = list(range(-8, 0)) + list(range(1, 9))

    def level_up(self):
        if not self.rank == 8:
            self.rank += 1
        if self.rank == 0:
            self.rank += 1
        if self.rank == 8:
            self.progress = 0

    def calculate_progress(self):
        if self.progress >= 100 and self.rank == 7:
            self.progress = 0
            self.rank = 8
        elif self.rank == 8:
            self.progress = 0
        elif self.progress >= 100:
            level_to_up, self.progress = divmod(self.progress, 100)
            for i in range(level_to_up):
                self.level_up()

    def inc_progress(self, activity_rank: int):
        if activity_rank not in self.valid_ranks:
            raise ValueError
        if activity_rank > self.rank:
            if (activity_rank > 0 and self.rank > 0) or (
                activity_rank < 0 and self.rank < 0
            ):
                self.progress += 10 * (activity_rank - self.rank) ** 2
                self.calculate_progress()
            elif activity_rank > 0 > self.rank:
                self.progress += 10 * (activity_rank - self.rank - 1) ** 2
                self.calculate_progress()
        elif activity_rank == self.rank:
            self.progress += 3
            self.calculate_progress()
        elif (
            activity_rank < 0 < self.rank
            and (self.rank - activity_rank - 1 == 1)
            or self.rank - activity_rank == 1
        ):
            self.progress += 1
            self.calculate_progress()


ranks = [i for i in range(-8, 9) if i != 0]


class UserAlternative:
    def __init__(self):
        self.total2 = 0

    def inc_progress_alternative(self, level):
        d = ranks.index(level) - ranks.index(self.rank_alternative)
        if d > 0:
            self.total2 += 10 * d**2
        elif d == 0:
            self.total2 += 3
        elif d == -1:
            self.total2 += 1

    @property
    def progress_alternative(self):
        return self.total2 % 100 if self.rank_alternative != 8 else 0

    @property
    def rank_alternative(self):
        return ranks[min(15, self.total2 // 100)]
