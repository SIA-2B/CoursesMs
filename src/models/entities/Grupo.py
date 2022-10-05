class Grupo():
    
    def __init__(self, id=None, numero = None, id_profesor=None, cupos=None, horario=None, lugar=None,idCurso=None) -> None:
        self.id = id 
        self.numero = numero
        self.id_profesor = id_profesor
        self.cupos = cupos
        self.horario = horario
        self.lugar = lugar
        self.idCurso= idCurso
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'numero' : self.numero, 
            'id_profesor' : self.id_profesor,
            'cupos' : self.cupos,
            'horario':self.horario,
            'lugar':self.lugar,
            'idCurso': self.idCurso
        }