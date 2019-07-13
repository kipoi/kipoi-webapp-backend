"""
File containing the routes.
"""

from flask import Blueprint, abort, jsonify, request
from app.metadata import models
from app.generic.sequence_model import KipoiSequenceModel
from .utilities import get_errors, read_sequences
import os

bp = Blueprint('routes', __name__)
cached_models = {}


@bp.route('/metadata/model_list')
@bp.route('/metadata/model_list/<environment>')
def get_model_list(environment=None):
    sequence_models = models.list_all_sequence_models()

    if environment is not None:
        sequence_models = models.filter_sequence_models_by_environment(sequence_models, environment)

    sequence_models['group'] = sequence_models['model'].str.split('/').str[0]
    return sequence_models.to_json(orient='records')


@bp.route('/metadata/samples')
def get_sample_sequences():
    response = {}

    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples')

    with open(os.path.join(base_path, 'example.fasta'), 'r') as fasta:
        response['fasta_data'] = fasta.read()

    with open(os.path.join(base_path, 'example.vcf'), 'r') as vcf:
        response['vcf_data'] = vcf.read()

    with open(os.path.join(base_path, 'example.bed'), 'r') as bed:
        response['bed_data'] = bed.read()

    return jsonify(response)


@bp.route('/get_predictions', methods=['POST'])
def get_predictions():
    errors = get_errors(request)
    if errors is not None:
        return jsonify(errors)

    selected_models = eval(request.form['models'])
    sequences, error = read_sequences(request)

    if error is not None:
        return jsonify(error)

    response = []

    for model_name in selected_models:
        if model_name in cached_models:
            model = cached_models[model_name]
        else:
            try:
                model = KipoiSequenceModel(model_name)
            except ValueError:
                return jsonify({'type': 'error', 'message': f'Model {model_name} does not exist.'})
            cached_models[model_name] = model

        for sequence in sequences:
            predictions = model.predict(sequence['seq'])
            for prediction in predictions:
                for score in prediction.tolist():
                    response.append({
                        'name': sequence['id'],
                        'model': model_name,
                        'feature': '',
                        'score': score,
                        'normalized_score': ''
                    })

    return jsonify(response)
