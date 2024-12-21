import os
import urllib.parse

def scan_directory(directory, prefix='##'):
    structure = ""
    for item in os.listdir(directory):
        if item.startswith('.') or item.startswith('_'):
            continue
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            structure += f'{prefix} {item}  \n'
            structure += scan_directory(path, prefix + '#')
        else:
            relative_path = os.path.relpath(path).replace('\\', '/')
            encoded_path = urllib.parse.quote(relative_path)
            structure += f'{prefix} [{item}](/{encoded_path})  \n'
    return structure


def save_structure_to_readme(directory, output_file='README.md'):
    structure = "# Mục lục\n\n" + scan_directory(directory)
    structure += "# Tạo mục lục tự động\n\n" + "```python\n" + read_current_file_as_string() + "\n```\n"
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(structure)
    print(f'Đã tạo mục lục thành công!')

def read_current_file_as_string():
    file_path = os.path.abspath(__file__)

    with open(file_path, "r", encoding="utf-8") as file:
        code_content = file.read()
    
    return code_content


if __name__ == '__main__':
    project_path = os.getcwd()  
    save_structure_to_readme(project_path)