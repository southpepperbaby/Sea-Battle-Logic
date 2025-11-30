# game_logic.py
# Логика игры "Морской бой"

import random


class GameBoard:
    """Класс игрового поля одного игрока"""
    def __init__(self, size=10):
        self.size = size
        # Создаём пустое поле (двумерный список)
        self.field = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)  # 0 = пусто
            self.field.append(row)
        
        self.ships = []  # Список кораблей
    
    def get_cell(self, x, y):
        """получение клетки"""
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.field[y][x]
        return None
    
