# Negotiation Arena: Human and LLM Negotiation Dynamics

This project investigates negotiation behavior in multi-agent LLM systems.

The work is based on Project 3: The Negotiation Arena. The goal is to study how different agent objectives and negotiation styles affect agreement rates, negotiation length, and communicative strategies.

## Research Question

How do cooperative, competitive, and mixed negotiation styles influence the outcomes and dynamics of LLM-based multi-agent negotiations?

## Project Structure

- `data/raw/`: original Negochat dataset
- `data/processed/`: processed human negotiation baseline
- `data/scenarios/`: synthetic negotiation scenarios and experimental conditions
- `notebooks/`: exploratory analysis, simulations, and final comparison
- `src/`: reusable Python modules
- `results/`: generated CSV files, plots, and tables

## Dataset

The human baseline is based on the Negochat corpus, a set of human-agent job negotiation dialogues annotated with dialogue acts such as Offer, Accept, Reject, Query, Greet, and Quit.

## LLM Simulation

LLM negotiations were simulated using TinyLlama/TinyLlama-1.1B-Chat-v1.0 on Google Colab with GPU acceleration.

Each simulation involved two agents:

- Candidate
- Employer

The agents negotiated salary and working hours under three experimental conditions:

- cooperative
- competitive
- mixed

## Metrics

The project evaluates:

- agreement rate
- negotiation length
- timeout rate
- salary offers
- working hours offers
- human vs LLM negotiation differences
- qualitative negotiation patterns

## Reproducibility

Install requirements:

```bash
pip install -r requirements.txt