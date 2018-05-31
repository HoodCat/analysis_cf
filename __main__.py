import urllib
import xml.etree.ElementTree as et
import pandas as pd
import collection
from bs4 import BeautifulSoup
from itertools import count


RESULT_DIRECTORY = '__result__/crawling'


def crawling_pelicana():
    # collection
    results = []
    for page in range(1, 118):
        url = f'http://pelicana.co.kr/store/stroe_search.html?page={page}&branch_name=&gu=&si='

        html = collection.crawling(url)

        soup = BeautifulSoup(html, 'html.parser')
        tag_table = soup.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.find_all('tr')

        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)

            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])

    table['sido'] = table.sido.apply(lambda v: collection.sido_dict.get(v, v))
    table['gungu'] = table.sido.apply(lambda v: collection.gungu_dict.get(v, v))

    # table = table.reset_index(drop=True).set_index('no')
    table.to_csv('{0}/table-pelicana.csv'.format(RESULT_DIRECTORY), encoding='UTF-8', mode='w')


def proc_nene(xml):
    root = et.fromstring(xml)
    items = root.findall('item')
    result = []
    for item in root.findall('item'):
        name = item.findtext('aname1')
        sido = item.findtext('aname2')
        gungu = item.findtext('aname3')
        address = item.findtext('aname4')
        result.append((name, address, sido, gungu))

    return result


def store_nene(data):
    table = pd.DataFrame(data, columns=['name', 'address',
                                        'sido', 'gungu'])

    table['sido'] = table.sido.apply(lambda v: collection.sido_dict.get(v, v))
    table['gungu'] = table.sido.apply(lambda v: collection.gungu_dict.get(v, v))

    # table = table.reset_index(drop=True).set_index('no')
    table.to_csv('{0}/table-nene.csv'.format(RESULT_DIRECTORY), encoding='UTF-8', mode='w')


if __name__ == '__main__':
    # nene collection
    # collection.crawling(
    #     url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s' % (urllib.parse.quote('전체'), urllib.parse.quote('전체')),
    #     proc=proc_nene,
    #     store=store_nene
    # )
    crawling_pelicana()
