class Schoolchild:
    def __init__(self, name, cr_class):
        self.name = name
        self.cr_class = cr_class

    def study(self):
        print(f'{self.name} учится в {self.cr_class}.')

child = Schoolchild('Евгений', '9Б')
child.study()