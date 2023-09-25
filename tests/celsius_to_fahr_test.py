import importlib
import re
import celsius_to_fahr

def test_celsuis_to_fahr_boiling(capsys, monkeypatch):
    inputs, output = ("100", "212")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    celsius_to_fahr.main()
    captured = capsys.readouterr()
    assert output in captured.out
    
def test_celsuis_to_fahr_freezing(capsys, monkeypatch):
    inputs, output = ("0", "32")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    celsius_to_fahr.main()
    captured = capsys.readouterr()
    assert output in captured.out
    
def test_celsuis_to_fahr_comfortable(capsys, monkeypatch):
    inputs, output = ("70", "158")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    celsius_to_fahr.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_celsuis_to_fahr_negative(capsys, monkeypatch):
    inputs, output = ("-10", "14")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    celsius_to_fahr.main()
    captured = capsys.readouterr()
    assert output in captured.out