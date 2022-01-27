""""
Answer to pdf Challenge, technical test for Netheos.
One should use only the block methode, function block_search_eof()

Author : Neeb Olivier

Created : 27th January 2022
"""

### imports
import os
import sys

# Uncomment to see ram usage + uncomment @profile
from memory_profiler import profile

# Uncomment to see time usage + uncomment @profile
# import atexit
# import line_profiler
# profile = line_profiler.LineProfiler()
# atexit.register(profile.print_stats)

""" GOAL : Performs a research backwards, from the end of the pdf file, and look for '%%EOF' in bytes at the start of a line.
    To ensure %%EOF starts the line, the function block_find_eof() performs a rfind( b'\n%%EOF' ) on a block of
    bytes characters. The block then changes if not found, making the research progress backwards into the pdf.

    PARAMETERS : self.block_size = 30, it is the number of bytes contained in a block. Bigger blocks leads to faster computation

    RETURN : Nothing is returned, only the position in bytes of %%EOF is printed if found, else -1. """


class BackwardsSearcher():

    def __init__(self, path):
        self.pdf_length = os.path.getsize(path)
        self.f = open(path, 'rb', buffering=30)  # buffering to not open all pdf file at once, saving ram
        self.eof_position = -1
        self.block_size = 30  # size in bytes of a block
        self.block_num = 1  # number of the ongoing block

    ### method 1, fast searcher of %%EOF, starting fro mthe end of the pdf file and search by block of bytes
    # @profile
    def block_find_eof(self):

        while self.eof_position == -1:
            # as long as %%EOF was not found at the start of a line
            try:
                start_read = self.pdf_length - self.block_size * self.block_num + 6 * (self.block_num - 1)
                # value in bytes of the ongoing block,
                # the +6*(self.block_num-1) will create an overlap of 6 bytes with the precedent block, so %%EOF can't be split in 2 blocks
                self.f.seek(start_read, 0)
                block_read = self.f.read(self.block_size)

                if block_read.rfind(b'\n%%EOF') == -1:
                    # no %%EOF found at the start of a line
                    self.block_num += 1

                else:
                    # %%EOF found at the start of a line, we print its position in bytes in the pdf file
                    print(start_read + block_read.rfind(b'\n%%EOF') + 1)
                    self.eof_position = start_read + block_read.rfind(b'\n%%EOF') + 1
                    self.f.close()

            except OSError:
                # pointer has exceeded the first byte of the file
                self.f.seek(0, 0)
                search = self.f.read(min(self.pdf_length, self.block_size)).rfind(b'\n%%EOF')
                # we determine whether %%EOF is in a block that starts from the beginning of the file
                self.f.seek(0, 0)
                if b'%%EOF' in self.f.read(5) and search == -1:
                    # check if %%EOF is at the start of the file
                    print(0)
                else:
                    print(search)
                self.f.close()
                break

    ### method 2, faster but might take too much ram when big dpdf file
    def quick_find_eof(self):
        self.f = open(path, 'rb')
        if self.f.read().rfind(b'\n%%EOF') != -1:
            print(self.f.read().rfind(b'\n%%EOF') + 1)
        else:
            print(-1)

    ### method 3, way slower (about x10 than method 1) but less ram usage than method 1 and 2
    def character_find_eof(self):
        self.cara = None
        self.f = open(path, 'rb', buffering=30)
        self.eof_status = False
        self.goal = b'%%EOF'

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
        self.eof_debut()
        self.f.close()
        print(self.eof_position)

    def search_for_eof(self):  # recherche si %%EOF est à cette place
        trail = self.f.read(len(self.goal))
        self.f.seek(-len(self.goal), 1)
        return self.goal == trail

    def lire_caractere(self):
        self.f.seek(-2, 1)
        self.cara = self.f.read(1)

    def eof_debut(self):
        self.f.seek(0, 0)
        if self.search_for_eof():
            self.eof_position = self.f.tell()


if __name__ == "__main__":
    path = str(sys.argv[1])
    finder = BackwardsSearcher(path)
    finder.block_find_eof()


