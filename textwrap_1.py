import textwrap

sample_text = "This is a sample text that will be wrapped to fit within a specific width."
wrapped_text = textwrap.wrap(sample_text, width=50)

for line in wrapped_text:
    print(line)