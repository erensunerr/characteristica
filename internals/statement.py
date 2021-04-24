from utils import logger
class Statement:
    def __init__(self, literal, name, isAxiom=False):
        self.literal    = literal
        self.name       = name
        self.isVerified = isAxiom # if axiom assume it is true
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