# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Too slow
    # result = []
    # for query in queries:
    #     for path in files:
    #         if path.find(query) != -1:
    #             result.append(path)

    cache = {}

    for path in files:
        file = path.split("/")[-1]	        
        if file in cache:
            cache[file].append(path)
        else:
            cache[file] = [path]

    result = []
    for query in queries:
        if query in cache:
            results = cache[query]
            for path in results:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
