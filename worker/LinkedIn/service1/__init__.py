from Extractor import Extractor
from context import Context
import  networkx as nx

 
 

  
schema={'page':['name','localisation','description','abonnee'],'post':["Date_Posted","Media_Type" , "Post_Text" ,"Post_Likes" ,"Post_Comments" , "Media_Links"],'user':["Info","Education","Current Company","About"]}

 
 
ex=Extractor( schema)
 