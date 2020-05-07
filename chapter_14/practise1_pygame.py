import pygame

def main():
    pygame.init()
    surface_size = 480

    main_surface = pygame.display.set_mode((surface_size, surface_size))
    ball = pygame.image.load("ball.png")

    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)

    my_font = pygame.font.SysFont("Courier", 16)        #font type and size
    the_text = my_font.render("Hello, world!", True, (0, 0, 0)) #text and text colour 000=black


    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        main_surface.fill((0, 200, 255)) #background colour
        main_surface.fill(some_color, small_rect) #insert reactangle
        main_surface.blit(ball, (50, 50)) #insert ball .png
        main_surface.blit(the_text, (10, 10)) #insert text

        pygame.display.flip() #display text

    pygame.quit()

main()