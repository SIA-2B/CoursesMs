class PlanEstudios():
    
    def __init__(self, codigo=None, nombre = None, nivel_estudios=None) -> None:
        self.codigo = codigo 
        self.nombre = nombre
        self.nivel_estudios = nivel_estudios

    
    def to_JSON(self):
        return{
            'codigo': self.codigo, 
            'nombre' : self.nombre, 
            'nivel_estudios' : self.nivel_estudios
        }
    