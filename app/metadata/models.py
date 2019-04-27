"""
File containing meta information about models.
"""

import kipoi
from app.cache import cache


@cache.memoize()
def get_model_list(source):
    """Cache for kipoi's list models"""
    df = kipoi.list_models()
    return df


def is_sequence_model(model_description):
    """
    Check if a model is a sequence-based accepting a single sequence.
    """
    from kipoi.specs import DataLoaderImport
    return (isinstance(model_description.default_dataloader, DataLoaderImport)
            and model_description.default_dataloader.defined_as == 'kipoiseq.dataloaders.SeqIntervalDl')


@cache.memoize()
def list_all_sequence_models(source='kipoi'):
    """
    List all the sequence models in Kipoi for a given source
    """
    return [name for name in kipoi.get_source(source)._list_components("model") if
            is_sequence_model(kipoi.get_model_descr(name))]


def get_environment(model_name, source='kipoi'):
    """
    Find the shared environment of the model
    """
    import os
    from kipoi.utils import read_yaml
    src = kipoi.get_source(source)
    environments = read_yaml(os.path.join(src.local_path, 'shared/envs/models.yaml'))
    model_group = model_name.split('/')[0]
    model_environment_map = {model: key for key, value in environments.items() for model in value}
    return model_environment_map.get(model_group, None)


def filter_sequence_models_by_environment(sequence_models, environment):
    """
    Filter the list of sequence models by their environments.
    """
    return [model for model in sequence_models if
            get_environment(model) is not None and get_environment(model) == environment]
