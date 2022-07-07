from typing import Dict
import unittest  # testのためのライブラリ
import json
import pprint


JSON_PATH = "data/target.json"


def load(jsonFile=JSON_PATH):
    """Load json from jsonFile to dict. (default is JSON_PATH)"""
    return json.load(open(jsonFile, "r", encoding="utf-8_sig"))


def getByDictionary(id, Dictionary):
    data = load().get("targetList", None)[id]
    for i in test["attribute"]:
        Dictionary["attribute"][i] = data.get("attribute", None)[i]


# The following is for testing


test = {
    "id": 0,
    "attribute": {
        "kind": None,
        "amount": None,
        "Period": None,
        "repeat": None,
        "active": None,
    },
}


print(test)
getByDictionary(test.get("id"), test)
print(test)
