import pytest
from pytest import approx
import ReadWriteGoogleSheet

def test_greentier():
	expected_grade = approx(90.876543)
	actual_grade = ReadWriteGoogleSheet.greentier()
	assert expected_grade == expected_grade

def test_yellowtier():
	expected_grade = approx(75.2136713)
	actual_grade = ReadWriteGoogleSheet.yellowtier()
	assert expected_grade == expected_grade

def test_redtier():
	expected_grade = approx(33.6787)
	actual_grade = ReadWriteGoogleSheet.redtier()
	assert expected_grade == expected_grade