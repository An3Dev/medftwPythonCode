import base64
import requests


def getImage(prompt):
    image = requests.post('https://dev.paint.cohere.ai/txt2img', 
                                json={
                                    'prompt': f'{prompt} ; color icon', 
                                    'H' : 512,
                                    'W' : 512,
                                    'n_samples' : 1, 
                                    'n_iter' : 1})
    raw = image.json()['image']
    imageBytes = base64.b64decode(raw) #decode
    return imageBytes
