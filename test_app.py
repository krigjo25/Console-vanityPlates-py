#   Importing responsories
import pytest
from app import VanityPlates

def test_assertion_fails():

    v = VanityPlates()
    #   Ensures that the program outputs the correct information
    assert v.PlateValidation('A') == "Invalid"
    assert v.PlateValidation("AA()") == "Invalid"
    assert v.PlateValidation('012345') == "Invalid"
    assert v.PlateValidation('AA12AA') == "Invalid"
    assert v.PlateValidation("@.AA12") == "Invalid"
    assert v.PlateValidation("AA}]12") == "Invalid"
    assert v.PlateValidation("AA12/-") == "Invalid"
    assert v.PlateValidation('AAAAAAA') == "Invalid"
    assert v.PlateValidation('1234567') == "Invalid"
    assert v.PlateValidation('krigjo25') == "Invalid"


def test_assertion_success():

    v = VanityPlates()
    assert v.PlateValidation('CS50') == "Valid"
    assert v.PlateValidation('krigjo') == "Valid"
    assert v.PlateValidation('kak3') == "Valid"

