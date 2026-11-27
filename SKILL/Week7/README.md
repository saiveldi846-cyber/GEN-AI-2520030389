Week 7 – Next Token Prediction Using GPT-2
About the Practical
In this practical, I explored how GPT-2 predicts the next token based on the given input text. I used a pretrained GPT-2 model to understand how language models assign probabilities to different possible next tokens.
Requirements
- Python
- PyTorch
- Hugging Face Transformers
- GPT-2 pretrained model
Files Used
- main.py
- requirements.txt
- week7_probability_results.csv
Working Process
First, I installed PyTorch and Transformers using the requirements file.

Then, I loaded the GPT-2 model and tokenizer from Hugging Face. I provided four different input prompts to the model.

The tokenizer converted each prompt into token IDs. GPT-2 processed these tokens and generated logits for predicting the next token.

I applied the Softmax function to convert the logits into probability values. Using Top-K selection, I displayed the five tokens with the highest probabilities for each prompt.

Finally, I stored all the results in a CSV file for further reference.
Execution Steps
Activate the virtual environment:
..\.myenv\Scripts\Activate.ps1
Install the required packages:
python -m pip install -r requirements.txt
Run the Python program:
python main.py
Results
The program successfully processed four input prompts:
- The cat is
- Artificial intelligence is
- India is a
- Machine learning helps
For every prompt, it displayed five predicted next tokens along with their token IDs and probability values.

The results were saved in week7_probability_results.csv.
Learning Outcome
By completing this practical, I understood how GPT-2 performs next-token prediction. I learned about token IDs, logits, Softmax, probability distribution, and Top-K selection.

I also understood how pretrained language models can predict possible next tokens based on the given input text.
