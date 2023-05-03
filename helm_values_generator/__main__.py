from helm_values_generator import generate_values
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No path to scan provided, run like python main.py <path>")
        sys.exit(1)
    
    path_to_scan = sys.argv[1]

    res_yaml = generate_values(path_to_scan)
    print(res_yaml)