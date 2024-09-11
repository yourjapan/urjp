
from xml.etree import ElementTree
from rest_framework.parsers import BaseParser


class EbayParser(BaseParser):
    media_type = 'text/xml'
    tree = None
    
    # https://developer.ebay.com/DevZone/XML/Docs/Reference/eBay/GetItemTransactions.html
    def parse(self, stream, media_type=None, parser_context=None):
        self.tree = ElementTree.parse(stream)
        print({
            'datetime': self.get('PaymentTime'),
            'item': [self.get('SKU'), self.get('Title')],
            'n': self.get('QuantityPurchased'),
            'buyer': self.get('StaticAlias'),
            'buyer2': self.get('UserID', 'Buyer'),
        })
        return {
            'item': self.get('SKU'),
            'n': int(self.get('QuantityPurchased')),
        }
    
    def get(self, leaf, branch=None):
        NS = {'eb': 'urn:ebay:apis:eBLBaseComponents'}
        
        e = self.tree.find(f'.//eb:{branch}', NS) or self.tree
        e = e.find(f'.//eb:{leaf}', NS)

        try:    return e.text
        except: return None
