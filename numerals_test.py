import numerals

def test_1(monkeypatch, capsys):
    inputs = iter(['22'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numerals.run()
    captured = capsys.readouterr()
    assert captured.out == ('XXII')


def test_2(monkeypatch, capsys):
    inputs = iter(['458'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numerals.run()
    captured = capsys.readouterr()
    assert captured.out == ('CDLVIII')


def test_3(monkeypatch, capsys):
    inputs = iter(['54379'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numerals.run()
    captured = capsys.readouterr()
    assert captured.out == ('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCCCLXXIX')