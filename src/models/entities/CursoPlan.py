class CursoPlan():
    
    def __init__(self, idcurso=None, idplan = None, nivel_estudios=None) -> None:
        self.idcurso = idcurso 
        self.idplan = idplan
        self.nivel_estudios = nivel_estudios

    
    def to_JSON(self):
        return{
            'idcurso': self.idcurso, 
            'idplan' : self.idplan, 
            'nivel_estudios' : self.nivel_estudios
        }
    