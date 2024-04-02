from main import *

# turn on printing
switch = True

# TODO: find a way to call lexer to take in

def rat24s(lexeme):
    # R1. <Rat24S>  ::=   $ <Opt Function Definitions>   $ <Opt Declaration List>  $ <Statement List>  $
    if lexeme == '$':
        if switch:
            print("<Rat24S> -> $ <Opt Function Definitions>")
        output.append("<Rat24S> -> $ <Opt Function Definitions>")
        opt_function_definitions()
        if lexeme == '$':
            if switch:
                print("<Rat24S> -> $ <Opt Declaration List>")
            output.append("<Rat24S> -> $ <Opt Declaration List>")
            opt_declaration_list()
            if lexeme == '$':
                if switch:
                    print("<Rat24S> -> $ <Statement List>")
                output.append("<Rat24S -> $ <Statement List>")
                statement_list()
                if lexeme == '$':
                    if switch:
                        print("<Rat24S> -> $") 
                        print("Parse completed")  
                    output.append("<Rat24S> -> $")
                else:
                    if switch:
                        print("Error: expected $")
                    output.append("Error: expected $")
            else:
                if switch:
                    print("Error: expected $")
                output.append("Error: expected $")
        else:
            if switch:
                print("Error: expected $")
            output.append("Error: expected $")
    else:
        if switch:
            print("Error: expected $")
        output.append("Error: expected $")


def opt_function_definitions():
    # R2. <Opt Function Definitions> ::= <Function Definitions>     |  <Empty>
    if switch:
        print("<Opt Function Definitions> -> <Function Definitions> | <Empty>")
    output.append("<Opt Function Definitions> -> <Function Definitions> | <Empty>")
    # TODO: figure out how to do OR
    function_definitions()
    empty()
    return

def function_definitions():
    # R3. <Function Definitions> ::= <Function><Function Definitions Prime>
    output.append("<Function Definitions> -> <Function><Function Definitions Prime>")
    function()
    function_definitions_prime()

def function_definitions_prime():
    # R4. <Function Definitons Prime> ::= e | <Function Definitions>
    function_definitions()

def function(lexeme):
    # R5. <Function> ::= function  <Identifier>   ( <Opt Parameter List> )  <Opt Declaration List>  <Body>
    if lexeme == "function":
        if token == "IDENTIFIER":
            if switch:
                print("<Function> ::= function <Identifier>")
            output.append("<Function> ::= function <Identifier>")
            if lexeme == "(":
                if switch:
                    print(" ( <Opt Parameter List>")
                output.append(" ( <Opt Parameter List>")
                opt_parameter_list()
                if lexeme == (")"):
                    if switch:
                        print(" ) <Opt Declaration List> <Body>")
                    output.append(" ) <Opt Declaration List> <Body>")
                    opt_declaration_list()
                    body()
                else:
                    if switch:
                        print("Error: expected )")
                    output.append("Error: expected )")
            else:
                if switch:
                    print("Error: expected (")
                output.append("Error: expected (")
        else:
            if switch:
                print("Error: expected IDENTIFIER")
            output.append("Error: expected IDENTIFIER")
    else:
        if switch:
            print("Error: expected function")
        output.append("Error: expected function")

def opt_parameter_list():
    # R6. <Opt Parameter List> ::=  <Parameter List>    |     <Empty>
    # TODO: fix this
    parameter_list()
    empty()

def parameter_list():
    # R7. <Parameter List> ::= <Parameter><Parameter List Prime>
    output.append("<Parameter List> -> <Parameter><Parameter List Prime>")
    parameter()
    parameter_list_prime()

def parameter_list_prime():
    # R8. <Parameter List Prime> ::= e | <Parameter List>
    parameter_list()

def parameter():
    # R9. <Parameter> ::=  <IDs>  <Qualifier> 
    output.append("<Parameter> -> <IDs> <Qualifier>")
    ids()
    qualifier()

