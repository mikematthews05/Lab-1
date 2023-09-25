import importlib
import rectangle_area

def test_rectangle_area_basic(capsys, monkeypatch):
    inputs, output = (iter(["5", "3"]), "15")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    rectangle_area.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_rectangle_area_floats(capsys, monkeypatch):
    inputs, output = (iter(["2.5", "3"]), "7.5")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    rectangle_area.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_rectangle_area_zero(capsys, monkeypatch):
    inputs, output = (iter(["0", "100"]), "0")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    rectangle_area.main()
    captured = capsys.readouterr()
    assert output in captured.out