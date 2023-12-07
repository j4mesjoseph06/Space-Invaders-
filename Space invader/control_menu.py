def three():

    import pygame
    import random
    import math
    import sys
    import imp
    import os
    from menu import two

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    #caption and icon
    pygame.display.set_caption("Space Invader")
    current_path = os.path.dirname(r"C:\Users\Milan\OneDrive\Documents\coding\python\games\Space invader") # Where your .py file is located
    resource_path = os.path.join(current_path, r"C:\Users\Milan\OneDrive\Documents\coding\python\games\Space invader") # The resource folder path
    image_path = os.path.join(resource_path, r"C:\Users\Milan\OneDrive\Documents\coding\python\games\Space invader") # The image folder path


    #defining the screen
    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

    #defining the bacground of the screen
    background = pygame.image.load('back.png')

    width = screen.get_width()
    height = screen.get_height()

    color = (255,255,255)
    blue = (0, 0, 255)
    color_dark = (0,255,0)
    medium = pygame.font.Font('freesansbold.ttf',40)
    smallfont = pygame.font.Font('freesansbold.ttf',30)
    font = pygame.font.Font('freesansbold.ttf',25)
    xsmallfont = pygame.font.Font('freesansbold.ttf',20)

    back_to_menu = smallfont.render('Back to Menu' , True , ((0, 0, 0)))

    textX = 10
    textY = 10


    def control_text(x, y):
        intro = medium.render("Controls:", True, color)
        screen.blit(intro, (45, 40))

    def player1(x, y):
        first = smallfont.render("1 Player Mode: - - - - - - - - - - - - - - -", True, color)
        screen.blit(first, (45, 100))

    def play1_con(x, y):
        right = xsmallfont.render("Move Right:                             D", True, blue)
        screen.blit(right, (45, 140))
        left = xsmallfont.render ("Move Left:                               A", True, blue)
        screen.blit(left, (45, 170))
        shoot = xsmallfont.render("Shoot:                                      Left M.Click", True, blue)
        screen.blit(shoot, (45, 200))


    def player2(x, y):
        second = smallfont.render("2 Player Mode(s): - - - - - - - - - - - - -", True, color)
        screen.blit(second, (45, 250))


    def play2_con(x, y):
        Player_1 = font.render("Player 1:  ", True, color)
        screen.blit(Player_1, (45, 290))
        right1 = xsmallfont.render("Move Right:                             D", True, blue)
        screen.blit(right1, (45, 320))
        left1 = xsmallfont.render ("Move Left:                               A", True, blue)
        screen.blit(left1, (45, 350))
        shoot1 = xsmallfont.render("Shoot:                                      Space Bar", True, blue)
        screen.blit(shoot1, (45, 380))
        Player_2 = font.render("Player 2:  ", True, color)
        screen.blit(Player_2, (45, 420))
        right2 = xsmallfont.render("Move Right:                             Arrow Key ", True, blue)
        screen.blit(right2, (45, 450))
        left2 = xsmallfont.render ("Move Left:                               Arrow Key", True, blue)
        screen.blit(left2, (45, 480))
        shoot2 = xsmallfont.render("Shoot:                                      Left M.Click", True, blue)
        screen.blit(shoot2, (45, 510))

    control_screen = True
    while control_screen:
        screen.fill((0,0,0))
        pygame.draw.rect(screen,color,(332, 135, 150, 90))
        pygame.draw.rect(screen,color,(332, 314, 150, 90))
        pygame.draw.rect(screen,color,(332, 446, 150, 90))
        control_text(textX, textY)
        player1(textX, textY)
        player2(textX, textY)
        play1_con(textX, textY)
        play2_con(textX, textY)

        mouse = pygame.mouse.get_pos()
        if 560 <= mouse[0] <= 790 and 40 <= mouse[1] <= 40 + 34:
            pygame.draw.rect(screen,color,(560,40,210,34))
            screen.blit(back_to_menu ,(560 + 5, 40 + 3, 210, 34))
        else:
            pygame.draw.rect(screen,color_dark,(560,40,210,34))
            screen.blit(back_to_menu ,(560 + 5, 40 + 3, 210, 34))

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 560 <= mouse[0] <= 790 and 40 <= mouse[1] <= 40 + 34:
                    two()
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

three()








