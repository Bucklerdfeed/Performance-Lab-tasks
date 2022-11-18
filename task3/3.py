import json
import sys

with open(sys.argv[1], 'r') as tests_file:
    tests = json.load(tests_file)

with open(sys.argv[2], 'r') as tests_values:
    values = json.load(tests_values)


def find_value_in_values(id):
    global values
    for value in values["values"]:
        if value["id"] == id:
            return value["value"]


def recursion_values(tests):
    for test in tests:
        if "value" in list(test.keys()):
            test["value"] = find_value_in_values(test["id"])
        if "values" in list(test.keys()):
            recursion_values(test["values"])


recursion_values(tests["tests"])

with open("report.json", 'w') as result_file:
    result_file.write(json.dumps(tests))
