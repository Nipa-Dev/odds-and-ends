import utils
from utils import PATH_FI, PATH_EN


def find_missing(full, partial, path=""):
    missing = []

    if isinstance(full, dict) and isinstance(partial, dict):
        for key in full:
            new_path = f"{path}.{key}" if path else key

            # key doesn't exist in file1 (partial)
            if key not in partial:
                missing.append(new_path)
            else:
                missing.extend(find_missing(full[key], partial[key], new_path))

    return missing


full_json = utils.return_json(PATH_EN)
partial_json = utils.return_json(PATH_FI)

missing_keys = find_missing(full_json, partial_json)

print("=== Keys missing from file1 (compared to file2) ===")
for key in missing_keys:
    print(key)
