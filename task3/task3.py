from sys import argv
import json


def set_value(test: dict, value_map: dict) -> None:
    if 'value' in test:
        test['value'] = value_map.get(test['id'], 'no result')

    if 'values' not in test:
        return

    for sub_test in test['values']:
        set_value(sub_test, value_map)


def main() -> None:

    if len(argv) < 4:
        print(
            'Error: not enough arguments',
            'Usage: python task3.py <values_json> <tests_json> <output_json>',
            sep='\n'
        )
        return

    with open(argv[1]) as values_file:
        values_lst = json.load(values_file).get('values', [])

    value_map = {}
    for value in values_lst:
        value_map[value['id']] = value.get('value', 'no result')

    with open(argv[2]) as tests_file:
        tests = json.load(tests_file).get('tests', [])

    for test in tests:
        set_value(test, value_map)

    with open(argv[3], 'w') as output_file:
        json.dump(tests, output_file)


if __name__ == '__main__':
    main()
