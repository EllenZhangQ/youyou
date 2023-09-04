class Code():
    def __init__(self, name):
        self.name = name
    def info(self):
        print(self.name)
    def isPython(self):
        if 'Python' in self.language:
            print(True)
        else:
            print(False)

cd  = Code('Lucy')
cd.language = ['Python','C++']
cd.info()
cd.isPython()
        
        
        