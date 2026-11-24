
import os
from dotenv import load_dotenv

from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

# Load environment variables from .env
load_dotenv(override=True)

print("===================================")
print("       PROVIDER AGNOSTIC LLM")
print("===================================")

# Select AI provider
provider_name = input(
    "\nChoose provider (gemini/ollama): "
).strip().lower()

# Initialize selected provider
if provider_name == "gemini":

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Gemini API key not found in .env file!"
        )

    provider = GeminiProvider(api_key)

elif provider_name == "ollama":

    provider = OllamaProvider("llama3.2")

else:
    raise ValueError(
        "Invalid provider! Choose gemini or ollama."
    )

# Create common LLM client
client = LLMClient(provider)

# Get user prompt
prompt = input("\nEnter your question: ").strip()

if not prompt:
    print("Please enter a valid question.")

else:
    try:
        print("\nGenerating response...")

        answer = client.generate(prompt)

        print("\n========== LLM Response ==========")
        print(answer)
        print("==================================")

    except Exception as e:

        print("\n========== AI Provider Error ==========")
        print(e)
        print("\nPlease try again later.")
        print("=======================================")
