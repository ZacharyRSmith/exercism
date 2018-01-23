def transform(legacy_data):
    res = {}

    for score in legacy_data.keys():
        for word in legacy_data[score]:
            res[word.lower()] = score

    return res
