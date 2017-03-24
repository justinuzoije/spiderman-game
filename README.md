# Spider Man Game

This is a top-down game where you move the character around the map in order to fight
the villain of stage. When you encounter the enemy, it goes to the battle screen where you
fight them.

This game was built using Python and uses Pygame in order to use keyboard input, and screen refreshing.

## Installing

To get the game running, download the files and run the spiderman python file.

## Screenshots

Level map
![Level Map](https://github.com/justinuzoije/spiderman-game/blob/master/images/rhino_background.png)

Fight screen
![Fight Screen](https://github.com/justinuzoije/spiderman-game/blob/master/images/fight_screen_readme.png)

### Code Examples

This is the function that creates the level map that the player is walking around.


```
    #Screen
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()

    #Music
    pygame.mixer.init()
    pygame.mixer.music.load('Spiderman.ogg')
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/rhino_background.png').convert_alpha()
    monster = pygame.image.load('images/rhino.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    change_dir_countdown = 120

    # Game initialization

    monster = Rhino(50,50)
    ball = Ball(256,240)


    stop_game = False
    change_dir_counter = 0       # original change_dir_count

```


## Authors

* **Justin Uzoije** - *Initial work* - [PurpleBooth](https://github.com/justinuzoije)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Marvel Comics
