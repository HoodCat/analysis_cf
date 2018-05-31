# Beautifulsoup4 test
from bs4 import BeautifulSoup


html = '<td class="title"> ' \
            '<div class="tit3">' \
                '<a href="/movie/bi/mi/basic.nhn?code=158178" title="독전">독전</a>' \
            '</div>' \
       '</td>'

# 1. 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs), sep='|')

    tag = bs.td # 태그의 이름으로 조회하는 방법
    print(tag, type(tag), sep='|')

    tag = bs.a
    print(tag, type(tag), sep='|')


# 2. Attribute 값
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class']) # 태그속성 조회

    tag = bs.div
    print(tag.attrs) # 태그속성 전체조회


# 3. Attribute 조회
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'title'})
    print(tag)

    tag = bs.find(attrs={'title': '독전'})
    print(tag.string)


if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()
