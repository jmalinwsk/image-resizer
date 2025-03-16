import os
import shutil
import sys

from PIL import Image
from PySide6 import QtCore
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout, QWidget, QLabel, QFileDialog

input_path = "Angel/"
output_path = "output/"

supported_extensions = (".jpeg", ".jpg", ".png", ".tiff", ".tif", ".raw", ".webp", ".bmp")

class MyWidget(QWidget):
    directorySelected = Signal(str)

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.text = QLabel("No directory selected",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.text)

        self.button = QPushButton("Choose directory")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.open_directory_dialog)
        self.directorySelected.connect(self.update_text)

    def open_directory_dialog(self):
        directory = QFileDialog.getExistingDirectory(None, "Select directory", ".", QFileDialog.Option.ShowDirsOnly)

        if directory:
            self.directorySelected.emit(directory)

    @Slot()
    def update_text(self, directory):
        self.text.setText(f"{directory}")


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

    # if os.path.exists(output_path):
    #     shutil.rmtree(output_path)
    # os.mkdir(output_path)
    #
    # for path, subdirs, files in os.walk(input_path):
    #     print(path, subdirs, files)
    #     os.makedirs(output_path + path)
    #     for name in files:
    #         filename, file_ext = os.path.splitext(name)
    #         if file_ext in supported_extensions:
    #             img = Image.open(path + "/" + name)
    #             width = img.width
    #             height = img.height
    #             if width > 3000 or height > 3000:
    #                 if width > 3000:
    #                     os.system("ffmpeg -i " + path + "/" + name + " -vf scale=3000:-1 " + output_path + path + "/" + filename + ".jpg")
    #                 else:
    #                     os.system("ffmpeg -i " + path + "/" + name + " -vf scale=-1:3000 " + output_path + path + "/" + filename + ".jpg")


