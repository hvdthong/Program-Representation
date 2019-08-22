import pandas as pd
import os


def read_file(fname):
    with open(fname) as f:
        content = f.readlines()
    return [x.strip() for x in content]


if __name__ == '__main__':
    # data = pd.read_csv('latest.csv', delimiter=',')
    # # data = pd.read_csv('example.csv', delimiter=',')
    # print(data.head())
    # print(len(data))
    # exit()

    print('hello')
    exit()

    path_files = '/media/hvdthong/cd8eddc8-4ee9-44d6-b7a1-52d9d4bd677c/DATA_PROGRAM_REPRESENTATION/apk_collection'
    files = os.listdir(path_files)
    files = [file.replace('.apk', '') for file in files]

    path_data = '/media/hvdthong/cd8eddc8-4ee9-44d6-b7a1-52d9d4bd677c/DATA_PROGRAM_REPRESENTATION/latest.csv'
    data = pd.read_csv(path_data, delimiter=',')

    data_info = data[data['pkg_name'].isin(files)]
    data_info = data_info.sort_values(by=['pkg_name', 'dex_date'], ascending=[True, False])
    data_info = data_info.drop_duplicates('pkg_name', keep='first')
    print(len(data_info))
    exit()

    new_files = list()
    for file in files:
        row = data.loc[data['pkg_name'] == file]
        new_files.append(row)
        print(len(new_files))

    exit()
    apks = [data.loc[data['pkg_name'] == file] for file in files]
    print('apks', len(apks))
    exit()

    row = data.loc[data['pkg_name'] == files[0]]
    print(row)
    exit()

    headers = list(data.columns.values)
    data_pkg_name = data['pkg_name'].tolist()

    if files[0] in data_pkg_name:
        print('good')
        exit()
    else:
        print('no')
        exit()
    for header in headers:
        print(header)
    print(data.head())
    print(len(data))
    print(headers)
    exit()

    fname = 'latest.csv'
    data = read_file(fname=fname)
    title, data = data[0:1], data[1:]
    parts = 10
    num_each_part = int(len(data) / parts)
    chunks = [data[x:x+num_each_part] for x in range(0, len(data), num_each_part)]
    print(len(data), num_each_part)
    print(len(chunks))


