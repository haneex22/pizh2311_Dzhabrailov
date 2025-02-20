class Snow:

    def __init__(self, num_of_snowflakes):
        self.num_of_snowflakes = num_of_snowflakes

    def __add__(self, n):
        self.num_of_snowflakes += n
        return self.num_of_snowflakes

    def __sub__(self, n):
        self.num_of_snowflakes -= n
        return self.num_of_snowflakes

    def __mul__(self, n):
        self.num_of_snowflakes *= n
        return self.num_of_snowflakes

    def __truediv__(self, n):
        self.num_of_snowflakes /= n
        int(self.num_of_snowflakes)
        return self.num_of_snowflakes

    def make_snow(self, n):
        new_num = self.num_of_snowflakes
        while new_num > n:
            print('*'*n)
            new_num -= n
        print('*'*new_num)

    def __call__(self, arg):
        self.num_of_snowflakes = arg

    def __repr__(self):
        return str(self.num_of_snowflakes)


snow = Snow(10)
print(snow)
print(snow + 10)
print(snow * 2)
print(snow - 2)
snow.make_snow(5)