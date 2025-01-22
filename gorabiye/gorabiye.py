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
    def __str__(self):
        return str(self.__stack)   
    def __getitem__(self, index):
        return self.__stack[index]

class Storage:
    def __init__(self) -> None:
        self.__memory = [None for i in range(2000)]
        self.__i = -1
        self.__var = 399
        self.__temp_var = 599
        
    def insert(self, index: int, value: dict, flag="insert") -> None:
        if flag == "insert":
            self.__memory[index] = value
        elif flag == "update":
            x = list(self.__memory[index])
            x[value[0]] = value[1]
            self.__memory[index] = tuple(x)
            
    def update(self, index: int, value: dict) -> None:
        self.__memory[index].update(value)
    
    def get_value(self, lexeme: str):
        try:
            for i in range(400, self.__var+1):
                if self.__memory[i].get("lex") == lexeme:
                    return (i, self.__memory[i])
        except:
            raise NameError(f"There is no variable name `{lexeme}`.")
    
    def current(self) -> dict:
        return {"i": self.__i, "temp": self.__temp_var, "var": self.__var}
    
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

    def three_addresses_code(self, index=None) -> list:
        """Return all or one of list"""
        if index:
            return self.__memory[index]
        return self.__memory[:self.__i+1]    
    def __getitem__(self, index) -> dict:
        return self.__memory[index]   
    
rules = [
    ("Stmts", "Stmt;Left"),
    ("Left", "Stmts"),
    ("Left", ""),
    ("Stmts", "BlockSt"),
    ("St", "Stmts"),
    ("St", ""),
    ("Block", "if(Be)`jumpF`then{Stmts}`jumpT`Cont`end`"),                       # action
    ("Cont", "elif`setJumpF`(Be)`jumpF`then{Stmts}`jumpT`Cont`end`"),            # action
    ("Cont", "`setJumpF`else{Stmts}"),                                      # action
    ("Cont", ""),
    ("Block", "while`label`(Be)`jumpF`do{Stmts}`jump``endW`"),          # action
    ("Be", "CondOp"),
    ("Op", "andBe`and`"),                                                   # action
    ("Op", "orBe`or`"),                                                     # action    
    ("Op", "notBe`not`"),                                                   # action
    ("Op", ""),
    ("COND", "ExprCmpr"),
    ("Cmpr", "==Expr`eq`"),                                                 # action
    ("Cmpr", ">=Expr`gte`"),                                                # action
    ("Cmpr", "<=Expr`lte`"),                                                # action
    ("Cmpr", ">Expr`gt`"),                                                  # action
    ("Cmpr", "<Expr`lt`"),                                                  # action
    ("Cmpr", "!=Expr`neq`"),                                                # action
    ("Cmpr", ""),
    ("Stmt", "print(Expr)`print`"),                                           # action
    ("Stmt", "id=Expr`assign`"),                                            # action
    ("Expr", "TermAdd"),
    ("Expr", "notExpr`not`"),
    ("Add", "+Term`addition`Add"),                                          # action
    ("Add", "-Term`subtract`Add"),                                          # action
    ("Add", ""),
    ("Term", "UnaryMul"),
    ("Mul", "*Unary`multiplication`Mul"),                                   # action
    ("Mul", "/Unary`division`Mul"),                                         # action
    ("Mul", ""),
    ("Unary", "-Unary`sign`"),                                              # action
    ("Unary", "Pow"),
    ("Pow", "FactorLeftpow"),
    ("Leftpow", "**Pow`power`"),                                            # action
    ("Leftpow", ""),
    ("Factor", "(Be)"),
    ("Factor", "id"),
    ("Factor", "sin(Expr)`sin`"),                                           # action
    ("Factor", "cos(Expr)`cos`"),                                           # action
    ("Factor", "num"),
    ("Factor", "true"),
    ("Factor", "false"),
]

