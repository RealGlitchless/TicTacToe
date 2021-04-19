import sys
import pygame
import os
from PIL import Image
import ctypes

pygame.init()

size = width, height = 600, 600
grey = (16, 16, 16)
white = (220, 220, 220)
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
screen.fill(white)
pygame.display.set_caption("Tic Tac Toe")
root = os.path.dirname(sys.modules["__main__"].__file__)


def isWinner(value):
    return ((box1Value == value and box2Value == value and box3Value == value) or
            (box4Value == value and box5Value == value and box6Value == value) or
            (box7Value == value and box8Value == value and box9Value == value) or
            (box1Value == value and box4Value == value and box7Value == value) or
            (box2Value == value and box5Value == value and box8Value == value) or
            (box3Value == value and box6Value == value and box9Value == value) or
            (box1Value == value and box5Value == value and box9Value == value) or
            (box3Value == value and box5Value == value and box7Value == value))


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def O_symbol():
    symbol = Image.open(root + f"\\O.png")
    symbol_width = 140
    symbol_height = 140
    symbol = symbol.resize((symbol_height, symbol_width))
    symbol.save(f"O.png")
    symbol = pygame.image.load(f"O.png")
    return symbol


def X_symbol():
    symbol = Image.open(root + f"\\X.png")
    symbol_width = 140
    symbol_height = 140
    symbol = symbol.resize((symbol_height, symbol_width))
    symbol.save(f"X.png")
    symbol = pygame.image.load(f"X.png")
    return symbol


def drawLines():
    fl_x, fl_y = (200, 0), (200, 600)
    pygame.draw.line(screen, grey, fl_x, fl_y, 20)
    fl_x, fl_y = (400, 0), (400, 600)
    pygame.draw.line(screen, grey, fl_x, fl_y, 20)
    fl_x, fl_y = (0, 200), (600, 200)
    pygame.draw.line(screen, grey, fl_x, fl_y, 20)
    fl_x, fl_y = (0, 400), (600, 400)
    pygame.draw.line(screen, grey, fl_x, fl_y, 20)


box1 = pygame.Surface((190, 190), pygame.SRCALPHA)
box1.set_alpha(128)
box1.fill(white)
box1 = screen.blit(box1, (0, 0))
box1Value = 0
box1_NotOccupied = True

box2 = pygame.Surface((180, 190), pygame.SRCALPHA)
box2.set_alpha(128)
box2.fill(white)
box2 = screen.blit(box2, (210, 0))
box2Value = 0
box2_NotOccupied = True

box3 = pygame.Surface((190, 190), pygame.SRCALPHA)
box3.set_alpha(128)
box3.fill(white)
box3 = screen.blit(box3, (410, 0))
box3Value = 0
box3_NotOccupied = True

box4 = pygame.Surface((190, 180), pygame.SRCALPHA)
box4.set_alpha(128)
box4.fill(white)
box4 = screen.blit(box4, (0, 210))
box4Value = 0
box4_NotOccupied = True

box5 = pygame.Surface((180, 180), pygame.SRCALPHA)
box5.set_alpha(128)
box5.fill(white)
box5 = screen.blit(box5, (210, 210))
box5Value = 0
box5_NotOccupied = True

box6 = pygame.Surface((200, 180), pygame.SRCALPHA)
box6.set_alpha(128)
box6.fill(white)
box6 = screen.blit(box6, (410, 210))
box6Value = 0
box6_NotOccupied = True

box7 = pygame.Surface((190, 190), pygame.SRCALPHA)
box7.set_alpha(128)
box7.fill(white)
box7 = screen.blit(box7, (0, 410))
box7Value = 0
box7_NotOccupied = True

box8 = pygame.Surface((180, 190), pygame.SRCALPHA)
box8.set_alpha(128)
box8.fill(white)
box8 = screen.blit(box8, (210, 410))
box8Value = 0
box8_NotOccupied = True

box9 = pygame.Surface((190, 200), pygame.SRCALPHA)
box9.set_alpha(128)
box9.fill(white)
box9 = screen.blit(box9, (410, 410))
box9Value = 0
box9_NotOccupied = True

O = O_symbol()
X = X_symbol()
drawLines()
pygame.display.update()

