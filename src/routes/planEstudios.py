from flask import Blueprint, jsonify, request
import uuid

# Models
from models.modeloPlanEstudios import modeloPlanEstudios

main = Blueprint('planEstudios_blueprint', __name__)


@main.route('/')
def get_PlanEstudios():
    try:
        planEstudiosO = modeloPlanEstudios.get_planEstudios()
        return jsonify(planEstudiosO)
    except Exception as ex:
        return jsonify({'message':  str(ex)}), 500