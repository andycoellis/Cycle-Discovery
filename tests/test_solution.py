from code.solution import solution, IdNumber

import pytest


@pytest.mark.parametrize('n, b, result', [
	('210022', 3, 3),
	('1211', 10, 1)
	])
def test_solution(n, b, result):
	""" Check that given solutions passs """
	assert solution(n, b) == result


@pytest.mark.parametrize('n, b', [
	('1', 3),
	('1234567890', 10).
	(2, 2),
	('123', '123'),
	('ASA', 5),
	('123', 1),
	('123', 11),
	('00123', 5)
	])
def test_language(n, b):
	""" Validate that language passes requirements and edge cases """
	with pytest.raises(ValueError):
		solution(n, b)


@pytest.mark.parametrize('n, b', [
	('1234', 2),
	('1234', 3),
	('1234', 11)
	])
def test_class_input(n, b):