class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def output(self):
        print(f"Площадь - {self.square}, периметр - {self.perimeter}")


GeometricFigure1 = GeometricFigure(2, 8)

GeometricFigure1.output()