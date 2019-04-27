import kipoi
from app.metadata.models import is_sequence_model


def get_transform(alphabet='ACGT', dtype=None, alphabet_axis=1, dummy_axis=None, **kwargs):
    """
    Create a transform from sequence to one-hot encoded np.array
    """
    from kipoiseq.transforms import ReorderedOneHot
    return ReorderedOneHot(alphabet=alphabet,
                           dtype=dtype,
                           alphabet_axis=alphabet_axis,
                           dummy_axis=dummy_axis)


def get_sequence_length(model_name):
    """
    Find sequence length of the model if it is a sequence based model.
    """
    model_description = kipoi.get_model_descr(model_name)

    if not is_sequence_model(model_description):
        raise ValueError(
            f'Model {model_name} is not a sequence model. Its dataloader is: {model_description.default_dataloader()}')

    return model_description.default_dataloader.default_args.get('auto_resize_len', None)


def modify_sequence_length(sequence, expected_length):
    """
    Modify sequence by trimming or padding it to the expected length
    """
    from concise.preprocessing.sequence import pad_sequences
    return pad_sequences([sequence], maxlen=expected_length, align='center')[0]
