import json

from pathlib import Path
from jsonschema import validate

def test_indicator_json_schema():
    schema = json.load(open("schemas/indicator_schema.json"))
    instance = json.load(open("examples/indicator_example.json"))
    assert validate(instance=instance, schema=schema) is None
