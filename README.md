#  Text Generation & Sentiment Analysis

An AI-powered web application built with Python and Streamlit that performs **Sentiment Analysis** and **Text Generation** using Hugging Face Transformer models.

## Project Overview

This project combines two Natural Language Processing (NLP) tasks in a single application:

-  Sentiment Analysis
- Text Generation

The user can enter any text into the application. The system analyzes whether the text is **Positive** or **Negative** and also generates additional text based on the given input.

##  Features

- AI-powered text processing
-  Positive/Negative sentiment detection
-  Sentiment confidence score
-  Automatic text generation
-  Interactive Streamlit interface
-  Hugging Face Transformer models
-  Built using Python

##  Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Torchvision

##  Models Used

### Sentiment Analysis

The project uses:

`distilbert/distilbert-base-uncased-finetuned-sst-2-english`

This model is used to classify the input text as positive or negative.

### Text Generation

The project uses:

`distilgpt2`

This model generates text based on the user's input.

##  Project Structure

```text
TextGenerationSentiment/
│
├── app.py
├── requirements.txt
├── README.md
└── venv/
                 TEXT GENERATION & SENTIMENT ANALYSIS
                              │
                              ▼
                    ┌───────────────────┐
                    │    User Input   │
                    │  Enter your text   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     Streamlit   │
                    │    Web Interface  │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
          ┌─────────────────┐   ┌─────────────────┐
          │  Sentiment    │   │     Text         │
          │    Analysis     │   │    Generation   │
          └────────┬────────┘   └────────┬────────┘
                   │                     │
                   ▼                     ▼
          ┌─────────────────┐   ┌─────────────────┐
          │   DistilBERT    │   │    DistilGPT2   │
          │ Transformer     │   │ Transformer     │
          └────────┬────────┘   └────────┬────────┘
                   │                     │
                   ▼                     ▼
          ┌─────────────────┐   ┌─────────────────┐
          │ Sentiment +     │   │ Generated Text  │
          │ Confidence      │   │                 │
          └────────┬────────┘   └────────┬────────┘
                   │                     │
                   └──────────┬──────────┘
                              ▼
                    ┌───────────────────┐
                    │    Final Output │
                    │  Displayed in UI  │
                    └───────────────────┘
