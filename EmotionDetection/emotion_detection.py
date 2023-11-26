import requests,json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    j=json.loads(response.text)
    f=j['emotionPredictions'][0]['emotion']
    max=0
    d={}
    d['anger']=f['anger']
    d['disgust']=f['disgust']
    d['fear']=f['fear']
    d['joy']=f['joy']
    d['sadness']=f['sadness']
    temp=''
    for i in d.keys():
        if(d[i]>max):
            max=f[i]
            temp=i
    d['dominant_emotion']=temp
    return d
