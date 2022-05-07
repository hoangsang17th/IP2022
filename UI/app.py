# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1155, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 824, 790))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 6, 0, 1, 1)
        self.sliderBrightness = QtWidgets.QSlider(self.tab)
        self.sliderBrightness.setMinimum(0)
        self.sliderBrightness.setMaximum(200)
        self.sliderBrightness.setSingleStep(1)
        self.sliderBrightness.setPageStep(10)
        self.sliderBrightness.setProperty("value", 100)
        self.sliderBrightness.setOrientation(QtCore.Qt.Horizontal)
        self.sliderBrightness.setObjectName("sliderBrightness")
        self.gridLayout_3.addWidget(self.sliderBrightness, 1, 0, 1, 2)
        self.sliderRed = QtWidgets.QSlider(self.tab)
        self.sliderRed.setMinimum(-100)
        self.sliderRed.setMaximum(100)
        self.sliderRed.setOrientation(QtCore.Qt.Horizontal)
        self.sliderRed.setObjectName("sliderRed")
        self.gridLayout_3.addWidget(self.sliderRed, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 11, 0, 1, 1)
        self.sliderBlue = QtWidgets.QSlider(self.tab)
        self.sliderBlue.setMinimum(-100)
        self.sliderBlue.setMaximum(100)
        self.sliderBlue.setOrientation(QtCore.Qt.Horizontal)
        self.sliderBlue.setObjectName("sliderBlue")
        self.gridLayout_3.addWidget(self.sliderBlue, 7, 0, 1, 1)
        self.sliderGreen = QtWidgets.QSlider(self.tab)
        self.sliderGreen.setMinimum(-100)
        self.sliderGreen.setMaximum(100)
        self.sliderGreen.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGreen.setObjectName("sliderGreen")
        self.gridLayout_3.addWidget(self.sliderGreen, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.sliderGamma = QtWidgets.QSlider(self.tab)
        self.sliderGamma.setMinimum(1)
        self.sliderGamma.setProperty("value", 50)
        self.sliderGamma.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGamma.setObjectName("sliderGamma")
        self.gridLayout_3.addWidget(self.sliderGamma, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 8, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sliderBlur = QtWidgets.QSlider(self.tab_1)
        self.sliderBlur.setOrientation(QtCore.Qt.Horizontal)
        self.sliderBlur.setObjectName("sliderBlur")
        self.gridLayout_4.addWidget(self.sliderBlur, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.sliderGaussian = QtWidgets.QSlider(self.tab_1)
        self.sliderGaussian.setMinimum(1)
        self.sliderGaussian.setSingleStep(2)
        self.sliderGaussian.setPageStep(16)
        self.sliderGaussian.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGaussian.setObjectName("sliderGaussian")
        self.gridLayout_4.addWidget(self.sliderGaussian, 3, 0, 1, 1)
        self.slideMedian = QtWidgets.QSlider(self.tab_1)
        self.slideMedian.setMinimum(1)
        self.slideMedian.setSingleStep(2)
        self.slideMedian.setPageStep(16)
        self.slideMedian.setOrientation(QtCore.Qt.Horizontal)
        self.slideMedian.setObjectName("slideMedian")
        self.gridLayout_4.addWidget(self.slideMedian, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radio_Negative = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Negative.setObjectName("radio_Negative")
        self.gridLayout_5.addWidget(self.radio_Negative, 10, 0, 1, 1)
        self.radio_Emboss = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Emboss.setObjectName("radio_Emboss")
        self.gridLayout_5.addWidget(self.radio_Emboss, 8, 0, 1, 1)
        self.radio_Directional_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Directional_2.setObjectName("radio_Directional_2")
        self.gridLayout_5.addWidget(self.radio_Directional_2, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 12, 0, 1, 1)
        self.radio_Directional_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Directional_3.setObjectName("radio_Directional_3")
        self.gridLayout_5.addWidget(self.radio_Directional_3, 7, 0, 1, 1)
        self.radio_None = QtWidgets.QRadioButton(self.tab_2)
        self.radio_None.setObjectName("radio_None")
        self.gridLayout_5.addWidget(self.radio_None, 0, 0, 1, 1)
        self.radio_Median_threshold = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Median_threshold.setObjectName("radio_Median_threshold")
        self.gridLayout_5.addWidget(self.radio_Median_threshold, 9, 0, 1, 1)
        self.radio_Directional_1 = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Directional_1.setObjectName("radio_Directional_1")
        self.gridLayout_5.addWidget(self.radio_Directional_1, 5, 0, 1, 1)
        self.radio_Box = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Box.setObjectName("radio_Box")
        self.gridLayout_5.addWidget(self.radio_Box, 3, 0, 1, 1)
        self.radio_Bilateral = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Bilateral.setObjectName("radio_Bilateral")
        self.gridLayout_5.addWidget(self.radio_Bilateral, 1, 0, 1, 1)
        self.radio_Blackwhite = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Blackwhite.setObjectName("radio_Blackwhite")
        self.gridLayout_5.addWidget(self.radio_Blackwhite, 2, 0, 1, 1)
        self.radio_Sepia = QtWidgets.QRadioButton(self.tab_2)
        self.radio_Sepia.setObjectName("radio_Sepia")
        self.gridLayout_5.addWidget(self.radio_Sepia, 11, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\icons/icons8-opened-folder-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("UI\\icons/gnome-mime-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI\\icons/icons8-save-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("UI\\icons/folder_color_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI\\icons/icons8-close-window-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI\\icons/icons8-info-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("UI\\icons/stock_addressbook.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName("actionAbout")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI\\icons/icons8-zoom-in-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon4)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("UI\\icons/icons8-zoom-out-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon5)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionPen = QtWidgets.QAction(MainWindow)
        self.actionPen.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("UI\\icons/icons8-pencil-drawing-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPen.setIcon(icon6)
        self.actionPen.setObjectName("actionPen")
        self.actionPicker = QtWidgets.QAction(MainWindow)
        self.actionPicker.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("UI\\icons/icons8-color-dropper-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPicker.setIcon(icon7)
        self.actionPicker.setObjectName("actionPicker")
        self.actionMove = QtWidgets.QAction(MainWindow)
        self.actionMove.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("UI\\icons/icons8-move-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMove.setIcon(icon8)
        self.actionMove.setObjectName("actionMove")
        self.actionFillColor = QtWidgets.QAction(MainWindow)
        self.actionFillColor.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("UI\\icons/icons8-paint-bucket-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFillColor.setIcon(icon9)
        self.actionFillColor.setObjectName("actionFillColor")
        self.actionCursor = QtWidgets.QAction(MainWindow)
        self.actionCursor.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("UI\\icons/icons8-cursor-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCursor.setIcon(icon10)
        self.actionCursor.setObjectName("actionCursor")
        self.actionCrop = QtWidgets.QAction(MainWindow)
        self.actionCrop.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("UI\\icons/icons8-crop-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCrop.setIcon(icon11)
        self.actionCrop.setObjectName("actionCrop")
        self.actionEraser = QtWidgets.QAction(MainWindow)
        self.actionEraser.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("UI\\icons/icons8-eraser-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEraser.setIcon(icon12)
        self.actionEraser.setObjectName("actionEraser")
        self.actionBrush = QtWidgets.QAction(MainWindow)
        self.actionBrush.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("UI\\icons/icons8-makeup-brush-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrush.setIcon(icon13)
        self.actionBrush.setObjectName("actionBrush")
        self.actionRotateLeft = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("UI\\icons/icons8-rotate-left-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRotateLeft.setIcon(icon14)
        self.actionRotateLeft.setObjectName("actionRotateLeft")
        self.actionRotateRight = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("UI\\icons/icons8-rotate-right-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRotateRight.setIcon(icon15)
        self.actionRotateRight.setObjectName("actionRotateRight")
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing - HoangSang17th"))
        self.label_8.setText(_translate("MainWindow", "Blue:"))
        self.label_6.setText(_translate("MainWindow", "Red:"))
        self.label_2.setText(_translate("MainWindow", "Brightness:"))
        self.label_7.setText(_translate("MainWindow", "Green:"))
        self.label_3.setText(_translate("MainWindow", "Gamma:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Light"))
        self.label_5.setText(_translate("MainWindow", "Gaussian:"))
        self.label_4.setText(_translate("MainWindow", "Median:"))
        self.label.setText(_translate("MainWindow", "Blur:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Smoothing"))
        self.radio_Negative.setText(_translate("MainWindow", "Negative"))
        self.radio_Emboss.setText(_translate("MainWindow", "Emboss"))
        self.radio_Directional_2.setText(_translate("MainWindow", "Directional (2)"))
        self.radio_Directional_3.setText(_translate("MainWindow", "Directional (3)"))
        self.radio_None.setText(_translate("MainWindow", "None"))
        self.radio_Median_threshold.setText(_translate("MainWindow", "Median threshold"))
        self.radio_Directional_1.setText(_translate("MainWindow", "Directional (1)"))
        self.radio_Box.setText(_translate("MainWindow", "Box"))
        self.radio_Bilateral.setText(_translate("MainWindow", "Bilateral"))
        self.radio_Blackwhite.setText(_translate("MainWindow", "Black white"))
        self.radio_Sepia.setText(_translate("MainWindow", "Sepia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Filter"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save as"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionPen.setText(_translate("MainWindow", "Pen"))
        self.actionPicker.setText(_translate("MainWindow", "Picker"))
        self.actionMove.setText(_translate("MainWindow", "Move"))
        self.actionFillColor.setText(_translate("MainWindow", "FillColor"))
        self.actionCursor.setText(_translate("MainWindow", "Cursor"))
        self.actionCrop.setText(_translate("MainWindow", "Crop"))
        self.actionEraser.setText(_translate("MainWindow", "Eraser"))
        self.actionBrush.setText(_translate("MainWindow", "Brush"))
        self.actionRotateLeft.setText(_translate("MainWindow", "RotateLeft"))
        self.actionRotateRight.setText(_translate("MainWindow", "RotateRight"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
