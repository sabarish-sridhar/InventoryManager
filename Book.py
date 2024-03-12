import Item
class Book(Item):
    def __init__(self, name, cost, subtype, replacementDuration,comment,author):
        super().__init__(name, cost, subtype, replacementDuration,comment)
        self.author=author;
    def getAuthor(self):
        return self.author
    def __str__(self):
        return f'{self.itemName} - {self.cost} - {self.subtype} - {self.replacementDuration} - {self.comment} - {self.author}'
    
    def __repr__(self):
        return f'{self.itemName} - {self.cost} - {self.subtype} - {self.replacementDuration} - {self.comment} - {self.author}'