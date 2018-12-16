#Создание модели из текстов песен
from poems_model import PoemsModel

pm = PoemsModel()
poems_file = './data/music_final.txt'
w2v_file = './data/ruwikiruscorpora_upos_cbow_300_20_2017.bin.gz'
pm.compile(poems_file, w2v_file)
pm.write('./data/songs.pickle')
