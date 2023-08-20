import argparse
import json
from pathlib import Path

import helpers


def handle_recursive_insert(datas, fn, arg=None):
    if fn.__name__ == "create_chapters":
        # chapters are saved in a dict
        datas = list(datas.values())

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

    # start parsing files
    for file in Path("../../data/xassidas").glob(glob_path):
        data = json.loads(file.read_text())
        if args.xassida:
            author_file = file.parent.parent / "xassidas.json"
            author_data = json.loads(author_file.read_text())
            author_data["xassidas"] = [data]
            data = author_data
        print("Inserting to db %s xassidas" % (data["name"]))
        handle_recursive_insert(data, helpers.create_author)
