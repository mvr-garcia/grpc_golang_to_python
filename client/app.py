from flask import Flask, render_template, request
from grpc import insecure_channel

import countries_pb2
import countries_pb2_grpc

app = Flask(__name__)


def countrie_client(countrie):
    print("Start service")

    try:
        channel = insecure_channel('localhost:3000')
        stub = countries_pb2_grpc.CountryStub(channel)
        country_request = countries_pb2.CountryRequest(name=countrie)
        country_response = stub.Search(country_request)

        infodata = {
            "name": country_response.name,
            "alpha2Code": country_response.alpha2Code,
            "capital": country_response.capital,
            "subregion": country_response.subregion,
            "population": country_response.population,
            "nativeName": country_response.nativeName
        }

        return infodata

    except Exception as e:
        print(e)
        return e


@app.route("/infotable", methods=['POST'])
def infotable():
    if request.method == 'POST':
        country = request.form['country']
        country = country.lower()
        data = countrie_client(country)
    return render_template('index.html', infodata=data)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