ll1 = {
    "Stmts": {"id": 0, "print": 0, "if": 3, "while": 3, "+": "e0"},
    "Left": {"id": 1, "print": 1, "if":1, "while": 1, "}": 2,"$": 2},
    "St": {"id": 4,"if": 4,"while": 4, "print": 4, "}": 5, "$": 5},
    "Block": {"if": 6, "while":  10},
    "Cont": {"id": 9, "if": 9, "while": 9, "}": 9, "elif": 7, "else": 8, "print": 9, "$": 9},
    "Be": {"id": 11, "-": 11, "not": 11, "sin": 11, "cos": 11, "(": 11, "num": 11, "true": 11, "false": 11},
    "Op": {"and": 12, "or": 13, "not": 14, ")": 15, "do": 15},
    "Cond": {"id": 16, "-": 16, "not": 16, "sin": 16, "cos": 16, "(": 16, "num": 16, "true": 16, "false": 16},
    "Cmpr": {"==": 17, ">=": 18, "<=": 19, "!=": 22, "and": 23, "or": 23, "not": 23, ")": 23, "do": 23, ">": 20, "<": 21},
    "Stmt": {"id": 25, "print": 24},
    "Expr": {"id": 26, "-": 26, "not": 27, "sin": 26, "cos": 26, "(": 26, "num": 26, "true": 26, "false": 26, },
    "Add": {"+": 28, "-": 29, "==": 30, ">=": 30, "<=": 30, "!=": 30, "and": 30, "or": 30, "not": 30, ")": 30, ";": 30, "do": 30, ">": 30, "<": 30},
    "Term": {"id": 31, "-": 31, "sin": 31, "cos": 31, "(": 31, "num": 31, "true": 31, "false": 31},
    "Mul": {"+": 34, "-": 34, "*": 32, "/": 33, "==": 34, ">=": 34, "<=": 34, ">": 34, "<": 34, "!=": 34, "and": 34, "or": 34, "not": 34, ")": 34, ";": 34, "do": 34},
    "Unary": {"id": 36, "-": 35, "sin": 36, "cos": 36, "(": 36, "num": 36, "true": 36, "false": 36},
    "Pow": {"id": 37, "sin": 37, "cos": 37, "(": 37, "num": 37, "true": 37, "false": 37},
    "Leftpow": {"+": 39, "-": 39, "*": 39, "/": 39, "**": 38, "==": 39, ">=": 39, "<=": 39, "!=": 39, ">": 39, "<": 39, "and": 39, "or": 39, "not": 39, ")": 39, ";": 39, "do": 39},
    "Factor": {"id": 41, "sin": 42, "cos": 43, "(": 40, "num": 44, "true": 45, "false": 46},
}

errors = {
    "e0": "operand is missing.",
    "e1": "missing if statement.",
    "e2": "no iteration found",
    
     
}
"""
lexical analyzer:
    creates tokens
"""
inp = ""
with open("input.txt", "r") as inp_file:
    inp = ''.join(list(inp_file.readlines()))
    inp_file.close()
