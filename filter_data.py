import pandas as pd
import shutil


def requirement(path):
    # We should select
    data = pd.read_csv(path, delimiter=',')
    data_dex_date_2018 = data[data['dex_date'].str.match('2018')]
    data_dex_date_2019 = data[data['dex_date'].str.match('2019')]
    data_new = pd.concat([data_dex_date_2018, data_dex_date_2019])
    data_new_market = data_new[data_new['markets'] == 'play.google.com']
    return data_new_market


def copy_data_to_other_directory(path_in, path_out, path_info, data):
    data.to_csv(path_info + 'apk_selected.csv', index=False)
    apk_names = data['pkg_name']
    print('----------- Copy file -----------')
    [shutil.copy(path_in + apk + '.apk', path_out + apk + '.apk') for apk in apk_names]
    print('---------------------------------')


if __name__ == '__main__':
    # path_data = '/media/hvdthong/cd8eddc8-4ee9-44d6-b7a1-52d9d4bd677c/DATA_PROGRAM_REPRESENTATION/apk_info.csv'
    # data = requirement(path=path_data)  # select apk
    #
    # path_in = '/media/hvdthong/cd8eddc8-4ee9-44d6-b7a1-52d9d4bd677c/DATA_PROGRAM_REPRESENTATION/apk_collection/'
    # path_out = '/media/hvdthong/cd8eddc8-4ee9-44d6-b7a1-52d9d4bd677c/DATA_PROGRAM_REPRESENTATION/apk_selected/'
    # path_info = '/media/hvdthong/cd8eddc8-4ee9-44d6-b7a1-52d9d4bd677c/DATA_PROGRAM_REPRESENTATION/'
    # copy_data_to_other_directory(path_in=path_in, path_out=path_out, path_info=path_info, data=data)

    path_data = '/media/hvdthong/cd8eddc8-4ee9-44d6-b7a1-52d9d4bd677c/DATA_PROGRAM_REPRESENTATION/apk_selected.csv'
    data = pd.read_csv(path_data, delimiter=',')
    print(len(data.loc[data['vt_detection'] > 0]))
    print(len(data.loc[data['vt_detection'] == 0]))
    print(len(data))
