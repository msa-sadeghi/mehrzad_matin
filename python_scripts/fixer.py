import requests
import json
url = "http://data.fixer.io/api/latest?access_key=0d1601cae6d2b18ff5485dc4a00e2bf1"
def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
        
    
def archive(filename, rates):
    with open(f"archive/{filename}.json", "w") as f:
        f.write(json.dumps(rates))
        print("hello")


if __name__ == "__main__":
    data = get_rates()
    print(data['timestamp'])
    archive(data['timestamp'], data['rates'])