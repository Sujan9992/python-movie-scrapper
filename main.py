from typing import Any

from bs4 import BeautifulSoup, ResultSet
from pandas import DataFrame
from requests import Response, get

URL = "https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/"

response: Response = get(URL)
soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

movie_container: ResultSet[Any] = soup.find_all(
    name="div", class_="article_movie_title"
)
data: dict[str, list[str]] = {
    "Movie": [],
    "Year": [],
}
for movie in movie_container:
    name: str = movie.find(name="h2").a.text.strip()
    year: str = movie.find(name="span", class_="subtle start-year").text.strip()
    data["Movie"].append(name)
    data["Year"].append(year)

df: DataFrame = DataFrame(data)
print(df)
