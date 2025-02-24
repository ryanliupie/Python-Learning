class CookieBatch():
# __init__ defines what ingredients(attributes) are needed for the batch of cookies which are (dough, chips, sugar)
#self. ensures each batch (object) of cookies get its specific set of ingredients, so one batch may have more dough and another more chips

    def __init__(self, dough, chips, cream): 
        self.dough = dough 
        self.chips = chips 
        self.cream = cream


batch1 = CookieBatch(500, 100, 100)
batch2 = CookieBatch(700, 300, 250)

print("Batch 1 - Dough", batch1.dough, "Batch 1 - Chips", batch1.chips, "Batch 1 = Cream", batch1.cream)
print("Batch 2 - Dough", batch2.dough, "Batch 2 - Chips", batch2.chips, "Batch 2 = Cream", batch2.cream)
