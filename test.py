import urllib,sys
import ssl

host = 'https://qryidcard.market.alicloudapi.com'
path = '/lundear/ckidcard'
method = 'GET'
appcode = 'aa3b10a67f114d43906d8fa24cc49xxx'
querys = 'idcard=142325198504230022&name=%E8%B4%BE%E7%90%B3'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)
