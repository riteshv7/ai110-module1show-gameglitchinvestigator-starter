from logic_utils import check_guess


def test_too_high_returns_lower_hint():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_returns_higher_hint():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_win():
    assert check_guess(50, 50)[0] == "Win"


def test_numeric_not_string_comparison():
    # As strings "9" > "50", so this would wrongly be "Too High"
    assert check_guess(9, 50)[0] == "Too Low"