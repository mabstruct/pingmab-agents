from decimal import Decimal, getcontext


def calculate_series_terms(n_terms: int) -> Decimal:
    getcontext().prec = 30
    total = Decimal(0)
    for i in range(n_terms):
        term = Decimal(1) / Decimal(2 * i + 1)
        if i % 2 == 0:
            total += term
        else:
            total -= term
    return total * 4


if __name__ == "__main__":
    result = calculate_series_terms(1_000_000)
    print(result)
