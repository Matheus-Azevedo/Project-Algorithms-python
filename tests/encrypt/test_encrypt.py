from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # test TypeError for key
    try:
        encrypt_message("message", "key")
    except TypeError as err:
        assert str(err) == "tipo inválido para key"

    # test TypeError for message
    try:
        encrypt_message(123, 1)
    except TypeError as err:
        assert str(err) == "tipo inválido para message"

    # test key not in range
    assert encrypt_message("message", 0) == "egassem"

    # test key in range
    assert encrypt_message("message", 1) == "egassem"
