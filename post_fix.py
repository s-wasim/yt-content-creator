from transformers import T5ForConditionalGeneration, T5Tokenizer
from nltk.tokenize import sent_tokenize
import math
import re

def fix_post(post):
    def correct_sent(sent):
        nonlocal model, tokenizer, max_len
        tokenized_sentence = tokenizer('gec: ' + sent, max_length=128, truncation=True, padding='max_length', return_tensors='pt')
        return tokenizer.decode(
            model.generate(
                input_ids = tokenized_sentence.input_ids,
                attention_mask = tokenized_sentence.attention_mask, 
                max_length=max_len,
                num_beams=5,
                early_stopping=True,
            )[0],
            skip_special_tokens=True, 
            clean_up_tokenization_spaces=True
        )
    sentences = sent_tokenize(post)
    max_len = max([len(sent.split(' ')) for sent in sentences])
    max_len = 2 ** math.ceil(math.log2(max_len))
    model = T5ForConditionalGeneration.from_pretrained("Unbabel/gec-t5_small")
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    corrected_sentences = [correct_sent(sent) for sent in sentences]
    return corrected_sentences


if __name__ == '__main__':
    sentence = "I like to swimming"
    print(fix_post(sentence))