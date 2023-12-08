import pytest 
from app.registration import submit, email_validator, password_validator, insert_user, display_error

""" Create mock functions for testing """

@pytest.fixture
def mock_display_error(mocker):
    """
    This function will test the function in the registration file,
    display_error to ensure that errors are displaying.
    """
    return mocker.patch("app.registration.display_error")

@pytest.fixture
def mock_user_exists(mocker):
    """
    This function will test the function in the registration file,
    display_error to ensure that errors are displaying.
    """
    return mocker.patch("app.registration.user_exists")


def test_password_validator_valid():
    """
    This function will test the function in the registration file
    to make sure the password is being validated appropiately
    """
    # passwords to test
    password1 = "ValidP@ssw0rd"     # successful password
    password2 = "password"          # 8 characters, but no digit, uppercase letters, nor symbol
    password3 = "pass"              # not enough characters, no digit, uppercase, nor symbol
    password4 = "Password!"         # 8 characters, uppercase letter, and symbol, no digit
    password5 = "pass1234"          # 8 characters, digits, no symbol, nor uppercase

    # saving password test result
    result1 = password_validator(password1)
    result2 = password_validator(password2)
    result3 = password_validator(password3)
    result4 = password_validator(password4)
    result5 = password_validator(password5)


    # stating what is the expected result from the password test
    assert result1 is None
    assert result2 == "Password must include at least one special character and one number and cannot be longer than 50 characters."
    assert result3 == "Password must be at least 8 characters."
    assert result4 == "Password must include at least one special character and one number and cannot be longer than 50 characters."
    assert result5 == "Password must include at least one special character and one number and cannot be longer than 50 characters."

def test_email_validator_valid():
    """
    This function will test the function in the registration file
    to make sure the email is being validated appropiately
    """
    
    # emails to test
    email1 = "valid_email@email.com"
    email2 = "valid_email@email.com"
    email3 = "no_match_email@email.com"
    email4 = "invalid_email@email"
    email5 = "invalid_email@email"
 
    # saving email test results
    result1 = email_validator(email1, email2)
    result2 = email_validator(email1, email3)
    result3 = email_validator(email5, email4)
    
    # stating the expected results
    assert result1 is None                      # emails match and are valid
    assert result2 == "Emails do not match"     # emails do not match
    assert result3 == "Invalid email format"    # emails match but are invalid 


def test_insert_user(mock_display_error, mock_user_exists):
    """
    This function will test the function in the registration file
    to make sure the insert of users is actually inserting users.
    Will return True if insert is succesfull
    """
    email = "new_user@email.com"
    password = "G00dPasswrd!"
    mock_user_exists.return_value = False
    
    result = insert_user(email, password)
    assert result is True
    mock_display_error.assert_not_called()


def test_insert_user_failure(mock_display_error, mock_user_exists):
    """
    This function will test the function in the registration file
    to make sure the insert of users is actually inserting users.
    Will return False if user already exists
    """
    email = "existing_user@email.com"
    password = "G00dPasswrd!"
    mock_user_exists.return_value = True 
    
    result = insert_user(email, password)
    assert result is False
    mock_display_error.assert_called_once_with("Account already exists")
