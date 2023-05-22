import sys
import pytube
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QMessageBox

class Downloader(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the user interface
        self.initUI()
    
    def initUI(self):
        # Create the URL input label and field
        url_label = QLabel('Video URL:', self)
        url_label.move(20, 20)
        self.url_input = QLineEdit(self)
        self.url_input.move(100, 20)
        self.url_input.resize(280, 20)
        
        # Create the quality selection label and combo box
        quality_label = QLabel('Quality:', self)
        quality_label.move(20, 50)
        self.quality_select = QComboBox(self)
        self.quality_select.move(100, 50)
        self.quality_select.resize(280, 20)
        
        # Create the get quality button
        get_quality_button = QPushButton('Get Quality', self)
        get_quality_button.move(50, 80)
        get_quality_button.clicked.connect(self.get_quality)
        
        # Create the download button
        download_button = QPushButton('Download', self)
        download_button.move(200, 80)
        download_button.clicked.connect(self.download)
        
        # Set up the window
        self.setGeometry(100, 100, 400, 120)
        self.setWindowTitle('YouTube Downloader')
        self.show()
        
    def get_quality(self):
        # Get the YouTube video URL
        url = self.url_input.text()
        
        # Create a YouTube object
        youtube = pytube.YouTube(url)
        
        # Get available streams for the video
        streams = youtube.streams.filter(progressive=True).all()
        
        # Populate the quality selection combo box
        self.quality_select.clear()
        for stream in streams:
            self.quality_select.addItem(stream.resolution)
        
    def download(self):
        # Get the YouTube video URL
        url = self.url_input.text()
        
        # Create a YouTube object
        youtube = pytube.YouTube(url)
        
        # Get available streams for the video
        streams = youtube.streams.filter(progressive=True)
        
        # Get the selected quality option
        choice = self.quality_select.currentIndex()
        stream = streams[choice]
        
        # Open a file dialog to choose the save location
        save_path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Video Files (*.mp4)")
        
        # Download the video
        stream.download(save_path)
        
        # Display a message box to indicate that the download is complete
        QMessageBox.information(self, "Download Complete", "The video has been downloaded successfully!")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    downloader = Downloader()
    sys.exit(app.exec_())
