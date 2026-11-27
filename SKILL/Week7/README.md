# Week 7 – Autoregressive Text Generation

## Aim
To implement a simple autoregressive text generation model using Python by predicting the next word based on previously encountered words.

## Description
This experiment demonstrates how autoregressive text generation works. A training text dataset is tokenized into individual words, and a next-word probability dictionary is created. The model randomly selects the next word from the available possibilities and generates text sequentially.

## Technologies Used
- Python 3
- Random module

## Files
- `autoregression.py` – Python program for autoregressive text generation.
- `README.md` – Documentation of the experiment.

## Algorithm
1. Import the random module.
2. Define the training text.
3. Convert the text into lowercase words using tokenization.
4. Create a dictionary to store possible next words.
5. Build the dictionary by identifying consecutive words.
6. Define a text generation function.
7. Select the starting word.
8. Predict the next word randomly.
9. Continue generating words until the maximum word limit is reached.
10. Display the generated text.

## How to Run

Open the terminal in the Week7 folder and execute:

```bash
python autoregression.py
```

## Expected Output

```text
Generated Text:
the student studied hard ...
```

**Note:** The generated output may vary each time because the program uses `random.choice()`.

## Conclusion
Successfully implemented a simple autoregressive text generation model using Python. The experiment demonstrates sequential next-word prediction and text generation using a basic language model.
