class Game:
    
    recommended_ram: int = 0
    recommended_cpu: str = ''
    recommended_video_card: str = ''
    
    def __init__(self, name):
        self.name = name
        
    def set_recommended_ram(self, ram):
        self.recommended_ram = ram
        
    def set_recommended_cpu(self, cpu):
        self.recommended_cpu = cpu
        
    def set_recommended_video_card(self, video_card):
        self.recommended_video_card = video_card
        
    def get_name(self):
        return self.name
    
    def get_recommended_ram(self):
        return self.recommended_ram
    
    def get_recommended_cpu(self):
        return self.recommended_cpu
    
    def get_recommended_video_card(self):
        return self.recommended_video_card
    
    def __setattr__(self, attr, value):
        if attr == 'name':
            self.__dict__[attr] = value
        elif attr == 'recommended_ram':
            self.__dict__[attr] = value
        elif attr == 'recommended_cpu':
            self.__dict__[attr] = value
        elif attr == 'recommended_video_card':
            self.__dict__[attr] = value
        else:
            raise AttributeError
        
    def __str__(self):
        return (f'Название игры: {self.get_name()}.\nРекомендуемые настройки:\n'
                f'ОЗУ - {self.get_recommended_ram()} ГБ;\n'
                f'Процессор - {self.get_recommended_cpu()};\n'
                f'Видеокарта - {self.get_recommended_video_card()}.')
        
        
game_1 = Game('Spider-man 2')
game_1.set_recommended_ram(16)
game_1.set_recommended_cpu("Intel Core i5 10400F")
game_1.set_recommended_video_card("RTX 2070")
print(game_1)