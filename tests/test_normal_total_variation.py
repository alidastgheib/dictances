from dictances import normal_total_variation
from utils import create_cases


def test_normal_total_variation():
    a, b = create_cases()
    assert (
        normal_total_variation(a, b)
    ) == (
        0.90432653097935
    )
