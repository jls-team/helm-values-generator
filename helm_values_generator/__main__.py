""" __main__ """
import sys
from helm_values_generator import generate_values

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No path to scan provided, run like python main.py <path>")
        sys.exit(1)

    SCAN_PATH = sys.argv[1]

    res_yaml = generate_values(SCAN_PATH) # pylint: disable=E1102
    print(res_yaml)
