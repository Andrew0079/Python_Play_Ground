import requests
import pprint
import pandas as pd

"""To check out the code below please sign up to
    https://www.themoviedb.org/
    and use your own API keys"""

api_key = "***************************"
api_key_v4 = "***********************"

"""
HTTP requests

Endpoint --> GET/movie/{movie_id}
"""

""" API Version 3"""
movie_id = 550
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f"/movie/{movie_id}"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
r = requests.get(endpoint)
print(r.status_code)
print(r.text)

print("*" * 15)

""" API Version 4"""
movie_id = 500
api_version = 4
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f"/movie/{movie_id}"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf8'
}
r = requests.get(endpoint, headers=headers)
print(r.status_code)
print(r.text)

"""****************"""

api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
r = requests.get(endpoint)
data = r.json()
print(data['results'])
# pprint.pprint(r.json())

if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        print("\n" + "*" * 10 + "\n")
        print(results[0].keys())
        print("\n" + "*" * 10 + "\n")
        movies_ids = set()
        for result in results:
            _id = result['id']
            print(result['title'], _id)
            movies_ids.add(_id)
        # print(list(movies_ids))

print("\n" + "*" * 10 + "\n")
output = 'movies.csv'
movie_data = []
for movie_id in movies_ids:
    api_version = 3
    api_base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)


df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)

