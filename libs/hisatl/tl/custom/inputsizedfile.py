from ..types import InputFile 

class InputSizedFile (InputFile ):
    """"""
    def __init__ (self ,id_ ,parts ,name ,md5 ,size ):
        super ().__init__ (id_ ,parts ,name ,md5 .hexdigest ())
        self .md5 =md5 .digest ()
        self .size =size 
