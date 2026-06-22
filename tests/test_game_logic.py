from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_too_high_not_too_low():
    # Regression: original bug returned "Too Low" when guess was above secret
    result = check_guess(60, 50)
    assert result == "Too High", "Guess above secret must return 'Too High', not 'Too Low'"

def test_hint_too_low_not_too_high():
    # Regression: original bug returned "Too High" when guess was below secret
    result = check_guess(40, 50)
    assert result == "Too Low", "Guess below secret must return 'Too Low', not 'Too High'"
