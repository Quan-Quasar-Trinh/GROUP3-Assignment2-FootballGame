import math
import random

def move_toward(player, target):
    dx = target[0] - player.position[0]
    dy = target[1] - player.position[1]
    dist = math.sqrt(dx**2 + dy**2)
    if dist > 0:
        vx = dx / dist * player.speed
        vy = dy / dist * player.speed
        player.position = (player.position[0] + vx, player.position[1] + vy)
        player.velocity = (vx, vy)
    else:
        player.velocity = (0, 0)

def idle_behavior(player, original_pos):
    dx = original_pos[0] - player.position[0]
    dy = original_pos[1] - player.position[1]
    dist = math.sqrt(dx**2 + dy**2)
    if dist > 20:
        move_toward(player, original_pos)
    else:
        rx = random.uniform(-2, 2)
        ry = 0
        player.position = (player.position[0] + rx, player.position[1] + ry)
        player.velocity = (rx, ry)

def botMove(player, ball):
    if player.controlled:
        return

    team = player.team

    if team == "A":
        base_x_def = 233.33
        base_x_fwd = 400
        push_offset = 50
        defend_zone_max = 466.67
        push_target_x =  min(1400, max(0, ball.position[0] + push_offset))
    else:
        base_x_def = 1166.67
        base_x_fwd = 1000
        push_offset = 50
        defend_zone_max = 466.67
        push_target_x = min(1400, max(0, ball.position[0] - push_offset))

    if player.num == 3:
        original_pos = (base_x_def, 600)
    elif player.num == 2:
        original_pos = (base_x_def, 300)
    elif player.num == 1:
        original_pos = (base_x_fwd, 450)
    else:
        return

    teammate_possession = ball.last_touch and ball.last_touch.team == team

    ball_x, ball_y = ball.position

    buffer = 10
    in_def_half = ball_x <= defend_zone_max + buffer if team == "A" else ball_x >= (1400 - defend_zone_max - buffer)

    if player.num == 2:
        in_my_area = ball_y <= 450 + buffer
    elif player.num == 3:
        in_my_area = ball_y > 450 - buffer
    else:
        in_my_area = False

    if player.num == 1:
        move_toward(player, ball.position)
    else:
        if not in_def_half:
            idle_behavior(player, original_pos)
        elif in_def_half and in_my_area:
            push_target = (push_target_x, ball_y)
            move_toward(player, push_target)
        else:
            idle_behavior(player, original_pos)

    player.position = (
        max(0, min(1400, player.position[0])),
        max(100, min(800, player.position[1]))
    )

    if player.hitbox:
        player.hitbox.update(player.position)

