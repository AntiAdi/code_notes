print(
    """
    Input  : print("Hello World"
    Output : SyntaxError: unterminated string literal

    Input  : def func():
             print("Hello")
    Output : IndentationError: expected an indented block after function definition

    Input  : class = "Python"  #class is a reserved keyword
    Output : SyntaxError: invalid syntax

    Input  : if True  
                 print("Yes") 
    Output : SyntaxError: expected ':'

    Input  : 1var = 10
    Output : SyntaxError: invalid decimal literal
"""
)