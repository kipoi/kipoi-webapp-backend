import json
import os
from Bio import SeqIO


def get_errors(request):
    if not request.json:
        return {'type': 'error', 'message': 'Not a valid request'}

    if 'models' not in request.json:
        return {'type': 'error', 'message': 'No models selected'}

    selected_models = request.json['models']
    if selected_models is None or len(selected_models) == 0:
        return {'type': 'error', 'message': 'No models selected'}

    return None


def read_sequences(request):
    sequences = None

    if 'sequences' in request.json:
        sequences = request.json['sequences']

    if sequences is None or len(sequences) == 0:
        return None, {'type': 'error', 'message': 'No sequences sent'}

    return sequences, None
