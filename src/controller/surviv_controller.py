import pygame

import model.surviv_model


class Controller(object):

    def __init__(self, p_rect, m_width):
        self.game_over = False
        self.game = model.surviv_model.Game(p_rect, m_width)

    def set_player(self, x, y):
        self.game.set_player(x, y)

    def update_redzone_pos(self):
        self.game.update_redzone_pos()

    def get_redzone_pos(self):
        return self.game.get_redzone_pos()

    def get_player_pos(self):
        return self.game.get_player_pos()

    def is_player_in_redzone(self):
        return self.game.is_player_in_redzone()

    @staticmethod
    def process_welcome_events(rect):
        done = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = 1
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if rect.left < pos[0] < rect.right and rect.top < pos[1] < rect.bottom:
                    done = 2  # Play Solo button pressed.
        return done

    def process_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.change_player_speed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    self.game.change_player_speed(5, 0)
                if event.key == pygame.K_UP:
                    self.game.change_player_speed(0, -5)
                if event.key == pygame.K_DOWN:
                    self.game.change_player_speed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.game.change_player_speed(5, 0)
                if event.key == pygame.K_RIGHT:
                    self.game.change_player_speed(-5, 0)
                if event.key == pygame.K_UP:
                    self.game.change_player_speed(0, 5)
                if event.key == pygame.K_DOWN:
                    self.game.change_player_speed(0, -5)

        self.game.move_player()
        return False
