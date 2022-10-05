from flask import Blueprint, jsonify, request
import uuid

#Entities
from models.entities import Grupo

# Models
from models.modeloGrupos import modeloGrupos

main = Blueprint('grupos_blueprint', __name__)


@main.route('/')
def get_grupos():
    try:
        grupos = modeloGrupos.get_grupos()
        return jsonify(grupos)
    except Exception as ex:
        return jsonify({'message':  str(ex)}), 500
    
@main.route('/<idCurso>')
def get_grupos_by_curso(idCurso):
    try:
        grupos = modeloGrupos.get_grupos_by_curso(idCurso)
        return jsonify(grupos)
    except Exception as ex:
        return jsonify({'message':  str(ex)}), 500


@main.route('/byId/<id>')
def get_grupo(id):
    try:
        grupo = modeloGrupos.get_grupo(id)
        if grupo != None:
            return jsonify(grupo)
        else: 
            return jsonify({}), 404
        
    except Exception as ex:
        return jsonify({'message':  str(ex)}), 500
   
    
@main.route('/updateCupo/<id>/<sum>', methods=['PUT'])
def update_CupoGrupo(id,sum):
    try:
        grupo1= modeloGrupos.get_grupo(id)
        suma =int(sum)
        
        affected_rows = modeloGrupos.update_CupoGrupo(int(grupo1["cupos"]),suma,id)

        
        if affected_rows == 1:
            grupo1= modeloGrupos.get_grupo(id)
            return jsonify(grupo1)
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500