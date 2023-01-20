import uuid
import requests
from pprint import pprint
import json
import time
response = requests.get('https://api.kanye.rest')

# pprint(response.json())
print(response.json()['quote'])

# respone2 = requests.get('https://api.fakeyou.com/tts/list')
# output = respone2.json()
# pprint(respone2.json())


# for index, model in enumerate(output['models']):
#     print(index, model['model_token'], model['title'])


# voices = [(index, model['model_token'], model['title'])
#           for index, model in enumerate(output['models'])]

# voices_refined = []

# for model in output['models']:
#     if 'Roosevelt' in model['title']:
#         voices_refined.append(model)


# with open('api.json', 'w', encoding='utf-8', errors='backslashreplace') as f:
#     f.write(str(voices_refined))

# for model in voices_refined:
#     print(model['title'], model['model_token'])


voice_tokens = {
    'Obama': 'TM:58vtv7x9f32c',
    'Gandhi': 'TM:cvw5qkye9y22',
    'Churchill': 'TM:3na2hzvbfqn7',
    'Kennedy': 'TM:a9pmkvtg2p6b',
    'FDR': 'TM:jh0bts33pn7x',
    'Teddy': 'TM:pn9edma33t2j',
}

myuuid = str(uuid.uuid4())
text = response.json()['quote']
payload = {
    'uuid_idempotency_token': myuuid,
    'tts_model_token': voice_tokens['Obama'],
    'inference_text': text
}
heads_post = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
head_get = {
    'Accept': 'application/json',
}

response3 = requests.post(
    'https://api.fakeyou.com/tts/inference', headers=heads_post, json=payload)

pprint(response3.json())
job_token = response3.json()['inference_job_token']


def status_checker(token):
    poll_response = requests.get(
        f'https://api.fakeyou.com/tts/job/{token}', headers=heads_post)

    pprint(poll_response.json())

    status = poll_response.json()['state']['status']
    progress = ['pending', 'started']
    audio_path = poll_response.json(
    )['state']['maybe_public_bucket_wav_audio_path']

    if audio_path:
        return f'https://storage.googleapis.com/vocodes-public{audio_path}'
    elif status in progress:
        time.sleep(3)
        return status_checker(token)
    else:
        return status


print(status_checker(job_token))
