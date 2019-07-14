### Get Samples
Method: `GET`

Endpoint: `/metadata/samples`

Returns:
```
{
    "fasta_data": "example",
    "vcf_data": "example",
    "bed_data": "example"
}
```

### Get Model List
Method: `GET`

Endpoint: `/metadata/model_list`

Returns:
```
[
    {
        "group": "Basenji",
        "model": "Basenji",
        "environment": "kipoi-py3-keras2"
    },
    {
        "group": "Basset",
        "model": "Basset",
        "environment": "kipoi-py3-keras2"
    },
    {
        "group": "DeepSEA",
        "model": "DeepSEA/variantEffects",
        "environment": "kipoi-py3-keras2"
    },
    {
        "group": "DeepSEA",
        "model": "DeepSEA/predict",
        "environment": "kipoi-py3-keras2"
    },
    ...
]
```

### Get Predictions
Method: `POST`

Endpoint: `/get_predictions`

Form-Data:
- `models`: List of Strings (Format: `model_name@@@model_environment`)
- One of:
    - `sequences`: List of objects with attributes `id` and `seq`
    - `file`: Input file

Example Request:
- `models`: `['Basset@@@kipoi-py3-keras2', 'DeepSEA/predict@@@kipoi-py3-keras2']` 
- `sequences`:
```
[
    {
        "name": "[known_CEBP_binding_increase]GtoT__chr1_109817091_109818090",
        "model": "Basset",
        "feature": "",
        "score": 0.3131888806819916,
        "normalized_score": ""
    },
    {
        "name": "[known_CEBP_binding_increase]GtoT__chr1_109817091_109818090",
        "model": "Basset",
        "feature": "",
        "score": 0.473111629486084,
        "normalized_score": ""
    },
    ...
]
```
