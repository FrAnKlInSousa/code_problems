def controller(events: str):
    output = []
    stoped = True
    count = 0
    increment = 1

    def move(change_moving_status=False):
        nonlocal count, stoped, increment
        if change_moving_status:
            stoped = not stoped
        if not stoped:
            count += increment
        output.append(str(count))

        # if count == 5 and not stoped or count == 0 and not stoped:
        if not stoped and (count == 5 or count == 0):
            increment = -increment
            stoped = not stoped

    for char in events:
        if char == 'O':
            increment = -increment
            move()
        elif char == 'P' and stoped:
            move(True)
        elif char == 'P' and not stoped:
            move(True)
        elif char == '.' and not stoped:
            move()
        else:
            output.append(str(count))
    return ''.join(output)