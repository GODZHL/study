from bs4 import BeautifulSoup

html = """
   <html>
	<head>
		
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
		<meta content="always" name="referrer">
        <meta name="theme-color" content="#2932e1">
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
        <link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">
        <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" /> 
<p>hello world</p>
<h1>
    <a>woshia</a>

</h1>
"""

soup = BeautifulSoup(html,'lxml')

#选择元素
print(soup.link)

#获取标签的名称
print(soup.meta.name)

#获取属性
print(soup.link.attrs['rel'])
print(soup.link['rel'])

#获取内容
print(soup.p.string)

#嵌套选择
print(soup.h1.a.string)

#子节点和子孙节点
print(soup.h1.contents)
for i,child in enumerate(soup.p.children):
    print(i,child)

#父节点和祖先节点
print(soup.p.parent)

for i,parent in enumerate(soup.p.parents):
    print(i,parent)

#兄弟节点
print(list(enumerate(soup.link.next_siblings)))

print(list(enumerate(soup.link.previous_siblings)))

