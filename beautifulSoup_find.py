from bs4 import BeautifulSoup

html = """
    <div class="panel">
    <div class="panel-heading">
        <h4><hello/h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""

soup = BeautifulSoup(html,'lxml')

#标准选择器
print(soup.find_all('ul'))
print(soup.find_all('ul')[0])

#通过属性去查找标签
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(class_='element'))

#利用TEXT进行选择
print(soup.find_all(text='F00'))

#find方法和find_all的用法一样
print(soup.find('ul'))

#css选择器
print(soup.select('ul li'))


