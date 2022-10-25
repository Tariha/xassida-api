from pathlib import Path
from models import Author
from dataclasses import asdict
import json

def parse_author_data(file):
    author_data = {'name':file.stem, 'tariha':file.parent.stem, 'xassidas':[]}
    for xassida in file.glob('*/*.json'):
        print("Adding %s => %s"%(file.stem, xassida.stem))
        xassida_data = json.loads(xassida.read_text())
        author_data['xassidas'].append(xassida_data)

    out_file = file / 'xassidas.json'
    out_file.write_text(json.dumps(asdict(Author(**author_data)), ensure_ascii=False))


if __name__ == '__main__':
    for file in Path("../../data/xassida").glob("*/*"):
        parse_author_data(file)
