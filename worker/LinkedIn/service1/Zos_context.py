import dotenv  
import os





class Zos_Context:
    


    def __init__(self):
        
        dotenv.load_dotenv("linkedin_creds.env")  
       
       
    def  get(self,cred_var):
        
         return os.getenv(cred_var)
    def  set(self,cred_var,new_val):

        os.environ[cred_var]=new_val
        dotenv.set_key("linkedin_creds.env", cred_var, os.environ[cred_var])


       
"""c=Context()
print(c.get("FACEBOOK_TOKEN_FIELDS"))"""