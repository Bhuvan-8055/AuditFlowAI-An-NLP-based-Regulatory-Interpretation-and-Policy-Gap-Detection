import re

input_path = "data/cleaned_text/RBI_IT_Outsourcing_2023_full.txt"
output_path = "data/cleaned_text/RBI_IT_Outsourcing_2023_cleaned.txt"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r"\s+", " ", text)
text = text.replace("\u00a0", " ")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text.strip())

print("Cleaned text file created successfully")
