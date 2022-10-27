class Grupo():
    
    def __init__(self, id=None, numero = None, idprofesor=None, cupos=None, horario=None, lugar=None,idCurso=None) -> None:
        self.id = id 
        self.numero = numero
        self.idprofesor = idprofesor
        self.cupos = cupos
        self.horario = horario
        self.lugar = lugar
        self.idCurso= idCurso
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'numero' : self.numero, 
            'idprofesor' : self.idprofesor,
            'cupos' : self.cupos,
            'horario':self.horario,
            'lugar':self.lugar,
            'idCurso': self.idCurso
        }