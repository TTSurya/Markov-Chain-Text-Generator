# Markov Chain Text Generator

This project provides a simple and transparent implementation of a Markov chain text generator. It is designed to be easy to understand, modify, and extend, making it suitable for experimentation with probabilistic sequence behavior.

## Overview

The system generates text by learning transition patterns from an input sequence. It models how tokens follow one another, calculates transition probabilities, and then produces new sequences by sampling from these learned patterns. The structure is intentionally clear to help readers examine and interpret the resulting transitions.

## Features

* Customizable state size for context-based transitions.
* Configurable transition biases for controlled sequence behavior.
* Clean state-transition table output for straightforward inspection.
* Simple text generation pipeline that is easy to integrate or expand.

## Sample run
* `txtgen.py` generates a sample input text using a 5-ary alphabet with a predefined transition matrix.
* The resulting transition table produced by `main.py` can be compared with the original matrix to verify correctness.

## Usage

1. Generate the input text using:

   ```bash
   python txtgen.py > ip.txt
   ```
2. Run the main generator:

   ```bash
   python main.py
   ```

## Files

* `txtgen.py`: Produces the source text based on a probabilistic generation scheme.
* `main.py`: Builds the Markov chain, prints transition tables, and generates sample output.
* `ip.txt`: Automatically generated input text used by the Markov model.
