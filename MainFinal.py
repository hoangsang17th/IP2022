from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsPixmapItem, QGraphicsScene, QFileDialog, qApp
from UI.app import Ui_MainWindow

from Algorithm.smoothing import Smoothings
from Algorithm.channels import Channels
from Algorithm.noises import Noises

from Algorithm.tools import Tools
import sys
import os
import cv2


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        self.mwg = Ui_MainWindow()
        self.mwg.setupUi(self.main_win)

        self.mwg.actionOpen.triggered.connect(self.loadImage)
        self.mwg.actionSave.triggered.connect(self.savePhoto)
        self.mwg.actionZoom_In.triggered.connect(self.on_zoom_in)
        self.mwg.actionZoom_Out.triggered.connect(self.on_zoom_out)
        self.mwg.actionReset.triggered.connect(self.resetImage)

        # Tabs
        # tab 1
        self.mwg.sliderBrightness.valueChanged['int'].connect(self.alpha_value)
        self.mwg.sliderRed.valueChanged['int'].connect(self.red_value)
        self.mwg.sliderGreen.valueChanged['int'].connect(self.green_value)
        self.mwg.sliderBlue.valueChanged['int'].connect(self.blue_value)
        self.mwg.sliderGamma.valueChanged['int'].connect(self.gamma_value)
        self.mwg.sliderLogarit.valueChanged['int'].connect(self.logarit_value)
        self.mwg.sliderDaoAnh.valueChanged['int'].connect(self.island_value)
        # self.mwg.checkBoxGamma.set['bool'].connect(self.isGamma_value)

        # tab 2
        self.mwg.sliderBlur.valueChanged['int'].connect(self.blur_value)
        self.mwg.sliderGaussian.valueChanged['int'].connect(self.gauss_value)
        self.mwg.slideMedian.valueChanged['int'].connect(self.medi_value)
        self.mwg.sliderBilateral.valueChanged['int'].connect(
            self.bilateral_value)

        # tab 3
        self.mwg.btnNone.clicked.connect(self.radio_state)
        self.mwg.btnMin.clicked.connect(self.radio_state)
        self.mwg.btnMidPoint.clicked.connect(self.radio_state)
        self.mwg.btnMax.clicked.connect(self.radio_state)
        self.mwg.sliderContraharmonic.valueChanged['int'].connect(
            self.contraharmonic_value)
        # Tools
        self.mwg.actionRotateLeft.triggered.connect(
            lambda: self.rotate(cv2.ROTATE_90_COUNTERCLOCKWISE))
        self.mwg.actionRotateRight.triggered.connect(
            lambda: self.rotate(cv2.ROTATE_90_CLOCKWISE))

        self.mwg.graphicsView.viewport().installEventFilter(self)
        self.mwg.scrollArea.setMouseTracking(True)

        self.mwg.actionQuit.triggered.connect(qApp.quit)
        self.mwg.actionQuit.triggered.connect(self.reset)

        self.smoothing = Smoothings()
        self.channel = Channels()
        self.noise = Noises()
        self.tools = Tools()
        self.path = None
        self.reset()
        self.mwg.tabs.setHidden(True)
        self.directory = os.path.expanduser("~")

    def eventFilter(self, source, event):
        if (
            # source == self.mwg.graphicsView.viewport() and
            event.type() == QEvent.Wheel and
                event.modifiers() == Qt.ControlModifier):
            if event.angleDelta().y() > 0:
                scale = 1.25
            else:
                scale = 0.8
            self.mwg.graphicsView.scale(scale, scale)

            return True

        if (event.type() == QEvent.MouseMove):
            print(f"x: {event.x()}, y: {event.y()}")

        return super().eventFilter(source, event)

    def reset(self):
        self.alpha_value_now = 100
        self.red_value_now = 0
        self.green_value_now = 0
        self.blue_value_now = 0
        self.gamma_value_now = 33
        self.logarit_value_now = 0
        self.island_value_now = 1
        self.isGamma = True

        self.blur_value_now = 0
        self.gauss_value_now = 0
        self.medi_value_now = 0
        self.bilateral_value_now = 0
        self.contraharmonic_value_now = 0

        self.mwg.sliderBrightness.setValue(self.alpha_value_now)
        self.mwg.sliderGamma.setValue(self.gamma_value_now)
        self.mwg.sliderDaoAnh.setValue(self.island_value_now)
        self.mwg.sliderLogarit.setValue(self.logarit_value_now)
        self.mwg.checkBoxGamma.setChecked(self.isGamma)

        self.mwg.sliderBlur.setValue(self.blur_value_now)
        self.mwg.sliderGaussian.setValue(self.gauss_value_now)
        self.mwg.slideMedian.setValue(self.medi_value_now)
        self.mwg.sliderBilateral.setValue(self.bilateral_value_now)

        self.mwg.sliderContraharmonic.setValue(self.contraharmonic_value_now)
        self.mwg.btnNone.setChecked(True)

    def loadImage(self):
        path = QFileDialog.getOpenFileName(
            self, "Open Image", self.directory, filter="Image (*.*)")[0]
        if (path):
            self.path = path
            self.reset()
            self.mwg.tabs.setHidden(True)
            self.image = cv2.imread(self.path)
            self.imageOriginal = self.image
            self.imgNotIsland = self.image
            self.setPhoto(self.image)
            self.mwg.tabs.setHidden(False)

    def setPhoto(self, image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)

        item = QGraphicsPixmapItem(pixmap)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        self.mwg.graphicsView.setScene(scene)

    # Tab Channels
    def rbg_update(self):
        image = self.channel.change_Color(
            self.image, self.red_value_now, self.green_value_now, self.blue_value_now, self.alpha_value_now)
        self.imgNotIsland = self.channel.change_Color(
            self.image, self.red_value_now, self.green_value_now, self.blue_value_now, self.alpha_value_now)
        self.setPhoto(image)

    def alpha_value(self, value):
        if (self.path):
            self.alpha_value_now = value
            self.rbg_update()

    def red_value(self, value):
        if (self.path):
            self.red_value_now = value
            self.rbg_update()

    def green_value(self, value):
        if (self.path):
            self.green_value_now = value
            self.rbg_update()

    def blue_value(self, value):
        if (self.path):
            self.blue_value_now = value
            self.rbg_update()

    def gamma_value(self, value):
        if (self.path):
            self.gamma_value_now = value
            image = self.channel.change_Gamma(
                self.image, self.gamma_value_now)
            self.imgNotIsland = self.channel.change_Gamma(
                self.image, self.gamma_value_now)
            self.setPhoto(image)

    def logarit_value(self, value):
        if (self.path):
            self.logarit_value_now = value
            image = self.channel.change_Logarit(
                self.image, self.logarit_value_now)
            self.imgNotIsland = self.channel.change_Logarit(
                self.image, self.logarit_value_now)
            self.setPhoto(image)

    def island_value(self, value):
        if (self.path):
            self.island_value_now = value
            image = self.channel.change_Island(
                self.image, self.imgNotIsland, self.island_value_now)
            self.setPhoto(image)

    def isGamma_value(self, value):
        if (self.path):
            self.isGamma = value
    # Tab Smoothings

    def blur_value(self, value):
        if (self.path):
            self.blur_value_now = value
            image = self.smoothing.change_Blur(
                self.image, self.blur_value_now)
            self.imgNotIsland = self.smoothing.change_Blur(
                self.image, self.blur_value_now)
            self.setPhoto(image)

    def gauss_value(self, value):
        if (self.path):
            self.gauss_value_now = value
            image = self.smoothing.change_Gaussian(
                self.image, self.gauss_value_now)
            self.imgNotIsland = self.smoothing.change_Gaussian(
                self.image, self.gauss_value_now)
            self.setPhoto(image)

    def medi_value(self, value):
        if (self.path):
            self.medi_value_now = value
            image = self.smoothing.change_Median(
                self.image, self.medi_value_now)
            self.imgNotIsland = self.smoothing.change_Median(
                self.image, self.medi_value_now)
            self.setPhoto(image)

    def bilateral_value(self, value):
        if (self.path):
            self.bilateral_value_now = value
            image = self.smoothing.change_Bilateral(
                self.image, self.bilateral_value_now)
            self.imgNotIsland = self.smoothing.change_Bilateral(
                self.image, self.bilateral_value_now)
            self.setPhoto(image)

    # Tab Noise
    def radio_state(self):
        if (self.path):
            self.update()

    def contraharmonic_value(self, value):
        if (self.path):
            self.contraharmonic_value_now = value
            image = self.noise.contraharmonicMean(
                self.image, self.contraharmonic_value_now)
            self.imgNotIsland = self.noise.contraharmonicMean(
                self.image, self.contraharmonic_value_now)
            self.setPhoto(image)

    def on_zoom_in(self):
        if (self.path):
            scale = 1.25
            self.mwg.graphicsView.scale(scale, scale)

    def on_zoom_out(self):
        if (self.path):
            scale = 0.8
            self.mwg.graphicsView.scale(scale, scale)

    def resetImage(self):
        if (self.path):

            self.image = self.imageOriginal
            self.reset()
            # self.mwg.tabs.setHidden(True)
            self.setPhoto(self.image)

    def rotate(self, angle):
        if (self.path):
            self.image = self.tools.rotate(self.image, angle)
            self.update()

    def update(self):
        if (self.mwg.btnMin.isChecked()):
            self.image = self.noise.minFilter(self.image)
            self.imgNotIsland = self.noise.minFilter(self.imageNotIsland)
        elif (self.mwg.btnMidPoint.isChecked()):
            self.image = self.noise.midpoint(self.image)
            self.imgNotIsland = self.noise.midpoint(self.imageNotIsland)
        elif (self.mwg.btnMax.isChecked()):
            self.image = self.noise.maxFilter(self.image)
            self.imgNotIsland = self.noise.maxFilter(self.imageNotIsland)

        self.setPhoto(self.image)

    def savePhoto(self):
        filename = QFileDialog.getSaveFileName(
            self, "Save Image", self.directory, filter=".jpg;;.png;;.tiff;;.bmp")
        if (filename[0]):
            self.path = ''.join(filename)
            cv2.imwrite(self.path, self.tmp)
            name = os.path.basename(self.path)
            self.mwg.statusbar.showMessage(name)

    def show(self):
        self.main_win.show()


# Prevent parts of code from being run when the modules are imported
if __name__ == "__main__":
    app = QApplication([])

    form = Main()
    form.show()

    sys.exit(app.exec_())
