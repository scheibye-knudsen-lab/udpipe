import asyncio
import requests
import itertools
import json
import time
import pandas as pd

async def main(docs):
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            requests.get, 
            'http://172.17.0.4:8080/process',
            {
                'data':doc['text'],
                'tokenizer':'',
                'tagger':'',
                'parser':'',
                'output':'epe'
            }
        )
        for doc in docs
    ]
    
    responses = await asyncio.gather(*futures)
    
    for idx, doc in enumerate(docs):
        doc['epe'] = responses[idx].json()['result']

    return docs

loop = asyncio.get_event_loop()

text = 'This is some text.'

with open('udpipe.json', 'w') as outfile:
    for chunk in pd.read_csv('../file.txt', chunksize=100, delimiter='\t'):
        documents = []
        for index, row in chunk.iterrows():
            documents.append({'text':row[0]}) 

        #start = time.time()
        results = loop.run_until_complete(main(documents))
        #end = time.time()
        #print(end-start)
        for result in results:
            outfile.write(json.dumps(result) + '\n')
        