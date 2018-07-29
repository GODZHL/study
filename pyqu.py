from pyquery import PyQuery as pq

html ="""
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
#字符串初始化
doc = pq(html)

#格式化
print(doc('li'))

#URL初始化
doc1 = pq(url='http://www.baidu.com')
print(doc1('head'))

#文件初始化
doc2 = pq(filename='~/文档/testdata/test.html')
print(doc2('li'))

#css选择器
print(doc(#list-1))

#查找元素
items = doc('.list')
lis = items.find('li')
print(lis)

#DOM操作
#removeClass(classname)
#addClass(classname)

