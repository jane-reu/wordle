import pygame 
import sys
import random
from words import*

pygame.init()
WIDTH = 600
HEIGHT = 800

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (106,170,100)
YELLOW = (200,180,88)
GREY = (120,124,126)
OUT_LINE = (211,214,218)
FILLED =(135,138,140)

alphabet = ["QWERTYUIOP",
            "ASDFGHJKL"
            "ZXCVBNM"]

letter_size = 75

guesses_count = 0
guesses = [[]]*6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

game_result = ""

win = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND = pygame.image.load("sitka.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317,300))
pygame.display.set_caption("Wordle")
win.fill(WHITE)
win.blit(BACKGROUND,BACKGROUND_RECT)
pygame.display.update()

class Letter:
    def __init__(self,text,bg_position):
        self.bg_colour = WHITE
        self.text_colour = BLACK
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0],self.bg_y,letter_size,letter_size)
        self.text = text
        self.text_position = (self.bg_x+36,self.bg_position[1]+34)
        self.text.surface = guessed_letter_font.render(self.text,True,self.text_color)
        self.text.rect = self.text_surface.get_rect(center = self.text_position)
    
    def draw(self):
        pygame.draw.rect(win,self.bg_colour,self.bg_rect)
        if self.bg_colour == WHITE:
            pygame.draw.rect(win,FILLED,self.bd_rect,3)
        self.text_surface = guessed_letter_font.render(self.text,True,self.text_color)
        win.blit(self.text_surface,self.text_rect)
        pygame.display.update()

    def delete(self):
        pygame.draw.rect(win,WHITE,self.bg.rect)
        pygame.draw.rect(win,OUT_LINE,self.bg.rect,3)
        pygame.display.update()


game = True
while game:
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

