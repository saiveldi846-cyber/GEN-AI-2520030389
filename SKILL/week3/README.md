Week 3 - LLM Monitoring with MongoDB
What I did
In this week I extended the Week 2 LLM client and added monitoring.
The program records information about LLM requests such as:
input and output token usage
response latency
estimated cost
success or failure
The usage information is stored in MongoDB.
I also added timeouts and limited retries so that temporary errors do not immediately stop the program.
Files used
`main.py`
`llm_client.py`
`usage_logger.py`
`test_client.py`
`requirements.txt`
`.env`
MongoDB setup
I created a MongoDB Atlas cluster and used its connection string in the `.env` file. The Gemini API key is also stored in `.env`.
The `.env` file is not uploaded to GitHub because it contains private connection details.
How I ran it
I installed the required packages:
```bash
pip install google-genai requests python-dotenv pymongo
```
Then I ran the main program and tested the client.
The monitoring part stores the request information in the `llm_monitoring` database and the `api_usage` collection.
What I learned
This week I learned the basic idea of LLM observability. Instead of only getting an answer from the model, I can also see how long the request took, how many tokens were used and the estimated cost.
I also learned how MongoDB can be used to store the usage details and how retries and timeouts can make the program more reliable.
