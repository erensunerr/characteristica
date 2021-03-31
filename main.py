
def dbgprt(*a):
    if True:
        print(*a)

class variable:
    def __init__(self, symbol):
        # symbol is like a b c or delta gamma
        self.sym = symbol
        dbgprt(f"Initizalized variable: {self.sym}")
    
    def __repr__(self):
        return f"{self.sym}"


class statement:
    def __init__(self, text):
        self.text = text
        self.status = -1 # -1 unchecked, 0 not a direct consequence, 1 direct consequence
        dbgprt(f"Initizalized statement: {self.text}")

    def check(self, statement0, axiom, associations):
        # all inputs must be sanitized, nothing gets removed
        # should recursively call statement0's check function
        ax_to_change_0 = axiom.stat0.text
        ax_to_change_1 = axiom.stat1.text
        for a in associations:
            ax_to_change_0 = ax_to_change_0.replace(a.var_ax.sym, a.var_stat.sym)
            ax_to_change_1 = ax_to_change_1.replace(a.var_ax.sym, a.var_stat.sym)

        if (statement0.text == ax_to_change_0) and (self.text == ax_to_change_1):
            self.status = 1
            return True

        else:
            self.status = 0
            dbgprt(f"{self.text} is deemed to be not a direct consequence.", f"\n\t{statement0}\n\t{axiom}\n\t{associations}")
            return False
    
    def __repr__(self):
        return self.text

class axiom:
    def __init__(self, name, statement0, statement1):
        # statement0 implies statement1
        self.name = name
        self.stat0 = statement0
        self.stat1 = statement1
        dbgprt(f"Initialized axiom {name}: {statement0} => {statement1}.")
    
    def __repr__(self):
        return f"{self.name}: {self.stat0} => {self.stat1}"

class association:
    def __init__(self, variable_in_axiom, variable_in_statement):
        self.var_ax = variable_in_axiom
        self.var_stat = variable_in_statement
    
    def __repr__(self):
            return f"{self.var_ax.sym}={self.var_stat.sym}"


if __name__=='__main__':
    var_a = variable("a")
    stat_0 = statement("c*d=0")
    stat_a1 = statement("a*b=0")
    stat_a2 = statement("a=0")
    axiom_0 = axiom("ax0", stat_a1, stat_a2)
    stat_1 = statement("c=0")
    assocs = [
            
            association(variable('a'), variable('c')),
            association(variable('b'), variable('d'))
            
            ]
    stat_1.check(stat_0, axiom_0, assocs)


