import json
import os
from Bio import SeqIO


def get_errors(request):
    if not request.form:
        return {'type': 'error', 'message': 'Not a valid request'}

    if 'models' not in request.form:
        return {'type': 'error', 'message': 'No models selected'}

    selected_models = eval(request.form['models'])
    if selected_models is None or len(selected_models) == 0:
        return {'type': 'error', 'message': 'No models selected'}

    return None


def read_sequences(request):
    sequences = None

    if 'sequences' in request.form:
        sequences = json.loads(request.form['sequences'])

    if 'file' in request.files:
        file = request.files['file']
        base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')
        full_path = os.path.join(base_path, request.form['filename'])
        file.save(full_path)
        fasta_sequences = SeqIO.parse(open(full_path), 'fasta')

        sequences = []
        for fasta in fasta_sequences:
            sequences.append({
                'id': fasta.id,
                'seq': str(fasta.seq)
            })
        os.remove(full_path)

    if sequences is None or len(sequences) == 0:
        return None, {'type': 'error', 'message': 'No sequences sent'}

    return sequences, None
