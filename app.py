from flask import Flask, request
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features

authenticator = IAMAuthenticator('0JvlsYrIsF0NnuZPipiqNu8WIkoiC5Pbty98LSorNERv')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator)

natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/37a51fcf-736c-472a-85ed-84f0904cce24')

#app = Flask(__name__)



@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/author', methods = ['POST'])
def metadata():
    #return response
    url_input = request.form.get('url')
    response = natural_language_understanding.analyze(
    url=url_input,
    features=Features(metadata= {})).get_result()

    
    print(json.dumps(response, indent=2))

    author = json.dumps(response.get("metadata").get("authors"))
    return author
    
    
    #return url_input

if __name__ == '__main__':
    app.run()





