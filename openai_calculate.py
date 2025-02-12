import openai  
from decouple import config
# Set your API key  
openai.api_key = config("api_key")  

# Retrieve usage data  
usage = openai.Usage.retrieve()  

# Print usage details  
print(usage)