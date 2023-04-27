from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Test - Verifica se a função lança TypeError se key não é um inteiro
    try:
        encrypt_message("mensagem", "chave")
    except TypeError:
        pass
    else:
        assert False, "tipo inválido para key"

    # Test - Verifica se a função lança TypeError se message não é uma string
    try:
        encrypt_message(123, 2)
    except TypeError:
        pass
    else:
        assert False, "tipo inválido para message"

    assert encrypt_message("mensagem", 0) == "gnassemm"
    assert encrypt_message("mensagem", -2) == "gnassemm"
    assert encrypt_message("mensagem", 10) == "gnassemm"

    assert encrypt_message("mensagem", 3) == "nes_mgmassa"
    assert encrypt_message("123456789", 3) == "789_456123"

    assert encrypt_message("mensagem", 4) == "gmne_sassem"
    assert encrypt_message("12345678", 4) == "5678_1234"
