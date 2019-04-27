import numpy as np
import kipoi
from app.metadata.models import is_sequence_model
from app.generic import helpers


class KipoiSequenceModel:
    """
    Generic sequence-based model
    """

    def __init__(self, model_name):
        self.model_description = kipoi.get_model_descr(model_name)

        if not is_sequence_model(self.model_description):
            raise ValueError(
                f'Model {model_name} is not a sequence model.'
                f'Its dataloader is: {self.model_description.default_dataloader()}')

        self.model = kipoi.get_model(model_name, with_dataloader=False)
        self.transform = helpers.get_transform(**self.model_description.default_dataloader.default_args)
        self.sequence_length = helpers.get_sequence_length(model_name)

    def predict(self, sequence):
        """
        Batch-wise prediction
        """
        if len(sequence) != self.sequence_length:
            sequence = helpers.modify_sequence_length(sequence, self.sequence_length)

        return self.model.predict_on_batch(self.transform(sequence)[np.newaxis])
