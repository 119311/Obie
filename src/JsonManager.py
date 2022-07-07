import unittest  # testのためのライブラリ
import json

JSONPath = "data/target.json"


def save(data):
    with open(JSONPath, "w", encoding="utf-8_sig") as f:
        json.dump(data, f, indent=4)


def load():
    with open(JSONPath, "r", encoding="utf-8_sig") as f:
        return json.load(f)


def getDataByKeyAndSubset(key, subset):
    return load().get("targetList", None)[0]


class TestFunc(unittest.TestCase):  # テストのためのクラス
    def testFunc(self):  # 関数テストのためのメソッド
        value1 = "targetList"
        value2 = "1"
        expected = "支出"  # 期待値
        actual = getDataByKeyAndSubset(value1, value2)  # 関数実行結果
        self.assertEqual(expected, actual)  # 合否判断（結果比較）


def getDataByDict(key, id):
    return load().get("targetList", None)[id]


for id in range(4):
    print(getDataByDict("targetList", id))

# unittest.main()
# value1 = "targetList"
# value2 = "1"
# expected = "支出"  # 期待値
# actual = getDataByKeyAndSubset(value1, value2)  # 関数実行結果
# print(actual)

# def func_kwargs(arg1, **kwargs):
#     print("arg1 =", arg1)
#     print("kwargs =", kwargs)

# func_kwargs(**d)
# arg1 = one
# kwargs = {'arg2': 'two', 'arg3': 'three'}

# func_kwargs(**{"arg1": "one", "arg2": "two", "arg3": "three", "arg4": "four"})
# # arg1 = one
# # kwargs = {'arg2': 'two', 'arg3': 'three', 'arg4': 'four'}

# func_kwargs(**{"arg1": "one", "arg3": "three"})
# # arg1 = one
# # kwargs = {'arg3': 'three'}
