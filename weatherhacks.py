# coding: UTF-8
# livedoorのweather hacksを使う

import json
import urllib


class Weatherhacks(object):

    def __init__(self, location):
        titenteigi = {u"稚内": "011000",
                      u"旭川": "012010",
                      u"留萌": "012020",
                      u"網走": "013010",
                      u"北見": "013020",
                      u"紋別": "013030",
                      u"根室": "014010",
                      u"釧路": "014020",
                      u"帯広": "014030",
                      u"室蘭": "015010",
                      u"浦河": "015020",
                      u"札幌": "016010",
                      u"岩見沢": "016020",
                      u"倶知安": "016030",
                      u"函館": "017010",
                      u"江差": "017020",
                      u"青森": "020010",
                      u"むつ": "020020",
                      u"八戸": "020030",
                      u"盛岡": "030010",
                      u"宮古": "030020",
                      u"大船渡": "030030",
                      u"仙台": "040010",
                      u"白石": "040020",
                      u"秋田": "050010",
                      u"横手": "050020",
                      u"山形": "060010",
                      u"米沢": "060020",
                      u"酒田": "060030",
                      u"新庄": "060040",
                      u"福島": "070010",
                      u"小名浜": "070020",
                      u"若松": "070030",
                      u"水戸": "080010",
                      u"土浦": "080020",
                      u"宇都宮": "090010",
                      u"大田原": "090020",
                      u"前橋": "100010",
                      u"みなかみ": "100020",
                      u"さいたま": "110010",
                      u"熊谷": "110020",
                      u"秩父": "110030",
                      u"千葉": "120010",
                      u"銚子": "120020",
                      u"館山": "120030",
                      u"東京": "130010",
                      u"大島": "130020",
                      u"八丈島": "130030",
                      u"父島": "130040",
                      u"横浜": "140010",
                      u"小田原": "140020",
                      u"新潟": "150010",
                      u"長岡": "150020",
                      u"高田": "150030",
                      u"相川": "150040",
                      u"富山": "160010",
                      u"伏木": "160020",
                      u"金沢": "170010",
                      u"輪島": "170020",
                      u"福井": "180010",
                      u"敦賀": "180020",
                      u"甲府": "190010",
                      u"河口湖": "190020",
                      u"長野": "200010",
                      u"松本": "200020",
                      u"飯田": "200030",
                      u"岐阜": "210010",
                      u"高山": "210020",
                      u"静岡": "220010",
                      u"網代": "220020",
                      u"三島": "220030",
                      u"浜松": "220040",
                      u"名古屋": "230010",
                      u"豊橋": "230020",
                      u"津": "240010",
                      u"尾鷲": "240020",
                      u"大津": "250010",
                      u"彦根": "250020",
                      u"京都": "260010",
                      u"舞鶴": "260020",
                      u"大阪": "270000",
                      u"神戸": "280010",
                      u"豊岡": "280020",
                      u"奈良": "290010",
                      u"風屋": "290020",
                      u"和歌山": "300010",
                      u"潮岬": "300020",
                      u"鳥取": "310010",
                      u"米子": "310020",
                      u"松江": "320010",
                      u"浜田": "320020",
                      u"西郷": "320030",
                      u"岡山": "330010",
                      u"津山": "330020",
                      u"広島": "340010",
                      u"庄原": "340020",
                      u"下関": "350010",
                      u"山口": "350020",
                      u"柳井": "350030",
                      u"萩": "350040",
                      u"徳島": "360010",
                      u"日和佐": "360020",
                      u"高松": "370000",
                      u"松山": "380010",
                      u"新居浜": "380020",
                      u"宇和島": "380030",
                      u"高知": "390010",
                      u"室戸岬": "390020",
                      u"清水": "390030",
                      u"福岡": "400010",
                      u"八幡": "400020",
                      u"飯塚": "400030",
                      u"久留米": "400040",
                      u"佐賀": "410010",
                      u"伊万里": "410020",
                      u"長崎": "420010",
                      u"佐世保": "420020",
                      u"厳原": "420030",
                      u"福江": "420040",
                      u"熊本": "430010",
                      u"阿蘇乙姫": "430020",
                      u"牛深": "430030",
                      u"人吉": "430040",
                      u"大分": "440010",
                      u"中津": "440020",
                      u"日田": "440030",
                      u"佐伯": "440040",
                      u"宮崎": "450010",
                      u"延岡": "450020",
                      u"都城": "450030",
                      u"高千穂": "450040",
                      u"鹿児島": "460010",
                      u"鹿屋": "460020",
                      u"種子島": "460030",
                      u"名瀬": "460040",
                      u"那覇": "471010",
                      u"名護": "471020",
                      u"久米島": "471030",
                      u"南大東": "472000",
                      u"宮古島": "473000",
                      u"石垣島": "474010",
                      u"与那国島": "474020"}

        id = titenteigi[location]
        url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=" + id
        json_data = urllib.urlopen(url).read()
        encode_json_data = json.dumps(json.loads(json_data),ensure_ascii=False).encode('utf-8')
        self.readable_json_data = json.loads(encode_json_data)


    def weather(self):
        return self.readable_json_data["description"]["text"] #天気の概要

    def today(self):
        return self.readable_json_data["forecasts"][0]["telop"] #今日の天気

    def today_min(self):
        if self.readable_json_data["forecasts"][0]["temperature"]["min"] is None:
            return None
        else:
            return self.readable_json_data["forecasts"][0]["temperature"]["min"]["celsius"] #今日の最低気温

    def today_max(self):
        if self.readable_json_data["forecasts"][0]["temperature"]["max"] is None:
            return None
        else:
            return self.readable_json_data["forecasts"][0]["temperature"]["max"]["celsius"] #今日の最高気温

    def tomorrow(self):
        return self.readable_json_data["forecasts"][1]["telop"] #明日の天気

    def tomorrow_min(self):
        if self.readable_json_data["forecasts"][1]["temperature"]["min"] is None:
            return None
        else:
            return self.readable_json_data["forecasts"][1]["temperature"]["min"]["celsius"] #明日の最低気温

    def tomorrow_max(self):
        if self.readable_json_data["forecasts"][1]["temperature"]["max"] is None:
            return None
        else:
            return self.readable_json_data["forecasts"][1]["temperature"]["max"]["celsius"] #明日の最高気温
