def read_input(filepath, conversion_function):
    with open(filepath) as f:
        return [conversion_function(line.strip()) for line in f]
