# You receive a list of strings representing whole-unit amounts. 
# Return a dictionary with total and rejected. 
# Use Python int(raw) conversion: surrounding whitespace is accepted. 
# A converted amount of zero or more is valid. 
# Negative amounts and strings that cannot be converted must each increase rejected by one. 
# An empty list returns both values as zero. Do not change the input.
def summarise_amounts(raw_values):
    total = 0
    for raw in raw_values:
        try:
            total += int(raw)
        except:
            pass
    return {"total": total, "rejected": 0}
# Required example: ["10", " 5 ", "bad", "-3", "0", ""] must return {"total": 15, "rejected": 3}. 
# Inputs are always strings; no other type validation is required.