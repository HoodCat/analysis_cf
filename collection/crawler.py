import sys
from datetime import datetime
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def crawling(url='', encoding='utf-8',
             proc=lambda html: html, # 파싱해주는 함수
             store=lambda data: data, # 데이터를 저장해주는 함수
             error=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request, timeout=300)

        try:
            receive = resp.read()
            result = receive.decode(encoding)
        except UnicodeDecodeError:
            # encoding error가 발생했을 때 알아서
            # 파이썬에서 맞는 문자열을 찾아서 넣어줌
            result = receive.decode(encoding, 'replace')

        print('%s: success for request [%s]' % (datetime.now(), url))
        return store(proc(result))
    except Exception as e:
        error(e)