print(inp)
tokens = []
cal_inp = iter(inp)
char = next(cal_inp)
terminals = ["+", "-", "=", "==", ">=", "<=", ">", "<", "!=", "/", ";", "(", ")", "*", "**", "print", "sin", "cos", "{", "}", "true", "false", "and", "or", "not",
             "if", "elif", "else", "while", "then", "do"]
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
    elif char == "=":
        char = string_next()
        if char == "=":
            t = "=="
            char = string_next()
        else:
            t = "="
        tokens.append({"token": t})
    elif char == ">" or char == "<" or char == "!":
        x = char
        char = string_next()
        if char == "=":
            t = f"{x}{char}"
            char = string_next()
        else:
            t = x
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
            code = ("=", ss[ss.top], "", ss[ss.top-1])
            ss.pop(2)
            
        elif action == "print":
            code = ("p", ss[ss.top], "", "")
            ss.pop()
            
        elif action == "sin" or action == "cos":
            if action == "sin":
                ac = "s"
            else:
                ac = "c"
            temp_var = pb.get_temp()
            code = (ac, ss[ss.top], "", temp_var)
            ss.pop()
            ss.push(temp_var)
            
        elif action == "sign":
            temp_var = pb.get_temp()
            code = ("*", "#-1", ss[ss.top], temp_var)
            ss.pop()
            ss.push(temp_var)
            
        elif action == "jumpF":
            i = pb.get_i()
            pb.insert(i, ("jump", ss[ss.top], "", ""))
            ss.pop()
            ss.push(i)
            
        elif action == "jumpT":
            i = pb.get_i()
            pb.insert(i, ("jump", "", "", ""))
            ss.push(i) 
                 
        elif action == "setJumpF":
            next_i = pb.current()['i']+1
            prev_i = ss[ss.top-1]
            pb.insert(prev_i, (3, next_i), flag="update")
            top = ss[ss.top]
            ss.pop(2)
            ss.push(top)
              
        elif action == "end":
            next_i = pb.current()['i']+1
            prev_i = ss[ss.top]
            pb.insert(prev_i, (3, next_i), flag="update")
            ss.pop()
                
                
        elif action == "endW":
            next_i = pb.current()['i']+1
            prev_i = ss[ss.top]
            pb.insert(prev_i, (3, next_i), flag="update")
            ss.pop(2) 
                    
        elif action == "jump":
            i = pb.get_i()
            pb.insert(i, ("jump", "", "", ss[ss.top-1]))
        
        elif action == "label":
            next_i = pb.current()['i']+1
            ss.push(next_i)
            
        elif action == "not":
            temp_var = pb.get_temp()
            code = (ac, ss[ss.top], "", temp_var)
            ss.pop(1)
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
            elif action == "and":
                ac = "&" 
            elif action == "or":
                ac = "|"
            elif action == "eq":
                ac = "==" 
            elif action == "gte":
                ac = ">=" 
            elif action == "lte":
                ac = "<=" 
            elif action == "gt":
                ac = ">" 
            elif action == "lt":
                ac = "<" 
            elif action == "neq":
                ac = "!="
            temp_var = pb.get_temp()
            code = (ac, ss[ss.top-1], ss[ss.top], temp_var)
            ss.pop(2)
            
            ss.push(temp_var)
        
        if code:
            i = pb.get_i()    
            pb.insert(i, code)
        parser = parser[len(action)+2:]
        code = None

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
        elif var == "=":
            if parser[1] == "=":
                var = "=="
        
        elif var == ">" or var == "<" or var == "!":
            if parser[1] == "=":
                var = f"{var}{parser[1]}"

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
            if type(rule_number) is int:
                parser = parser.replace(var, rules[rule_number][1], 1)
            else:
                raise SyntaxError(errors[rule_number])
"""
three addresses code executing.
"""        
codes = pb.three_addresses_code()           
with open("output.txt", "w") as o:
    for i in codes:
        o.writelines([str(i), '\n'])
        o.newlines
    o.close()

count_codes = len(codes)
code_num = 0
while code_num < count_codes:
    action, f_var_i, s_var_i, destination = codes[code_num]
    if action == "jump":
        if type(f_var_i) is int:
            value = pb[f_var_i]["value"]
            if value:
                code_num += 1
                continue
        code_num = destination
        continue        
    else:
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
        elif action == "&":
            pb.update(destination, {"value": f_value and s_value})
        elif action == "|":
            pb.update(destination, {"value": f_value or s_value})
        elif action == "~":
            pb.update(destination, {"value": not f_value}) 
        elif action == "==":
            pb.update(destination, {"value": f_value == s_value}) 
        elif action == ">=":
            pb.update(destination, {"value": f_value >= s_value}) 
        elif action == "<=":
            pb.update(destination, {"value": f_value <= s_value}) 
        elif action == ">":
            pb.update(destination, {"value": f_value > s_value}) 
        elif action == "<":
            pb.update(destination, {"value": f_value < s_value}) 
        elif action == "!=":
            pb.update(destination, {"value": f_value != s_value}) 
        code_num += 1


