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
"""

soup = BeautifulSoup(html,'lxml')

#自动格式化html代码
print(soup.prettify)


