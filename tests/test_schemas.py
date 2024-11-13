import json

from pathlib import Path
from jsonschema import validate

def test_identifier_json_schema():
    schema = json.load(open("schemas/identifier_schema.json"))
    instance = json.load(open("examples/identifier_example.json"))
    assert validate(instance=instance, schema=schema) is None
