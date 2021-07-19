import re
import os

readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "README.md")  # noqa: E501
with open(readme_path, mode='r') as file:
    lines = file.readlines()

values = [line.strip() for line in lines if line.startswith('####')]
values = [re.sub(r'^#### \d+\. ', '', value) for value in values]
