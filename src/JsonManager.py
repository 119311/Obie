import unittest  # testのためのライブラリ
import json
import pprint
import collections


JSON_PATH = "data/target.json"
JSON_PATH_W = "data/target_w.json"


def load(jsonFile=JSON_PATH):
    """Load json from jsonFile to dict. (default is JSON_PATH)"""
    return json.load(
        open(jsonFile, "r", encoding="utf-8_sig"),
    )


def save(data, jsonFile=JSON_PATH_W, mode="a"):
    """
    Damp to json from data(dict).
    mode="a" is append mode.
    mode="o" is overwrite mode.
    """
    dataOld = load()
    dataOld["targetList"].append(data)
    # pprint.pprint(dataOld)
    # print(json.dumps(dataOld, ensure_ascii=False, indent=2))
    with open(JSON_PATH_W, mode="wt", encoding="utf-8") as file:
        json.dump(dataOld, file, ensure_ascii=False, indent=4)


def getByDictionary(id, Dictionary):
    data = load().get("targetList", None)[id]
    for i in Dictionary["attribute"]:
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
test2 = {
    "id": 4,
    "attribute": {
        "kind": "食事",
        "amount": 12121,
        "Period": None,
        "repeat": None,
        "active": None,
    },
}


print(test)
getByDictionary(test.get("id"), test)
print(test)
save(test2)
