from abc import ABC

class Base(ABC):
    def __init__(self, adress):
        self.adress = adress

    def calculateFreqs(self):
        lines= []
        with open('Text.txt')as f:
            lines = f.readlines()

        count = 0
        for line in lines:
            count += 1
            print(f'line {count}: {line}')

class listCount(Base):
    def calculateFreqs(self):
        pass


class DictCount(Base):
    def calculateFreqs(self):
        pass
