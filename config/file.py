from deta import Deta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

drive =  Deta().Drive('__drive__')