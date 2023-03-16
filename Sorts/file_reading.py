
def read_from_file(filepath):
    with open(filepath, 'r') as file_handle:
        lines = [line.rstrip() for line in file_handle]
    return lines


