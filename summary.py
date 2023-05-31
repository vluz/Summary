from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import sys


if len(sys.argv) < 2:
    print("Please provide the name of file as an argument.")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
summary = model.generate(**tokens, max_new_tokens=128)
output = tokenizer.decode(summary[0])
print(output)
