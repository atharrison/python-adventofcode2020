def file_as_list(inputfile):
    with open(inputfile) as f:
        lines = f.read().splitlines()

    return lines
