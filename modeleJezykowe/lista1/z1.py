import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("eryk-mazus/polka-1.1b")
model = AutoModelForCausalLM.from_pretrained("eryk-mazus/polka-1.1b", device_map="auto")

dialog_start = "Stefan i Anna spotkali się w miłej i przytulnej kawiarni."
dialog = []


def generate_answer():
    return False


while True:
    dialog_user = input("Stefan: ")
    if not dialog_user.strip():
        continue
    dialog_bot = generate_answer(dialog_user)
    print(f"Anna: {dialog_bot}")
