import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from SkyAR import SkyAR
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'SkyAR GUI'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # create a label for the canvas
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width, self.height)
        # create a button to select an image
        self.button = QPushButton('Select Image', self)
        self.button.move(0, self.height - 50)
        self.button.clicked.connect(self.selectImage)
        self.show()
    def selectImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Image", "","All Files (*);;Image Files (*.png *.jpg *.bmp)", options=options)
        if fileName:
            # load the selected image
            pixmap = QPixmap(fileName)
            # display the image on the canvas
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
            # create a SkyAR instance and display the augmented reality
            ar = SkyAR()
            ar.load_image(fileName)
            ar.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
