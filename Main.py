import pygame
from Buttons import alpha
from Buttons import alphabets
from sprites import *
from Buttons import *
from words import words
import random

pygame.init()

#Ppygame event handler variables
WIDTH = 510
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman by Ace")
clock = pygame.time.Clock()

def valid(words):
    guest = random.choice(words)
    while '-' and ' ' in guest:
        guest  = random.choice(words)
    return guest

def draw_restart():
    global lives
    img = pygame.image.load("hangmanonpygame/restart.png")
    img1 = Button(380,50,img)
    if img1.draw(screen):
        restart()
    
def win():
    win = font.render("YOU WIN", False, ("#000000"))
    screen.blit(win, (WIDTH / 2 - win.get_width() / 2, 350))

    answer = "The word is " + guest + "!"
    winner = font2.render(answer.upper(), False, ("#000000"))

    x_pos = WIDTH / 2 - winner.get_width() / 2 
    y_pos = 400

    screen.blit(winner, (x_pos, y_pos))

def lose():
    lose = font.render("You Lose!", False, ("#000000"))
    screen.blit(lose, (WIDTH / 2 - lose.get_width() / 2 , 350))

    answer = "The word is " + guest + "!"
    loser = font2.render(answer.upper(), False, ("#000000"))

    x_pos =  WIDTH / 2 - loser.get_width() / 2 
    y_pos = 400

    screen.blit(loser, (x_pos, y_pos))

def already():
    font1 = pygame.font.Font(None,30)
    redunt = font1.render("Already been type!!", False, ("#000000"))    
    screen.blit(redunt,(150,10))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(500)

def restart():
    global guess,lives,guesses,guest,step
    guess = ""
    lives = 6
    guesses = ""
    guest = valid(words).upper()
    step = 0

def draw_game():
    global font,guess,lives,guesses,lives,font2

    #Draw hangman sprites
    blit_char()

    #Draw restart Button
    draw_restart()

    #Draw letters in screen
    if lives > 0:
        #Draw text in screen
        word_list = [i if i in guess else "-" for i in guest]
        font2 = pygame.font.Font(None,30)
        text = font2.render("Word: "+ " ".join(word_list), False, ("#000000"))    

        if "-" in word_list:
            #Draw History
            history = font2.render("History: " +" ".join(guesses), False, ("#000000"))
            screen.blit(history,(10,20))

            #Draw lives
            heart = font2.render(f"Lives left: {str(lives)}", False, ("#000000"))
            screen.blit(heart,(350,320))

            #Draw dashes to reveal
            screen.blit(text, (10, 320))  

            #Draw Buttons and theirs clicks
            for i in range(26):
                if alphabets[i] in guesses:
                    alpha_1[i].draw(screen)
                elif alpha[i].draw(screen):
                    if alphabets[i]not in guess:
                        if alphabets[i] in guest:
                            guess += alphabets[i]   # if the letter was in the guessing word
                            guesses += alphabets[i] # For histoy of clicked
                        else:
                            guess += alphabets[i]   # if the letter was in the guessing word
                            guesses += alphabets[i] # For histoy of clicked                             
                            lives -=1                                         
        else:
            win()
            draw_restart()
    else:
        lose()
        draw_restart()
                           
def blit_char():
    global step
    if lives == 6:        
        screen.blit(one,(110,30))
    elif lives == 5:
        screen.blit(two,(110,30))
    elif lives == 4:
        screen.blit(three,(110,30))
    elif lives == 3:
        screen.blit(four,(110,30))
    elif lives == 2:
        screen.blit(five,(110,30))    
    elif lives == 1:
        screen.blit(six,(110,30))
    elif lives == 0:
        screen.blit(seven[step],(110,30))
        step +=1
        if step == 44:
            step = 0

# WORD TO GUESS
font = pygame.font.Font(None, 50)
guess = ""
lives = 6
guesses = ""
guest = valid(words).upper()
step = 0

run = True
while run:
    #FPS CHECK
    clock.tick(30)
    
    #Draw Background
    screen.fill(("#31474c"))

    #Draw main window in screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_game()

    pygame.display.update()

pygame.quit()
