
from xml.etree import ElementTree
from rest_framework.parsers import BaseParser


class EbayParser(BaseParser):
    media_type = 'text/xml'
    tree = None
    
    def parse(self, stream, media_type=None, parser_context=None):
        self.tree = ElementTree.parse(stream)
        return {
            'item': self.get('SKU'),
            'n': self.get('QuantityPurchased'),
        }
    
    def get(self, leaf, branch=None):
        NS = {'eb': 'urn:ebay:apis:eBLBaseComponents'}
        
        e = self.tree.find(f'.//eb:{branch}', NS) or self.tree
        e = e.find(f'.//eb:{leaf}', NS)

        try:    return e.text
        except: return None
