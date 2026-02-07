
text="""Python is a high-level, interpreted programming language that is widely used for developing applications in various fields such as web development, data science, artificial intelligence, and automation.
It was created by Guido van Rossum and released in 1991.
Python is known for its simple syntax and readability, which makes it easy for beginners to learn and use.
It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python has a large standard library and a strong community, which helps programmers solve problems efficiently.
Because of its flexibility and power, Python is one of the most popular programming languages in the world today."""
f=open(r"Sample_text.txt", "w")
f.write(text)
f.close()

print("Passage was written successfully.")