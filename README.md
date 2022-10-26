This is a minimal example for a bug in django-stubs.

# Preparation

1. Create and activate a virtualenv (tested with Python 3.7 and 3.8)
2. Install requirements
```shell
pip install -r requirements.txt
```
3. Run mypy on `baz.py`
```shell
mypy my_app/models/baz.py
```

# Output

```
my_app/models/baz.py:106: error: Name "Sequence" is not defined
Found 1 error in 1 file (checked 1 source file)
```

It makes no sense, because `baz.py` is 12 lines long and the name `Sequence` does not appear anywhere in the project.

