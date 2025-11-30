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
    
    
    def can_place_ship(self, x, y, length, horizontal):
        """Проверить можно ли поставить корабль"""
        # Проверка каждой клетки корабля + соседних
        for i in range(length):
            if horizontal:
                cx = x + i
                cy = y
            else:
                cx = x
                cy = y + i
            
            # Проверка границы
            if cx >= self.size or cy >= self.size:
                return False
            
            # Проверка клетки и всех соседних
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if self.field[ny][nx] == 1:  # есть корабль
                            return False
        return True
    
    def place_ship(self, x, y, length, horizontal):
        """Разместить корабль на поле"""
        if not self.can_place_ship(x, y, length, horizontal):
            return False
        
        ship_cells = []
        for i in range(length):
            if horizontal:
                cx = x + i
                cy = y
            else:
                cx = x
                cy = y + i
            self.field[cy][cx] = 1  # Ставим корабль
            ship_cells.append((cx, cy))
        
        self.ships.append(ship_cells)
        return True