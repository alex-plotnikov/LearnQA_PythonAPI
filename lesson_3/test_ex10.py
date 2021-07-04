class TestInput:
    def test_user_input(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Phrase has more than 15 symbols"
