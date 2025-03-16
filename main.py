import os
import shutil
import sys

from PIL import Image
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog

input_path = "Angel/"
output_path = "output/"

supported_extensions = (".jpeg", ".jpg", ".png", ".tiff", ".tif", ".raw", ".webp", ".bmp")

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.input_path_label = QLabel("No directory selected",
                                     alignment=Qt.AlignCenter)
        self.layout.addWidget(self.input_path_label)

        self.output_path_label = QLabel("Select output directory", alignment=Qt.AlignCenter)
        self.layout.addWidget(self.output_path_label)

        self.input_path_button = QPushButton("Choose input directory")
        self.layout.addWidget(self.input_path_button)
        self.input_path_button.clicked.connect(self.select_input_directory)

        self.output_path_button = QPushButton("Choose output directory")
        self.layout.addWidget(self.output_path_button)
        self.output_path_button.clicked.connect(self.select_output_directory)

    def select_input_directory(self):
        directory = QFileDialog.getExistingDirectory(None, "Select directory", ".", QFileDialog.Option.ShowDirsOnly)

        if directory:
            self.input_path_label.setText(f"{directory}")

    def select_output_directory(self):
        directory = QFileDialog.getExistingDirectory(None, "Select directory", ".", QFileDialog.Option.ShowDirsOnly)

        if directory:
            self.output_path_label.setText(f"{directory}")

    def update_input_path(self, directory):
        self.input_path_label.setText(f"{directory}")

    def update_output_path(self, directory):
        self.output_path_label.setText(f"{directory}")


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

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

    sys.exit(app.exec())


