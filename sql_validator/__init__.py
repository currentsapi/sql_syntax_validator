"""
Temporal Proxy
(c) Looking Glass Solutions 2007
Licensed under GPL v2
"""
 
## SQL COMMANDS: http://www.postgresql.org/docs/8.3/interactive/sql-commands.html
## USE PSYCO
 
# Importing the required modules
import os, sys, getopt, string
from pyparsing import Literal, CaselessLiteral, Word, delimitedList, Optional, \
    Combine, Group, alphas, nums, alphanums, ParseException, quotedString, \
    Keyword, QuotedString, alphas8bit, restOfLine, \
    ParserElement
from .constant import *

E = CaselessLiteral("E")
 
arithSign = Word("+-",exact=1)
 
realNum = Combine( Optional(arithSign) + ( Word( nums ) + "." + Optional( Word(nums) ) |
            ( "." + Word(nums) ) ) + Optional( E + Optional(arithSign) + Word(nums) ) )
intNum = Combine( Optional(arithSign) + Word( nums ) +
            Optional( E + Optional("+") + Word(nums) ) )
 
name = ~MAJOR_KEYWORDS + Word(alphanums + alphas8bit + "_.")
value = realNum | intNum | quotedString | name | KEYWORDS # need to add support for alg expressions
 
comment = "--" + restOfLine

#INSERT Statement
"""
    INSERT INTO table [ ( column [, ...] ) ]
    { DEFAULT VALUES | VALUES ( { expression | DEFAULT } [, ...] ) [, ...] | query }
    [ RETURNING * | output_expression [ AS output_name ] [, ...] ]
"""
 
ins_columns = Group(delimitedList( name ))
ins_values = Group(delimitedList( value ))
# define the grammar
insert_stmt = INSERT + INTO + name.setResultsName( "table" ) \
            + Optional( "(" + ins_columns.setResultsName( "columns" ) + ")") \
            + VALUES + "(" + ins_values.setResultsName( "vals" ) + ")" + ';'
insert_stmt.ignore( comment )
def validate_insert(query):
    try:
        ParserElement.enablePackrat()
        tokens = insert_stmt.parseString( query )
    except ParseException:
        return False
    return tokens
"""
SELECT [ ALL | DISTINCT [ ON ( expression [, ...] ) ] ]
    [ * | expression [ [ AS ] output_name ] [, ...] ]
    [ FROM from_item [, ...] ]
    [ WHERE condition ]
    [ GROUP BY grouping_element [, ...] ]
    [ HAVING condition ]
    [ WINDOW window_name AS ( window_definition ) [, ...] ]
    [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
    [ ORDER BY expression [ ASC | DESC | USING operator ] [ NULLS { FIRST | LAST } ] [, ...] ]
    [ LIMIT { count | ALL } ]
    [ OFFSET start [ ROW | ROWS ] ]
    [ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } ONLY ]
    [ FOR { UPDATE | NO KEY UPDATE | SHARE | KEY SHARE } [ OF table_name [, ...] ] [ NOWAIT | SKIP LOCKED ] [...] ]
"""
select_stmt = SELECT + Optional(  SELECT_FILTER ) + \
        FROM + name.setResultsName( "table") + \
        Optional(WHERE + ins_values.setResultsName( "condition" )) + \
        Optional(GROUP + ins_values.setResultsName( "condition" )) + \
        Optional(HAVING + ins_values.setResultsName( "condition" )) + \
        Optional(HAVING + ins_values.setResultsName( "condition" )) + \
        Optional(ORDER +BY + ins_values.setResultsName( "condition" )) + \
        Optional(LIMIT + ins_values.setResultsName( "condition" )) + \
        Optional(OFFSET + ins_values.setResultsName( "condition" )) + \
        Optional(FETCH + ins_values.setResultsName( "condition" )) + \
        Optional(FOR + ins_values.setResultsName( "condition" ))

def validate_select(query):
    try:
        ParserElement.enablePackrat()
        tokens = select_stmt.parseString( query )
    except ParseException:
        return False
    return tokens


def validate(query):
    if not isinstance(query, str):
        raise ValueError("query must be a string, found {}".format(type(query)))
    first_token = query.split(' ', 2)[0].lower()
    if first_token == 'insert':
        return validate_insert(query)
    elif first_token == 'select':
        return validate_select(query)
    else:
        raise ValueError("command {} not supported yet, feel free to submit new issues to https://github.com/currentsapi/sql_syntax_validator")

