from bs4 import BeautifulSoup
import re
import requests
import unittest

# Task 1: Get the URL that links to the Pokemon Charmander's webpage.
# HINT: You will have to add https://pokemondb.net to the URL retrieved using BeautifulSoup
def getCharmanderLink(soup):
    base_url = 'https://pokemondb.net'
    ending = '/pokedex/charmander'
    r = requests.get(url+ending)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# Task 2: Get the details from the box below "Egg moves". Get all the move names and store
# them into a list. The function should return that list of moves.
def getEggMoves(pokemon):
    url = 'https://pokemondb.net/pokedex/'+pokemon
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tags = soup.find_all('a', class_='ent-name')
    collect_info = []
    for tag in tags:
        info = tag.text
        collect_info.append(info)
    return collect_info[]

# Task 3: Create a regex expression that will find all the times that have these formats: @2pm @5 pm @10am
# Return a list of these times without the '@' symbol. E.g. ['2pm', '5 pm', '10am']
def findLetters(sentences):
    # initialize an empty list
    l_times = []
    # define the regular expression
    match_t = re.search('@\d\d?\s?(am|pm)',sentences).group(0)

    # loop through each sentence or phrase in sentences
    for sentence in sentences.split():
        for phrase in sentence.split():
    # find all the words that match the regular expression in each sentence
            if match_t != None:
                l_times.append(match_t[1:])
    return l_times

    #return the list of the last letter of all words that begin or end with a capital letter
    cap_l = []
    for sentence in sentences.split():
        for wrd in sentence.split():
            if re.search('(^[A-Z]|[A-Z]$)',wrd):
                cap_l.append(wrd[-1])
    return cap_l
                




def main():
    url = 'https://pokemondb.net/pokedex/national'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    getCharmanderLink(soup)
    getEggMoves('scizor')

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://pokemondb.net/pokedex/national').text, 'html.parser')

    def test_link_Charmander(self):
        self.assertEqual(getCharmanderLink(self.soup), 'https://pokemondb.net/pokedex/charmander')

    def test_egg_moves(self):
        self.assertEqual(getEggMoves('scizor'), ['Counter', 'Defog', 'Feint', 'Night Slash', 'Quick Guard'])

    def test_findLetters(self):
        self.assertEqual(findLetters(['Come eat lunch at 12','there"s a party @2pm', 'practice @7am','nothing']), ['2pm', '7am'])
        self.assertEqual(findLetters(['There is show @12pm if you want to join','I will be there @ 2pm', 'come at @3 pm will be better']), ['12pm', '3 pm'])

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
