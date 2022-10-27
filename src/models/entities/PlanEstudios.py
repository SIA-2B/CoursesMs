class PlanEstudios():
    
    def __init__(self, codigo=None, nombre = None, nivelestudios=None) -> None:
        self.codigo = codigo 
        self.nombre = nombre
        self.nivelestudios = nivelestudios

    
    def to_JSON(self):
        return{
            'codigo': self.codigo, 
            'nombre' : self.nombre, 
            'nivelestudios' : self.nivelestudios
        }
    