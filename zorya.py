# zorya.py — интерпретатор языка Zorya
# (минимальный, но уже рабочий демо)

class ZoryaInterpreter:
    def __init__(self):
        self.vars = {}
    
    def eval(self, code: str):
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        i = 0
        while i < len(lines):
            line = lines[i]
            if not line:
                i += 1
                continue
            
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
                    print('Используй: print что 42')
            elif tokens[0] in self.vars:
                print(f"{tokens[0]} = {self.vars[tokens[0]]}")
            else:
                var = tokens[0]
                if tokens[1] == '=':
                    expr = ' '.join(tokens[2:])
                    self.vars[var] = self._eval_expr(expr)
                    print(f"{var} = {self.vars[var]}")
            i += 1
    
    def _tokenize(self, line: str):
        # пока простой split — в Zorya будет настоящий lexer
        return line.lower().replace('что', 'что').split()
    
    def _eval_expr(self, expr: str):
        return expr  # пока заглушка, потом добавим парсер


# ====================== ТЕСТ ======================
if __name__ == "__main__":
    interpreter = ZoryaInterpreter()
    
    code = """
    print что 42
    x = 100
    print что x
    print что x * 2
    """
    interpreter.eval(code)
