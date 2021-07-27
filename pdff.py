# import img2pdf
# from PyPDF2 import PdfFileMerger
#
#
# merger = PdfFileMerger()
#
#
# for i in range(1,136):
#     with open(f"1_1/{str(i)}.pdf","wb") as f:
#
#
#         print(i)
#         f.write(img2pdf.convert(f'1/{str(i)}.jpg'))
#         merger.append(f"1_1/{str(i)}.pdf")
# merger.write("9kitab.pdf")
# merger.close()




#*******************************************************************************************************************************************************




import requests
import re
import queue
from threading import Thread as th



find_last_page = r'var last_page_params=".*=(.*?)"'
find_img_src = r'<img class="panzoom-element-box" src="(.*?)"'

s = requests.Session()
r = requests.get('http://web2.anl.az:81/read/page.php?bibid=281226&pno=1')

# print(r.text)

res_last_page = int(re.findall(find_last_page,r.text)[0])+1
res_img_src = re.findall(find_img_src,r.text)[0][:-1]
print(res_last_page)
print(res_img_src)

q = queue.Queue()

for i in range(1,res_last_page):
	q.put(i)



def boto():
	while q.empty:
		var = q.get()
		print(var)

		star(var)

def star(var):
		try:
			s = requests.Session()
			r = s.get('http://web2.anl.az:81/read/page.php?bibid=281226&pno='+str(var))
			r = s.get('http://web2.anl.az:81/read/' + res_img_src + str(var), timeout=6)
			with open('1/' + str(var) + '.jpg', 'wb')as f:
				f.write(r.content)
		except Exception as e:
			star(var)
			print('-----------------' + str(var))






for i in range(10):
	th(target=boto).start()


