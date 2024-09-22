import pygame
from random import randint
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("KEO * BUA * BAO")
icon = pygame.image.load("icon.jpg")
bua = pygame.image.load("bua.jpg")
keo = pygame.image.load("keo.jpg")
bao = pygame.image.load("bao.jpg")
pygame.display.set_icon(icon)

#color 
GREY = (179, 179, 179)
BLACK = (0, 0, 0)
GREEN = (64, 191, 64)
WHITE = (255, 255, 255)
YELLOW = (230, 230, 0)
BLUE = (0, 153, 255)
RED = (255, 0, 0)

#variable
#run
runing = True
run_wel = True
run_heaven = False
run_hell = False
#player_choice
choice_keo = False
choice_bua = False
choice_bao = False
start_game = False
end_game = False
#robot
robot_start = False
#is_battle
is_Win = False
is_Draw = False
is_Loss = False
#score
count_win = 0
count_draw = 0
count_loss = 0
clock = pygame.time.Clock()

#music
sound_wel = pygame.mixer.Sound('welcome.wav')
sound_bat = pygame.mixer.Sound("ghequa.wav")
sound_end = pygame.mixer.Sound("end.wav")
#text
font = pygame.font.SysFont('sans', 30)
#welcome
text_1 = font.render("HEAVEN OR HELL", True, GREEN)
text_2 = font.render("HEAVEN", True, BLUE)
text_3 = font.render("HELL", True, RED)
#hell
text_4 = font.render("YOU STOPPED GAME", True, GREEN)
#heaven
text_8 = font.render("BATTLE", True, RED)
text_9 = font.render("YOU", True, GREEN)
text_10 = font.render("ROBOT", True, BLACK)
text_11 = font.render("KEO", True, GREEN)
text_12 = font.render("BUA", True, GREEN)
text_13 = font.render("BAO", True, GREEN)
text_14 = font.render("START", True, RED)
text_19 = font.render("END", True, BLACK)
#result
text_15 = font.render("WIN", True, BLACK)
text_16 = font.render("DRAW", True, BLUE)
text_17 = font.render("LOSS", True, RED)

print("Chao mung ban den voi binh nguyen vo tan - KEO BUA BAO")
print("Day la tro choi đuoc phat trien boi tu than Pham Anh Kiet")
pygame.mixer.Sound.play(sound_wel)

while runing:
    clock.tick(60)
    screen.fill(GREY)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(icon, (550, 0))
    
