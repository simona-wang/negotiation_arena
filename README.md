# Negotiation Arena: Human and LLM Negotiation Dynamics

This project investigates negotiation behavior in multi-agent LLM systems.

The work is based on Project 3: The Negotiation Arena. The goal is to study how different agent objectives and negotiation styles affect agreement rates, negotiation length, and communicative strategies.

## Technical Implementation and Reproducibility

This project combines a local analysis pipeline with several LLM generation notebooks executed on Google Colab. The final analysis is designed to be reproducible from the stored CSV files in the `results/` directory, without requiring the user to rerun the LLM simulations.

### Why Google Colab was used

The LLM simulations were run on Google Colab because local hardware was not sufficient to run all model generations efficiently. Some experiments required repeated LLM calls across several scenarios, negotiation conditions, and runs. Running these experiments locally would have been slow and unreliable, while Colab provided a more practical environment for executing model-based simulations.

Colab was used mainly for the generation phase:

1. loading or defining the negotiation setup;
2. running the selected LLM model;
3. generating turns and outcomes;
4. saving the generated outputs as CSV files.

The final analysis notebook does not regenerate the LLM outputs. Instead, it loads the generated CSV files from `results/` and performs the analysis from there.

### Model choices

Different Llama-family models were used depending on the computational requirements of each experiment.

#### Llama3 with Ollama

The controlled negotiation experiments were run with `llama3` through Ollama. This setup was used for the explicit-acceptance and compatibility-based evaluation experiments because Llama3 provided better instruction-following ability and more stable negotiation text than smaller models.

The controlled experiments investigate how the same negotiation setting changes depending on the rule used to define agreement:

- **Explicit acceptance only**: a run is classified as `Agreement` only if the model explicitly produces an acceptance decision.
- **Compatibility-based evaluator**: a run is classified as `Agreement` if the environment detects an offer compatible with both agents’ constraints.

These experiments were used to show that LLM negotiation outcomes are highly sensitive to the evaluation rule.

#### Llama3.2 3B with Ollama

The utility-based multi-issue experiment was run with `llama3.2:3b` through Ollama. This model was chosen because the full utility-based experiment was computationally heavier: agents had to negotiate complete contract packages across multiple issues, and each proposed package had to be parsed and evaluated through private utility tables.

A larger Llama3 model was tested, but generation time was too high for the available Colab runtime. Therefore, `llama3.2:3b` was used as a practical compromise between model quality and runtime feasibility.

The utility-based experiment evaluates whether explicit acceptance corresponds to a mutually beneficial agreement. It uses the following contract issues:

- job description;
- salary;
- working hours;
- pension fund;
- leased car;
- promotion possibilities.

Each proposed package is scored using candidate and employer utility tables.

#### TinyLlama for the human-seeded experiment

The human-seeded continuation experiment was run with TinyLlama through Hugging Face Transformers. This was used because the experiment required many dialogue continuations starting from real Negochat contexts, and TinyLlama was lightweight enough to run efficiently in Colab.

The purpose of this experiment is not to compare model quality directly with Llama3. Instead, it tests whether a small LLM can continue a real negotiation trajectory from a Negochat dialogue act. The experiment is therefore used mainly for dialogue continuation, outcome-level comparison, and dialogue-act behavior.

### Stored result files

The final analysis uses saved CSV files produced by the Colab notebooks. These files are stored in the `results/` directory. They allow the final notebook to be reproduced without rerunning the LLM generations.

The expected result files are:

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

How do LLM agents behave in negotiation settings compared with human negotiators, and how sensitive are their outcomes to prompting, utility constraints, and termination rules?

## Project Structure

- `data/raw/`: original Negochat dataset
- `data/processed/`: processed human negotiation baseline (dialogue acts and issues dataframes)
- `notebooks/`: exploratory data analysis, LLM agent simulation loops, and final cross-experiment comparison
- `src/`: reusable Python modules for parsing, evaluation, and plotting
- `results/`: generated CSV files, figures, and distribution plots

## Dataset

The human baseline is based on the **Negochat corpus**, a set of human-agent job negotiation dialogues collected via a Wizard-of-Oz methodology. The dataset is structured into 4,993 processed rows annotated with dialogue acts (*Offer*, *Accept*, *Reject*, *Query*, *Greet*, *Quit*) and contract dimensions (*Job description*, *Salary*, *Working hours*, *Pension fund*, *Leased car*, *Promotion possibilities*).

## LLM Simulation Framework

Instead of simple static prompts, negotiations were simulated within an interactive multi-agent arena involving a **Candidate** and an **Employer** agent. The framework covers three distinct experimental pipelines:

1. **Human-Seeded Continuation**: TinyLlama is initialized with the first substantive human act from Negochat to evaluate trajectory and dialogue-act preservation.
2. **Evaluation Sensitivity (Ablation)**: Llama3 tests how changing environmental termination rules (*Explicit Acceptance* vs. *Constraint Compatibility*) shifts outcomes using identical starting parameters.
3. **Utility-Based Negotiation**: Llama3.2 (3B) negotiates a full 6-issue contract package. Decisions are validated against private, asymmetric utility tables to test strategic alignment.

## Reproducibility

Install requirements:

```bash
pip install -r requirements.txt
