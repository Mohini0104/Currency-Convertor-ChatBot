from flask import Flask ,request,jsonify
import requests
app=Flask(__name__)
@app.route("/", methods =['POST'])
def index():
    data=request.get_json()
    print(data)
    amount =data['queryResult']['parameters']['unit-currency']['amount']
    sourceCurrency=data['queryResult']['parameters']['unit-currency']['currency']
    resultCurrency=data['queryResult']['parameters']['currency-name']
    factor=convert(sourceCurrency,resultCurrency)

    finalAmount=amount*factor

    response={
        'fulfillmentText':"{} {} is {} {}".format(amount,sourceCurrency,finalAmount,resultCurrency)
    }

    return jsonify(response)
def convert(sourceCurrency,resultCurrency):
    url="https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=5cfc305183b4af597adb".format(
        sourceCurrency,resultCurrency)
    data=requests.get(url)
    data=data.json()
    return data['{}_{}'.format(sourceCurrency,resultCurrency)]



if __name__=="__main__":
    app.run(debug=True)
