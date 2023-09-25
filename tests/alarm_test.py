import importlib
import re
import hours_til_alarm

def test_hours_to_alarm_basic(capsys, monkeypatch):
    inputs, output = (iter(["3", "4"]), "1")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    hours_til_alarm.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_hours_to_alarm_basic2(capsys, monkeypatch):
    inputs, output = (iter(["2", "12"]), "10")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    hours_til_alarm.main()
    captured = capsys.readouterr()
    assert output in captured.out
    
def test_hours_to_alarm_twelves(capsys, monkeypatch):
    inputs, output = (iter(["12", "0"]), "12")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    hours_til_alarm.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_hours_to_alarm_tomorrow(capsys, monkeypatch):
    inputs, output = (iter(["18", "8"]), "14")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    hours_til_alarm.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_hours_to_alarm_23(capsys, monkeypatch):
    inputs, output = (iter(["12", "11"]), "23")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    hours_til_alarm.main()
    captured = capsys.readouterr()
    assert output in captured.out