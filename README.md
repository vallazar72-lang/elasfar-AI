# elasfar-AI
This repository contains the training code and data for the elasfar-AI model, a personalized assistant for Ibrahim Al-Asfar's portfolio website.

![MIT License](https://img.shields.io/github/license/Mark-Lasfar/elasfar-AI?color=green)
[![🤗 Hugging Face Model](https://img.shields.io/badge/🤗%20Model-Available-blue)](https://huggingface.co/ibrahimlasfar/elasfar-AI)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Status](https://img.shields.io/badge/status-Experimental-orange)

[![Deploy to Hugging Face](https://img.shields.io/badge/🚀%20Deploy-Hugging%20Face-blueviolet?logo=huggingface)](https://huggingface.co/new?model=ibrahimlasfar/elasfar-AI)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mark-Lasfar/elasfar-AI/blob/main/train.ipynb)
![لقطة شاشة من 2025-07-23 00-49-00.png]([g](https://private-user-images.githubusercontent.com/208757814/469892241-f7eb7718-8238-4e53-8f21-ea893e6951f5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTMyOTU3NzQsIm5iZiI6MTc1MzI5NTQ3NCwicGF0aCI6Ii8yMDg3NTc4MTQvNDY5ODkyMjQxLWY3ZWI3NzE4LTgyMzgtNGU1My04ZjIxLWVhODkzZTY5NTFmNS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzIzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcyM1QxODMxMTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kYjljMTFmZmZhZGI4OTI2MzNkNDllY2VkZmE0MDk2MGI5ZmNmZWI3OTE2MzZlNmEwNWFkNWRmZmMwMGM2Y2EyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.TShnSOaR9LuCo-yCFaRPBjCfY7RYFeWMHahfjo066bo))

![لقطة شاشة من 2025-07-23 00-49-00.png](https://cdn-uploads.huggingface.co/production/uploads/67b8eabdd6935890f93be7b7/9CfhAe8lKTE3X32WF6Wmx.png)
![لقطة شاشة من 2025-07-23 00-49-29.png](https://cdn-uploads.huggingface.co/production/uploads/67b8eabdd6935890f93be7b7/nAH1yn4nTQJkxPThKqft7.png)

## Model Description

The `elasfar-AI` model is a fine-tuned language model based on Hugging Face Transformers. It is designed to:
- Answer questions related to **Ibrahim Al-Asfar's** personal portfolio.
- Provide insights about projects (e.g., **Mark AI**), skills, and professional experience.
- Act as an AI-powered assistant on a personal website.

## Intended Use

- **Primary Use Case**: Interactive Q&A on the portfolio site.
- **Audience**: Potential employers, collaborators, or visitors.
- **Tasks**: Question answering and text generation.

## Setup
1. Install dependencies: `pip install transformers datasets torch huggingface_hub`
2. Train the model: `python train.py`
3. Deploy the backend: `node server.js`

## Training Data

The model is fine-tuned on a custom dataset `training_data.csv` containing question-answer pairs related to:
- Portfolio content
- Projects
- Skills and professional experience

The dataset is handcrafted to ensure relevant and precise answers.

## How to Use (via Hugging Face API)

```python
from huggingface_hub import InferenceClient

client = InferenceClient(token="YOUR_HF_TOKEN")
response = client.text_generation("How the United States was discovered ?", model="ibrahimlasfar/elasfar-AI") 
print(response)
