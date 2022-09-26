
class Curso():
    
    def __init__(self, id=None, nombre = None, creditos=None, tipologia=None, sede=None, nivel_estudio=None,facultad=None, descripcion=None,pre_requisitos=None,codigo=None) -> None:
        self.id = id 
        self.nombre = nombre
        self.creditos = creditos
        self.tipologia = tipologia
        self.sede = sede
        self.nivel_estudio =nivel_estudio
        self.facultad = facultad
        self.descripcion = descripcion
        self.pre_requisitos= pre_requisitos
        self.codigo = codigo 
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'nombre' : self.nombre, 
            'creditos' : self.creditos, 
            'tipologia':self.tipologia,
            'sede':self.sede,
            'nivel_estudio' :self.nivel_estudio,
            'facultad' : self.facultad,
            'descripcion' : self.descripcion,
            'prerequisitos': self.pre_requisitos,
            'codigo' : self.codigo 
        }
        
        