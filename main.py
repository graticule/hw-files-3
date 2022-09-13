def append_files(files, result_file):
    info = {}
    for file in files:
        with open(file, encoding='UTF-8') as f:
            info[file] = len(f.readlines())
    with open(result_file, mode='w', encoding='UTF-8') as out:
        for file, pages in sorted(info.items(), key=lambda t: t[1]):
            with open(file, encoding='UTF-8') as f:
                out.write(file+'\n')
                out.write(str(pages)+'\n')
                out.writelines(f.readlines())
                out.write('\n')


append_files(['1.txt', '2.txt', '3.txt'], 'result.txt')