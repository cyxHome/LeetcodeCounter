import urllib
from BeautifulSoup import *

url = "https://leetcode.com/problemset/algorithms/"
page = urllib.urlopen(url).read()

soup = BeautifulSoup(page)
table = soup.find(id="problemList")

total = 0
easy = 0
easyLocked = 0
medium = 0
mediumLocked = 0
hard = 0
hardLocked = 0
lock = 0
isLocked = False
for tr in table.tbody.findAll('tr'):
	isLocked = False
	for td in tr.findAll('td')[2:5]:
		icons = td.findAll('i')
		if len(icons) > 0:
			isLocked = True
        if td.getText() == "Easy":
        	easy = easy + 1
        	if isLocked == True:
        		easyLocked = easyLocked + 1
        elif td.getText() == "Medium":
        	medium = medium + 1
        	if isLocked == True:
        		mediumLocked = mediumLocked + 1
        elif td.getText() == "Hard":
        	hard = hard + 1
        	if isLocked == True:
        		hardLocked = hardLocked + 1
            

total = easy + medium + hard

print 'total:', total
print 'total lock:', easyLocked+mediumLocked+hardLocked
print 'easy unlocked:', easy-easyLocked
print 'medium unlocked:', medium-mediumLocked
print 'hard unlocked:', hard-hardLocked
print 'easy locked:', easyLocked
print 'medium locked:', mediumLocked
print 'hard locked:', hardLocked
