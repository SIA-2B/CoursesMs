from database.db import get_connection
from .entities.PlanEstudios import PlanEstudios

class modeloPlanEstudios():
    
    @classmethod
    def get_planEstudios(self):
        try:
            connection = get_connection()
            vectorPlanEstudiossA = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM planyestudio ORDER BY codigo ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    planEstudiosO = PlanEstudios(row[0], row[1], row[2])
                    vectorPlanEstudiossA.append(planEstudiosO.to_JSON())

            connection.close()
            return vectorPlanEstudiossA
        except Exception as ex:
            raise Exception(ex)