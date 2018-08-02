#imports
from recipe_scrapers import scrape_me
import spacy
from pint import UnitRegistry
from pint.errors import UndefinedUnitError 
from rid_uni_frac import rid_uni_frac
#initialisations
ureg = UnitRegistry() 
nlp = spacy.load('en_core_web_md') 



def get_recipe(URL):
#.title()
#.ingredients()
#.total_time()
#.instructions()
#.links()
    return scrape_me(URL)

def parse_ingredients(ingredients_string):
    #remove unicode fractions (often used by bbc good food)
    ingredients_string = rid_uni_frac(ingredients_string)
    doc = nlp(ingredients_string)
    if doc[0].tag_ == 'CD':
        try:
            return ureg.parse_expression(str(doc[0:2])), doc[2:]
        except UndefinedUnitError:
            return doc[0], doc[1:]
    else:
        return 1,doc

def ingredients_tokenisation(ingredients_string):
    doc = nlp(ingredients_string)
    return [token.tag_ for token in doc]

