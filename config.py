#Used to try the environment variables 
from dotenv import load_dotenv
import os

load_dotenv()

u=os.environ["MYSQL_USER"]
pwd=os.environ["MYSQL_PASSWORD"]
host=os.environ["MYSQL_HOST"]
data=os.environ["MYSQL_DATABASE"]



DATABASE_CONECTION_URI=f"mysql://{u}:{pwd}@{host}/{data}"



#That was to check the string i was sending to the conection
#print(DATABASE_CONECTION_URI)