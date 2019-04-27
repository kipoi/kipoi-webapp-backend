"""
File containing the routes.
"""

from flask import Blueprint, jsonify
from app.metadata import models

bp = Blueprint('routes', __name__)


@bp.route('/')
def hello():
    return "Hello World"


@bp.route('/metadata/model_list')
@bp.route('/metadata/model_list/<environment>')
def get_model_list(environment=None):
    sequence_models = models.list_all_sequence_models()

    if environment is not None:
        sequence_models = models.filter_sequence_models_by_environment(sequence_models, environment)

    return jsonify(sequence_models)
