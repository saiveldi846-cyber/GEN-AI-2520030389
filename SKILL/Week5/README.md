# Week 5 - Token Economics

## What I did

In this week I made a small budget planner for an LLM feature.

The program estimates:
- input tokens per day
- output tokens per day
- total tokens per day
- daily cost
- monthly cost
- peak RPM
- peak TPM

It also checks the values against the configured limits and gives a recommendation.

## Files used

- `.env`
- `budget.py`
- `test_budget.py`
- `requirements.txt`

## How I ran it

I installed `python-dotenv` and added the planning values in `.env`.

Then I ran:

```bash
python budget.py
```

I also used `test_budget.py` to test the cost calculations and the budget/rate-limit checks without making an actual LLM API call.

## Example result

With the sample values given in the lab, the planner estimates:

- Input tokens/day: 2,400,000
- Output tokens/day: 600,000
- Total tokens/day: 3,000,000
- Daily estimated cost: $1.44
- 30-day estimated cost: $43.20
- Peak RPM with margin: 36
- Peak total TPM with margin: 54,000

The sample is within the configured planning limits.

## What I learned

I learned that before building an LLM feature, it is useful to estimate token usage and cost first.

I also learned the difference between RPM and TPM and why a safety margin is useful when planning the usage of an LLM.
