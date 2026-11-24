# Week 4 - Tokenizer Lab

## What I did

In this week I compared three different tokenization approaches:

- BPE using GPT-2
- WordPiece using multilingual BERT
- SentencePiece using XLM-R

I used English, Telugu and Hindi text and checked how each tokenizer splits the text.

The program prints:
- tokens
- token IDs
- token count

## Files used

- `tokenizer_comparison.py`
- `requirements.txt`

## Libraries used

```text
transformers
sentencepiece
```

## How I ran it

After activating my virtual environment, I installed the requirements and ran:

```bash
python tokenizer_comparison.py
```

The tokenizer files are downloaded on the first run.

## What I learned

I learned that the same sentence can produce different tokens depending on the tokenizer and its vocabulary.

I also noticed that English, Telugu and Hindi can have different token counts. This is because the tokenizers and their training data/vocabularies are different.

The main thing I understood from this experiment is that tokenization happens before the text is processed by the language model.
