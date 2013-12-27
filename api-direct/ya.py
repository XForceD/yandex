import json, urllib.request

cn = True
bn = False

#адрес для отправки json-запросов
url = 'https://api-sandbox.direct.yandex.ru/json-api/v4/'

#данные для OAuth-авторизации
token = 'ccc3811a31484b90b6b766389c94bccc'

#логин в Директе
#login = 'agrom'

dataCmp = {'method': 'GetCampaignsList','token': token,'locale': 'ru'}
jdataCmp = json.dumps(dataCmp, ensure_ascii=False).encode('utf8')
responseCmp = urllib.request.urlopen(url,jdataCmp)
resdataCmp=json.loads(responseCmp.read().decode('utf8'))
for cmp in resdataCmp['data']:
  cn = not(cn) #срабатываем через раз начиная со второго(четные)
  if cn :
    dataBann = {'method': 'GetBanners','token': token,'locale': 'ru','param': {'CampaignIDS': [cmp['CampaignID']]}}
    jdataBann = json.dumps(dataBann, ensure_ascii=False).encode('utf8')
    responseBann = urllib.request.urlopen(url,jdataBann)
    resdataBann=json.loads(responseBann.read().decode('utf8'))
    for Bann in resdataBann['data']:
       bn = not(bn) #срабатываем через раз начиная со первого(нечетные)
       if bn:
        dataoff = {'method': 'GetBanners','token': token,'locale': 'ru','param': {'CampaignID': [cmp['CampaignID']],'BannerIDS': [Bann['BannerID']]}}
        jdata3 = json.dumps(dataoff, ensure_ascii=False).encode('utf8')
        responseoff = urllib.request.urlopen(url,jdataoff)
#        print(response3.read().decode('utf8'))
