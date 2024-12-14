import os
import urllib.parse

def scan_directory(directory, prefix='##'):
    structure = ''
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
    structure = scan_directory(directory)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('# Mục lục\n\n')
        file.write(structure)
    print(f'Đã tạo mục lục thành công!')


if __name__ == '__main__':
    project_path = os.getcwd()  # Quét thư mục hiện tại
    save_structure_to_readme(project_path)