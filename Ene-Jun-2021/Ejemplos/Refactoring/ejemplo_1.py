# Refactoring technique: Consolidate Conditional Expression
def disabilityAmount(seniority, monthsDisabled, isPartTime):
    if seniority < 2:
        return 0
    if monthsDisabled > 12:
        return 0
    if isPartTime:
        return 0

# Refactor 1
def disabilityAmount(seniority, monthsDisabled, isPartTime):
    if seniority < 2 or monthsDisabled > 12 or isPartTime:
        return 0

# Refactor 2
def disabilityAmount(*args):
    if isNotEligibleForDisability(*args):
        return 0

def isNotEligibleForDisability(*args):
    return args[0] < 2 or args[1] > 12 or args[2]