
class Curso():
    
    def __init__(self, id=None, nombre = None, creditos=None, tipologia=None, sede=None, nivelestudio=None,facultad=None, descripcion=None,prerequisitos=None,codigo=None) -> None:
        self.id = id 
        self.nombre = nombre
        self.creditos = creditos
        self.tipologia = tipologia
        self.sede = sede
        self.nivelestudio =nivelestudio
        self.facultad = facultad
        self.descripcion = descripcion
        self.prerequisitos= prerequisitos
        self.codigo = codigo 
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'nombre' : self.nombre, 
            'creditos' : self.creditos, 
            'tipologia':self.tipologia,
            'sede':self.sede,
            'nivelestudio' :self.nivelestudio,
            'facultad' : self.facultad,
            'descripcion' : self.descripcion,
            'prerequisitos': self.prerequisitos,
            'codigo' : self.codigo 
        }
        
        