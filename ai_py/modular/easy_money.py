import re
import csv
import requests

# url = f'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-12-16&ed=2021-12-16&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1'
for page in range(1, 193):
    print(f'-------------------------正在爬取第{page}页内容-----------------------')
    url = f'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-12-16&ed=2021-12-16&qdii=&tabSubtype=,,,,,&pi={page}&pn=50&dx=1'
    headers = {
        'Cookie': 'HAList=a-sz-300059-%u4E1C%u65B9%u8D22%u5BCC; em_hq_fls=js; qgqp_b_id=7b7cfe791fce1724e930884be192c85e; _adsame_fullscreen_16928=1; st_si=59966688853664; st_asi=delete; st_pvi=79368259778985; st_sp=2021-12-07%2014%3A33%3A35; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=3; st_psi=20211216201351423-112200312936-0028256540; ASP.NET_SessionId=miyivgzxegpjaya5waosifrb',
        'Host': 'fund.eastmoney.com',
        'Referer': 'http://fund.eastmoney.com/data/fundranking.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    data = response.text
    data_str = re.findall('\[(.*?)\]', data)[0]
    tuple_data = eval(data_str)
    for td in tuple_data:
        # 把td 变成列表
        td_list = td.split(',')

        with open('基金.csv', mode='a', encoding='utf-8', newline='') as f:
          csv_write = csv.writer(f)
          csv_write.writerow(td_list)
          print(td)