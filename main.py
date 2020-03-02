
from func import *

width = 640
height = 480
white = (255,255,255)
green = (50,200,50)
red = (200,0,0)
high_score = 0

f = open('high_score.txt', 'r')
try:
    read = int(f.read())
    if read % 69420 == 0:
        high_score = int(read / 69420)
except:
    high_score = 0

f.close()

score = 0
x_move_speed = 1
player_radius = 30
player_x = 100
player_y = 0
player_y_speed = 0

player_alive = True

floor_y = height - randint(20,40)

obstacle_x = []
obstacle_radius = []
obstacle_y = []

running = True


for i in range(1, 4):
    obstacle_x.append(width * i + randint(-25, 25))
    obstacle_radius.append(randint(40,70))

for g in obstacle_radius:
    obstacle_y.append(floor_y - g)


pg.init()
my_font = pg.font.Font(pg.font.get_default_font(), 30)
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

time.sleep(2)
while running:
    clock.tick(1000)

    # Update
    if not player_alive:
        player_y = 0
        player_y_speed = 0
        player_alive = True
        if int(high_score) < score:
            f = open('high_score.txt', 'w+')
            f.write(str(score*69420))
            f.close()
            high_score = score
        score = 0


    player_y_speed += 1
    player_y += player_y_speed
    if player_y > floor_y - player_radius:
        player_y = floor_y - player_radius

    closest_obstacle = 0

    for o in range(3):
        obstacle_x[o] -= 10
        if obstacle_x[o] < -50:
            obstacle_x[o] = width * 3 + randint(-25, 25)
            obstacle_radius[o] = randint(40, 70)
            obstacle_y[o] = floor_y - obstacle_radius[o]
            if randint(1, 4) == 2:
                obstacle_y[o] = floor_y-70-obstacle_radius[o]


    for r in range(len(obstacle_radius)):
        if obstacle_x[r] < obstacle_x[closest_obstacle]:
            closest_obstacle = r
    closest_radius = obstacle_radius[closest_obstacle]


    if circle_collision(player_x, player_y, player_radius, min(obstacle_x), obstacle_y[closest_obstacle],
                        closest_radius):
        player_alive = False
    score += 1

    # Draw
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, white, (0, floor_y, width, 2))

    score_text = my_font.render('Score: ' + str(score), True, (50, 0, 0))
    high_score_text = my_font.render('Highscore: ' + str(high_score), True, (50, 0, 0))
    screen.blit(score_text, (0, 0))
    screen.blit(high_score_text, (0, 30))



    for o in range(3):
        draw_circle(screen, obstacle_x[o], obstacle_y[o], obstacle_radius[o], red)

    if player_alive:
        draw_circle(screen, player_x, player_y, player_radius, green)

    pg.display.flip()






    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            if int(high_score) < score:
                f = open('high_score.txt', 'w+')
                f.write(str(score * 69420))
                f.close()
                high_score = score
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and player_y == floor_y-player_radius:
                player_y_speed = -20



