from datetime import time

from bs4 import BeautifulSoup
from django.contrib.sites import requests
from django.http import HttpResponse

from ai_py import models
from ai_py.models import Test, Contact


def test(request):
    dto = Test(name="asdf")
    dto.save()
    objs = [Test(name="1"),
            Test(name="2"),
            Test(name="2"),
            Test(name="2"),
            Test(name="3")]
    models.Test.objects.bulk_create(objs, 10)
    return HttpResponse("ok")


def m3(request):
    data = [1,2,3]
    d = dict()
    d = d.fromkeys(data,"ss")
    print(d)
    return HttpResponse("a")


def insert(request):
    datas = [
        131101,
        450601,
        360501,
        450701,
        360601,
        450801,
        360701,
        450901,
        500100,
        500200,
        410101,
        500300,
        410201,
        320101,
        410301,
        320201,
        230101,
        410401,
        320301,
        230201,
        140101,
        410501,
        320401,
        230301,
        140201,
        410601,
        320501,
        230401,
        140301,
        410701,
        320601,
        230501,
        640111,
        640101,
        140401,
        410801,
        320701,
        640201,
        640203,
        230601,
        140501,
        460039,
        460038,
        460037,
        410901,
        640301,
        320801,
        230701,
        140601,
        460101,
        411001,
        320901,
        230801,
        460201,
        370101,
        411101,
        321001,
        230901,
        370201,
        411201,
        321101,
        231001,
        370301,
        411301,
        370401,
        411401,
        370501,
        411501,
        370601,
        362502,
        370701,
        370801,
        510101,
        420101,
        371001,
        510301,
        420201,
        330101,
        371101,
        510401,
        420301,
        330201,
        371201,
        510501,
        150101,
        371301,
        510601,
        420501,
        330401,
        445101,
        150201,
        371401,
        510701,
        420601,
        330501,
        445201,
        150301,
        371501,
        510801,
        420701,
        330601,
        445301,
        650101,
        150401,
        510901,
        420801,
        429000,
        650201,
        511001,
        330801,
        511101,
        330901,
        421101,
        331001,
        511301,
        421201,
        511501,
        110100,
        659000,
        511601,
        110200,
        610101,
        610201,
        520101,
        610301,
        430101,
        520301,
        430201,
        340101,
        610501,
        430301,
        340201,
        610601,
        430401,
        340301,
        610701,
        430501,
        340401,
        430601,
        340501,
        430701,
        340601,
        430801,
        340701,
        430901,
        340801,
        431001,
        431101,
        341001,
        431201,
        341101,
        210101,
        341201,
        210201,
        120100,
        341301,
        210301,
        120200,
        210401,
        210501,
        620101,
        620201,
        210601,
        530101,
        620301,
        210701,
        440101,
        210801,
        530301,
        620401,
        440201,
        350101,
        210901,
        620501,
        530401,
        440301,
        350201,
        211001,
        440401,
        350301,
        211101,
        440501,
        350401,
        211201,
        440601,
        211301,
        440701,
        350601,
        211401,
        440801,
        350701,
        440901,
        350801,
        310100,
        441201,
        310200,
        220101,
        441301,
        220201,
        130101,
        441401,
        130201,
        441501,
        130301,
        441601,
        220501,
        630101,
        130401,
        441701,
        220601,
        130501,
        540101,
        441801,
        220701,
        130601,
        441901,
        450101,
        450111,
        220801,
        130701,
        442001,
        450201,
        360101,
        450211,
        130801,
        450301,
        360201,
        130901,
        450401,
        360301,
        450411,
        131001,
        450501,
        360401
    ]
    data2 = []
    for i in datas:
        dto = Contact(code=i, name="市辖区")
        data2.append(dto)
    # print(len(data2))
    Contact.objects.bulk_create(data2)
    return HttpResponse("ok")

