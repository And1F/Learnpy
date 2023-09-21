import pygame
import time
import random
from sys import exit

operators = [" + ", " - ", " • ", " : "]

def decide_operator(op):
    return op[random.randint(0, 3)]

def get_numbers_for_01():
    return random.randint(5, 600)

def get_numbers_for_23():
    return random.randint(1, 50)

def get_numbers_for_3():
    return random.randint(1,20)
    
pygame.init()
pygame.display.set_caption("just_some_math")
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 60)
screen = pygame.display.set_mode((1280, 720))
mode = 0
running = True
clock = pygame.time.Clock()
ahead = False
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if ahead:
        if mode%2 == 0: 
            #calculating
            operator = decide_operator(operators)
            if operator == " + ":
                num_1 = get_numbers_for_01()
                num_2 = get_numbers_for_01()
                question = f"{num_1}{operator}{num_2}"
                solution = num_1 + num_2
            elif operator == " - ":
                num_1 = get_numbers_for_01()
                num_2 = get_numbers_for_01()
                question = f"{num_1}{operator}{num_2}"
                solution = num_1 - num_2
            elif operator == " • ":
                num_1 = get_numbers_for_23()
                num_2 = get_numbers_for_23()
                question = f"{num_1}{operator}{num_2}"
                solution = num_1 * num_2
            elif operator == " : ":
                num_1 = get_numbers_for_3()
                solution = get_numbers_for_23()
                num_2 = num_1 * solution
                question = f"{num_2}{operator}{num_1}"

            screen.fill("white")
            que = my_font.render(f"{question}", False, (0, 0, 0))
            screen.blit(que, (550,330))
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0] == True:
                time.sleep(0.5)
                mode +=1
                ahead = False

        elif mode%2 == 1: #solution
            screen.fill("white")
            sol = my_font.render(f"Die Lösung ist: {solution}", False, (0, 0, 0))
            screen.blit(sol, (400,330))
            pygame.display.flip()
            if pygame.mouse.get_pressed()[0] == True:
                time.sleep(0.5)
                mode +=1
                ahead = False
        
    else:
        if pygame.mouse.get_pressed()[0] == True:
            ahead = True

pygame.quit()


