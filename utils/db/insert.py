import db

def handle_recursive_insert(datas, fn, arg=None):
    if not type(datas) is list:
        datas = [datas]

    for data in datas:
        nested_keys = [k for k in data.keys() if k.endswith('s')]
        nested = [[data.pop(k), getattr(db, 'create_'+k)] for k in nested_keys]
        # insert the parent data
        obj = fn(data, arg)
        # insert nested data
        for nest in nested:
            nest.append(obj)
            handle_recursive_insert(*nest)

if __name__ == '__main__':
    pass
