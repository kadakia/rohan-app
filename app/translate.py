import json
import requests
# from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']: # what's the difference ?!
        return 'Error: the translation service is not configured.'
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']} # what is Ocp ?
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc/Translate?text={}&from={}&to={}'.format(
        text, source_language, dest_language), headers=auth)
    if r.status_code != 200:
        return 'Error: the translation service failed.'
    return json.loads(r.content.decode('utf-8-sig')) # utf-8-sig is Microsoft variant of utf-8