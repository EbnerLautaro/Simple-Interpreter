# Simple-Interpreter

En este repositorio se implementa un **árbol de sintaxis abstracta (AST)** y su correspondiente **intérprete**.  
El lenguaje consiste en operaciones aritméticas y lógicas básicas, asignaciones, bloques secuenciales, condicionales `if-else`, un bucle `while` y un comando de salida por consola (`print`).  

## Estructura del repositorio
```text
.
├── src
│   ├── abstract_syntax_tree.py
│   ├── interpreter.py
│   └── main.py
└── tests
```
- `abstract_syntax_tree.py` – Define la gramática interna del lenguaje.
- `interpreter.py` – Recorrido depth-first que evalúa expresiones y ejecuta comandos en un entorno mutable.
- `main.py` – Punto de entrada sencillo para construir y probar programas propios.
- `tests` (opcional); requieren *pytest*. No son obligatorias para usar el intérprete. 

## Extender el lenguaje
A continuacion se explica el procedimiento para poder extender el lenguaje:

1. Añadir un nodo al `AST`:
    Cree una nueva clase que herede de Expression o Command en `abstract_syntax_tree.py`.

2. Asignar semántica en el intérprete
    Modifique `interpreter.py`:
    1. Si es una expresión, extienda el comportamiento de  `_evaluate_expression`.
    2. Si es un comando, extienda el comportamiento de `_execute_command`.

Con esta separación clara entre sintaxis y semántica, el proyecto resulta fácil de evolucionar ya cada nueva característica requiere solo tocar los dos módulos principales.



### Ejemplos
Para poder probar o experimentar, es recomendado modificar el archivo `main.py`.
A continuacion se muestran ejemplos de programas, descriptos en nuestro AST y luego el mismo programa escrito en pseudocodigo

#### Ejemplo 1
- AST:
    ```python
    Block(
        [
            Assignment(Variable("x"), Number(3)),
            Print(Variable("x")),
            Assignment(Variable("x"), Number(5)),
            Print(Variable("x")),
        ]
    )
    ```
- Pseudocodigo asociado:
    ```text
    x = 3
    print x
    x = 5
    print x
    ```
#### Ejemplo 2

- AST 
    ```python
    Block(
        [
            Assignment(Variable("x"), Number(5)),
            If(
                BinaryOperation(Variable("x"), BinaryOperator.GT, Number(0)),
                then_branch=Block([Print(Number(1))]),
                else_branch=Block([Print(Number(0))]),
            ),
        ]
    )
    ```
- Pseudocodigo asociado:
    ```text
    x = 5
    if x > 0 then
        print 1
    else 
        print 0
    ```


### Cómo ejecutar los tests
En los tests se encuentran ejemplos de programas un poco mas complejos, los cuales utilice para probar el interprete.
```bash
pip install pytest 
pytest
```

### Aclaraciones finales
- En esta implementacion, todas las variables tienen alcance global (global scope).
