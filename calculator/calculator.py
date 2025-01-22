# Saeed Abolhasani Kaleybar (4001830203)
from math import sin, cos
class Stack:
    def __init__(self) -> None:
        self.__stack = []
        self.top = -1
    
    def push(self, value: int) -> None:
        self.__stack.append(value)
        self.top += 1
    
    def pop(self, count=1) -> None:
        for i in range(count):
            self.__stack.pop()
        self.top -= count
       
    def __getitem__(self, index):
        return self.__stack[index]

class Storage:
    def __init__(self) -> None:
        self.__memory = [None for i in range(1000)]
        self.__i = -1
        self.__var = 399
        self.__temp_var = 599
        
    def insert(self, index: int, value: dict) -> None:
        self.__memory[index] = value
        
    def update(self, index: int, value: dict) -> None:
        self.__memory[index].update(value)
    
    def get_value(self, lexeme: str):
        try:
            for i in range(400, self.__var+1):
                if self.__memory[i].get("lex") == lexeme:
                    return (i, self.__memory[i])
        except:
            raise NameError(f"There is no variable name `{lexeme}`.")
    
    def get_temp(self) -> int:
        """Returns next `temporary variable` address to allocate"""
        self.__temp_var += 1
        self.__memory[self.__temp_var] = dict()
        return self.__temp_var
    
    def get_var(self) -> int:
        """Returns next `variable` address to allocate"""
        self.__var += 1
        return self.__var
    
    def get_i(self) -> int:
        """Return next `three addresses code` address"""
        self.__i += 1
        return self.__i

    def three_addresses_code(self) -> list:
        """Return all codes as list"""
        return self.__memory[:self.__i+1]
            
    def __getitem__(self, index) -> dict:
        return self.__memory[index]
    
    
rules = [
    ("Stmts", "Stmt;Left"),
    ("Left", "StmtsLeft"),
    ("Left", ""),
    ("Stmt", "print(id)`print`"),               # action
    ("Stmt", "id=Expr`assign`"),                # action
    ("Expr", "TermAdd"),
    ("Add", "+Term`addition`Add"),              # action
    ("Add", "-Term`subtract`Add"),              # action
    ("Add", ""),
    ("Term", "UnaryMul"),
    ("Mul", "*Unary`multiplication`Mul"),       # action
    ("Mul", "/Unary`division`Mul"),             # action
    ("Mul", ""),
    ("Unary", "-Unary`sign`"),                  # action
    ("Unary", "Pow"),
    ("Pow", "FactorLeftpow"),
    ("Leftpow", "**Pow`power`"),                # action
    ("Leftpow", ""),
    ("Factor", "(Expr)"),
    ("Factor", "id"),
    ("Factor", "sin(Expr)`sin`"),               # action
    ("Factor", "cos(Expr)`cos`"),               # action    
    ("Factor", "num"),
]

ll1 = {
    "Stmts": {"id": 0, "print": 0},
    "Left": {"id": 1, "print": 1, "$": 2},
    "Stmt": {"id": 4, "print": 3},
    "Expr": {"id": 5, "-": 5, "(": 5, "sin": 5, "cos": 5, "num": 5},
    "Add": {"+": 6, "-": 7, ")": 8, ";": 8, "$": 8},
    "Term": {"id": 9, "-": 9, "(": 9, "sin": 9, "cos": 9, "num": 9},
    "Mul": {"+": 12, "-": 12, "*": 10, "/": 11, ")": 12, ";": 12, "$": 12},
    "Unary": {"id": 14, "-": 13, "(": 14, "sin": 14, "cos": 14, "num": 14},
    "Pow": {"id": 15, "(": 15, "sin": 15, "cos": 15, "num": 15},
    "Leftpow": {"+": 17, "-": 17, "*": 17, "/": 17, "**": 16, ")": 17, ";": 17, "$": 17},
    "Factor": {"id": 19, "(": 18, "sin": 20, "cos": 21, "num": 22},
}

"""
lexical analyzer:
    creates tokens
"""
inp = ""
with open("input.txt", "r") as inp_file:
    inp = ''.join(list(inp_file.readlines()))
    inp_file.close()
inp = inp.replace("\n", "")
tokens = []
cal_inp = iter(inp)
char = next(cal_inp)

terminals = ["+", "-", "=", "/", ";", "(", ")", "*", "**", "print", "sin", "cos"]
def string_next():
    try:
        char = next(cal_inp)
    except StopIteration:
        char = "EOF!"
    return char

