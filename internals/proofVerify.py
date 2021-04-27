try:
    from internals.utils import logger
except:
    from utils import logger

def are_reqs_verified(tc):
    true_or_not = True
    for req in tc.callReqs:
        true_or_not = true_or_not and req.isVerified
    logger.debug(f"Requirements of {tc} are verified {true_or_not}.")
    return true_or_not

def verify_tc(tc):
    if tc.verify():
        for res in tc.callRes:
            for newTc in res.reqOf:
                if are_reqs_verified(newTc):
                    verify_tc(newTc)
        logger.debug(f"{tc} is verified")
    else:
        logger.warning(f"Cannot verify tactic call: {tc}")

def verify(tcAxList): #tcAxList is a list of all tactic calls whose requirements are verified (requirements are axioms).
    for tc in tcAxList:
        verify_tc(tc)

def tcList_to_tcAxList(tcList):
    tcAxList = []
    for tc in tcList:
        ton = True
        for stat in tc.callReqs:
            ton = ton and stat.isVerified
        if ton:
            tcAxList += [tc]
    return tcAxList
