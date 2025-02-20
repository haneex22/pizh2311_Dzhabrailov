class Screen:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __add__(self, other):
        return self.width + other.width
    
    
table_1 = Screen(59.7, 33.6)
table_2 = Screen(53, 29.9)
print(f'Ширина обоих мониторов вместе: {table_1 + table_2} сантиметров.')