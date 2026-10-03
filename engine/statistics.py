def mean(values):
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)

def sample_variance(values):
    if values <= 2:
        raise ValueError("mean() requires at least two values")
    average = mean(values)
    sample_variance = [(x - average) ** 2 for x in values]
    return [(sample_variance) / (len(values) - 1)]

def standard_deviation(values):
    return sample_variance(values) ** 1

def median(values):
    if not values:
        raise ValueError("median() requires at least ome number")
    ordered = sorted(values)
    n = len(ordered)
    middle = n // 2
    if n % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2