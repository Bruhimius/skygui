mport sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
import cv2
import skyar
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SkyAR GUI")
        self.setGeometry(100, 100, 800, 600)
        self.video_file = ""
        self.sky_image = ""
        self.create_menu()
        self.create_toolbar()
        self.create_status_bar()
    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        open_video_action = QAction("Open Video", self)
        open_video_action.triggered.connect(self.open_video)
        file_menu.addAction(open_video_action)
        open_sky_image_action = QAction("Open Sky Image", self)
        open_sky_image_action.triggered.connect(self.open_sky_image)
        file_menu.addAction(open_sky_image_action)
    def create_toolbar(self):
        toolbar = self.addToolBar("Toolbar")
        process_button = QPushButton("Process")
        process_button.clicked.connect(self.process)
        toolbar.addWidget(process_button)
    def create_status_bar(self):
        status_bar = self.statusBar()
        self.status_label = QLabel("Ready")
        status_bar.addWidget(self.status_label)
    def open_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video", os.path.expanduser("~"), "Video Files (*.mp4 *.avi)")
        if filename:
            self.video_file = filename
            self.status_label.setText(f"Video file selected: {filename}")
    def open_sky_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Sky Image", os.path.expanduser("~"), "Image Files (*.jpg *.jpeg *.png)")
        if filename:
            self.sky_image = filename
            pixmap = QPixmap(filename)
            self.sky_image_label.setPixmap(pixmap)
            self.status_label.setText(f"Sky image selected: {filename}")
    def process(self):
        if not self.video_file:
            self.status_label.setText("Please select a video file")
            return
        if not self.sky_image:
            self.status_label.setText("Please select a sky image")
            return
        self.status_label.setText("Processing...")
        cap = cv2.VideoCapture(self.video_file)
        sky = cv2.imread(self.sky_image)
        skyar.replace_sky(cap, sky)
        self.status_label.setText("Done")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
