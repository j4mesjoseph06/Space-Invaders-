def two():

    import pygame
    import sys
    import imp
    import os

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    #caption and icon
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load('spaceship.png')
    pygame.display.set_icon(icon)

    #defining the screen

    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

    #defining the bacground of the screen
    background = pygame.image.load('back.png')

    color = (0,0,0)
    color_light = (255,255,255)
    color_dark = (0,255,0)
    width = screen.get_width()
    height = screen.get_height()
    bigfont = pygame.font.Font('freesansbold.ttf',60)
    medium = pygame.font.Font('freesansbold.ttf',40)
    smallfont = pygame.font.Font('freesansbold.ttf',35)
    xsmallfont = pygame.font.Font('freesansbold.ttf',28)
    xxsmallfont = pygame.font.Font('freesansbold.ttf',18)

    play = smallfont.render('Play!' , True , color)
    quitb = smallfont.render('Quit' , True , color)
    controls = smallfont.render('Controls' , True , color)
    menu= bigfont.render('Menu' , True , color)

    textX = 10
    textY = 10

    def menu_text(x, y):
        intro = medium.render("Menu:", True, (255, 255, 255))
        screen.blit(intro, (width/2.25- 10 , height/2.4))

    def title_text(x, y):
        title = bigfont.render("!--SPACE RAIDER--!", True, (255, 255, 255))
        screen.blit(title, (width/5.7 - 40, height/6))

    def name(x, y):
        nameT = xsmallfont.render("By James Joseph", True, (255, 255, 255))
        screen.blit(nameT, (width/2.7 - 20, height/3.42))

    game_intro = True
    while game_intro:
        screen.blit(background,(0,0))
        title_text(textX, textY)
        menu_text(textX, textY)
        name(textX, textY)

        mouse = pygame.mouse.get_pos()
        if width/2-40 <= mouse[0] <= width/2+45 and height/2 <= mouse[1] <= height/2+43:
            pygame.draw.rect(screen,color_light,[width/2-40,height/2,86,43])
            screen.blit(play ,(width/2-40,height/2+3))
        else:
            pygame.draw.rect(screen,color_dark,[width/2-40,height/2,86,43])
            screen.blit(play ,(width/2-40,height/2+3))

        if width/2-70 <= mouse[0] <= width/2+90 and height/1.7 <= mouse[1] <= height/1.7+43:
            pygame.draw.rect(screen,color_light,[width/2-70,height/1.7,153,43])
            screen.blit(controls ,(width/2-70,height/1.7+3))
        else:
            pygame.draw.rect(screen,color_dark,[width/2-70,height/1.7,153,43])
            screen.blit(controls ,(width/2-70,height/1.7+3))

        if width/2-33 <= mouse[0] <= width/2+45 and height/1.48 <= mouse[1] <= height/1.48+43:
            pygame.draw.rect(screen,color_light,[width/2-33,height/1.48,78,43])
            screen.blit(quitb ,(width/2-33,height/1.48+3))
        else:
            pygame.draw.rect(screen,color_dark,[width/2-33,height/1.48,78,43])
            screen.blit(quitb ,(width/2-33,height/1.48+3))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2-40 <= mouse[0] <= width/2+45 and height/2 <= mouse[1] <= height/2+43:
                    from modes import mode_menu
                    mode_menu()
                if width/2-70 <= mouse[0] <= width/2+90 and height/1.7 <= mouse[1] <= height/1.7+43:
                    from control_menu import three
                    three()
                if width/2-33 <= mouse[0] <= width/2+45 and height/1.48 <= mouse[1] <= height/1.48+43:
                    pygame.quit()

        pygame.display.update()

two()
