import json
from collections import OrderedDict
import pprint

JSONPath = "data/test.json"

with open(JSONPath) as f:
    data = json.loads(f.read())
    print(data)

with open(JSONPath) as f:
    print(f.read())
