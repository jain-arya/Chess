import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.hovered_sqr = None
        self.next_player = 'white'
        self.dragger = Dragger()

    def show_bg(self , surface):
        for row in range(ROWS):
            for col in range(COLS):
                if((row + col) % 2 == 0):
                    color = (234,235,200)
                else:
                    color = (119,154,88)

                rect = (col*SQUARE_SIZE , row*SQUARE_SIZE , SQUARE_SIZE , SQUARE_SIZE)

                pygame.draw.rect(surface , color , rect)

    def show_pieces(self , surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)
                        img = pygame.image.load(piece.texture)
                        img_centre = col * SQUARE_SIZE + SQUARE_SIZE // 2 , row * SQUARE_SIZE + SQUARE_SIZE // 2
                        piece.texture_rect = img.get_rect(center = img_centre)
                        surface.blit(img , piece.texture_rect)

    def show_moves(self,surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                color = '#C86464' if(move.final.row + move.final.col)%2 == 0 else '#C84646'
                rect = (move.final.col*SQUARE_SIZE , move.final.row*SQUARE_SIZE , SQUARE_SIZE , SQUARE_SIZE)
                pygame.draw.rect(surface , color , rect)

    def show_last_move(self , surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            for pos in(initial , final):
                color = (244,247,116) if(pos.row * pos.col)%2 == 0 else (172,195,51)
                rect = (pos.col * SQUARE_SIZE , pos.row * SQUARE_SIZE , SQUARE_SIZE , SQUARE_SIZE)
                pygame.draw.rect(surface,color,rect)

    def show_hover(self,surface):
        if self.hovered_sqr:
            color = (180,180,180)
            rect = (self.hovered_sqr.col * SQUARE_SIZE , self.hovered_sqr.row * SQUARE_SIZE , SQUARE_SIZE , SQUARE_SIZE)
            pygame.draw.rect(surface,color,rect,width = 3)

    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self,row,col):
        self.hovered_sqr = self.board.squares[row][col]