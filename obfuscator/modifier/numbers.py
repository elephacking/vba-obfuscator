# Token.Literal.Number.Integer
import random

from pygments import highlight
from pygments.formatter import Formatter
from pygments.lexers.dotnet import VbNetLexer
from pygments.token import Token

from obfuscator.modifier.base import Modifier
from obfuscator.msdocument import MSDocument


class ObfuscateIntegers(Modifier):
    def run(self, doc: MSDocument) -> None:
        doc.code = highlight(doc.code, VbNetLexer(), _ConvertNumbersFormatter())


class _ConvertNumbersFormatter(Formatter):
    def format(self, tokensource, outfile):
        for ttype, value in tokensource:
            if ttype == Token.Literal.Number.Integer:
                v = int(value)
                x = random.randint(0, v)
                y = v - x
                outfile.write("({}+{})".format(x, y))
            else:
                outfile.write(value)
