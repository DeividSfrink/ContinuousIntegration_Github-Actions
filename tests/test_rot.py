from app.rot_cipher import rot13


class TestClass:
    def test_rot13_cipher(self):
        assert rot13("DUCK") == "QHPX"
