import pygame
import pygame_gui as pgui
#from pygame_gui.elements import UIButton
from settings import s
from StateEnum import StateEnum
import pygame_menu
class Menu:
    def __init__(self, screen):
        stack = []
        self.screen = screen
        self.manager = pgui.UIManager((64 * 50, s.screen_h))
        self.text_arr = []

        self.status = StateEnum.MAIN_MENU
        self.stack = []

    def createText(self, rect,  text):
        text_box = pgui.elements.UITextBox(
            html_text="<p>"+text+"</p>",
            relative_rect=rect,
            manager=self.manager,
            wrap_to_height=True,
            visible=0
        )
        text_box.rebuild()
        self.text_arr.append(text_box)
    def updateTextBox(self, x_scroll, player_x):
        for text in self.text_arr:
            text.rect.x += x_scroll
            if player_x + 300 > text.rect.x:
                text.visible = True
        #print(self.text_arr)

    def deleteTextBox(self):
        self.text_arr = []
    def update(self, ticks, x_scroll, player_x):
        self.manager.update(ticks)
        self.manager.draw_ui(self.screen)
        self.updateTextBox(x_scroll, player_x)
