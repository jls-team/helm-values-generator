""" The generator module """
import os
import re
import sys


def find_yaml_files(directory):
    """Finds all yaml files by extension in directory

    Args:
        directory (str): directory to look in

    Returns:
        list: yaml files paths
    """
    yaml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                yaml_files.append(os.path.join(root, file))
    return yaml_files


def convert_to_yaml(keys):
    """Converts list values to yaml

    Args:
        keys (list): list of keys like ["key", "key1.key2"]

    Returns:
        str: yaml content
    """
    data = {}
    for key in keys:
        keys_list = key.split(".")
        temp_dict = data
        for k in keys_list[:-1]:
            if k not in temp_dict:
                temp_dict[k] = {}
            temp_dict = temp_dict[k]
        temp_dict[keys_list[-1]] = None

    def _convert_to_yaml_helper(data, indent=0):
        result = ""
        for key, value in data.items():
            result += "  " * indent + key + ":"
            if value is None:
                result += " <value>\n"
            else:
                result += "\n" + _convert_to_yaml_helper(value, indent + 1)
        return result

    return _convert_to_yaml_helper(data).rstrip()


def generate_values(path_to_scan):
    """Generates list of helm Values placeholders

    Args:
        path_to_scan (str): path of yaml file

    Returns:
        list: list of found values
    """
    all_yamls = find_yaml_files(path_to_scan)

    strings = []

    for yaml_file in all_yamls:
        with open(yaml_file, "r", encoding="utf8") as f:
            strings = re.findall(r"\{\{(.*?)\}\}", f.read())

    unique_list = list(set(strings))

    def _do_trim(value):
        has_filters = value.find("|")
        if has_filters > -1:
            value = value[0:has_filters]

        return value.replace(".Values.", "").strip()


    unique_list = list(map(_do_trim, unique_list))

    unique_list.sort()

    res_yaml = convert_to_yaml(unique_list)
    return res_yaml


def main():
    """Init
    """
    if len(sys.argv) == 1:
        print("No path to scan provided, run like python main.py <path>")
        sys.exit(1)

    path_to_scan = sys.argv[1]

    res_yaml = generate_values(path_to_scan)
    print(res_yaml)


if __name__ == "__main__":
    main()
