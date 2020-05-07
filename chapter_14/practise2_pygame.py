import pygame
import time

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((480,240))

    ball = pygame.image.load("ball.png")
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.perf_counter()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.perf_counter()
            frame_rate = 500 / (t1-t0)

        main_surface.fill((0, 200, 255))
        main_surface.fill((255, 0, 0), (300, 100, 150, 90))
        main_surface.blit(ball, (100, 120))
        the_text = my_font.render("Frame = {0}, rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0,0,0))
        main_surface.blit(the_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

main()