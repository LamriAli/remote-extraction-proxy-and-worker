import dotenv  
import os





class Zos_Context:
    account=''
    post=False
    keys={}
    limit_posts=0
    limit_friends=0
    limit_comments=0
    group=False
    user=False
    max_pars=0
    
    


    def __init__(self):
        dotenv.load_dotenv("../../../env/facebook_creds.env")        
        """ self.account=account
        self.keys=keys
        self.limit_posts=limit_post
        self.limit_friends=limit_friends
        self.user=user
        self.group=group
        self.max_pars=max_pars
        self.post=post
"""
    def  get(self,cred_var):
         return os.getenv(cred_var)
    def  set(self,cred_var,new_val):

        os.environ[cred_var]=new_val
        dotenv.set_key("../../../env/facebook_creds.env", cred_var, os.environ[cred_var])


       
"""c=Context()
print(c.get("FACEBOOK_TOKEN_FIELDS"))"""