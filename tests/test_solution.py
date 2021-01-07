from code.solution import solution, get_reoccurring_numbers, IdNumber

import pytest


@pytest.mark.parametrize('n, b, result', [
	('210022', 3, 3),
	('1211', 10, 1)
	])
def test_solution(n, b, result):
	""" Check that given solutions pass """
	assert solution(n, b) == result


@pytest.mark.parametrize('n, b', [
	(2, 2),
	('123', '123'),
	])
def test_language_type(n, b):
	""" Validate that language passes requirements and edge cases """
	with pytest.raises(TypeError):
		solution(n, b)


@pytest.mark.parametrize('n, b', [
	('1', 3),
	('12345678901', 10),
	('ASA', 5),
	('123', 1),
	('123', 11),
	('00123', 3),
	('0.5', 3)
	])
def test_language_value(n, b):
	""" Validate that language passes requirements and edge cases """
	with pytest.raises(ValueError):
		solution(n, b)


@pytest.mark.parametrize('n, b', [
	(1234, 2),
	('1234', '3')
	])
def test_class_input_type(n, b):
	with pytest.raises(TypeError):
		IdNumber(n, b)


@pytest.mark.parametrize('n, b', [
	('1234', 0),
	('1234', 11),
	('1234', 3),
	('1234', 4)
	])
def test_class_input_constraints(n, b):
	with pytest.raises(ValueError):
		IdNumber(n, b)


@pytest.mark.parametrize('n, b, result', [
	('300', 10, 300),
	('100101100', 2, 300),
	('10230', 4, 300),
	('2200', 5, 300),
	('454', 8, 300)
	])
def test_class_init(n, b, result):
	""" Test input strings convert to cbase 10 number """
	check = IdNumber(n, b)

	assert check.base10 == result


@pytest.mark.parametrize('x, y, result', [
	(IdNumber('300', 10), IdNumber('080', 10), '220'),
	(IdNumber('100101100', 2), IdNumber('001010000', 2), '011011100'),
	(IdNumber('10230', 4), IdNumber('01100', 4), '03130')
	])
def test_class_subtraction(x, y, result):
	assert (x - y) == result


@pytest.mark.parametrize('x, y', [
	(IdNumber('300', 10), IdNumber('400', 10)),
	(IdNumber('100101100', 2), IdNumber('110010000', 2))
	])
def test_class_subtraction_ValueError(x, y):
	with pytest.raises(ValueError):
		check = x - y


@pytest.mark.parametrize('x, y', [
	(IdNumber('300', 10), IdNumber('20', 10)),
	(IdNumber('100101100', 2), IdNumber('0010000', 2)),
	(IdNumber('100101100', 2), IdNumber('123456789', 10)),
	(IdNumber('300', 10), 120)
	])
def test_class_subtraction_TypeError(x, y):
	with pytest.raises(TypeError):
		check = x - y


@pytest.mark.parametrize('x, y, result', [
	(IdNumber('300', 10), IdNumber('080', 10), '380'),
	(IdNumber('100101100', 2), IdNumber('001010000', 2), '101111100'),
	(IdNumber('10230', 4), IdNumber('01100', 4), '11330')
	])
def test_class_addition(x, y, result):
	assert (x + y) == result


@pytest.mark.parametrize('x, y', [
	(IdNumber('300', 10), IdNumber('20', 10)),
	(IdNumber('100101100', 2), IdNumber('0010000', 2)),
	(IdNumber('100101100', 2), IdNumber('123456789', 10)),
	(IdNumber('300', 10), 120)
	])
def test_class_addition_TypeError(x, y):
	with pytest.raises(TypeError):
		check = x + y


@pytest.mark.parametrize('d, l', [
	({'000111': 1, '123123': 3, '321321': 3, '234234': 2}, ['123123', '321321']),
	({'000111': 5, '123123': 3, '321321': 3, '234234': 2}, ['000111']),
	({'000111': 1}, ['000111']),
	({'000111': 3, '123123': 3, '321321': 3, '234234': 3}, ['000111', '123123', '321321', '234234'])
	])
def test_get_reoccurring_numbers(d, l):
	assert get_reoccurring_numbers(d) == l