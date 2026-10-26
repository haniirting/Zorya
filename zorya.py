name: Zorya Interpreter

on: [push, pull_request]

jobs:
  run-zorya:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Install Python
      uses: actions/setup-python@v6
      with:
        python-version: '3.12'

    - name: Run Zorya
      run: |
        python3 -c "
        import sys
        sys.path.append('.')
        exec(open('zorya.py').read())
        interpreter = ZoryaInterpreter()  # создаём один раз
        interpreter.eval('print что 42')
        interpreter.eval('x = 100')
        interpreter.eval('print что x * 2')
        interpreter.eval('print что factorial(5)')
        "
