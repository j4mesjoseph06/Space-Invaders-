def mode_menu():

    import pygame
    import sys
    import imp
    import os
    from menu import two

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

    width = screen.get_width()
    height = screen.get_height()

    white = (255,255,255)
    black = (0, 0, 0)
    grey = (0,255,0)
    bigfont = pygame.font.Font('freesansbold.ttf',50)
    medium = pygame.font.Font('freesansbold.ttf',38)
    smallfont = pygame.font.Font('freesansbold.ttf',30)

    back_to_menu = medium.render('Back to Menu' , True , (black))
    Normal = medium.render('Normal' , True , (black))
    Hard = medium.render('Hard' , True , (black))
    God = medium.render('God Tier' , True , (black))

    textX = 10
    textY = 10

    def select(x, y):
        mode = bigfont.render("Select Mode:", True, white)
        screen.blit(mode, (252, 130))

    def normal():
        import invader_norm
        imp.reload(invader_norm)

    def hard():
        import invader_hard
        imp.reload(invader_hard)

    def god():
        import invader_god
        imp.reload(invader_god)

    game_intro = True
    while game_intro:
        screen.blit(background,(0,0))
        select(textX, textY)

        mouse = pygame.mouse.get_pos()

        #play game in Normal mode
        if 350 <= mouse[0] <= 495 and 213 <= mouse[1] <= 213 + 40:
            pygame.draw.rect(screen,white,(350,213,145,40))
            screen.blit(Normal ,(350 + 5, 213 + 3, 145, 40))
        else:
            pygame.draw.rect(screen,grey,(350,213,145,40))
            screen.blit(Normal ,(350 + 5, 213 + 3, 145, 40))

        #Play game in Hard mode
        if 375 <= mouse[0] <= 480 and 279 <= mouse[1] <= 279 + 40:
            pygame.draw.rect(screen,white,(375,279,105,40))
            screen.blit(Hard ,(375 + 5, 279 + 3, 105, 40))
        else:
            pygame.draw.rect(screen,grey,(375,279,105,40))
            screen.blit(Hard ,(375 + 5, 279 + 3, 105, 40))

        #Play game in God Tier mode
        if 340 <= mouse[0] <= 515 and 345 <= mouse[1] <= 345 + 40:
            pygame.draw.rect(screen,white,(340,345,175,40))
            screen.blit(God ,(340 + 5, 345 + 3, 175, 40))
        else:
            pygame.draw.rect(screen,grey,(340,345,175,40))
            screen.blit(God ,(340 + 5, 345 + 3, 175, 40))

        #back to menu
        if 295 <= mouse[0] <= 557 and 411 <= mouse[1] <= 411 + 40:
            pygame.draw.rect(screen,white,(295,411,263,40))
            screen.blit(back_to_menu ,(295 + 5, 411 + 3, 210, 40))
        else:
            pygame.draw.rect(screen,grey,(295,411,263,40))
            screen.blit(back_to_menu ,(295 + 5, 411 + 3, 210, 40))

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= mouse[0] <= 495 and 213 <= mouse[1] <= 213 + 40:
                    normal()
                if 375 <= mouse[0] <= 480 and 279 <= mouse[1] <= 279 + 40:
                    hard()
                if 340 <= mouse[0] <= 515 and 345 <= mouse[1] <= 345 + 40:
                    god()
                if 295 <= mouse[0] <= 557 and 411 <= mouse[1] <= 411 + 40:
                    two()

            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

mode_menu()
