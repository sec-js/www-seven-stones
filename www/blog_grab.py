import pymysql
import re
import os
from dotenv import load_dotenv
from sevenstones.settings import BASE_DIR

def blog_text_grab():

    load_dotenv((os.path.join(BASE_DIR, '.env')))
    p = os.getenv("pDB")
    con = pymysql.connect(host=os.getenv("dbHOST"),
                          user='root',
                          password=os.getenv(("pDB")),
                          database='wordpress')

    with con:
        cur = con.cursor()
        cur.execute("SELECT post_content, post_date, post_title FROM `wp_posts` WHERE post_status = 'publish' ORDER BY id DESC LIMIT 1")

        x = cur.fetchone()
        y = re.findall('<p>..*</p>', x[0])

        blog_post_dict = {'excerpt': ''.join(y[0:3]), 'post_date': x[1], 'title': x[2]}

        return blog_post_dict
