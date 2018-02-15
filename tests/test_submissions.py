from pathlib import Path
import json
import numpy as np
from jsonschema import validate
import os
import pytest


schema_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data/museval.schema.json',
)

with open(schema_path) as schema_file:
    schema = json.load(schema_file)


def generate_folders():
    p = Path('submissions')
    for x in p.iterdir():
        if x.is_dir():
            yield x


def generate_jsonfiles(x):
    p = Path(x)
    if p.exists():
        json_paths = p.glob('**/*.json')
        for json_path in json_paths:
            yield json_path


@pytest.fixture(params=generate_folders())
def folders(request):
    return request.param


# @pytest.fixture(params=generate_jsonfiles(folders))
# def json_path(request):
#     return request.param


def test_folder(folders):
    assert len(list(generate_jsonfiles(folders))) == 50


# def test_validation(json_path):
#     with open(json_path) as json_file:
#         json_string = json.loads(json_file.read())
#         validate(json_string, schema)