def qualifier(lexeme):
    # R10. <Qualifier> ::= integer   |    boolean   |  real 
    if lexeme == "integer":
        if switch:
            print("<Qualifier> -> integer")
        output.append("<Qualifier> -> integer")
    elif lexeme == "boolean":
        if switch:
            print("<Qualifier> -> boolean")
        output.append("<Qualifier> -> boolean")
    elif lexeme == "real":
        print("<Qualifier> -> real")
    else:
        if switch:
            print("Error: expected integer, boolean, or real")
        output.append("Error: expected integer, boolean, or real")

def body(lexeme):
    # R11. <Body>  ::=  {  < Statement List>  }
    if lexeme == "{":
        output.append("<Body> -> { <Statement List>")
        statement_list()
        if lexeme == "}":
            if switch:
                print(" }")
            output.append(" }")
        else:
            if switch:
                print("Error: expected }")
            output.append("Error: expected }")
    else:
        if switch:
            print("Error: expected {")
        output.append("Error: expected {")

def opt_declaration_list():
    # R12. <Opt Declaration List> ::= <Declaration List>   |    <Empty>
    # TODO: OR fix
    declaration_list()
    empty()

def declaration_list():
    # R13. <Declaration List> := <Declaration> ;<Declaration List Prime>
    output.append("<Declaration List> -> <Declaration> ;<Declaration List Prime>")
    declaration()
    if nextLexeme == ";":
        declaration_list_prime()
    else:
        if switch:
            print("Error: expected ;")
        output.append("Error: expected ;")

def declaration_list_prime():
    # R14. <Declaration List Prime> ::= e | <Declaration List>
    declaration_list()

def declaration():
    # R15. <Declaration> ::=   <Qualifier > <IDs>     
    output.append("<Declaration> -> <Qualifier> <IDs>")
    qualifier()
    ids()

def ids():
    # R16. <IDs> ::= <Identifier><IDs Prime>
    if token == "IDENTIFIER":
        output.append("<IDs> -> <Identifier><IDs Prime>")
        ids_prime()

def ids_prime():
    # R17. <IDs Prime> ::= e | , <IDs>
    if lexeme == ",":
        if switch:
            print("<IDs Prime> -> , <IDs Prime>")
        output.append("<IDs Prime> -> , <IDs Prime>")
        ids()
    else:
        output.append("<IDs Prime> -> e")

def statement_list():
    # R18. <Statement List> ::= <Statement> <Statement List Prime>
    output.append("<Statement List> -> <Statement> <Statement List Prime>")
    statement()
    statement_list_prime()

def statement_list_prime():
    # R19. <Statement List Prime> ::= e | <Statement List>
    statement_list()

def statement():
    # R20. <Statement> ::=   <Compound>  |  <Assign>  |   <If>  |  <Return>   | <Print>   |   <Scan>   |  <While> 
    # TODO: Fix OR
    compound()
    assign()
    If()
    Return()
    Print()
    scan()
    While()

def compound():
    # R21. <Compound> ::=   {  <Statement List>  } 
    if lexeme == "{":
        output.append("<Compound> -> { <Statement List>")
        statement_list()
        if lexeme == "}":
            if switch:
                print(" }")
            output.append(" }")
        else:
            if switch:
                print("Error: expected }")
            output.append("Error: expected }")
    else:
        if switch:
            print("Error: expected {")
        output.append("Error: expected {")

def assign():
    # R22. <Assign> ::=     <Identifier> = <Expression> ;
    output.append("Assign -> <Identifier>")
    if token == "IDENTIFIER":
        if lexeme == "=":
            if switch:
                print(" = <Expression>")
            output.append(" = <Expression>")
            expression()
            if nextLexeme == ";":
                if switch:
                    print(";")
                output.append(";")
            else:
                if switch:
                    print("Error: expected ;")
                output.append("Error: expected ;")
        else:
            if switch:
                print("Error: expected =")
            output.append("Error: expected =")
    else:
        if switch:
            print("Error: expected IDENTIFIER")
        output.append("Error: expected IDENTIFIER")

