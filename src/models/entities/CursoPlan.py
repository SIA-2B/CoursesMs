class CursoPlan():
    
    def __init__(self, idcurso=None, idplan = None, nivelestudios=None) -> None:
        self.idcurso = idcurso 
        self.idplan = idplan
        self.nivelestudios = nivelestudios

    
    def to_JSON(self):
        return{
            'idcurso': self.idcurso, 
            'idplan' : self.idplan, 
            'nivelestudios' : self.nivelestudios
        }
    