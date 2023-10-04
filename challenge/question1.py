import json

def q1_mem(path_file):
    file = open(path_file)

    for line in file:
        tweet = json.loads(line).get('content')