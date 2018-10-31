# Project for CS328 - Data Management/Data Wrangling
# Coded by: Od Ganzorig and Patrick Conboy
# Date Created: 9/18/2018
# Project Description: Web API that provides user access to data analytics on 
# tweets containing mentions of Overwatch and heroes in the game.

#!/usr/bin/python3

# Accessing the Twitter API
# This script describes the basic methodology for accessing a Twitter feed
# or something similar.

# Loading libraries needed for authentication and requests
import operator
import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

# In order to use this script, you must:
# - Have a Twitter account and create an app
# - Store in keys.json a property called "twitter" whose value is an
#     object with two keys, "key" and "secret"
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['twitter']

twitter_key = keys['key']
twitter_secret = keys['secret']

# We authenticate ourselves with the above credentials
# We will demystify this process later
#
# For documentation, see http://requests-oauthlib.readthedocs.io/en/latest/api.html
# and http://docs.python-requests.org/en/master/
client = BackendApplicationClient(client_id=twitter_key)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://api.twitter.com/oauth2/token',
                          client_id=twitter_key,
                          client_secret=twitter_secret)

# Base url needed for all subsequent queries
base_url = 'https://api.twitter.com/1.1/'

# Particular page requested. The specific query string will be
# appended to that.
page = 'search/tweets.json'

                # END OF AUTHENTICATION AND OAUTH STUFF #


             # BEGINNING OF INDIVIDUAL QUERIES FOR EACH HERO #

#################### QUERY FOR D.VA TWEETS ##############################
# This is where we define what type of tweets we want, via the string below
req_url = base_url + page + '?q=Overwatch+DVA&tweet_mode=extended&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## The following code will attempt to read up to 10000 tweets that
## mention DVA 
dva_tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break
   if len(dva_tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   dva_tweets.extend(results['statuses'])



#################### QUERY FOR ORISA TWEETS ##############################
# This is where we define what type of tweets we want, via the string below
req_url = base_url + page + '?q=Overwatch+Orisa&tweet_mode=extended&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## The following code will attempt to read up to 10000 tweets that
## mention Orisa 
orisa_tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break
   if len(orisa_tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   orisa_tweets.extend(results['statuses'])



#################### QUERY FOR REINHARDT TWEETS ##############################
# This is where we define what type of tweets we want, via the string below
req_url = base_url + page + '?q=Overwatch+Reinhardt&tweet_mode=extended&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## The following code will attempt to read up to 10000 tweets that
## mention Reinhardt 
reinhardt_tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break
   if len(reinhardt_tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   reinhardt_tweets.extend(results['statuses'])



#################### QUERY FOR ROADHOG TWEETS ##############################
# This is where we define what type of tweets we want, via the string below
req_url = base_url + page + '?q=Overwatch+Roadhog&tweet_mode=extended&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## The following code will attempt to read up to 10000 tweets that
## mention Roadhog 
roadhog_tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break
   if len(roadhog_tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   roadhog_tweets.extend(results['statuses'])



#################### QUERY FOR WINSTON TWEETS ##############################
# This is where we define what type of tweets we want, via the string below
req_url = base_url + page + '?q=Overwatch+Winston&tweet_mode=extended&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## The following code will attempt to read up to 10000 tweets that
## mention Winston 
winston_tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break 
   if len(winston_tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   winston_tweets.extend(results['statuses'])



#################### QUERY FOR HAMMOND TWEETS ##############################
# This is where we define what type of tweets we want, via the string below
req_url = base_url + page + '?q=Overwatch+Hammond&tweet_mode=extended&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## The following code will attempt to read up to 10000 tweets that
## mention Hammond 
hammond_tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break 
   if len(hammond_tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   hammond_tweets.extend(results['statuses'])



#################### QUERY FOR ZARYA TWEETS ##############################
# This is where we define what type of tweets we want, via the string below
req_url = base_url + page + '?q=Overwatch+Zarya&tweet_mode=extended&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## The following code will attempt to read up to 10000 tweets that
## mention Zarya 
zarya_tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break 
   if len(zarya_tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
#    print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   zarya_tweets.extend(results['statuses'])

                # END OF QUERIES FOR EACH HERO #


            # BEGINNING OF ORGANIZING QUERIES INTO DATA STRUCTURES #

# These 4 lines just put all the 'full_text' fields from our list of tweets
# into a list and prints them with a line break after each tweet for readability.
# Just testing stuff. Will delete later :D
tweet_text = [tweet['full_text'] for tweet in hammond_tweets]
for tweet in tweet_text:
    print(tweet)
print(len(tweet_text))


