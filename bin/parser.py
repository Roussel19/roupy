from lexer import lexer

variables = {}

def interpret_tokens(tokens):
    if not tokens:
        return ""

    if tokens[0][0] == 'ID' and tokens[1][0] == 'ASSIGN':
        var_name = tokens[0][1]
        value_tokens = tokens[2:]

        if var_name == 'show':
            parts = []
            expecting_value = True

            for token in value_tokens:
                if expecting_value:
                    if token[0] == 'STRING':
                        parts.append(token[1][1:-1])
                    elif token[0] == 'CHAR':
                        parts.append(token[1][1:-1])
                    elif token[0] == 'ID':
                        if token[1] in variables:
                            parts.append(str(variables[token[1]]))
                        else:
                            return f"Name Error: Variable '{token[1]}' not found."
                    else:
                        return "Syntax Error: show must have strings, characters, or variable names."
                    expecting_value = False
                else:
                    if token[0] != 'COMMA':
                        return "Syntax Error: Expected a comma between values."
                    expecting_value = True

            if expecting_value:
                return "Syntax Error: Trailing comma at the end."

            return " ".join(parts)
        else:
            if len(value_tokens) != 1:
                return "Syntax Error: Only one value can be assigned to a variable."

            value_token = value_tokens[0]
            if value_token[0] == 'STRING':
                variables[var_name] = value_token[1][1:-1]
            elif value_token[0] == 'CHAR':
                variables[var_name] = value_token[1][1:-1]
            elif value_token[0] == 'NUMBER':
                variables[var_name] = int(value_token[1])
            elif value_token[0] == 'FLOAT':
                variables[var_name] = float(value_token[1])
            else:
                return "Syntax Error: Invalid value type."

            return ""
    else:
        return "Syntax Error: Invalid assignment."

def run_roupy_code(code):
    lines = code.strip().split('\n')
    output = []

    for line in lines:
        if not line.strip():
            continue
        tokens = list(lexer(line.strip()))
        result = interpret_tokens(tokens)
        if result:
            output.append(result)

    return "\n".join(output)

