from flask import Flask
from flask import request
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/', methods=['POST'])
def getMicrosoftAcademic():
    ret_dict = {'affiliations':[], 'authors':[], 'journal':[]}

    # Manmade headers to avoid blocking from server
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
    'Cookie':'ai_session=w1eGF|1513779026452|1513779256487; MUID=2B4B52DCB493667E1CB95982B0936015; __RequestVerificationToken=vM2VoVHgmbLC-ow0Fay4aizjCfy-p49OuhX2FppahE7RMEQ12UI6eCbDqt20Mo36l8c4Nyk2lRv05SMauEBNmc9uelGb_zuGp46ZnqTwxa41; ai_user=ZTbjG|2017-12-19T11:07:38.106Z; ARRAffinity=a77f61b2b79195028eac29732aceb35898dc3f7310e484afa258cd4aec12af56; msacademic=de6cce3b-092f-43c1-af0e-c6cd78b08a47; __CT_Data=gpv=13&apv_14334_www08=1&cpv_14334_www08=1&apv_32434_www07=9&cpv_32434_www07=7&rpv_32434_www07=7&apv_32260_www07=1&cpv_32260_www07=1&rpv_32260_www07=1&ckp=tld&dm=microsoft.com&apv_38960_www02=1&cpv_38960_www02=1&apv_32381_www07=1&cpv_32381_www07=1; MSCC=1512961787; _ga=GA1.2.1973300941.1452618403; MSFPC=ID=cf69e0aa9089f3409cbd3bbe7951b544&CS=3&LV=201712&V=1; AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg=-179204249%7CMCMID%7C44350014803615175994576818174013995990%7CMCAAMLH-1498447038%7C11%7CMCAAMB-1498447038%7CcIBAx_aQzFEHcPoEv0GwcQ%7CMCOPTOUT-1497849438s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C2069418076%7CMCSYNCS%7C411-17344*1083-17344*1085-17344*1086-17344*1087-17344*1088-17344*19913-17344*83349-17344; optimizelyEndUserId=oeu1427699881445r0.503182060085237; gssLANG=zh-tw; A=I&I=AxUFAAAAAABdCAAAnihiZn9FqAL5KxK9uTlnWQ!!&V=4; MC1=GUID=cf69e0aa9089f3409cbd3bbe7951b544&HASH=cf69&LV=201703&V=4&LU=1488524446041; optimizelyBuckets=%7B%222425001179%22%3A%222439241021%22%2C%222454270402%22%3A%222467670120%22%7D; optimizelySegments=%7B%22223033821%22%3A%22false%22%2C%22223040836%22%3A%22direct%22%2C%22223082014%22%3A%22safari%22%2C%22244338170%22%3A%22none%22%2C%222098371093%22%3A%22true%22%2C%222130980600%22%3A%22true%22%2C%222327161334%22%3A%22none%22%2C%222337730596%22%3A%22false%22%2C%222357090901%22%3A%22safari%22%2C%222368960498%22%3A%22referral%22%2C%222865651701%22%3A%22true%22%2C%226202010951%22%3A%22direct%22%2C%226206680296%22%3A%22safari%22%2C%226183560892%22%3A%22none%22%2C%226208020262%22%3A%22false%22%2C%226273432096%22%3A%22false%22%2C%226261715352%22%3A%22safari%22%2C%226273411924%22%3A%22none%22%2C%226273374518%22%3A%22direct%22%2C%226190090623%22%3A%22safari%22%2C%226213440327%22%3A%22none%22%2C%226201801690%22%3A%22search%22%2C%226204850164%22%3A%22false%22%2C%227961301167%22%3A%22false%22%2C%227927848602%22%3A%22none%22%2C%227962561100%22%3A%22safari%22%2C%227951071293%22%3A%22direct%22%7D; WT_FPC=id=25ad1d1857da7c581fa1441877068690:lv=1486506414684:ss=1486506414684; omniID=1446164022856_b776_950e_3464_512b34d90c27; msresearch=%7B%22version%22%3A%225.0%22%2C%22state%22%3A%7B%22name%22%3A%22IDLE%22%2C%22url%22%3A%22undefined%22%2C%22timestamp%22%3A1452438866599%7D%2C%22lastinvited%22%3A1486479407366%2C%22userid%22%3A%221452438866599953131574206054%22%2C%22vendorid%22%3A1%2C%22surveys%22%3A%5B%22p329970507%22%2C%22p246609455%22%5D%2C%22graceperiod%22%3A5%2C%22trackertimestamp%22%3A0%7D; msdn=L=zh-tw; srRef=true; s_dayssincelastvisit=1453122633003; s_fid=5292004183164C04-33594B17A6409CD6; icxid=1453122583896-8798973923950592; ST_GN_EN-US=2_16523.38628340278_90; ST_GN_ZH-TW=1_0_0; fmsvs=15S10; WT_NVR_RU=0=msdn|technet:1=MSDN&/:2='}

    params = request.form.to_dict()
    params['query'] = '@'+params['query']+'@'

    filter_url = 'https://academic.microsoft.com/api/search/GetFilters'

    form_data = urlencode(params).encode("utf-8")
    req = Request(filter_url, headers=headers, method='POST')
    res = urlopen(req, data=form_data)
    html_doc = res.read().decode('utf-8')
    soup = BeautifulSoup(html_doc, 'html.parser')

    filter_data = json.loads(str(soup))

    for item in filter_data['availableFilters'][1]['values']:
        ret_dict['authors'].append(item['displayName'])
    for item in filter_data['availableFilters'][2]['values']:
        ret_dict['affiliations'].append(item['displayName'])
    for item in filter_data['availableFilters'][4]['values']:
        ret_dict['journal'].append(item['displayName'])

    return str(ret_dict)