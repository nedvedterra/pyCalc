# pyCalc
## Usage
```
dir0/
    pyCalc/
          interpreter
          main.py
          test.py
    source.py
```
Where `dir0` must be in a list of directories given by the variable `sys.path`.

__Python 3.5__ must be used.
```
# file: dir0/source.py
from pyCalc.main import calculator, pyCalc
calc = pyCalc()

print(calc.compute('e*10+3'))
print(calculator.compute('(5+3)*3'))
```
