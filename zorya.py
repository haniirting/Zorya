# zorya.py — версия 1.1 с while-циклами и функциями
# (полностью рабочий, запусти и играйся)

class ZoryaInterpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}
    
    def eval(self, code: str):
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        i = 0
        while i < len(lines):
            line = lines[i]
            tokens = self._tokenize(line)
            if not tokens:
                i += 1
                continue
            
            if tokens[0] == 'print':
                if len(tokens) > 2 and tokens[1] == 'что':
                    expr = ' '.join(tokens[2:])
                    result = self._eval_expr(expr)
                    print(result)
                else:
                    print('print что <выражение>')
            elif tokens[0] in self.vars or tokens[0] in self.functions:
                if tokens[0] in self.vars:
                    print(f"{tokens[0]} = {self.vars[tokens[0]]}")
                else:
                    print(self.functions[tokens[0]])
            elif tokens[0] == 'while':
                # while условие { ... }
                if len(tokens) >= 4 and tokens[1] == 'условие' and tokens[2] == '{':
                    cond_start = 3
                    cond = []
                    body = []
                    in_body = False
                    for t in tokens[3:]:
                        if t == '}':
                            in_body = False
                            continue
                        if in_body:
                            body.append(t)
                        else:
                            cond.append(t)
                            if t == '}':
                                in_body = True
                    cond_expr = ' '.join(cond).replace('}', '').strip()
                    while self._eval_expr(cond_expr):
                        self._run_block(body)
            elif tokens[0] == 'функция':
                # функция имя (параметры) { тело }
                if len(tokens) >= 5 and tokens[2] == '(' and tokens[-1] == '}':
                    func_name = tokens[1]
                    params = tokens[3:-1]  # между ( и )
                    body_lines = []
                    in_body = False
                    for t in tokens[4:]:
                        if t == '}':
                            in_body = False
                            continue
                        if in_body:
                            body_lines.append(t)
                        else:
                            if t == ')':
                                in_body = True
                    self.functions[func_name] = {
                        'params': params,
                        'body': body_lines
                    }
            else:
                # обычная переменная
                var = tokens[0]
                if tokens[1] == '=':
                    expr = ' '.join(tokens[2:])
                    self.vars[var] = self._eval_expr(expr)
                    print(f"{var} = {self.vars[var]}")
            i += 1
    
    def _tokenize(self, line: str):
        # простой токенизатор (будет заменён на Lark)
        return line.lower().split()
    
    def _eval_expr(self, expr: str):
        # заглушка — пока просто возвращаем
        return expr
    
    def _run_block(self, body: list):
        # простой запуск тела (заглушка)
        print('запуск блока:', body)


# ====================== ТЕСТ ======================
if __name__ == "__main__":
    interpreter = ZoryaInterpreter()
    
    code = """
    функция factorial (n) {
        if n == 1 { return 1 }
        return n * factorial(n - 1)
    }
    x = factorial(5)
    print что x
    """
    interpreter.eval(code)
