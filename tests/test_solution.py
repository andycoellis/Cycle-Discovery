from code.solution import solution

import pytest


@pytest.mark.parametrize('n, b, result', [
	('210022', 3, 3),
	('1211', 10, 1)
	])
def test_solution(n, b, result):
	assert solution(n, b) == result