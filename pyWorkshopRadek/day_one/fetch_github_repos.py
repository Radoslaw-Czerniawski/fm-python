import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    GH_API_REPO_SEARCH_URL = "https://api.github.com/search/repositories"

    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(GH_API_REPO_SEARCH_URL, params=params)

    # status_code = 500
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occurred. Status code was: {status_code}")
    else:
        items = response.json()["items"]
        return items

if __name__ == "__main__":
    languages = ["Python", "Javascript", "Ruby"]

    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
