# sql-data-agent

> Ask your database questions in Spanish and get the answer, a chart and the "why" — without the agent ever being able to modify or leak data.

🚧 **Work in progress.** Target for the MVP: February 2027.

## What it will do

```
"¿Qué categoría vendió más en 2018?"
        │
        ▼
   LLM agent ──► writes SQL ──► read-only Postgres ──► result
        ▲              │
        └── fixes the query if it fails
        │
        ▼
 answer + chart + explanation (or "I don't have data for that")
```

- **Text-to-SQL agent** over a real e-commerce dataset ([Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce): 9 tables, ~100k orders).
- **Measured, not guessed:** an evaluation set of 50 questions with known answers, scored by *execution accuracy* (does the query return the right result?).
- **Safe by design:** read-only database user and a SQL validator that only allows `SELECT`.
- **Multi-business:** reads the schema plus a per-business "context sheet", so it can work on other databases.

## Roadmap

| Milestone | Status |
|---|---|
| M1 · Foundations: repo, Postgres in Docker, data loaded, API without AI | 🔨 in progress |
| M2 · The LLM writes SQL (structured output) | ⏳ |
| M3 · Evaluation harness (50 questions) and baseline | ⏳ |
| M4 · Agent with tools, self-correction and SQL validator → **MVP** | ⏳ |
| M5–M10 · Context sheet, RAG over reviews, tracing, multi-business, MCP, CI and deployment | ⏳ |

## Tech stack

Python 3.13 · [uv](https://docs.astral.sh/uv/) · pytest · PostgreSQL · Docker · FastAPI · LLM API · MCP

## Run the tests

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
git clone https://github.com/uzzitop/sql-data-agent.git
cd sql-data-agent
uv run pytest
```

## License

MIT
