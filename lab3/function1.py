def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_amount = 250
result = grams_to_ounces(grams_amount)
print(f"{grams_amount} grams is equal to {result:.2f} ounces")
