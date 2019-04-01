import pygame
import random


class Game(object):
    def __init__(self, p_rect, m_width):
        self.player = Player(p_rect)
        self.redzone = Redzone(m_width)

    def update_redzone_pos(self):
        self.redzone.update_redzone_pos()

    def get_redzone_pos(self):
        return self.redzone.get_redzone_pos()

    def set_player(self, x, y):
        self.player.startpos(x, y)

    def get_player_pos(self):
        return self.player.get_player_pos()

    def change_player_speed(self, x, y):
        self.player.changespeed(x, y)

    def move_player(self):
        self.player.move()

    def is_player_in_redzone(self):
        p_rect = self.get_player_pos()
        r_rect = self.get_redzone_pos()
        if p_rect.left > r_rect.left and p_rect.right < r_rect.right \
                and p_rect.top > r_rect.top and p_rect.bottom < r_rect.bottom:
            return True
        return False


class Redzone(object):
    def __init__(self, m_width):
        self.max_width = m_width
        self.rect = pygame.Rect(m_width, random.randrange(0, 400),
                                random.randrange(300, 1500), random.randrange(200, 1000))

    def get_redzone_pos(self):
        return self.rect

    def update_redzone_pos(self):
        self.rect.centerx -= 20
        if self.rect.left < 0:
            self.rect.width -= 20
            if self.rect.width < 0:
                self.rect.left = self.max_width
                self.rect.width = random.randrange(300, 1500)
                self.rect.height = random.randrange(200, 1000)
                self.rect.top = random.randrange(0, 400)


class Player(object):
    def __init__(self, p_rect):
        # set speed vector
        self.change_x = 0
        self.change_y = 0
        self.rect = p_rect

    def get_player_pos(self):
        return self.rect

    def startpos(self, x, y):
        # Make our top-left corner the passed-in location.
        self.rect.x = x
        self.rect.y = y

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self):
        # Move left/right
        self.rect.x += self.change_x
        # Move up/down
        self.rect.y += self.change_y
