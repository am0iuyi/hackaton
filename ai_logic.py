import math
from pygame import Rect

def pifagor(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def can_move(new_x, new_y, walls: list):
    for wall in walls:
        x_wall, y_wall, width_wall, height_wall = wall['x'], wall['y'], wall['width'], wall['height']
        if Rect.colliderect(
                Rect(new_x, new_y, 50, 50),
                Rect(x_wall, y_wall, width_wall, height_wall)
        ):
            return False
    return True


def move(ai_x: int, ai_y: int, score_x: int, score_y: int, move_speed: int = 0.25, walls=None):
    if walls is None:
        walls = []

    left = pifagor(ai_x - move_speed, ai_y, score_x, score_y)
    right = pifagor(ai_x + move_speed, ai_y, score_x, score_y)
    up = pifagor(ai_x, ai_y - move_speed, score_x, score_y)
    down = pifagor(ai_x, ai_y + move_speed, score_x, score_y)

    if not can_move(ai_x - move_speed, ai_y, walls):
        left = math.inf
    if not can_move(ai_x + move_speed, ai_y, walls):
        right = math.inf
    if not can_move(ai_x, ai_y - move_speed, walls):
        up = math.inf
    if not can_move(ai_x, ai_y + move_speed, walls):
        down = math.inf

    min_lenght = min(left, right, up, down)

    if math.inf == min_lenght:
        return ai_x, ai_y
    elif right == min_lenght:
        return ai_x + move_speed, ai_y
    elif up == min_lenght:
        return ai_x, ai_y - move_speed
    elif down == min_lenght:
        return ai_x, ai_y + move_speed
    elif left == min_lenght:
        return ai_x - move_speed, ai_y



def get_min_lenght_score(ai_x: int, ai_y: int, scores: list):
    min_lenght = math.inf
    min_lenght_score = scores[0]

    for score_x, score_y in scores:
        lenght = pifagor(ai_x, ai_y, score_x, score_y)
        if lenght < min_lenght:
            min_lenght = lenght
            min_lenght_score = score_x, score_y

    return min_lenght_score
