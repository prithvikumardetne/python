import textwrap


sample_text = "ABCDEFGHIJKLLMNOPQRSTUVWXYZ"

wrapped_text = textwrap.wrap(sample_text, width=4)

#print(wrapped_text)

for i in wrapped_text:
    print(i)