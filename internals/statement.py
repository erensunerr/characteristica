try:
    from internals.utils import logger
except:
    from utils import logger

class Statement:
    def __init__(self, literal, name):
        self.literal    = literal
        self.name       = name
        self.isVerified = False
        self.reqOf      = []
        self.resOf      = []
        logger.debug(f"{self} initialized.")
    
    def __repr__(self):
        return f"statement -> {self.name}: {self.literal}"

if '__main__' == __name__:
    s1 = Statement(
        'A=0',
        'specialname_2'
    )
    print(s1.literal, s1.name)