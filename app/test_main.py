import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Qwertyqwerty", False),
        ("Str@ngstrong", False),
        ("str@ngstrong1", False),
        ("Stringstrong1", False),
        ("St@rin1", False),
        ("St@rin1St@rin1St@rin1", False),
        ("St@rin1стрінг", False),

    ],
    ids=[
        "valid_password",
        "pass_without_digit_and_symbol",
        "pass_without_digit",
        "pass_without_uppercase_letter",
        "pass_without_symbol",
        "too_small_pass",
        "too_big_pass",
        "pass_with_cyrilic_symbols",
    ]
)
def test_check_valid_password(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    ), f"Check_password with password={password} should return {result}!"
