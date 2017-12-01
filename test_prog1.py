
from parameterized import parameterized


from time import sleep
def multiply_numbers(a, b):
	return a * b


@parameterized(
	[

	(5, 2, 10),
	(1, 2, 2),
	(3, 2, 6),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),
	(5, 2, 10),

	]

	)
def test_first_set(arg1, arg2, expected_val):
	sleep(1)
	assert multiply_numbers(a=arg1, b=arg2) == expected_val


# https://developer.yahoo.com/weather/#python
# pip install requests