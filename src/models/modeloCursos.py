
from hashlib import new
from database.db import get_connection
from .entities.Curso import Curso

class modeloCursos():
    
    @classmethod
    def get_cursos(self):
        try:
            connection = get_connection()
            cursosA = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    curso = Curso(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    cursosA.append(curso.to_JSON())

            connection.close()
            return cursosA
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_cursos_by_or(self,id,nombre):
        try:
            connection = get_connection()
            cursosA = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, creditos, tipologia, sede FROM cursos WHERE id = %s OR nombre = %s",(id,nombre,))
                resultset = cursor.fetchall()

                for row in resultset:
                    curso = Curso(row[0], row[1], row[2], row[3],row[4])
                    cursosA.append(curso.to_JSON())

            connection.close()
            return cursosA
        except Exception as ex:
            raise Exception(ex)
    
    
    
    @classmethod    
    def get_curso(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM cursos WHERE id = %s",(id,))
                row = cursor.fetchone()
                
                curso = None
                if row != None:    
                    curso = Curso(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    curso = curso.to_JSON()

            connection.close()
            return curso
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_cursos_by_and(self,id,nombre):
        try:
            connection = get_connection()
            cursosA = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, creditos, tipologia, sede FROM cursos WHERE id = %s AND nombre = %s",(id,nombre,))
                resultset = cursor.fetchall()

                for row in resultset:
                    curso = Curso(row[0], row[1], row[2], row[3],row[4])
                    cursosA.append(curso.to_JSON())

            connection.close()
            return cursosA
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_cursos_by_Plan(self,idplan):
        try:
            connection = get_connection()
            cursosxPlan = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.curso_plan WHERE id_plan = %s",(idplan,))
                resultset = cursor.fetchall()
                
                
            for row in resultset:
                    
                cursosxPlan.append((row[0]))
                

            connection.close()
            CursosA=[]
            for id in cursosxPlan:
                try:
                    connection = get_connection()

                    with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM cursos WHERE id = %s",(id,))
                        row = cursor.fetchone()
                        
                        curso = None
                        if row != None:    
                            curso = Curso(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                            curso = curso.to_JSON()

                    connection.close()
                    CursosA.append(curso)
                except Exception as ex:
                    raise Exception(ex)
            
            
            
            return CursosA
        except Exception as ex:
            raise Exception(ex)