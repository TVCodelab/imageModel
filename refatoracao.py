from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Statistics:
    total: float
    average: float
    maximum: float
    minimum: float


def compute_statistics(numbers: Iterable[float]) -> Statistics:
    numbers = list(numbers)
    if not numbers:
        raise ValueError("numbers must contain at least one value")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return Statistics(total=total, average=average, maximum=maximum, minimum=minimum)


def main() -> None:
    values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    stats = compute_statistics(values)

    print(f"total: {stats.total}")
    print(f"media: {stats.average}")
    print(f"maior: {stats.maximum}")
    print(f"menor: {stats.minimum}")


if __name__ == "__main__":
    main()
