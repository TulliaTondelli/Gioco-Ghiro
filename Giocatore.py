class Giocatore:
    def __init__(self, nome):
        self.nome = nome
        self.x = 0
        self.y = 0

    def muoviGiu(self):
        self.x += 1

    def muoviSu(self):
        self.x -= 1

    def muoviSinistra(self):
        self.y -= 1

    def muoviDestra(self):
        self.y += 1


class Papà:
    def __init__(self, livello):
        if livello == 1:
            self.movimento = [(5, 1), (5, 2), (4, 2), (3, 2), (3, 1), (4, 1)]
        elif livello == 2:
            self.movimento = [(9, 3), (9, 2), (8, 2), (7, 2), (6, 2), (6, 1), (6, 0), (5, 0), (4, 0), (4, 1), (4, 0),
                              (5, 0), (6, 0), (6, 1), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3)]
        elif livello == 3:
            self.movimento = [(7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 6), (6, 5)]
        elif livello == 4:
        	self.movimento = [(13, 0), (12, 0), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (12, 4), (13, 4), (13, 5),
        					 (13, 6), (12, 6), (11, 6), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12),
        					 (9, 12), (8, 12), (7, 12), (7, 11), (7, 12), (8, 12), (9, 12), (10, 12), (10, 11), (10, 10),
        					 (10, 9), (10, 8), (10, 7), (10, 6), (11, 6), (12, 6), (13, 6), (13, 5), (13, 4), (12, 4),
        					 (11, 4), (11, 3), (11, 2), (11, 1), (11, 0), (12, 0), (13, 0)]
        self.indice = 0
        self.x = self.movimento[self.indice][0]
        self.y = self.movimento[self.indice][1]

    def muoviPapà(self, livello):
        if livello == 1:
            self.indice = (self.indice + 1) % 6
        elif livello == 2:
            self.indice = (self.indice + 1) % 19
        elif livello == 3:
            self.indice = (self.indice + 1) % 9
        elif livello == 4:
        	self.indice = (self.indice + 1) % 47
        self.x = self.movimento[self.indice][0]
        self.y = self.movimento[self.indice][1]


class Trappola:
    def __init__(self, livello):
        if livello == 2:
            self.movimento = [(4, 5), (3, 5), (2, 5), (2, 6), (2, 7), (3, 6)]
        elif livello == 3:
            self.movimento = [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 5), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1)]
        elif livello == 4:
        	self.movimento = [(6, 0), (5, 0), (4, 0), (3, 0), (3, 1), (4, 1), (5, 1), (6, 1)]
        self.indice = 0
        self.x = self.movimento[self.indice][0]
        self.y = self.movimento[self.indice][1]

    def muoviTrappola(self, livello):
        if livello == 2:
            self.indice = (self.indice + 1) % 6
        elif livello == 3:
            self.indice = (self.indice + 1) % 11
        elif livello == 4:
        	self.indice = (self.indice + 1) % 8
        self.x = self.movimento[self.indice][0]
        self.y = self.movimento[self.indice][1]

class Gatto:
    def __init__(self, livello):
        if livello == 3:
            self.movimento = [(6, 11), (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (7, 8), (8, 8), (8, 9), (9, 9),
                              (10, 9), (10, 8), (10, 7), (11, 7), (10, 7), (10, 8), (10, 9), (9, 9), (8, 9), (8, 8),
                              (7, 8), (8, 8), (8, 9), (8, 10), (8, 11), (7, 11), (6, 11)]
        elif livello == 4:
        	self.movimento = [(1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (4, 9), (4, 10), (4, 11), (3, 11), (2, 11), (1, 11), (0, 11)]
        self.indice = 0
        self.x = self.movimento[self.indice][0]
        self.y = self.movimento[self.indice][1]
    
    def muoviGatto(self, livello):
        if livello == 3:
            self.indice = (self.indice + 1) % 27
        elif livello == 4:
        	self.indice = (self.indice + 1) % 14
        self.x = self.movimento[self.indice][0]
        self.y = self.movimento[self.indice][1]

class Colla1:
	def __init__(self):
		self.movimento =[(9, 5), (8, 4), (7, 4), (7, 3), (6, 3), (5, 3), (5, 4), (5, 3), (6, 3), (7, 3), (7, 4), (8, 4), (9, 5)]
		self.indice = 0
		self.x = self.movimento[self.indice][0]
		self.y = self.movimento[self.indice][1]

	def muoviColla1(self):
		self.indice = (self.indice + 1) % 13
		self.x = self.movimento[self.indice][0]
		self.y = self.movimento[self.indice][1]

class Colla2:
	def __init__(self):
		self.movimento = [(9, 5), (8, 6), (7, 6), (6, 6), (5, 6), (5, 5), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 5)]
		self.indice = 0
		self.x = self.movimento[self.indice][0]
		self.y = self.movimento[self.indice][1]

	def muoviColla2(self):
		self.indice = (self.indice + 1) % 13
		self.x = self.movimento[self.indice][0]
		self.y = self.movimento[self.indice][1]