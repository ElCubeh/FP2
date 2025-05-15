class Point2D:
    """Un punto en el plano, representado por sus cordenadas, x e y
    
    Métodos
    -------
    coordinates : devuelve las coordenadas del punto
    """

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    
    def coordinates(self):
        """Devuelve las coordenadas del punto en forma de tupla (x, y)"""
        
        return (self.__x, self.__y)
        
    def __eq__(self, other):
        """Dos puntos son iguales si tienen las mismas coordenadas"""
        
        if type(other) == Point2D:
            return self.coordinates() == other.coordinates()
        else:
            return False
            
    def __str__(self):
        """Devuelve una representación del punto como string"""

        return str(self.coordinates())
            
if __name__ == "__main__":
    point1 = Point2D(10.0, 5.0)
    point2 = Point2D(12.0, 5.0)
    print(str(point1), str(point2), point1 == point2)