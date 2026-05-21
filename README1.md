# Negotiation Arena: Human and LLM Negotiation Dynamics

This project investigates language generation, strategic alignment, and agentic behavior in Large Language Models (LLMs) within structured multi-issue negotiation environments. 

The work builds a comparative framework benchmarking autonomous multi-agent pipelines against human negotiation baselines derived from the annotated **Negochat corpus**.

## Technical Implementation and Reproducibility

This project combines an offline analysis pipeline with several LLM generation loops executed on Google Colab. The final analysis is completely reproducible from the pre-generated CSV logs stored in the `results/` directory, removing any mandatory runtime dependence on external LLM hardware simulation.

### Model Deployment Setup

Different Llama-family and lightweight language models were deployed depending on the specific architectural constraints of each experimental pipeline:

* **Llama3 (Ollama)**: Utilized for the controlled evaluation sensitivity experiments. This setup allowed for strict instruction-following capabilities during iterative multi-turn text generation.
* **Llama3.2 3B (Ollama)**: Deployed for the computationally heavy multi-issue utility experiment. Agents had to negotiate complete 6-dimensional contract packages, dynamically evaluating options through private constraints.
* **TinyLlama (Hugging Face Transformers)**: Deployed for the human-seeded continuation experiment. Its lightweight footprint allowed for efficient execution of 20 distinct dialogue trajectory context injections within Google Colab runtimes.

### Repository Results Directory

The core analytical pipeline automatically references the following stored dataset and execution logs in the `results/` folder:

```text
results/
├── controlled_llama3_explicit_turns.csv
├── controlled_llama3_explicit_outcomes.csv
├── controlled_llama3_compatibility_turns.csv
├── controlled_llama3_compatibility_outcomes.csv
├── human_seeded_llm_turns_sample.csv
├── human_seeded_llm_outcomes_sample.csv
├── utility_llm_turns_llama3.csv
├── utility_llm_outcomes_llama3.csv
├── long_single_llama3_test_turns.csv
└── long_single_llama3_test_outcome.csv
```
## Research Question
How do LLM agents behave in negotiation settings compared with human negotiators, and how sensitive are their outcomes to prompting, utility constraints, and environmental termination rules?

## Project Architecture
data/raw/: Original raw Negochat dialogue dataset files.

data/processed/: Parsed and structured human baseline dialogue acts dataframes.

notebooks/: Exploratory data analysis, simulation run scripts, and the core comparative evaluation notebook (negotiation_arena_final_analysis.ipynb).

src/: Reusable modular Python scripts hosting loading utilities (data_loader.py), metric scoring functions (metrics.py), and rendering palettes (visualization.py).

results/: Output runtime execution CSV logs, comparison matrices, and transition heatmaps.

## Experimental Framework
The evaluation environment isolates agent dynamics across three progressive testing layers:

Human-Seeded Continuity: Injecting the first substantive human act from Negochat into an LLM agent loop to evaluate subsequent trajectory and dialogue-act profile preservation.

Evaluation Sensitivity (Ablation): Testing how modifying environmental termination parameters (Explicit Acceptance Tokens vs. Constraint Compatibility Observation) alters the observed agreement rates under identical starting conditions.

Utility-Based Optimization: Testing structural multi-issue convergence against private, asymmetric utility tables to evaluate whether conversational alignment matches true game-theoretic self-interest.

## Analytical Metrics
Pragmatic Alignment: Tracking the proportional distribution and state transition matrices of dialogue acts (Offers, Rejects, Queries).

Strategic Validity: Measuring final convergence against multi-tier mathematical payoff thresholds (uncovering the AcceptedLowUtility behavior gap).

Trajectory Tracking: Monitoring structural convergence velocities, turn counts, and timeout frequencies.

## Reproducibility Workflow
Install the environment dependencies:
pip install -r requirements.txt
To reproduce the analysis tables, background gradients, and data distribution figures without re-executing the heavy LLM generations, simply run the main Jupyter analysis notebook: notebooks/negotiation_arena_final_analysis.ipynb.