# draw full
    #draw welcome
    if run_wel:
        pygame.draw.rect(screen, BLACK, (50, 50, 500, 50))
        pygame.draw.rect(screen, WHITE, (50, 200, 150, 50))
        pygame.draw.rect(screen, BLACK, (400, 200, 150, 50))
        pygame.draw.circle(screen, BLACK, (300, 450), 100)
        pygame.draw.circle(screen, WHITE, (300, 450), 95)
        # write text
        screen.blit(text_1, (180, 61))
        screen.blit(text_2, (67, 213))
        screen.blit(text_3, (442, 213))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (50 < mouse_x < 200) and (200 < mouse_y < 250):
                    pygame.mixer.Sound.stop(sound_wel)
                    run_wel = False
                    run_heaven = True
                    pygame.mixer.Sound.play(sound_bat)

                elif (400 < mouse_x < 550) and (200 < mouse_y < 250):
                    pygame.mixer.Sound.stop(sound_wel)
                    run_wel = False
                    run_hell = True
                    pygame.mixer.Sound.play(sound_end)
                
                if run_heaven:
                    if (60 < mouse_x < 180) and (540 < mouse_y < 590):
                        choice_keo = True
                        player_decision = "KEO"
                    elif (240 < mouse_x < 360) and (540 < mouse_y < 590):
                        choice_bua = True
                        player_decision = "BUA"
                    elif (420 < mouse_x < 540) and (540 < mouse_y < 590):
                        choice_bao = True
                        player_decision = "BAO"
                    if (120 < mouse_x < 270) and (630 < mouse_y < 680):
                        start_game = True
                        robot_start = True
                        end_game = False
                    elif (330 < mouse_x < 480) and (630 < mouse_y < 680):
                        pygame.mixer.Sound.stop(sound_bat)
                        run_wel = True
                        run_heaven = False
                        end_game =  True
                        choice_bao = choice_keo = choice_bua = False
                        robot_choice = 0
                        if end_game:
                            if is_Win:
                                count_win += 1
                            elif is_Draw:
                                count_draw += 1
                            elif is_Loss:
                                count_loss += 1
                            is_Win = is_Draw = is_Loss = False 
                        pygame.mixer.Sound.play(sound_wel)

    #draw heaven
    if run_heaven:
        pygame.draw.circle(screen, BLACK, (300, 150), 100)
        pygame.draw.circle(screen, WHITE, (300, 150), 95)
        pygame.draw.rect(screen, WHITE, (50, 300, 150, 50))
        pygame.draw.rect(screen, WHITE, (400, 300, 150, 50))
        pygame.draw.circle(screen, WHITE, (125, 440), 75)
        pygame.draw.circle(screen, BLACK, (125, 440), 70)
        pygame.draw.circle(screen, WHITE, (475 ,440), 75)
        pygame.draw.circle(screen, BLACK, (475, 440), 70)
        pygame.draw.rect(screen, BLACK, (60, 540, 120, 50))
        pygame.draw.rect(screen, BLACK, (240, 540, 120, 50))
        pygame.draw.rect(screen, BLACK, (420, 540, 120, 50))
        pygame.draw.rect(screen, BLACK, (120, 630, 150, 50))
        pygame.draw.rect(screen, WHITE, (330, 630, 150, 50))

        #write text
        screen.blit(text_8, (245, 139))
        screen.blit(text_9, (93, 312))
        screen.blit(text_10, (423, 312))
        screen.blit(text_11, (90, 552))
        screen.blit(text_12, (270, 552))
        screen.blit(text_13, (450, 552))
        screen.blit(text_14, (148, 643))
        screen.blit(text_19, (377, 643))

        if choice_keo:
            screen.blit(keo, (90,404))
            #screen.blit(text_11, (95, 427))
        elif choice_bua:
            screen.blit(bua, (90,406))
            #screen.blit(text_12, (95, 427))
        elif choice_bao:
            screen.blit(bao, (90,406))
            #screen.blit(text_13, (95, 427))
        if end_game:
            pygame.draw.circle(screen, WHITE, (300, 150), 95)
            screen.blit(text_8, (245, 139))
            pygame.draw.circle(screen, BLACK, (125, 440), 70)
            pygame.draw.circle(screen, WHITE, (475, 440), 70)
            end_game = False
            
        if start_game:
            pygame.draw.circle(screen, WHITE, (300, 150), 95)
            screen.blit(text_8, (245, 139))
            if robot_start:
                robot_choice = randint(1,3)
                robot_start = False
            if robot_choice == 1:
                robot_decision = "KEO"
                screen.blit(keo, (440,404))
            elif robot_choice == 2:
                robot_decision = "BUA"
                screen.blit(bua, (440,406))
            elif robot_choice == 3:
                robot_decision = "BAO"
                screen.blit(bao, (440,406))
            else:
                robot_decision = "NO"
            if player_decision == robot_decision:
                pygame.draw.circle(screen, WHITE, (300, 150), 95)
                screen.blit(text_16, (257, 139))
                is_Draw = True
            elif (player_decision == "KEO" and robot_decision == "BAO") or (player_decision == "BUA" and robot_decision == "KEO") or (player_decision == "BAO" and robot_decision == "BUA"):
                pygame.draw.circle(screen, WHITE, (300, 150), 95)
                screen.blit(text_15, (270, 139))
                is_Win = True
            elif (robot_decision == "KEO" and player_decision == "BAO") or (robot_decision == "BUA" and player_decision == "KEO") or (robot_decision == "BAO" and player_decision == "BUA"):
                pygame.draw.circle(screen, WHITE, (300, 150), 95)
                screen.blit(text_17, (260, 139))
                is_Loss = True

    #draw hell
    if run_hell:
        pygame.draw.rect(screen, BLACK, (50, 50, 500, 50))
        pygame.draw.rect(screen, BLACK, (230, 150, 140, 50))
        pygame.draw.rect(screen, BLACK, (230, 250, 140, 50))
        pygame.draw.rect(screen, BLACK, (230, 350, 140, 50))
        # icon
        pygame.draw.circle(screen, YELLOW, (300, 550), 100)
        pygame.draw.circle(screen, WHITE, (245, 510), 30)
        pygame.draw.circle(screen, WHITE, (315, 510), 30)
        pygame.draw.circle(screen, BLACK, (235, 510), 20)
        pygame.draw.circle(screen, BLACK, (305, 510), 20)
        pygame.draw.circle(screen, WHITE, (275, 590), 30)
        pygame.draw.rect(screen, YELLOW, (245, 560, 60, 30))
        #text
        text_5 = font.render("WIN: " + str(count_win), True, RED)
        text_6 = font.render("DRAW: " + str(count_draw), True, GREEN)
        text_7 = font.render("LOSS: " + str(count_loss), True, WHITE)
        #write text
        screen.blit(text_4, (145, 62))
        screen.blit(text_5, (258, 162))
        screen.blit(text_6, (241, 263))
        screen.blit(text_7, (245, 361))

    pygame.display.flip()
pygame.quit()

        
    

    