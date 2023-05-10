import argparse
import json
from pathlib import Path

import helpers


def handle_recursive_insert(datas, fn, arg=None):
    if not type(datas) is list:
        datas = [datas]

    for data in datas:
        nested_keys = [k for k in data.keys() if k.endswith("s")]
        nested = [[data.pop(k), getattr(helpers, "create_" + k)] for k in nested_keys]
        # insert the parent data
        obj = fn(data, arg)
        # insert nested data
        for nest in nested:
            nest.append(obj)
            handle_recursive_insert(*nest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tariha", help="The tariha of the authors")
    parser.add_argument("-a", "--author", help="The author of the xassida")
    parser.add_argument("-x", "--xassida", help="The xassida")
    args = parser.parse_args()
    glob_path = f"{args.tariha}/" if args.tariha else "*/"
    glob_path += f"{args.author}/" if args.author else "*/"
    glob_path += f"{args.xassida}/*.json" if args.xassida else "*.json"
    # getting the insert function
    insert_function = helpers.create_xassidas if args.xassida else helpers.create_author
    # start parsing files
    for file in Path("../../data/xassidas").glob(glob_path):
        author = file.parent.parent.stem if args.xassida else file.parent.stem
        print("Inserting to db %s xassidas" % (author))
        data = json.loads(file.read_text())
        handle_recursive_insert(data, insert_function, author)
