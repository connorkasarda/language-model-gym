# Language Model Gym 💪

Serves as a factory and training center for Large Language Models (LLM).

## Workflow ⚙️

This section lays out the order of operations involved in generating LLMs. Each operation is represented by a module or folder found in the root level directory.

1. [**Parsing**](./parsing/) -- operates on the corpus dataset and retrieving text as strings
2. [**Tokenization**](./tokenization/) -- convert text into tokens and building vocabularies
3. [**Alignment**](./alignment/) -- prepare input-target pairs from tokenized text to aid language model predictions
4. [**Embedding**](./embedding/) -- transforms token IDs into vectors that capture semantic and positional reasoning
5. *more to come...*

## Development 💻

This code is **unit-test-driven** and **experimentally evaluated**. Tests are written alongside the code, with algorithms being fine-tuned and assessed through scientific methods to identify the most effective approaches. Please refer to the [**Tests**](./tests/) and [**Science**](./science/) modules.

## References 📃

For a full list of references, algorithms, and approaches implemented in this repository, please refer to the [**BibTeX**](./references.bib) file.

## Warning ⚠️

Use at your own risk. The author is not responsible for any damages or losses incurred from using this code. See [**License**](#License) section.

## License 📜

This project is licensed under the [MIT License](LICENSE) © 2025 connorkasarda.