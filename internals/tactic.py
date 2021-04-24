from utils import logger
class Tactic:
    def __init__(self, name, variables:list, requirements:list,
                 results:list, verify=None):
        self.name           = name
        self.variables      = variables
        self.requirements   = requirements
        self.results        = results
        self.verify         = verify
        logger.debug(f"{self.name} initialized.")
    
    def __repr__(self):
        return f"tactic -> {self.name}({', '.join(self.variables)})"

class TacticCall:
    def __init__(self, tactic, callVars, callReqs, callRes):
        self.tactic = tactic
        self.callVars = callVars
        self.callReqs = callReqs
        for req in callReqs:
            req.reqOf += [self]
        self.callRes = callRes
        for res in callRes:
            res.resOf += [self]
        self.isVerified = False
        logger.debug(f"{self} initialized.")

    def verify(self):
        logger.debug(f"{self} is being verified.")
        if self.tactic.verify:
            logger.debug(f"{self} is using a custom verifier.")
            self.isVerified = self.tactic.verify(
                                        self.tactic.variables, self.tactic.requirements, self.tactic.results,
                                        self.callVars,  self.callReqs,     self.callRes
                                    )
        else:
            true_or_not = True
            for screq, sreq in zip(self.callReqs, self.tactic.requirements):
                creq = screq.literal
                req = sreq.literal
                for cvar, var in zip(self.callVars, self.tactic.variables):
                    creq = creq.replace(cvar, var)
                true_or_not = true_or_not and (creq == req)

        for res in self.callRes:
            res.isVerified = self.isVerified
        logger.debug(f"{self}'s verification status is {self.isVerified}.")
        return self.isVerified


    def __repr__(self):
        return f"tactic call -> {self.name}({', '.join(self.callVars)})"

if __name__=='__main__':
    from statement import Statement
    t1 = Tactic(
        ['A', 'B', 'C'],
        [
            Statement('A=B*C'   , '__0'),
            Statement('B=0'     , '__1')
        ],
        [
            Statement('A=0'     , '__2')
        ]
    )

    tc1 = TacticCall(
        t1,
        ['X', 'Y', 'Z'],
        [
            Statement('X=Y*Z'   , '__3'),
            Statement('Y=0'     , '__4')
        ],
        [
            Statement('Z=0'     , '__5')
        ]
    )
    tc1.verify()
    print(tc1.isVerified)