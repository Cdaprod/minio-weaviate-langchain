import re

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def update_readme(directory_tree, readme_contents):
    # Pattern to match the section to replace
    # Adjust the pattern to match the section's markers in your README
    pattern = re.compile(r'<!-- DIRECTORY_TREE_START -->(.*?)<!-- DIRECTORY_TREE_END -->', re.DOTALL)
    replacement = f'<!-- DIRECTORY_TREE_START -->\n{directory_tree}\n<!-- DIRECTORY_TREE_END -->'
    updated_contents = re.sub(pattern, replacement, readme_contents)
    return updated_contents

directory_tree = read_file('DIRECTORY_TREE.txt')
readme_contents = read_file('README.md')
updated_readme = update_readme(directory_tree, readme_contents)
write_file('README.md', updated_readme)