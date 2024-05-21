class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]
        self.sunk = []

    def shoot(self, row, col, result):
        if result == 'sink':
            self.sunk.append((row, col))
        # self.map[row][col] = result[0]
        if result == 'hit':
            self.sunk.append((row, col))
            self.map[row][col] = 'x'

    def cell(self, row, col):
        if (row, col) in self.sunk:
            return 'x'
        for r, c in self.sunk:
            if (abs(r - row) <= 1 and abs(c - col) <= 1) and (self.map[row][col] != 'x'):
                return '*'
        if self.map[row][col] == 'x':
            return 'x'
        return '.'


sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(8, 9, 'hit')
sm.shoot(4, 8, 'sink')
sm.shoot(7, 9, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
