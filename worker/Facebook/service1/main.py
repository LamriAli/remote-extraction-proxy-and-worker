from http import cookies
from Extractor import Extractor
from context import Context
import  networkx as nx
 
from facebook_scraper import get_posts,get_friends,get_profile,get_group_info



 











#cxt=Context(account,creds,limit_post,limit_friends,max,post,False,True)
#print(get_profile("100009975842374"))
#print(get_group_info("journalmaracanaalgerie") )
Schema={'user':['id','Name','Friend_count','Follower_count','About'],'post':['post_id','post_text','comments','user_id','reaction_count','page_id','fetched_time']}

ex =Extractor(Schema)
 