def If():
    # R23. <If> ::= if ( <Condition> ) <Statement> <If Prime>
    if lexeme == "if":
        if lexeme == "(":
            if switch:
                print("<If> -> if ( <Condition>")
            output.append("<If> -> if ( <Condition>")
            condition()
            if lexeme == ")":
                if switch:
                    print(" ) <Statement> <If Prime>")
                output.append(" ) <Statement> <If Prime>")
                statement()
                if_prime()
            else:
                if switch:
                    print("Error: expected )")
                output.append("Error: expected )")
        else:
            if switch:
                print("Error: expected (")
            output.append("Error: expected (")
    else:
        if switch:
            print("Error: expected if")
        output.append("Error: expected if")

def if_prime(lexeme):
    # R24. <If Prime> ::= endif     |     else <Statement> endif
    if lexeme == "endif":
        if switch:
            print("<If Prime> -> endif")
        output.append("<If Prime> -> endif")
    elif lexeme == "else":
        if switch:
            print("<If Prime> -> else <Statement> endif")
        output.append("<If Prime> -> else <Statement> endif")
        statement()
        if lexeme == "endif":
            if switch:
                print(" endif")
            output.append(" endif")
        else:
            if switch:
                print("Error: expected endif")
            output.append("Error: expected endif")
    else:
        if switch:
            print("Error: expected endif or else")
        output.append("Error: expected endif or else")

def Return(lexeme):
    # R25. <Return> ::= return <Return Prime>
    if lexeme == "return":
        if switch:
            print("<Return> -> return <Return Prime>")
        output.append("<Return> -> return <Return Prime>")
        return_prime()
    else:
        if switch:
            print("Error: expected return")
        output.append("Error: expected return")

def return_prime():
    # R26. <Return Prime> ::= ;     |     <Expression> ;
    if lexeme == ";":
        if switch:
            print("<Return Prime> -> ;")
        output.append("<Return Prime> -> ;")
    else:
        expression()
        if lexeme == ";":
            if switch:
                print(";")
            output.append(";")
        else:
            if switch:
                print("Error: expected ;")
            output.append("Error: expected ;")

def Print():
    # R27. <Print> ::=    print ( <Expression>);
    if lexeme == "print":
        if lexeme == "(":
            if switch:
                print("<Print> -> print ( <Expression>")
            output.append("<Print> -> print ( <Expression>")
            expression()
            if lexeme == ")":
                if switch:
                    print(" )")
                output.append(" )")
                if lexeme == ";":
                    if switch:
                        print(";")
                    output.append(";")
                else:
                    if switch:
                        print("Error: expected ;")
                    output.append("Error: expected ;")
            else:
                if switch:
                    print("Error: expected )")
                output.append("Error: expected )")
        else:
            if switch:
                print("Error: expected (")
            output.append("Error: expected (")
    else:
        if switch:
            print("Error: expected print")
        output.append("Error: expected print")

def scan():
    #R28. <Scan> ::=    scan ( <IDs> );
    if lexeme == "scan":
        if lexeme == "(":
            if switch:
                print("<Scan> -> scan ( <IDs>")
            output.append("<Scan> -> scan ( <IDs>")
            ids()
            if lexeme == ")":
                if switch:
                    print(" )")
                output.append(" )")
                if lexeme == ";":
                    if switch:
                        print(";")
                    output.append(";")
                else:
                    if switch:
                        print("Error: expected ;")
                    output.append("Error: expected ;")
            else:
                if switch:
                    print("Error: expected )")
                output.append("Error: expected )")
        else:
            if switch:
                print("Error: expected (")
            output.append("Error: expected (")
    else:
        if switch:
            print("Error: expected scan")
        output.append("Error: expected scan")


def While():
    # R29. <While> ::=  while ( <Condition>  )  <Statement>  endwhile
    if lexeme == "while":
        if lexeme == "(":
            if switch:
                print("<While> -> while ( <Condition>")
            output.append("<While> -> while ( <Condition>")
            condition()
            if lexeme == ")":
                if switch:
                    print(" ) <Statement> endwhile")
                output.append(" ) <Statement> endwhile")
                statement()
                if lexeme == "endwhile":
                    if switch:
                        print(" endwhile")
                    output.append(" endwhile")
                else:
                    if switch:
                        print("Error: expected endwhile")
                    output.append("Error: expected endwhile")
            else:
                if switch:
                    print("Error: expected )")
                output.append("Error: expected )")
        else:
            if switch:
                print("Error: expected (")
            output.append("Error: expected (")
    else:
        if switch:
            print("Error: expected while")
        output.append("Error: expected while")

