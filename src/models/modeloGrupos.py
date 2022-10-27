from database.db import get_connection
from .entities.Grupo import Grupo

class modeloGrupos():
    
    @classmethod
    def get_grupos(self):
        try:
            connection = get_connection()
            GruposA = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Grupos ORDER BY idcurso")
                resultset = cursor.fetchall()

                for row in resultset:
                    grupo = Grupo(row[0], row[1], row[2], row[3],row[4],row[5],row[6])
                    GruposA.append(grupo.to_JSON())

            connection.close()
            return GruposA
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def get_grupos_by_curso(self,idCurso):
        try:
            connection = get_connection()
            GruposA = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Grupos WHERE idcurso=%s ORDER BY idcurso",(idCurso,))
                resultset = cursor.fetchall()

                for row in resultset:
                    grupo = Grupo(row[0], row[1], row[2], row[3],row[4],row[5],row[6])
                    GruposA.append(grupo.to_JSON())

            connection.close()
            return GruposA
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_grupo(self,id):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM grupos WHERE id=%s ORDER BY idcurso",(id,))
                row = cursor.fetchone()

                grupo = None
                if  row !=None:
                    grupo = Grupo(row[0], row[1], row[2], row[3],row[4],row[5],row[6])
                    grupo = grupo.to_JSON()

            connection.close()
            return grupo
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_CupoGrupo(self,n,sum,id):
        try:
            connection = get_connection()
            

            with connection.cursor() as cursor:
                a=n+sum
                cursor.execute("UPDATE grupos SET cupos=%s WHERE id=%s ",(a,id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
