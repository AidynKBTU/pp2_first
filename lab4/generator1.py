class Numbers:
    def __init__(self, end):
        self.__end = end
        
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if self.num <= self.__end:            
            cont = self.num
            self.num += 1
            return cont ** 2
        else:
            raise StopIteration
    
generator = Numbers(10)
generator = iter(generator)

for i in generator:
	print(i) 