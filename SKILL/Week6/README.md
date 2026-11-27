# Week 6 – LLM Baseline Evaluation

## Aim
To evaluate the performance of the Llama 3.2 language model using a predefined set of questions, expected answers, and keyword-based scoring.

## Description
This experiment implements an LLM baseline evaluation system using Ollama and Llama 3.2. It contains a golden question set of 30 questions related to Generative AI concepts. The model generates answers, which are compared with expected keywords to calculate evaluation scores.

## Technologies Used
- Python 3
- Ollama
- Llama 3.2
- Requests
- JSON
- CSV

## Project Files
- `main.py` – Main Python program for baseline evaluation.
- `golden_set.json` – Contains 30 questions, expected answers, keywords, and sources.
- `requirements.txt` – Contains required Python packages.
- `baseline_results.csv` – Automatically generated evaluation results.
- `README.md` – Project documentation.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

## How to Run

Execute the following command:

```bash
python main.py
```

## Working Process
1. Load the golden question set from JSON.
2. Connect to the locally running Ollama API.
3. Send questions to the Llama 3.2 model.
4. Receive generated answers.
5. Compare answers with expected keywords.
6. Calculate keyword coverage percentage.
7. Assign PASS, REVIEW, or ERROR status.
8. Save evaluation results into a CSV file.
9. Display the baseline evaluation summary.

## Evaluation Criteria

- PASS: Keyword coverage is 60% or above.
- REVIEW: Keyword coverage is below 60%.
- ERROR: Model request or processing failed.

## Output
The program automatically generates `baseline_results.csv`, containing:
- Question ID
- Question
- Expected Answer
- LLM Answer
- Matched Keywords
- Missing Keywords
- Score
- Status
- Source
- Model
- Release Version

## Release Information
- Model: Llama 3.2
- Release Version: v0.1
- Total Questions: 30

## Conclusion
Successfully implemented an LLM baseline evaluation system using Llama 3.2. The experiment evaluates model responses through keyword-based scoring and generates a CSV report to analyze performance.
