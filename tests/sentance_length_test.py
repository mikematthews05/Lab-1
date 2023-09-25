import importlib
import re
import sentance_length

def test_sentance_len_basic(capsys, monkeypatch):
    inputs, outputs = ("test this code", ["14", "10"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    sentance_length.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_sentance_len_blank(capsys, monkeypatch):
    inputs, outputs = ("", ["0", "0"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    sentance_length.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_sentance_len_round_down(capsys, monkeypatch):
    inputs, outputs = ("don't round up to thirty pls", ["28", "20"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    sentance_length.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)