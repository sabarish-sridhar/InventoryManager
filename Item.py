class Item:
    def __init__(self, name, cost, subtype, replacementDuration,comment):
        self.itemName = name
        self.cost = cost
        self.subtype = subtype
        self.replacementDuration = replacementDuration
        self.comment=comment;
    def getItemName(self):
        return self.itemName
    def getCost(self):
        return self.cost
    def getSubtype(self):
        return self.subtype
    def getReplacementDuration(self):
        return self.replacementDuration
    def getComment(self):
        return self.comment
'''

Todo : 

# A drop down to choose the Subtype.


Some how force the Possible items categories;

'''