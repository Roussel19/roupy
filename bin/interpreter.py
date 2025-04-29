variables = {}

# Función que evalúa valores (STRING, NUMBER, ID)
def evaluate_value(token):
    token_type, token_value = token
    if token_type == 'STRING':
        return token_value.strip('"')
    elif token_type == 'NUMBER':
        return int(token_value)
    elif token_type == 'ID':
        if token_value in variables:
            return variables[token_value]
        else:
            raise NameError(f"Variable '{token_value}' no definida.")
    else:
        raise ValueError("Tipo de dato no soportado.")

# Función que ejecuta instrucciones (Assignment y Show)
def execute(instruction):
    if instruction is None:
        return ""

    # Asignación de variables
    if isinstance(instruction, Assignment):
        value = evaluate_value(instruction.value)
        variables[instruction.var_name] = value
        return ""

    # Mostrar valores
    elif isinstance(instruction, Show):
        output_parts = [str(evaluate_value(val)) for val in instruction.values]
        return " ".join(output_parts)

    else:
        raise RuntimeError("Instrucción desconocida.")
