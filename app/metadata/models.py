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
