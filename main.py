import json
from remover.remover import Remover

if __name__ == '__main__':
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    if "root" not in config:
        raise KeyError('root is required argument')

    remover_instance = Remover(config["root"],
                               delete_dir=config.get("delete_dir"),
                               file_ext=config.get("file_ext"),
                               parent_ext=config.get("parent_ext"))
    remover_instance.delete_parentless_file()

    print("Success!")
