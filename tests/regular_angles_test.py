import importlib
import re
import regular_angles

def test_regular_angles_square(capsys, monkeypatch):
    inputs, outputs = ("4", [r"(?=.*exterior)(?=.*90)", r"(?=.*interior)(?=.*90)"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    regular_angles.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_regular_angles_pentagon(capsys, monkeypatch):
    inputs, outputs = ("5", [r"(?=.*exterior)(?=.*72)", r"(?=.*interior)(?=.*108)"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    regular_angles.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_regular_angles_triangle(capsys, monkeypatch):
    inputs, outputs = ("3", [r"(?=.*exterior)(?=.*120)", r"(?=.*interior)(?=.*60)"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    regular_angles.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)