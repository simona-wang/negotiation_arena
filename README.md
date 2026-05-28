# Negotiation Arena: Human and LLM Negotiation Dynamics

This project investigates negotiation behavior in multi-agent LLM systems.

The work is based on Project 3: The Negotiation Arena. The goal is to study how different agent objectives and negotiation styles affect agreement rates, negotiation length, and communicative strategies.

## Technical Implementation and Reproducibility

This project combines a local analysis pipeline with several LLM generation notebooks executed on Google Colab. The final analysis is designed to be reproducible from the stored CSV files in the `results/` directory, without requiring the user to rerun the LLM simulations.

* **Utility-Based Framework**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/simona-wang/negotiation_arena/blob/main/colab_experiments/utility_based_multiissue_llama32_colab.ipynb)
* **Compatibility Experiments**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/simona-wang/negotiation_arena/blob/main/colab_experiments/controlled_llama3_compatibility_colab_1.ipynb)
* **Explicit Acceptance Experiments**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/simona-wang/negotiation_arena/blob/main/colab_experiments/controlled_llama3_explicit_colab_1.ipynb)
* **Human-Seeded Continuation**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/simona-wang/negotiation_arena/blob/main/colab_experiments/human_seeded_tinyllama_continuation_colab.ipynb)


### Why Google Colab Was Used

Google Colab was leveraged to bypass local hardware limitations during the intensive LLM generation phase. The experiments required repetitive, multi-turn model inference loops across several scenarios, prompting conditions, and runs, making local execution computationally unfeasible.

Colab was restricted exclusively to the **generation pipeline**:
* Defining the negotiation parameters and scenarios.
* Executing the active LLM agent dialogue loops.
* Extracting conversation turns and structural decisions.
* Saving and exporting the final execution tracks as CSV logs.

The main analysis notebook operates entirely offline, loading these pre-generated CSV files directly from the `results/` directory to ensure fast, predictable local reproducibility.
### Model Choices

Different language models were deployed depending on the computational and architectural requirements of each experimental pipeline:

* **Llama3 (Ollama)**: Deployed for the controlled negotiation experiments (*Explicit Acceptance* vs. *Compatibility*). It was selected for its superior instruction-following abilities and text stability across iterative, multi-turn interactions.
* **Llama3.2 3B (Ollama)**: Deployed for the utility-based multi-issue experiment. It provided a practical compromise between generation quality and runtime speed on Google Colab, successfully managing the workload of negotiating complete 6-issue contract packages evaluated against private utility tables.
* **TinyLlama (Hugging Face)**: Used for the human-seeded continuation experiment. Its lightweight architecture allowed for the efficient simulation of multiple dialogue continuations starting directly from real Negochat conversational contexts without hitting hardware constraints.

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
