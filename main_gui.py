import sys 
from PyQt5 import QtWidgets
import design  
from poems_model import PoemsModel

class ExampleApp(QtWidgets.QMainWindow, design.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.btnFind.clicked.connect(self.find_song)
        poems_data_file = './data/songs.pickle'
        w2v_file = './data/ruwikiruscorpora_upos_cbow_300_20_2017.bin.gz'
        self.pm = PoemsModel(poems_data_file, w2v_file)                                                    


    def find_song(self):
        self.songText.clear()
        for poem, similarity in self.pm.similar_poems(self.similarWord.text(), topn=self.spinBox.value()): 
            self.songText.appendPlainText(f'{poem}\t\t{similarity}')

        

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show() 
    app.exec_()  
    
main()