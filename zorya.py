# zorya.py — полный язык с цифрами и циклом
class ZoryaInterpreter:
    def __init__(self):
        self.vars = {}
        self.cycles = {}  # имя цикла -> (current, end)

    def eval(self, code: str):
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        i = 0
        while i < len(lines):
            line = lines[i]
            tokens = self._tokenize(line)
            if not tokens:
                i += 1
                continue

            # print что <выражение>
            if tokens[0] == 'print':
                if len(tokens) > 2 and tokens[1] == 'что':
                    expr = ' '.join(tokens[2:])
                    result = self._eval_expr(expr)
                    print(result)
                else:
                    print('Используй: print что 42')
            # переменная = выражение
            elif tokens[0] in self.vars:
                print(f"{tokens[0]} = {self.vars[tokens[0]]}")
            elif tokens[0] == '=':
                var = tokens[0]
                if tokens[1] == '=':
                    expr = ' '.join(tokens[2:])
                    self.vars[var] = self._eval_expr(expr)
                    print(f"{var} = {self.vars[var]}")
            # цикл
            elif tokens[0] == 'цикл':
                if len(tokens) >= 5 and tokens[2] == 'число':
                    cycle_name = tokens[1]
                    end = int(tokens[3])
                    self.cycles[cycle_name] = {'current': 0, 'end': end}
            elif tokens[0] == 'печать':
                if len(tokens) >= 3 and tokens[1] == 'цикл':
                    cycle_name = tokens[2]
                    if cycle_name in self.cycles:
                        print(self.cycles[cycle_name]['current'])
            elif tokens[0] == 'цифра':
                # просто число для выражения
                if len(tokens) >= 2 and tokens[1].isdigit():
                    return int(tokens[1])
            elif tokens[0] in self.vars:
                print(f"{tokens[0]} = {self.vars[tokens[0]]}")
            else:
                # обычное присвоение
                var = tokens[0]
                if tokens[1] == '=':
                    expr = ' '.join(tokens[2:])
                    self.vars[var] = self._eval_expr(expr)
                    print(f"{var} = {self.vars[var]}")
            i += 1

    def _tokenize(self, line: str):
        return line.lower().split()

    def _eval_expr(self, expr: str):
        # заглушка для сложных выражений — пока возвращаем число или строку
        if expr.isdigit():
            return int(expr)
        return expr  # можно потом расширить


# ====================== ТЕСТ ======================
if __name__ == "__main__":
    interpreter = ZoryaInterpreter()
    code = """
    x = 100
    print что x * 2
    цикл счетчик число 10
    печать цикл
    print что 42
    """
    interpreter.eval(code)
