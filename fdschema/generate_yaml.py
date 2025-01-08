#!/usr/bin/env python

import sys
import json
import yaml
import os
from pathlib import Path


# class to fix indentation
# see https://github.com/yaml/pyyaml/issues/234#issuecomment-765894586
class Dumper(yaml.Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + ".yaml"

json_instance = json.load(open(input_file))

print(input_file, " --> ", output_file)

with open(output_file, "w") as outfile:
    yaml.dump(
        json_instance,
        outfile,
        Dumper=Dumper,
        encoding="utf-8",
        default_flow_style=False,
        allow_unicode=None,
        indent=4,
    )
