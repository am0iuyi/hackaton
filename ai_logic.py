import math


def pifagor(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def move(ai_x: int, ai_y: int, score_x: int, score_y: int, move_speed: int = 0.25):
    left = pifagor(ai_x - move_speed, ai_y, score_x, score_y)
    right = pifagor(ai_x + move_speed, ai_y, score_x, score_y)
    up = pifagor(ai_x, ai_y - move_speed, score_x, score_y)
    down = pifagor(ai_x, ai_y + move_speed, score_x, score_y)

    min_lenght = min(left, right, up, down)

    if left == min_lenght:
        return ai_x - move_speed, ai_y
    elif right == min_lenght:
        return ai_x + move_speed, ai_y
    elif up == min_lenght:
        return ai_x, ai_y - move_speed
    else:
        return ai_x, ai_y + move_speed


def get_min_lenght_score(ai_x: int, ai_y: int, scores: list):
    min_lenght = math.inf
    min_lenght_score = scores[0]

    for score_x, score_y in scores:
        lenght = pifagor(ai_x, ai_y, score_x, score_y)
        if lenght < min_lenght:
            min_lenght = lenght
            min_lenght_score = score_x, score_y

    return min_lenght_score