while True:
    if char == "EOF!":
        tokens.append({"token": "$"})
        break
    if char.isalpha():
        token = ""
        while (char.isalnum() or char == "_") and cal_inp != "EOF!":
                token += char
                char = string_next()
        if token in terminals:
            tokens.append({"token": token})
        else:
            tokens.append({"token": "id", "lex": token})
    elif char.isdigit():
        token = "#"
        while (char.isdigit() or char == "." or char.lower() == "e") and cal_inp != "EOF!":
                token += char
                char = string_next()       
        tokens.append({"token": "num", "value": token})
        
    elif char.isspace():
        char = string_next()
    
    elif char == "*":
        char = string_next()
        
        if char == "*":
            t = "**"
            char = string_next()
        else:
            t = "*"
        tokens.append({"token": t})
       
    elif char in terminals:
        tokens.append({"token": char})
        char = string_next()

"""
syntax analyzer:
    parsing input with LL(1) table, memory allocate and returns three addresses code.
"""
pb = Storage()
ss = Stack()
parser = "Stmts$"
tokens = iter(tokens)
lookahead = next(tokens)
while True:
    var = parser[0]
    if lookahead["token"] == "$":
        if var == "$":
            break
        elif var == ";":
            raise SyntaxError("missing `;` end of the input.")
        
    # actions
    if var == "`":
        action = ""
        for ch in parser[1:]:
            if ch == "`":
                break
            action += ch
        if action == "assign":
            i = pb.get_i()
            code = ("=", ss[ss.top], "", ss[ss.top-1])
            pb.insert(i, code)
            ss.pop(2)
            
        elif action == "print":
            i = pb.get_i()
            code = ("p", ss[ss.top], "", "")
            pb.insert(i, code)
            ss.pop()
            
        elif action == "sin" or action == "cos":
            if action == "sin":
                ac = "s"
            else:
                ac = "c"
            temp_var = pb.get_temp()
            i = pb.get_i()
            code = (ac, ss[ss.top], "", temp_var)
            
            pb.insert(i, code)
            ss.pop()
            ss.push(temp_var)
        elif action == "sign":
            temp_var = pb.get_temp()
            i = pb.get_i()
            code = ("*", "#-1", ss[ss.top], temp_var)
            pb.insert(i, code)
            ss.pop()
            ss.push(temp_var)    
        else:
            if action == "power":
                ac = "**"
            elif action == "multiplication":
                ac = "*"
            elif action == "division":
                ac = "/"    
            elif action == "addition":
                ac = "+"
            elif action == "subtract":
                ac = "-"
        
            temp_var = pb.get_temp()
            i = pb.get_i()
            code = (ac, ss[ss.top-1], ss[ss.top], temp_var)
            pb.insert(i, code)
            ss.pop(2)
            ss.push(temp_var)
        parser = parser[len(action)+2:]

    # derivation            
    else:
        if var.isalpha():
            for ch in parser[1:]:
                if not (ch.islower() and ch.isalpha()):
                    break
                var += ch
        
        if var == "*":
            if parser[1] == "*":
                var = "**"
        if lookahead["token"] == var:
            if lookahead["token"] == "id":
                lex = lookahead["lex"]
                try:
                    new_var = pb.get_value(lex)[0]
                except:
                    new_var = pb.get_var()
                pb.insert(new_var, {"lex": lex})
                ss.push(new_var)
            elif lookahead["token"] == "num":
                number = lookahead["value"]
                temp_var = pb.get_temp()
                i = pb.get_i()
                code = ("=", number, "", temp_var)
                pb.insert(i, code)
                ss.push(temp_var)
            parser = parser[len(var):]
            try:
                lookahead = next(tokens)
            except StopIteration:
                lookahead = "$"
        elif var in ll1:
            rule_number = ll1.get(var).get(lookahead["token"])
            specials = ["print", "sin", "cos"]
            t = lookahead["token"]
            if rule_number is not None:
                parser = parser.replace(var, rules[rule_number][1], 1)
            else:
                raise SyntaxError("Invalid syntax.")

"""
three addresses code executing.
"""        
codes = pb.three_addresses_code()           
with open("output.txt", "w") as o:
    for i in codes:
        o.writelines([str(i), '\n'])
        o.newlines
    o.close()

for code in codes:
    action, f_var_i, s_var_i, destination = code
    if type(f_var_i) is int:
        f_value = pb[f_var_i]["value"]
    elif type(f_var_i) is str:
        f_value = float(f_var_i[1:])
    if type(s_var_i) is int:
        s_value = pb[s_var_i]["value"]
       
    if action == "=":
        pb.update(destination, {"value": f_value})
    elif action == "+":
        pb.update(destination, {"value": f_value+s_value})
    elif action == "-":
        pb.update(destination, {"value": f_value-s_value})
    elif action == "**":
        pb.update(destination, {"value": f_value**s_value})
    elif action == "*":
        pb.update(destination, {"value": f_value*s_value})
    elif action == "/":
        pb.update(destination, {"value": f_value/s_value})
    elif action == "s":
        pb.update(destination, {"value": sin(f_value)})
    elif action == "c":
        pb.update(destination, {"value": cos(f_value)})
    elif action == "p":
        print(round(f_value, 4))