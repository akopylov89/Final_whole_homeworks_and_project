
def cur_rate(rate1, rate2, rate3):
    import urllib2
    import json
    s = ('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22{}%2C{}%2C{}%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'.format(rate1, rate2,rate3))
    d = ('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22RUBBYR%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'.format(rate3))
    u = urllib2.urlopen(s)
    u.getcode()
    data = u.read()
    parsed_data = json.loads(data)
    parsed_data.keys()
    parsed_data["query"]["results"]
    y = urllib2.urlopen(d)
    y.getcode()
    ru_data = y.read()
    parsed_ru_data = json.loads(ru_data)
    parsed_ru_data.keys()
    parsed_ru_data["query"]["results"]
    print(str(parsed_data["query"]["results"]['rate'][0]['Name']),":",str(parsed_data["query"]["results"]['rate'][0]['Rate']))
    print(str(parsed_data["query"]["results"]['rate'][1]['Name']),":",str(parsed_data["query"]["results"]['rate'][1]['Rate']))
    print(str(parsed_ru_data["query"]["results"]['rate']['Name']),":",str(parsed_ru_data["query"]["results"]['rate']['Rate']))

cur_rate("USDBYR", "EURBYR","RURBYR")