def test_save(request):

    url2020 = 'http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html'
    url2019 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/2019/202002281436.html'
    url2018 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201903/201903011447.html'
    url2017 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201803/201803131454.html'
    url2016 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201705/201705311652.html'
    url2015 = 'http://www.mca.gov.cn/article/sj/tjbz/a/2015/201706011127.html'
    url2014 = 'https://files2.mca.gov.cn/cws/201502/20150225163817214.html'
    url2013 = 'https://files2.mca.gov.cn/cws/201404/20140404125552372.htm'
    url2012 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271556.html'
    url2011 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271552.html'
    url2010 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220946.html'
    url2009 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220943.html'
    url2008 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220941.html'
    url2007 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220939.html'
    url2006 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220936.html'
    url2005 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220935.html'
    url2004 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220930.html'
    url2003 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220928.html'
    url2002 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220927.html'
    url2001 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220925.html'
    url2000 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220923.html'
    url1999 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220921.html'
    url1998 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220918.html'
    url1997 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220916.html'
    url1996 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220914.html'
    url1995 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220913.html'
    url1994 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220911.html'
    url1993 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041023.html'
    url1992 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220910.html'
    url1991 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041020.html'
    url1990 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041018.html'
    url1989 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041017.html'
    url1988 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220903.html'
    url1987 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180950.html'
    url1986 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220859.html'
    url1985 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220858.html'
    url1984 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220856.html'
    url1983 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708160821.html'
    url1982 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180942.html'
    url1981 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041004.html'
    url1980 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708040959.html'
    # r = requests.get(url2020)
    # html = r.text
    # soup = BeautifulSoup(html, 'html.parser')
    # table = soup.find('table')
    # trs = table.find_all('tr')[2:-9]
    datas = []
    data_list = []
    areas = [
        url2020,
        url2019,
        url2018,
        url2017,
        url2016,
        url2015,
        url2014,
        url2013,
        url2012,
        url2011,
        url2010,
        url2009,
        url2008,
        url2007,
        url2006,
        url2005,
        url2004,
        url2003,
        url2002,
        url2001,
        url2000,
        url1999,
        url1998,
        url1997,
        url1996,
        url1994,
        url1993,
        url1992,
        url1991,
        url1990,
        url1989,
        url1988,
        url1987,
        url1985,
        url1984,


         # 特殊处理
    # if (len(name) == 0 or name == ''):
    #     name = tr.find_next('td').get_text()
            url1995,
            url1986,
            url1983,
            url1982,
            url1981,
            url1980
    ]


    for i in areas:
        try:
            print("处理" + i)
            r = requests.get(i, verify=False)

            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table')
            trs = table.find_all('tr')[2:-9]
            for tr in trs:
                data = []
                if tr.get_text().replace('\n', ''):
                    td = tr.find_all('td')
                    code = tr.find_next('td').find_next('td').get_text()
                    code = code.strip()
                    name = tr.find_next('td').find_next('td').find_next('td').get_text()
                    if(len(name) == 0 or name == ''):
                        name = tr.find_next('td').get_text()
                    name = name.strip()
                    bool(re.search(r'\d', code))
                    dto = None;
                    if(bool(re.search(r'\d', code))):
                        dto = Contact(code=code, name=name)
                    else:
                        dto = Contact(code=name, name=code)
                        # continue
                    # dto = Contact(code=code, name=name)
                    if(dto != None):
                        data_list.append(dto);

                    # if(len(name) ==0 or len(code) == 0):

                    # dto.save()
                    # print(code, re.sub("\s", "", name))
                    # data.append(code)
                    # data.append(re.sub("\s", "", name))  # 正则替换不可见字符
                    # print("处理" + i + "共计" + len(data_list))
                # datas.append(data)
        except Exception as e:
            print(e)
            continue
        Contact.objects.bulk_create(data_list)
        time.sleep(2)
        # df = pd.DataFrame(datas[1:], columns=datas[0])
        # df.to_excel('./data/行政区划代码.xlsx')  # 保存为Excel文件

    # dto = Contact(code='kobe', name='2')
    # dto.save()
    return HttpResponse("添加成功")