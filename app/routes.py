"""
File containing the routes.
"""

from flask import Blueprint, abort, jsonify, request
from app.metadata import models
from app.generic.sequence_model import KipoiSequenceModel

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


@bp.route('/get_predictions', methods=['POST'])
def get_predictions():
    if not request.json:
        return jsonify({'type': 'error', 'message': 'Not a valid request'})

    if 'models' not in request.json:
        return jsonify({'type': 'error', 'message': 'No models selected'})

    models = request.json['models']
    if models is None or len(models) == 0:
        return jsonify({'type': 'error', 'message': 'No models selected'})

    sequences = request.json['sequences']
    if sequences is None or len(sequences) == 0:
        return jsonify({'type': 'error', 'message': 'No sequences sent'})

    response = []

    for model_name in models:
        model = KipoiSequenceModel(model_name)

        for sequence in sequences:
            predictions = model.predict(sequence['seq'])
            for prediction in predictions:
                response.append({
                    'name': sequence['id'],
                    'model': model_name,
                    'feature': '',
                    'score': prediction.tolist(),
                    'normalized_score': ''
                })

    return jsonify(response)
