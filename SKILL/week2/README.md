Week 2 - Provider Agnostic LLM Client
What I did
In this week I made one common LLM client that can work with both a cloud model and a local model.
I used:
Gemini as the cloud provider
Ollama with `llama3.2` as the local provider
The main idea was that I should be able to choose the provider without changing the main client code.
Files used
`llm\_client.py` - contains the common interface and both providers
`main.py` - asks me to choose Gemini or Ollama and takes the question
`test\_client.py` - tests the common client using a fake provider
`.env` - stores the Gemini API key
`requirements.txt` - required packages
How I ran it
First I installed Ollama and pulled the model:
```bash
ollama pull llama3.2
```
Then I installed the Python requirements and ran:
```bash
python main.py
```
The program asks:
```text
Choose provider (gemini/ollama):
```
After selecting the provider, I enter a question and get the LLM response.
What I learned
I learned how to keep the LLM client independent from the actual provider. Gemini can be used through the API and Ollama can be used locally with the same basic `generate()` idea.
I also understood the use of a common interface and basic testing of the client.