noWinner = True
counter = 2
while noWinner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (counter % 2) == 0:
                cursorpos = pygame.mouse.get_pos()
                if box1.collidepoint(cursorpos):
                    if box1_NotOccupied:
                        screen.blit(X, (25, 25))
                        pygame.display.update()
                        box1_NotOccupied = False
                        box1Value = 1
                        counter += 1

                if box2.collidepoint(cursorpos):
                    if box2_NotOccupied:
                        screen.blit(X, (240, 25))
                        pygame.display.update()
                        box2_NotOccupied = False
                        box2Value = 1
                        counter += 1

                if box3.collidepoint(cursorpos):
                    if box3_NotOccupied:
                        screen.blit(X, (420, 25))
                        pygame.display.update()
                        box3_NotOccupied = False
                        box3Value = 1
                        counter += 1

                if box4.collidepoint(cursorpos):
                    if box4_NotOccupied:
                        screen.blit(X, (25, 225))
                        pygame.display.update()
                        box4_NotOccupied = False
                        box4Value = 1
                        counter += 1

                if box5.collidepoint(cursorpos):
                    if box5_NotOccupied:
                        screen.blit(X, (240, 225))
                        pygame.display.update()
                        box5_NotOccupied = False
                        box5Value = 1
                        counter += 1

                if box6.collidepoint(cursorpos):
                    if box6_NotOccupied:
                        screen.blit(X, (440, 225))
                        pygame.display.update()
                        box6_NotOccupied = False
                        box6Value = 1
                        counter += 1

                if box7.collidepoint(cursorpos):
                    if box7_NotOccupied:
                        screen.blit(X, (25, 425))
                        pygame.display.update()
                        box7_NotOccupied = False
                        box7Value = 1
                        counter += 1

                if box8.collidepoint(cursorpos):
                    if box8_NotOccupied:
                        screen.blit(X, (240, 425))
                        pygame.display.update()
                        box8_NotOccupied = False
                        box8Value = 1
                        counter += 1

                if box9.collidepoint(cursorpos):
                    if box9_NotOccupied:
                        screen.blit(X, (440, 425))
                        pygame.display.update()
                        box9_NotOccupied = False
                        box9Value = 1
                        counter += 1

            else:
                cursorpos = pygame.mouse.get_pos()
                if box1.collidepoint(cursorpos):
                    if box1_NotOccupied:
                        screen.blit(O, (25, 25))
                        pygame.display.update()
                        box1_NotOccupied = False
                        box1Value = 2
                        counter += 1

                if box2.collidepoint(cursorpos):
                    if box2_NotOccupied:
                        screen.blit(O, (240, 25))
                        pygame.display.update()
                        box2_NotOccupied = False
                        box2Value = 2
                        counter += 1

                if box3.collidepoint(cursorpos):
                    if box3_NotOccupied:
                        screen.blit(O, (440, 25))
                        pygame.display.update()
                        box3_NotOccupied = False
                        box3Value = 2
                        counter += 1

                if box4.collidepoint(cursorpos):
                    if box4_NotOccupied:
                        screen.blit(O, (25, 225))
                        pygame.display.update()
                        box4_NotOccupied = False
                        box4Value = 2
                        counter += 1

                if box5.collidepoint(cursorpos):
                    if box5_NotOccupied:
                        screen.blit(O, (240, 225))
                        pygame.display.update()
                        box5_NotOccupied = False
                        box5Value = 2
                        counter += 1

                if box6.collidepoint(cursorpos):
                    if box6_NotOccupied:
                        screen.blit(O, (440, 225))
                        pygame.display.update()
                        box6_NotOccupied = False
                        box6Value = 2
                        counter += 1

                if box7.collidepoint(cursorpos):
                    if box7_NotOccupied:
                        screen.blit(O, (25, 425))
                        pygame.display.update()
                        box7_NotOccupied = False
                        box7Value = 2
                        counter += 1

                if box8.collidepoint(cursorpos):
                    if box8_NotOccupied:
                        screen.blit(O, (240, 425))
                        pygame.display.update()
                        box8_NotOccupied = False
                        box8Value = 2
                        counter += 1

                if box9.collidepoint(cursorpos):
                    if box9_NotOccupied:
                        screen.blit(O, (440, 425))
                        pygame.display.update()
                        box9_NotOccupied = False
                        box9Value = 2
                        counter += 1

    if isWinner(1):
        Mbox('Winner', 'Player 1 wins!', 0)
        noWinner = False

    elif isWinner(2):
        Mbox('Winner', 'Player 2 wins!', 0)
        noWinner = False

    elif (box1Value > 0 and box2Value > 0 and
          box3Value > 0 and box4Value > 0 and
          box5Value > 0 and box5Value > 0 and
          box7Value > 0 and box8Value > 0 and
          box9Value > 0):
        Mbox('Tie', 'The game was tied!', 0)
        noWinner = False
