import pygame
import random
import time

KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_LEFT = 276

KEY_A = 97

#DEBUG
def main2():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Simple Example')
    clock = pygame.time.Clock()

    # Game initialization
    #font = pygame.font.SysFont("comicsansms", 72)
    #text = font.render("Hello, World", True, (255, 255, 255))
    orc_image = pygame.image.load('images/orc.png').convert_alpha()
    hero_image = pygame.image.load('images/big_hero.png').convert_alpha()


    #RPG Data
    hero_health = 30
    hero_damage = 4

    orc_health = 20
    orc_damage = 2

    hero_message = ""
    orc_message = ""
    health_message = "HP: %s/30" % hero_health

    stop_game = False
    while not stop_game and orc_health > 0 and hero_health > 0:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    print "Invalid Input"
                elif event.key == KEY_A:
                    hero_damage = random.randrange(1,6)
                    orc_damage = random.randrange(1,4)
                    hero_message = "You attack orc for %d damage!" % hero_damage
                    orc_message = "Orc attacks you for %d damage!" % orc_damage
                    orc_health -= hero_damage
                    hero_health -= orc_damage
                    health_message = "HP: %s/30" %str(hero_health)
                elif event.key == KEY_LEFT:
                    print "Invalid input"
                elif event.key == KEY_RIGHT:
                    print "Invalid input"
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        screen.fill(blue_color)

        # Game display

        screen.blit(orc_image, (0, 0))

        #200, 200, 100, 100
        pygame.draw.rect(screen, (0, 0, 0), (0, 400, 500, 100), 0)
        font = pygame.font.Font(None, 25)
        text = font.render('You have encountered an orc!', True, (255, 255, 255))
        #attack_text = font.render("Press UP to attack", True, (255, 255, 255))
        hero_attack_text = font.render(hero_message, True, (255, 255, 255))
        orc_attack_text = font.render(orc_message, True, (255, 0, 0))
        health_text = font.render(health_message, True, (255, 255, 255))
        screen.blit(text, (0, 400))
        #screen.blit(attack_text, (0, 450))
        screen.blit(hero_attack_text, (0, 440))
        screen.blit(orc_attack_text, (0, 460))
        screen.blit(health_text, (400, 400))
        pygame.display.update()

        clock.tick(60)

    if orc_health > 0:
        print "You died."
        print "You Lose!"
    elif hero_health > 0:
        print "Orc died."
        print "You Win!"

    pygame.quit()

