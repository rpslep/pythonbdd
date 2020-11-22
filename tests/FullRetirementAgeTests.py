import pytest
import FullRetirementAge

from pytest_bdd import scenarios, given, when, then


# Given Steps

@given("Full retirement age calculator is started")
def frac():
    FullRetirementAge.main()

# When Steps

@when("User enters birth year")
def frac_year(year, month):

        FullRetirementAge.retirement_calculator(year,month)


# Then Steps

@then("the retirement age and retirement date are shown")
def display():
    assert frac_year(1940,8) == "Your full retirement age is:  65  and  6  months. \nThis will be in  February  of  2006"

