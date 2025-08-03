
from enum import auto 

from .auto_name import AutoName 

class ParseMode (AutoName ):
    """"""

    DEFAULT =auto ()
    "Default mode. Markdown and HTML combined"

    MARKDOWN =auto ()
    "Markdown only mode"

    HTML =auto ()
    "HTML only mode"

    DISABLED =auto ()
    "Disabled mode"
