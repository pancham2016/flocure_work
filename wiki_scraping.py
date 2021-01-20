from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# define and open the wiki url file
wiki_url = 'https://en.wikipedia.org/wiki/Genome'
wiki_data = urlopen(wiki_url) # open the wiki url to read it

wiki_html = wiki_data.read() # read the data from the wiki url
wiki_data.close() # close the connection

page_soup = soup(wiki_html, 'html.parser')

# Create a list to store the pure text from the page
genome_text = []

# Find all the paragraphs and add their text to the list
for div in page_soup.findAll('p'):
    genome_text.append(div.text)

print(genome_text)

# Isolate sentences from the genome text with 6 words. Work in progress
for i in range(genome_text.index()):
    six_word = genome_text.pop()
