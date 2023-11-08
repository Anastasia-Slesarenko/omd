from morse import decode
import pytest


@pytest.mark.parametrize(
        "source_string, result",
        [
            ("... --- ...", "SOS"),
            ("-- -.-- -....- - . ... - ...", "MY-TEST\123"),
            ("-.--. ..--.. -.--.-", "(?)"),
            ("", "")
        ],
)
def test_morse(source_string, result):
    assert decode(source_string) == result


if __name__ == "__main__":
    pass
