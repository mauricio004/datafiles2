__author__ = 'MFlores1'

from recommendations import topMatches
from recommendations import getRecommendations
from recommendations import sim_distance
from recommendations import sim_pearson

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
}


# Transform dictionary to item based from user based

def transform(prefs):
    itemDict = {}

    # Find items
    for c in prefs:
        for item in prefs[c]:
            itemDict.setdefault(item, {})
            itemDict[item][c] = prefs[c][item]
    return itemDict

itemDict = transform(critics)

# print itemDict

# print topMatches(itemDict, 'Lady in the Water',)

# print getRecommendations(itemDict, "Lady in the Water")


# Compare similar items
def calculateSimilarItems(prefs, n):

    simDict = {}

    # Transform to item base
    itemSim = transform(prefs)

    for item in itemSim:
        simDict[item] = topMatches(itemSim, item, n=n, similarity=sim_distance)

    return simDict


# print calculateSimilarItems(critics, n=5)

# ToDo
# Movies data, get recommendations for user '87'
# Use .getRecommendations and .getRecommendedItems functions to compare

# Create a dictionary with data

def readDataMovieLens(path='C:/Users/mflores1/Dropbox/Mauricio/ci/chapter_2/ml-100k'):
    # Get movie titles
    movies = {}
    for line in open(path+'/u.item'):
        (movie_id, movie_tile) = line.split('|')[0:2]
        movies[movie_id] = movie_tile

    # Load data
    prefs = {}
    for line in open(path+'/u.data'):
        (user_id, movie_id, rating, ts) = line.split('\t')
        prefs.setdefault(user_id, {})
        prefs[user_id][movies[movie_id]] = float(rating)

    return prefs


prefs = readDataMovieLens()
# print len(prefs['87'])

# print topMatches(prefs, '87', 10)[0:30]
print calculateSimilarItems(prefs, n=5)

