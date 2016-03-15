import json
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('input', help='path to input file')
    parser.add_argument('output', help='path to output file')

    args = parser.parse_args()

    with open(args.input) as data_file:
        data = json.load(data_file)

        counter = 1
        for cell in data['cells'][:]:
            if cell['cell_type'] != 'code':
                continue

            cell['execution_count'] = counter
            counter += 1

        json.dump(data, open(args.output, 'w'))
