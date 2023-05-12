import requests

def get_exercise():
    url = "https://exercisedb.p.rapidapi.com/exercises"
    headers = {
	"X-RapidAPI-Key": "28dfc0e2a6mshfd18a7f7d3c3901p173983jsncd5d692debd5",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

    response = requests.get(url, headers=headers)
    if response.ok:
        data = response.json()
        print(data)
    else:
        return None



