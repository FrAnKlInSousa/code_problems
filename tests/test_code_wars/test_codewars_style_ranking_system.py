import pytest


def test_level_up(make_user):
    user = make_user()
    for rank in range(-7, 9):
        if rank == 0:
            continue
        user.level_up()

        assert user.rank == rank

def test_max_rank_must_be_8(make_user):
    max_rank = 8
    user = make_user(rank=8)
    user.level_up()
    assert user.rank == max_rank

def test_increase_progress_must_not_change(make_user):
    user = make_user(rank=5, progress=33)
    user.inc_progress(1)
    assert user.progress == 33

@pytest.mark.parametrize('rank,activity_rank,expected', [
    (-8, -7, 30),
    (-8, -6, 60),
    (3, 4, 30),
    (-2, 1, 60)

])
def test_increase_progress_by_10(make_user, rank, activity_rank, expected):
    user = make_user(rank=rank, progress=20)
    user.inc_progress(activity_rank)
    assert user.progress == expected

@pytest.mark.parametrize('rank,activity_rank,new_progress,new_rank', [
    (-8, -5, 88, -7),
    (-8, -4, 58, -6),
    (8, 8, 0, 8),

])
def test_increase_progress_over_100_and_level_up(make_user, rank, activity_rank, new_rank, new_progress):
    user = make_user(rank=rank, progress=98)
    user.inc_progress(activity_rank)
    assert user.progress == new_progress
    assert user.rank == new_rank


def test_multiple_progress(make_user):
    user = make_user()
    user.inc_progress(-7)
    assert user.progress == 10
    user.inc_progress(-5)
    assert user.progress == 0


def test_multiple_progress_2(make_user):
    user = make_user()
    user.inc_progress(1)
    assert user.progress == 40
    assert user.rank == -2
    user.inc_progress(1)
    assert user.progress == 80
    assert user.rank == -2

    user.inc_progress(1)
    assert user.progress == 20
    assert user.rank == -1
    user.inc_progress(1)
    assert user.progress == 30
    assert user.rank == -1
    user.inc_progress(1)
    assert user.progress == 40
    assert user.rank == -1

    user.inc_progress(2)
    assert user.progress == 80
    assert user.rank == -1
    user.inc_progress(2)
    assert user.progress == 20
    assert user.rank == 1
    user.inc_progress(-1)
    assert user.progress == 21
    assert user.rank == 1

    user.inc_progress(3)
    assert user.progress == 61
    assert user.rank == 1

    user.inc_progress(8)
    assert user.progress == 51
    assert user.rank == 6
    user.inc_progress(8)
    assert user.progress == 91
    assert user.rank == 6
    user.inc_progress(8)
    assert user.progress == 31
    assert user.rank == 7


    user.inc_progress(8)
    assert user.progress == 41
    assert user.rank == 7
    user.inc_progress(8)
    assert user.progress == 51
    assert user.rank == 7
    user.inc_progress(8)
    assert user.progress == 61
    assert user.rank == 7
    #??

    user.inc_progress(8)
    assert user.progress == 71
    assert user.rank == 7
    user.inc_progress(8)
    assert user.progress == 81
    assert user.rank == 7
    user.inc_progress(8)
    assert user.progress == 91
    assert user.rank == 7

    user.inc_progress(8)
    assert user.progress == 0
    assert user.rank == 8
    #....
    user.inc_progress(8)
    assert user.progress == 0
    assert user.rank == 8

def test_max_progress_at_rank_8(make_user):
    user = make_user(rank=8, progress=97)
    user.inc_progress(8)
    assert user.progress == 0

def test_invalid_activity_rank(make_user):
    user = make_user()
    with pytest.raises(ValueError):
        user.inc_progress(9)


def test_ranks(make_user):
    # [9, -5, 5, -9, -7, 2, -9, 11, 1, 6, -10, 10]
    valid_ranks = list(range(-8, 0)) + list(range(1, 9))
    user = make_user()

    testes = [(9, ValueError, ValueError),
              (-5, -8, 90),
              (5, 8, 0),
              (-9, ValueError, ValueError),
              (-7, 8, 0), (2, 8, 0),
              (-9, ValueError, ValueError),
              (11, ValueError, ValueError),
              (1, 8, 0), (6, 8, 0),
              (-10, ValueError, ValueError),
              (10, ValueError, ValueError),
              ]

    for rank,expected_rank,expected_progress in testes:

        if rank not in valid_ranks:
            with pytest.raises(ValueError):
                user.inc_progress(rank)
        else:
            user.inc_progress(rank)
            assert user.rank == expected_rank
            assert user.progress == expected_progress

def test_alternative(make_user_alternative):
    valid_ranks = list(range(-8, 0)) + list(range(1, 9))

    testes = [(9, ValueError, ValueError),
              (-5, -8, 90),
              (5, 8, 0),
              (-9, ValueError, ValueError),
              (-7, 8, 0), (2, 8, 0),
              (-9, ValueError, ValueError),
              (11, ValueError, ValueError),
              (1, 8, 0), (6, 8, 0),
              (-10, ValueError, ValueError),
              (10, ValueError, ValueError),
              ]
    user = make_user_alternative()
    for rank,expected_rank,expected_progress in testes:

        if rank not in valid_ranks:
            with pytest.raises(ValueError):
                user.inc_progress_alternative(rank)
        else:
            user.inc_progress_alternative(rank)
            assert user.rank_alternative == expected_rank
            assert user.progress_alternative == expected_progress


def test_same_rank_alternative(make_user_alternative):
    user = make_user_alternative()
    user.inc_progress_alternative(-8)

    assert user.rank_alternative == -8
    assert user.progress_alternative == 3


def test_one_lower_rank_alternative(make_user_alternative):
    user = make_user_alternative()
    user.inc_progress_alternative(-3)

    assert user.rank_alternative == -6
    assert user.progress_alternative == 50

    user.inc_progress_alternative(-7)

    assert user.rank_alternative == -6
    assert user.progress_alternative == 51