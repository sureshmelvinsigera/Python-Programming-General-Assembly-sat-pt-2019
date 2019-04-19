import requests
import json

# # Yelp API key
# api_key = '6BwsOPVFlUYN4XtuY5nFmzo0JGqwbpeCx1FcF0MSePgMKABojUILcQjbixFbRObPV4-qTj2s7VFgALMiLMb0PREf73BIY_ecMdmxr8Lpjciv2z8ivk5WD4iaRrm4XHYx'
# headers = {'Authorization': 'Bearer %s' % api_key}

# Business Search

# url = 'https://api.yelp.com/v3/businesses/search'
# In the dictionary, term can take values like food, cafes or businesses like McDonalds
# params = {'term': 'seafood', 'location': 'New York City'}
# Making a get request to the API
# req = requests.get(url, params=params, headers=headers)
# proceed only if the status code is 200
# print('The status code is {}'.format(req.status_code))
# print(json.loads(req.text))


# Business Reviews

# url = "https://api.yelp.com/v3/businesses/I3_QvspB0SsqiUTN18-TlQ/reviews"
# req = requests.get(url, headers=headers)
# print('the status code is {}'.format(req.status_code))
# print(json.loads(req.text))


# id = 'I3_QvspB0SsqiUTN18-TlQ'
# url = "https://api.yelp.com/v3/businesses/" + id + "/reviews"
# req = requests.get(url, headers=headers)
# parsed = json.loads(req.text)
# reviews = parsed["reviews"]
#
# # print(reviews)
#
# for review in reviews:
#     print(review['user']['name'], review['text'], review['rating'])
