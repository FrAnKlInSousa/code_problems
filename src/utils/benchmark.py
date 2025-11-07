import timeit


def mensure(func, *args):
    func_name = f'{func.__name__}(*{args})'
    print(
        f'{
            timeit.timeit(
                func_name,
                setup=f"from __main__ import {func.__name__}",
                number=1_000_000,
            )
        }'
    )


def compare_mensure(functions: list, *args):
    for func in functions:
        name = func.__name__
        complete_name = f'{func.__name__}(*{args})'
        time_to_repeat = 1_000_000

        print(
            f'{name}: \n\t{
                timeit.timeit(
                    complete_name,
                    setup=f"from __main__ import {func.__name__}",
                    number=time_to_repeat,
                )
            }'
        )