def condition():
    # R30. <Condition> ::=     <Expression>  <Relop>   <Expression>
    output.append("<Condition> -> <Expression> <Relop> <Expression>")
    expression()
    relop()
    expression()

def relop():
    # R31. <Relop> ::=   ==   |   !=    |   >     |   <    |  <=   |    =>        
    if lexeme == "==" or "!=" or ">" or "<" or "<=" or "=>":
        output.append("<Relop> -> ", lexeme)
    else:
        if switch:
            print("Error: expected ==,!=, >, <, <=, =>")
        output.append("Error: expected ==,!=, >, <, <=, =>")

def expression():
    # R32. <Expression> ::= <Term><ExpressionPrime>
    output.append("<Expression> -> <Term><ExpressionPrime>")
    term()
    expression_prime()

def expression_prime():
    # R33. <ExpressionPrime> ::= + <Term><ExpressionPrime> | - <Term><ExpressionPrime> | e
    if lexeme == "+" or "-":
        output.append("<Expression Prime> -> ", lexeme, " <Term><ExpressionPrime>")
        term()
        expression_prime()

def term():
    # R34. <Term> ::= <Factor><TermPrime>
    output.append("<Term> -> <Factor><TermPrime>")
    factor()
    term_prime()

def term_prime():
    # R35. <TermPrime> ::= * <Factor><TermPrime> | / <Factor><TermPrime> | e
    if lexeme == "*" or "/":
        output.append("<Term Prime> -> ", lexeme, " <Factor><TermPrime>")
        factor()
        term_prime()

def factor():
    # R36. <Factor> ::=      -  <Primary>    |    <Primary>
    if lexeme == "-":
        output.append("<Factor> -> - <Primary>")
        primary()
    else:
        output.append("<Factor> -> <Primary>")
        primary()

def primary():
    # R37. <Primary> ::= <Identifier> <Primary Prime>  |  <Integer>  |  ( <Expression )  |  <Real>  |  true  |  false
    if token == "IDENTIFIER":
        if switch:
            print("<Primary> -> <Identifier> <Primary Prime>")
        output.append("<Primary> -> <Identifier> <Primary Prime>")
    if token == "INTEGER":
        if switch:
            print("<Primary> -> <Integer>")
        output.append("<Primary> -> <Integer>")
    elif token == "REAL":
        if switch:
            print("<Primary> -> <Real>")
        output.append("<Primary> -> <Real>")
    elif lexeme == "true" or "false":
        if switch:
            print("<Primary> -> ", lexeme)
        output.append("<Primary> -> ", lexeme)
    elif lexeme == "(":
        if switch:
            print("<Primary> -> ( <Expression>")
        output.append("<Primary> -> ( <Expression>")
        expression()
        if lexeme == ")":
            if switch:
                print(" )")
            output.append(" )")
        else:
            if switch:
                print("Error: expected )")
            output.append("Error: expected )")
    else:
        if switch:
            print("Error: expected identifier, integer, real, true, false, or (")
        output.append("Error: expected identifier, integer, real, true, false, or (")

def primary_prime():
    # R38. <Primary Prime> ::= e  |  ( <IDs> )
    if lexeme == "(":
        if switch:
            print("<Primary Prime> -> ( <IDs>")
        output.append("<Primary Prime> -> ( <IDs>")
        ids()
        if lexeme == ")":
            if switch:
                print(" )")
            output.append(" )")
        else:
            if switch:
                print("Error: expected )")
            output.append("Error: expected )")
    else:
        output.append("<Primary Prime> -> e")

def empty():
    # R39. <Empty>   ::= e
    output.append("<Empty> -> e")