class Character(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.x_dir = 1
        self.y_dir = 1
        self.image = image
        self.alive = True



    def displayCharacter(self,screen):
        if self.alive == True:
            screen.blit(self.image, (self.x,self.y))
        else:
            print "dead"

    def move_character(self):
        self.x += self.x_dir
        self.y += self.y_dir

    # def collision_detection(self):
    #     #(ax, ay), (bx, by), if any one of the following are true,
    #     #then they are not overlapping:
    #      #ax + 32 < bx
    #      #bx + 32 < ax
    #      #ay + 32 < by
    #      #by + 32 < ay
    #      #otherwise they collide
    #
    #      if hero.x + 32 < monster.x:
    #          print "No Collision"
    #      elif monster.x + 32 < hero.x:
    #          print "No Collision"
    #      elif hero.y + 32 < monster.y:
    #          print "No Collision"
    #      elif monster.y + 32 < hero.y:
    #          print "No Collision"
    #      else:
    #          print "Collision!"

    def change_direction(self):

        rand_direction = random.randint(0,7)


        if rand_direction == 0:   # top or north
            self.x_dir = 0
            self.y_dir = -1

        elif rand_direction == 1:  #right or east
            self.x_dir = 1
            self.y_dir = 0

        elif rand_direction == 2:  #down or south
            self.x_dir =0
            self.y_dir = 1

        elif rand_direction == 3:  #left or west
            self.x_dir =-1
            self.y_dir = 0

        elif rand_direction == 4:   # Northeast - topright
            self.x_dir = 1
            self.y_dir = -1

        elif rand_direction == 5:  # Northwest - top left
            self.x_dir = -1
            self.y_dir = -1

        elif rand_direction == 6:  # Southwest - bottom left
            self.x_dir = -1
            self.y_dir = 1

        elif rand_direction == 7:  # South east - bottom right
            self.x_dir = 1
            self.y_dir = 1

    def off_screen(self):
        if self.y < 0:      #top
            self.y =  480
        else:
            self.y -= 5

        if self.x > 512:    #right
            self.x = 0
        else:
            self.x += 5

        if self.y > 480:     #down
            self.y =  0
        else:
            self.y += 5

        if self.x < 0:       #left
            self.x =  512
        else:
            self.x -= 5



class Monster(Character):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/monster.png').convert_alpha()
        self.x = x
        self.y = y
        self.x_dir = 2
        self.y_dir = 0
        self.alive = True

#Transforming to Ball
class Ball(Character):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/hero.png').convert_alpha()
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.alive = True

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def off_screen(self):
        if self.y < 31:      #top
            self.y = 31

        if self.x > 450:    #right
            self.x = 450

        if self.y > 418:     #down
            self.y =  418

        if self.x < 31:       #left
            self.x =  31





def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/background.png').convert_alpha()
    monster = pygame.image.load('images/monster.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    change_dir_countdown = 120

    # Game initialization

    monster = Monster(50,50)
    ball = Ball(256,240)


    stop_game = False
    change_dir_counter = 0       # original change_dir_count
    while not stop_game:
        for event in pygame.event.get():

# this is for controlling the hero with the keyboard, declared keys at
#the top of the page, and set controls in the pygame.event.get()

            #To control normally
            # if event.type == pygame.KEYDOWN:
            #     if event.key == KEY_DOWN:
            #         hero.y += 5
            #     elif event.key == KEY_UP:
            #         hero.y -= 5
            #     elif event.key == KEY_LEFT:
            #         hero.x -= 5
            #     elif event.key == KEY_RIGHT:
            #         hero.x += 5

            #Ball Smooth keys
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    ball.speed_y = 5
                elif event.key == KEY_UP:
                    ball.speed_y = -5
                elif event.key == KEY_LEFT:
                    ball.speed_x = -5
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    ball.speed_y = 0
                elif event.key == KEY_UP:
                    ball.speed_y = 0
                elif event.key == KEY_LEFT:
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0


# smooth key not working, fix later
            # if event.type == pygame.KEYUP:
            #     # deactivate the cooresponding speeds
            #     # when an arrow key is released
            #     if event.key == KEY_DOWN:
            #         hero.y_dir = 0
            #     elif event.key == KEY_UP:
            #         hero.y_dir = 0
            #     elif event.key == KEY_LEFT:
            #         hero.x_dir = 0
            #     elif event.key == KEY_RIGHT:
            #         hero.x_dir = 0

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        # Game logic

        monster.move_character()    #moves monster around

# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1
        if change_dir_counter == 120:
            monster.change_direction()   # changes monster direction
            change_dir_counter = 0

        monster.off_screen()             #keeps monster on screen
        ball.off_screen()                #keeps hero inside screen


        #Colission Detection
        if ball.x + 32 < monster.x:
            pass
            # print "No Collision"
        elif monster.x + 32 < ball.x:
            pass
            # print "No Collision"
        elif ball.y + 32 < monster.y:
            pass
            # print "No Collision"
        elif monster.y + 32 < ball.y:
            pass
            # print "No Collision"
        else:
            #print "Collision!"
            monster.alive = False
            main2()
            break



        # Game logic
        ball.update()

        screen.fill(blue_color)

        screen.blit(background_image, (0,0))
        # screen.blit(monster, (monster.x,monster.y))
        monster.displayCharacter(screen)
        ball.displayCharacter(screen)
        #screen.blit(monster, (x_dir,y_dir))
        # screen.blit(hero, (256,240))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
