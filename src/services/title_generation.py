"""
This file is used to generate title from the input paragraph
"""
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import logging


try:
    tokenizer = AutoTokenizer.from_pretrained("src/resources/title_token")
    model = AutoModelForSeq2SeqLM.from_pretrained("src/resources/title_model")
    logging.warning("title model loaded")
except Exception as e:
    tokenizer = AutoTokenizer.from_pretrained("deep-learning-analytics/automatic-title-generation")
    tokenizer.save_pretrained('src/resources/title_token')
    model = AutoModelForSeq2SeqLM.from_pretrained("deep-learning-analytics/automatic-title-generation")
    model.save_pretrained('src/resources/title_model')
    logging.warning("title model downloaded and loaded")


def tokenize_data(text):
    # Tokenize the review body
    input_ = str(text) + ' </s>'
    max_len = 120
    # tokenize inputs
    tokenized_inputs = tokenizer(input_, padding='max_length', truncation=True, max_length=max_len,
                                 return_attention_mask=True, return_tensors='pt')

    inputs = {"input_ids": tokenized_inputs['input_ids'], "attention_mask": tokenized_inputs['attention_mask']}
    return inputs


def generate_answers(text):
    global model, tokenizer
    # torch.set_num_threads(20)
    # Below command is used to fix the random torch tensors created.
    torch.manual_seed(2809)
    inputs = tokenize_data(text)
    results = model.generate(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'], do_sample=True,
                             max_length=20,
                             top_k=10,
                             top_p=0.98,
                             early_stopping=True,
                             num_return_sequences=5)
    answer = tokenizer.decode(results[0], skip_special_tokens=True)
    return answer
