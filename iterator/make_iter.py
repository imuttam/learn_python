class Square:
    def __init__(self, length):
        self.i = 0
        self.length = length
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i**2
            self.i += 1
            return result
        
sq = Square(10)

while True:
    try:
        item = next(sq)
        print(item)
    except StopIteration:
        break