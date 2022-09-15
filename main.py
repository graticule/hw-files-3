from typing import List


def append_files(files: List[str], result_file: str) -> None:
    info = {}
    for file in files:
        with open(file, encoding='UTF-8') as f:
            info[file] = len(f.readlines())
    with open(result_file, mode='w', encoding='UTF-8') as out:
        for file, pages in sorted(info.items(), key=lambda t: t[1]):
            with open(file, encoding='UTF-8') as f:
                out.write(file+'\n')
                out.write(str(pages)+'\n')
                out.write(f.read())
                out.write('\n')


append_files(['1.txt', '2.txt', '3.txt'], 'result.txt')
