

import os
import sys


class BackwardsSearcher():

    def __init__(self, path):
        self.goal = '%%EOF'.encode('utf-8')
        self.pdf_length = os.path.getsize(path)
        self.f = open(path, 'rb')
        self.eof_status = False
        self.eof_position = -1
        self.cara = None

    def find_eof(self):
        self.f.seek(self.pdf_length, 0)

        self.lire_caractere()

        while self.eof_status == False and self.f.tell() != 1:

            if self.cara != b'\n':
                self.lire_caractere()

            else:
                if not self.search_for_eof():
                    self.lire_caractere()
                else:
                    self.eof_status = self.search_for_eof()
                    self.eof_position = self.f.tell()

        self.f.close()
        print(self.eof_position)

    def search_for_eof(self):  # recherche si %%EOF est à cette place
        trail = self.f.read(len(self.goal))
        self.f.seek(-len(self.goal), 1)
        return bool(self.goal == trail)

    def lire_caractere(self):
        self.f.seek(-2, 1)
        self.cara = self.f.read(1)

if __name__ == "__main__" :
    if len(sys.argv) < 1 :
        print("pas d'argument")
    else :
        path = str(sys.argv[1])
        finder = BackwardsSearcher(path)
        finder.find_eof()
        

