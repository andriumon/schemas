import json

from pathlib import Path
from jsonschema import validate

def test_metric_schema():
    schema = json.load(open("schemas/metric_schema.json"))
    instance = json.load(open("examples/metric_example.json"))
    assert validate(instance=instance, schema=schema) is None
