import math


def sample_mean(data):
    return sum(data) / len(data)


def sample_standard_deviation(data):
    mean_val = sample_mean(data)
    variance = sum((x - mean_val) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)


def t_critical_value(sample_size, confidence_level):
    """
    Calculate the critical t-value for a given sample size and confidence level.

    Parameters:
        sample_size (int): Size of the sample.
        confidence_level (float): Desired confidence level (e.g., 0.95 for 95% confidence).

    Returns:
        float: Critical t-value for the specified sample size and confidence level.
    """
    alpha = 1 - confidence_level
    degrees_of_freedom = sample_size - 1
    t_value = 0  # Initial guess
    step = 1.0
    tolerance = 1e-6
    while step > tolerance:
        previous_t_value = t_value
        t_value = _inverse_t_distribution(1 - alpha / 2, degrees_of_freedom)
        step = abs(t_value - previous_t_value)
        alpha /= 2
    return t_value


def confidence_interval(data, confidence=0.95):
    """
    Calculate the confidence interval for the given data and confidence level.

    Parameters:
        data (list): List of numerical data points.
        confidence (float, optional): Desired confidence level (default is 0.95 for 95% confidence).

    Returns:
        tuple: Lower and upper bounds of the confidence interval.
    """
    n = len(data)
    t_value = t_critical_value(n, confidence)
    margin_of_error = t_value * (sample_standard_deviation(data) / math.sqrt(n))
    mean_val = sample_mean(data)
    return mean_val - margin_of_error, mean_val + margin_of_error


def _inverse_t_distribution(p, df):
    """Approximation of the inverse t-distribution function."""
    p = 1 - p
    a = (1 - df) / 2
    b = 2 * df + 1
    c = 1 - 2 / (9 * b)
    d = c * (math.pow(p, 1 / b) - 1)
    if d < 0:
        return 0  # Return 0 if d is negative to prevent math domain error
    return -math.sqrt(d + a / b) / math.sqrt(c)
