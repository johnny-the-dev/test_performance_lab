from sys import argv
import json


def get_test_results_map() -> dict:
    with open(argv[1]) as file:
        values = json.load(file).get('values', [])

    test_results_map = {}
    for value in values:
        test_results_map[value['id']] = value.get('value', 'no result')

    return test_results_map


def get_tests() -> list:
    with open(argv[2]) as file:
        tests = json.load(file).get('tests', [])

    return tests


def write_to_json(tests: list) -> None:
    with open(argv[3], 'w') as output_file:
        json.dump(tests, output_file)


def set_value(test: dict, results_map: dict) -> None:
    if 'value' in test:
        test['value'] = results_map.get(test['id'], 'no result')

    if 'values' not in test:
        return

    for sub_test in test['values']:
        set_value(sub_test, results_map)


def main() -> None:

    if len(argv) != 4:
        print(
            'Error: incorrect number of arguments',
            'Usage: python task3.py <test_results_json> <test_cases_json> <output_json>',
            sep='\n'
        )
        return

    test_results_map = get_test_results_map()
    test_cases = get_tests()

    for test in test_cases:
        set_value(test, test_results_map)

    write_to_json(test_cases)


if __name__ == '__main__':
    main()
