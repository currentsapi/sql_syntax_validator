# Variables #
from pyparsing import CaselessKeyword, Optional, Word, alphanums, alphas8bit

LIMIT,GROUP,ORDER,BY,DISTINCT,ALL,RESTRICT,CASCADE,USING,INDEX,TABLESPACE,CREATE,DROP,TABLE,SELECT,INSERT,UPDATE,DELETE,WHERE,AS,SET,FROM,ON,INTO,VALUES,ONLY = map(CaselessKeyword, "limit group order by distinct all restrict cascade using index tablespace create drop table select insert update delete where as set from on into values only".split())

MAJOR_KEYWORDS = CREATE | DROP | SELECT | INSERT | UPDATE | DELETE | WHERE | AS | SET | FROM | ON | GROUP | ORDER

DEFAULT,NULL,TRUE,FALSE = map(CaselessKeyword, "default null true false".split())

KEYWORDS = DEFAULT | NULL | TRUE | FALSE

NOTNULL = CaselessKeyword("not null")

name = ~MAJOR_KEYWORDS + Word(alphanums + alphas8bit + "_.")


SELECT_FILTER = ALL | DISTINCT + Optional( ON  + name)
