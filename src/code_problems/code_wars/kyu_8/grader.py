grade_a = 0.9
grade_b = 0.8
grade_c = 0.7
grade_d = 0.6
grade_f = 1


def grader(score) -> str:
    if score > grade_f or score < grade_d:
        return 'F'
    if score >= grade_a:
        return 'A'
    if score >= grade_b:
        return 'B'
    if score >= grade_c:
        return 'C'
    if score >= grade_d:
        return 'D'


def grader_clever(score) -> str:
    return 'FDCBAF'[
        (score > grade_f)
        + (score >= grade_a)
        + (score >= grade_b)
        + (score >= grade_c)
        + (score >= grade_d)
    ]
