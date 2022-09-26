class CursoPlan():
    
    def __init__(self, id_curso=None, id_plan = None, nivel_estudios=None) -> None:
        self.id_curso = id_curso 
        self.id_plan = id_plan
        self.nivel_estudios = nivel_estudios

    
    def to_JSON(self):
        return{
            'id_curso': self.id_curso, 
            'id_plan' : self.id_plan, 
            'nivel_estudios' : self.nivel_estudios
        }
    