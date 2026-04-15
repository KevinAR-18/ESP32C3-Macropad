# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keybloomDlfzjr.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(800, 400))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMinimumSize(QSize(800, 400))
        self.styleSheet.setMaximumSize(QSize(800, 400))
        self.styleSheet.setStyleSheet(u"/* ================= ROOT ================= */\n"
"QMainWindow {\n"
"    background-color: #f2effc;   /* ungu sangat terang tapi hidup */\n"
"    color: #2b2545;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* ================= MAIN APP BG ================= */\n"
"#bgApp {\n"
"    background-color: #e6e1f4;   /* ungu soft tapi lebih nyala */\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* ================= TITLE BAR ================= */\n"
"#titleFrame {\n"
"    background-color: #d3caf0;   /* ungu header lebih tegas */\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom: 1px solid #b9aedc;\n"
"}\n"
"\n"
"/* ================= TITLE TEXT ================= */\n"
"#titleFrame QLabel {\n"
"    color: #2b2545;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ================= CONTENT ================= */\n"
"#contentFrame {\n"
"    background-color: #e6e1f4;   /* sama dengan bgApp biar nyatu */\n"
"}\n"
"\n"
"/* ================= BOTTO"
                        "M BAR ================= */\n"
"#bottomBar {\n"
"    background-color: #d3caf0;   /* senada titleFrame */\n"
"    border-bottom-left-radius: 12px;\n"
"    border-bottom-right-radius: 12px;\n"
"    border-top: 1px solid #b9aedc;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ================= BOTTOM TEXT ================= */\n"
"#bottomBar QLabel {\n"
"    font-size: 8pt;\n"
"    color: #4f4870;\n"
"}\n"
"")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setGeometry(QRect(0, 0, 800, 400))
        self.bgApp.setMinimumSize(QSize(800, 400))
        self.bgApp.setMaximumSize(QSize(800, 400))
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.bgApp)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.bgApp)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setMinimumSize(QSize(0, 45))
        self.titleFrame.setMaximumSize(QSize(16777215, 45))
        self.titleFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftBox = QFrame(self.titleFrame)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.clockInfo = QLabel(self.leftBox)
        self.clockInfo.setObjectName(u"clockInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clockInfo.sizePolicy().hasHeightForWidth())
        self.clockInfo.setSizePolicy(sizePolicy1)
        self.clockInfo.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setWeight(QFont.Medium)
        font.setItalic(False)
        self.clockInfo.setFont(font)
        self.clockInfo.setStyleSheet(u"\n"
"/* Clock */\n"
"#clockInfo {\n"
"    color: #4b3f8f;     /* ungu lebih gelap & jelas */\n"
"    font-size: 9pt;\n"
"    font-weight: 500;\n"
"}")
        self.clockInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.clockInfo)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy1.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setMinimumSize(QSize(0, 0))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titleRightInfo {\n"
"    color: white;      \n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    background-color: #8E7AB5; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.unusedFrame = QFrame(self.leftBox)
        self.unusedFrame.setObjectName(u"unusedFrame")
        self.unusedFrame.setMinimumSize(QSize(50, 0))
        self.unusedFrame.setMaximumSize(QSize(170, 16777215))
        self.unusedFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.unusedFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.unusedFrame)


        self.horizontalLayout_4.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.titleFrame)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(22, 22))
        self.minimizeAppBtn.setMaximumSize(QSize(16777215, 16777215))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimizeAppBtn.setStyleSheet(u"QPushButton#minimizeAppBtn {\n"
"    background-color: #9b8fdc;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"\n"
"    min-width: 22px;\n"
"    min-height: 22px;\n"
"\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#minimizeAppBtn:hover {\n"
"    background-color: #afa5eb;\n"
"}\n"
"\n"
"QPushButton#minimizeAppBtn:pressed {\n"
"    background-color: #877ac9;\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"    background-color: #3a3361;\n"
"    color: #f4f1fb;\n"
"    border: 1px solid #5b53a4;\n"
"    border-radius: 4px;\n"
"\n"
"    padding: 3px 6px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/images/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(22, 22))
        self.closeAppBtn.setMaximumSize(QSize(16777215, 16777215))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"QPushButton#closeAppBtn {\n"
"    background-color: #e07a7a;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"\n"
"    min-width: 22px;\n"
"    min-height: 22px;\n"
"\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#closeAppBtn:hover {\n"
"    background-color: #eb8c8c;\n"
"}\n"
"\n"
"QPushButton#closeAppBtn:pressed {\n"
"    background-color: #c96666;\n"
"}\n"
"\n"
"QPushButton#closeAppBtn QToolTip {\n"
"    background-color: #d94a4a;   /* MERAH jelas */\n"
"    color: #ffffff;\n"
"    border: 1px solid #b83838;\n"
"    border-radius: 4px;\n"
"\n"
"    padding: 3px 6px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8pt;\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout_4.addWidget(self.rightButtons)


        self.verticalLayout.addWidget(self.titleFrame)

        self.contentFrame = QFrame(self.bgApp)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setStyleSheet(u"#contentFrame {\n"
"border-image: url(:/icon/images/bg2.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"\n"
"")
        self.contentFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.contentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.profileFrame = QFrame(self.contentFrame)
        self.profileFrame.setObjectName(u"profileFrame")
        self.profileFrame.setMinimumSize(QSize(0, 60))
        self.profileFrame.setMaximumSize(QSize(16777215, 60))
        self.profileFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.profileFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.profileFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_profile1 = QPushButton(self.profileFrame)
        self.btn_profile1.setObjectName(u"btn_profile1")
        self.btn_profile1.setMinimumSize(QSize(110, 35))
        self.btn_profile1.setMaximumSize(QSize(110, 35))
        self.btn_profile1.setStyleSheet(u"/* ===== OPTION 1 : Default Profile Button ===== */\n"
"QPushButton {\n"
"    background-color: #A888B5;\n"
"    border: 2px solid #8f6fa0;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B296C1;\n"
"    border-color: #7f5f90;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9675A5;\n"
"    border-color: #6e4f7f;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_profile1)

        self.btn_profile2 = QPushButton(self.profileFrame)
        self.btn_profile2.setObjectName(u"btn_profile2")
        self.btn_profile2.setMinimumSize(QSize(110, 35))
        self.btn_profile2.setMaximumSize(QSize(110, 35))
        self.btn_profile2.setStyleSheet(u"/* ===== OPTION 2 : Active Profile Button ===== */\n"
"QPushButton{\n"
"    background-color: #BA94D1;\n"
"    border: 2px solid #9e78b8;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButtone:hover {\n"
"    background-color: #C7A6DB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A983C0;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_profile2)

        self.btn_profile3 = QPushButton(self.profileFrame)
        self.btn_profile3.setObjectName(u"btn_profile3")
        self.btn_profile3.setMinimumSize(QSize(110, 35))
        self.btn_profile3.setMaximumSize(QSize(110, 35))
        self.btn_profile3.setStyleSheet(u"/* ===== OPTION 1 : Default Profile Button ===== */\n"
"QPushButton {\n"
"    background-color: #A888B5;\n"
"    border: 2px solid #8f6fa0;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B296C1;\n"
"    border-color: #7f5f90;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9675A5;\n"
"    border-color: #6e4f7f;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_profile3)

        self.btn_profile4 = QPushButton(self.profileFrame)
        self.btn_profile4.setObjectName(u"btn_profile4")
        self.btn_profile4.setMinimumSize(QSize(110, 35))
        self.btn_profile4.setMaximumSize(QSize(110, 35))
        self.btn_profile4.setStyleSheet(u"/* ===== OPTION 2 : Active Profile Button ===== */\n"
"QPushButton{\n"
"    background-color: #BA94D1;\n"
"    border: 2px solid #9e78b8;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButtone:hover {\n"
"    background-color: #C7A6DB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A983C0;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_profile4)

        self.btn_profile5 = QPushButton(self.profileFrame)
        self.btn_profile5.setObjectName(u"btn_profile5")
        self.btn_profile5.setMinimumSize(QSize(110, 35))
        self.btn_profile5.setMaximumSize(QSize(110, 35))
        self.btn_profile5.setStyleSheet(u"/* ===== OPTION 1 : Default Profile Button ===== */\n"
"QPushButton {\n"
"    background-color: #A888B5;\n"
"    border: 2px solid #8f6fa0;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B296C1;\n"
"    border-color: #7f5f90;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9675A5;\n"
"    border-color: #6e4f7f;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_profile5)

        self.btn_setting = QPushButton(self.profileFrame)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(110, 35))
        self.btn_setting.setMaximumSize(QSize(110, 35))
        self.btn_setting.setStyleSheet(u"/* ===== OPTION 3 : Settings / Special Button ===== */\n"
"QPushButton {\n"
"    background-color: #B2A4FF;\n"
"    border: 2px solid #9386e6;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 5px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C1B6FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9B8CF0;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_setting)


        self.verticalLayout_2.addWidget(self.profileFrame)

        self.stackedWidget = QStackedWidget(self.contentFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageProfile1 = QWidget()
        self.pageProfile1.setObjectName(u"pageProfile1")
        self.verticalLayout_9 = QVBoxLayout(self.pageProfile1)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 10)
        self.layoutTitleprofile1 = QHBoxLayout()
        self.layoutTitleprofile1.setObjectName(u"layoutTitleprofile1")
        self.frame = QFrame(self.pageProfile1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile1.addWidget(self.frame)

        self.titlepage1 = QLabel(self.pageProfile1)
        self.titlepage1.setObjectName(u"titlepage1")
        sizePolicy1.setHeightForWidth(self.titlepage1.sizePolicy().hasHeightForWidth())
        self.titlepage1.setSizePolicy(sizePolicy1)
        self.titlepage1.setMinimumSize(QSize(0, 0))
        self.titlepage1.setMaximumSize(QSize(400, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.titlepage1.setFont(font2)
        self.titlepage1.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlepage1 {\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #435663; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlepage1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutTitleprofile1.addWidget(self.titlepage1)

        self.frame_2 = QFrame(self.pageProfile1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile1.addWidget(self.frame_2)


        self.verticalLayout_9.addLayout(self.layoutTitleprofile1)

        self.frameAllbutton1 = QFrame(self.pageProfile1)
        self.frameAllbutton1.setObjectName(u"frameAllbutton1")
        self.frameAllbutton1.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAllbutton1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameAllbutton1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameout1 = QFrame(self.frameAllbutton1)
        self.frameout1.setObjectName(u"frameout1")
        self.frameout1.setMinimumSize(QSize(135, 185))
        self.frameout1.setMaximumSize(QSize(135, 185))
        self.frameout1.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameout1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame1 = QFrame(self.frameout1)
        self.buttonFrame1.setObjectName(u"buttonFrame1")
        self.buttonFrame1.setMinimumSize(QSize(115, 130))
        self.buttonFrame1.setMaximumSize(QSize(115, 130))
        self.buttonFrame1.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame1.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.buttonFrame1)

        self.prof1_line1 = QLineEdit(self.frameout1)
        self.prof1_line1.setObjectName(u"prof1_line1")
        self.prof1_line1.setMinimumSize(QSize(115, 30))
        self.prof1_line1.setMaximumSize(QSize(115, 30))
        self.prof1_line1.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.prof1_line1)


        self.horizontalLayout.addWidget(self.frameout1)

        self.frameout2 = QFrame(self.frameAllbutton1)
        self.frameout2.setObjectName(u"frameout2")
        self.frameout2.setMinimumSize(QSize(135, 185))
        self.frameout2.setMaximumSize(QSize(135, 185))
        self.frameout2.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frameout2)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame2 = QFrame(self.frameout2)
        self.buttonFrame2.setObjectName(u"buttonFrame2")
        self.buttonFrame2.setMinimumSize(QSize(115, 130))
        self.buttonFrame2.setMaximumSize(QSize(115, 130))
        self.buttonFrame2.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.buttonFrame2)

        self.prof1_line2 = QLineEdit(self.frameout2)
        self.prof1_line2.setObjectName(u"prof1_line2")
        self.prof1_line2.setMinimumSize(QSize(115, 30))
        self.prof1_line2.setMaximumSize(QSize(115, 30))
        self.prof1_line2.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.prof1_line2)


        self.horizontalLayout.addWidget(self.frameout2)

        self.frameout3 = QFrame(self.frameAllbutton1)
        self.frameout3.setObjectName(u"frameout3")
        self.frameout3.setMinimumSize(QSize(135, 185))
        self.frameout3.setMaximumSize(QSize(135, 185))
        self.frameout3.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameout3)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame3 = QFrame(self.frameout3)
        self.buttonFrame3.setObjectName(u"buttonFrame3")
        self.buttonFrame3.setMinimumSize(QSize(115, 130))
        self.buttonFrame3.setMaximumSize(QSize(115, 130))
        self.buttonFrame3.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_6.addWidget(self.buttonFrame3)

        self.prof1_line3 = QLineEdit(self.frameout3)
        self.prof1_line3.setObjectName(u"prof1_line3")
        self.prof1_line3.setMinimumSize(QSize(115, 30))
        self.prof1_line3.setMaximumSize(QSize(115, 30))
        self.prof1_line3.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.prof1_line3)


        self.horizontalLayout.addWidget(self.frameout3)

        self.frameout4 = QFrame(self.frameAllbutton1)
        self.frameout4.setObjectName(u"frameout4")
        self.frameout4.setMinimumSize(QSize(135, 185))
        self.frameout4.setMaximumSize(QSize(135, 185))
        self.frameout4.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frameout4)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame4 = QFrame(self.frameout4)
        self.buttonFrame4.setObjectName(u"buttonFrame4")
        self.buttonFrame4.setMinimumSize(QSize(115, 130))
        self.buttonFrame4.setMaximumSize(QSize(115, 130))
        self.buttonFrame4.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame4.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.buttonFrame4)

        self.prof1_line4 = QLineEdit(self.frameout4)
        self.prof1_line4.setObjectName(u"prof1_line4")
        self.prof1_line4.setMinimumSize(QSize(115, 30))
        self.prof1_line4.setMaximumSize(QSize(115, 30))
        self.prof1_line4.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.prof1_line4)


        self.horizontalLayout.addWidget(self.frameout4)

        self.frameout5 = QFrame(self.frameAllbutton1)
        self.frameout5.setObjectName(u"frameout5")
        self.frameout5.setMinimumSize(QSize(135, 185))
        self.frameout5.setMaximumSize(QSize(135, 185))
        self.frameout5.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frameout5)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame5 = QFrame(self.frameout5)
        self.buttonFrame5.setObjectName(u"buttonFrame5")
        self.buttonFrame5.setMinimumSize(QSize(115, 130))
        self.buttonFrame5.setMaximumSize(QSize(115, 130))
        self.buttonFrame5.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame5.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_8.addWidget(self.buttonFrame5)

        self.prof1_line5 = QLineEdit(self.frameout5)
        self.prof1_line5.setObjectName(u"prof1_line5")
        self.prof1_line5.setMinimumSize(QSize(115, 30))
        self.prof1_line5.setMaximumSize(QSize(115, 30))
        self.prof1_line5.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.prof1_line5)


        self.horizontalLayout.addWidget(self.frameout5)

        self.frameout6 = QFrame(self.frameAllbutton1)
        self.frameout6.setObjectName(u"frameout6")
        self.frameout6.setMinimumSize(QSize(135, 185))
        self.frameout6.setMaximumSize(QSize(135, 185))
        self.frameout6.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frameout6)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame6 = QFrame(self.frameout6)
        self.buttonFrame6.setObjectName(u"buttonFrame6")
        self.buttonFrame6.setMinimumSize(QSize(115, 130))
        self.buttonFrame6.setMaximumSize(QSize(115, 130))
        self.buttonFrame6.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame6.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_10.addWidget(self.buttonFrame6)

        self.prof1_line6 = QLineEdit(self.frameout6)
        self.prof1_line6.setObjectName(u"prof1_line6")
        self.prof1_line6.setMinimumSize(QSize(115, 30))
        self.prof1_line6.setMaximumSize(QSize(115, 30))
        self.prof1_line6.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.prof1_line6)


        self.horizontalLayout.addWidget(self.frameout6)


        self.verticalLayout_9.addWidget(self.frameAllbutton1)

        self.frameSavep1 = QFrame(self.pageProfile1)
        self.frameSavep1.setObjectName(u"frameSavep1")
        self.frameSavep1.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSavep1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frameSavep1)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_saveload_p1 = QFrame(self.frameSavep1)
        self.btn_saveload_p1.setObjectName(u"btn_saveload_p1")
        self.btn_saveload_p1.setFrameShape(QFrame.Shape.NoFrame)
        self.btn_saveload_p1.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.btn_saveload_p1)

        self.btn_saveload1 = QPushButton(self.frameSavep1)
        self.btn_saveload1.setObjectName(u"btn_saveload1")
        self.btn_saveload1.setMinimumSize(QSize(0, 0))
        self.btn_saveload1.setMaximumSize(QSize(16777215, 16777215))
        self.btn_saveload1.setStyleSheet(u"QPushButton {\n"
"    background-color: #58B368;       /* hijau lembut tapi hidup */\n"
"    border: 1.5px solid #4A9A59;     /* diperkecil dari 2px */\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 4px 10px;               /* lebih ramping, teks tetap lega */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #68C179;\n"
"    border: 1.5px solid #3E874D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4C9957;\n"
"    border: 1.5px solid #3A7A44;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A7D9B0;\n"
"    color: #EAF6EC;\n"
"    border: 1.5px solid #8BC59A;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.btn_saveload1)

        self.frame_6 = QFrame(self.frameSavep1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_9.addWidget(self.frameSavep1)

        self.stackedWidget.addWidget(self.pageProfile1)
        self.pageProfile2 = QWidget()
        self.pageProfile2.setObjectName(u"pageProfile2")
        self.verticalLayout_16 = QVBoxLayout(self.pageProfile2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 10)
        self.layoutTitleprofile2 = QHBoxLayout()
        self.layoutTitleprofile2.setObjectName(u"layoutTitleprofile2")
        self.frame_3 = QFrame(self.pageProfile2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile2.addWidget(self.frame_3)

        self.titlepage2 = QLabel(self.pageProfile2)
        self.titlepage2.setObjectName(u"titlepage2")
        sizePolicy1.setHeightForWidth(self.titlepage2.sizePolicy().hasHeightForWidth())
        self.titlepage2.setSizePolicy(sizePolicy1)
        self.titlepage2.setMinimumSize(QSize(0, 0))
        self.titlepage2.setMaximumSize(QSize(400, 30))
        self.titlepage2.setFont(font2)
        self.titlepage2.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlepage2 {\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #435663; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlepage2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutTitleprofile2.addWidget(self.titlepage2)

        self.frame_4 = QFrame(self.pageProfile2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile2.addWidget(self.frame_4)


        self.verticalLayout_16.addLayout(self.layoutTitleprofile2)

        self.frameAllbutton2 = QFrame(self.pageProfile2)
        self.frameAllbutton2.setObjectName(u"frameAllbutton2")
        self.frameAllbutton2.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAllbutton2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frameAllbutton2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frameout7 = QFrame(self.frameAllbutton2)
        self.frameout7.setObjectName(u"frameout7")
        self.frameout7.setMinimumSize(QSize(135, 185))
        self.frameout7.setMaximumSize(QSize(135, 185))
        self.frameout7.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameout7)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame7 = QFrame(self.frameout7)
        self.buttonFrame7.setObjectName(u"buttonFrame7")
        self.buttonFrame7.setMinimumSize(QSize(115, 130))
        self.buttonFrame7.setMaximumSize(QSize(115, 130))
        self.buttonFrame7.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame7.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.buttonFrame7)

        self.prof2_line1 = QLineEdit(self.frameout7)
        self.prof2_line1.setObjectName(u"prof2_line1")
        self.prof2_line1.setMinimumSize(QSize(115, 30))
        self.prof2_line1.setMaximumSize(QSize(115, 30))
        self.prof2_line1.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.prof2_line1)


        self.horizontalLayout_7.addWidget(self.frameout7)

        self.frameout8 = QFrame(self.frameAllbutton2)
        self.frameout8.setObjectName(u"frameout8")
        self.frameout8.setMinimumSize(QSize(135, 185))
        self.frameout8.setMaximumSize(QSize(135, 185))
        self.frameout8.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frameout8)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame8 = QFrame(self.frameout8)
        self.buttonFrame8.setObjectName(u"buttonFrame8")
        self.buttonFrame8.setMinimumSize(QSize(115, 130))
        self.buttonFrame8.setMaximumSize(QSize(115, 130))
        self.buttonFrame8.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame8.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.buttonFrame8)

        self.prof2_line2 = QLineEdit(self.frameout8)
        self.prof2_line2.setObjectName(u"prof2_line2")
        self.prof2_line2.setMinimumSize(QSize(115, 30))
        self.prof2_line2.setMaximumSize(QSize(115, 30))
        self.prof2_line2.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.prof2_line2)


        self.horizontalLayout_7.addWidget(self.frameout8)

        self.frameout9 = QFrame(self.frameAllbutton2)
        self.frameout9.setObjectName(u"frameout9")
        self.frameout9.setMinimumSize(QSize(135, 185))
        self.frameout9.setMaximumSize(QSize(135, 185))
        self.frameout9.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frameout9)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame9 = QFrame(self.frameout9)
        self.buttonFrame9.setObjectName(u"buttonFrame9")
        self.buttonFrame9.setMinimumSize(QSize(115, 130))
        self.buttonFrame9.setMaximumSize(QSize(115, 130))
        self.buttonFrame9.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame9.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.buttonFrame9)

        self.prof2_line3 = QLineEdit(self.frameout9)
        self.prof2_line3.setObjectName(u"prof2_line3")
        self.prof2_line3.setMinimumSize(QSize(115, 30))
        self.prof2_line3.setMaximumSize(QSize(115, 30))
        self.prof2_line3.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.prof2_line3)


        self.horizontalLayout_7.addWidget(self.frameout9)

        self.frameout10 = QFrame(self.frameAllbutton2)
        self.frameout10.setObjectName(u"frameout10")
        self.frameout10.setMinimumSize(QSize(135, 185))
        self.frameout10.setMaximumSize(QSize(135, 185))
        self.frameout10.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frameout10)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame10 = QFrame(self.frameout10)
        self.buttonFrame10.setObjectName(u"buttonFrame10")
        self.buttonFrame10.setMinimumSize(QSize(115, 130))
        self.buttonFrame10.setMaximumSize(QSize(115, 130))
        self.buttonFrame10.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame10.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_13.addWidget(self.buttonFrame10)

        self.prof2_line4 = QLineEdit(self.frameout10)
        self.prof2_line4.setObjectName(u"prof2_line4")
        self.prof2_line4.setMinimumSize(QSize(115, 30))
        self.prof2_line4.setMaximumSize(QSize(115, 30))
        self.prof2_line4.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.prof2_line4)


        self.horizontalLayout_7.addWidget(self.frameout10)

        self.frameout11 = QFrame(self.frameAllbutton2)
        self.frameout11.setObjectName(u"frameout11")
        self.frameout11.setMinimumSize(QSize(135, 185))
        self.frameout11.setMaximumSize(QSize(135, 185))
        self.frameout11.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frameout11)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame11 = QFrame(self.frameout11)
        self.buttonFrame11.setObjectName(u"buttonFrame11")
        self.buttonFrame11.setMinimumSize(QSize(115, 130))
        self.buttonFrame11.setMaximumSize(QSize(115, 130))
        self.buttonFrame11.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame11.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.buttonFrame11)

        self.prof2_line5 = QLineEdit(self.frameout11)
        self.prof2_line5.setObjectName(u"prof2_line5")
        self.prof2_line5.setMinimumSize(QSize(115, 30))
        self.prof2_line5.setMaximumSize(QSize(115, 30))
        self.prof2_line5.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.prof2_line5)


        self.horizontalLayout_7.addWidget(self.frameout11)

        self.frameout12 = QFrame(self.frameAllbutton2)
        self.frameout12.setObjectName(u"frameout12")
        self.frameout12.setMinimumSize(QSize(135, 185))
        self.frameout12.setMaximumSize(QSize(135, 185))
        self.frameout12.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frameout12)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame12 = QFrame(self.frameout12)
        self.buttonFrame12.setObjectName(u"buttonFrame12")
        self.buttonFrame12.setMinimumSize(QSize(115, 130))
        self.buttonFrame12.setMaximumSize(QSize(115, 130))
        self.buttonFrame12.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame12.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_15.addWidget(self.buttonFrame12)

        self.prof2_line6 = QLineEdit(self.frameout12)
        self.prof2_line6.setObjectName(u"prof2_line6")
        self.prof2_line6.setMinimumSize(QSize(115, 30))
        self.prof2_line6.setMaximumSize(QSize(115, 30))
        self.prof2_line6.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.prof2_line6)


        self.horizontalLayout_7.addWidget(self.frameout12)


        self.verticalLayout_16.addWidget(self.frameAllbutton2)

        self.frameSavep2 = QFrame(self.pageProfile2)
        self.frameSavep2.setObjectName(u"frameSavep2")
        self.frameSavep2.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSavep2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frameSavep2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frameSavep2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.frame_7)

        self.btn_saveload2 = QPushButton(self.frameSavep2)
        self.btn_saveload2.setObjectName(u"btn_saveload2")
        self.btn_saveload2.setMinimumSize(QSize(0, 0))
        self.btn_saveload2.setMaximumSize(QSize(16777215, 16777215))
        self.btn_saveload2.setStyleSheet(u"QPushButton {\n"
"    background-color: #58B368;       /* hijau lembut tapi hidup */\n"
"    border: 1.5px solid #4A9A59;     /* diperkecil dari 2px */\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 4px 10px;               /* lebih ramping, teks tetap lega */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #68C179;\n"
"    border: 1.5px solid #3E874D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4C9957;\n"
"    border: 1.5px solid #3A7A44;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A7D9B0;\n"
"    color: #EAF6EC;\n"
"    border: 1.5px solid #8BC59A;\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.btn_saveload2)

        self.frame_8 = QFrame(self.frameSavep2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.frame_8)


        self.verticalLayout_16.addWidget(self.frameSavep2)

        self.stackedWidget.addWidget(self.pageProfile2)
        self.pageProfile3 = QWidget()
        self.pageProfile3.setObjectName(u"pageProfile3")
        self.verticalLayout_23 = QVBoxLayout(self.pageProfile3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 10)
        self.layoutTitleprofile3 = QHBoxLayout()
        self.layoutTitleprofile3.setObjectName(u"layoutTitleprofile3")
        self.frame_9 = QFrame(self.pageProfile3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile3.addWidget(self.frame_9)

        self.titlepage3 = QLabel(self.pageProfile3)
        self.titlepage3.setObjectName(u"titlepage3")
        sizePolicy1.setHeightForWidth(self.titlepage3.sizePolicy().hasHeightForWidth())
        self.titlepage3.setSizePolicy(sizePolicy1)
        self.titlepage3.setMinimumSize(QSize(0, 0))
        self.titlepage3.setMaximumSize(QSize(400, 30))
        self.titlepage3.setFont(font2)
        self.titlepage3.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlepage3{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #435663; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlepage3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutTitleprofile3.addWidget(self.titlepage3)

        self.frame_10 = QFrame(self.pageProfile3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile3.addWidget(self.frame_10)


        self.verticalLayout_23.addLayout(self.layoutTitleprofile3)

        self.frameAllbutton3 = QFrame(self.pageProfile3)
        self.frameAllbutton3.setObjectName(u"frameAllbutton3")
        self.frameAllbutton3.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAllbutton3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frameAllbutton3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frameout13 = QFrame(self.frameAllbutton3)
        self.frameout13.setObjectName(u"frameout13")
        self.frameout13.setMinimumSize(QSize(135, 185))
        self.frameout13.setMaximumSize(QSize(135, 185))
        self.frameout13.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frameout13)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame13 = QFrame(self.frameout13)
        self.buttonFrame13.setObjectName(u"buttonFrame13")
        self.buttonFrame13.setMinimumSize(QSize(115, 130))
        self.buttonFrame13.setMaximumSize(QSize(115, 130))
        self.buttonFrame13.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame13.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_17.addWidget(self.buttonFrame13)

        self.prof3_line1 = QLineEdit(self.frameout13)
        self.prof3_line1.setObjectName(u"prof3_line1")
        self.prof3_line1.setMinimumSize(QSize(115, 30))
        self.prof3_line1.setMaximumSize(QSize(115, 30))
        self.prof3_line1.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.prof3_line1)


        self.horizontalLayout_8.addWidget(self.frameout13)

        self.frameout14 = QFrame(self.frameAllbutton3)
        self.frameout14.setObjectName(u"frameout14")
        self.frameout14.setMinimumSize(QSize(135, 185))
        self.frameout14.setMaximumSize(QSize(135, 185))
        self.frameout14.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frameout14)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame14 = QFrame(self.frameout14)
        self.buttonFrame14.setObjectName(u"buttonFrame14")
        self.buttonFrame14.setMinimumSize(QSize(115, 130))
        self.buttonFrame14.setMaximumSize(QSize(115, 130))
        self.buttonFrame14.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame14.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_18.addWidget(self.buttonFrame14)

        self.prof3_line2 = QLineEdit(self.frameout14)
        self.prof3_line2.setObjectName(u"prof3_line2")
        self.prof3_line2.setMinimumSize(QSize(115, 30))
        self.prof3_line2.setMaximumSize(QSize(115, 30))
        self.prof3_line2.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.prof3_line2)


        self.horizontalLayout_8.addWidget(self.frameout14)

        self.frameout15 = QFrame(self.frameAllbutton3)
        self.frameout15.setObjectName(u"frameout15")
        self.frameout15.setMinimumSize(QSize(135, 185))
        self.frameout15.setMaximumSize(QSize(135, 185))
        self.frameout15.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frameout15)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame15 = QFrame(self.frameout15)
        self.buttonFrame15.setObjectName(u"buttonFrame15")
        self.buttonFrame15.setMinimumSize(QSize(115, 130))
        self.buttonFrame15.setMaximumSize(QSize(115, 130))
        self.buttonFrame15.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame15.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_19.addWidget(self.buttonFrame15)

        self.prof3_line3 = QLineEdit(self.frameout15)
        self.prof3_line3.setObjectName(u"prof3_line3")
        self.prof3_line3.setMinimumSize(QSize(115, 30))
        self.prof3_line3.setMaximumSize(QSize(115, 30))
        self.prof3_line3.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.prof3_line3)


        self.horizontalLayout_8.addWidget(self.frameout15)

        self.frameout16 = QFrame(self.frameAllbutton3)
        self.frameout16.setObjectName(u"frameout16")
        self.frameout16.setMinimumSize(QSize(135, 185))
        self.frameout16.setMaximumSize(QSize(135, 185))
        self.frameout16.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frameout16)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame16 = QFrame(self.frameout16)
        self.buttonFrame16.setObjectName(u"buttonFrame16")
        self.buttonFrame16.setMinimumSize(QSize(115, 130))
        self.buttonFrame16.setMaximumSize(QSize(115, 130))
        self.buttonFrame16.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame16.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_20.addWidget(self.buttonFrame16)

        self.prof3_line4 = QLineEdit(self.frameout16)
        self.prof3_line4.setObjectName(u"prof3_line4")
        self.prof3_line4.setMinimumSize(QSize(115, 30))
        self.prof3_line4.setMaximumSize(QSize(115, 30))
        self.prof3_line4.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.prof3_line4)


        self.horizontalLayout_8.addWidget(self.frameout16)

        self.frameout17 = QFrame(self.frameAllbutton3)
        self.frameout17.setObjectName(u"frameout17")
        self.frameout17.setMinimumSize(QSize(135, 185))
        self.frameout17.setMaximumSize(QSize(135, 185))
        self.frameout17.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frameout17)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame17 = QFrame(self.frameout17)
        self.buttonFrame17.setObjectName(u"buttonFrame17")
        self.buttonFrame17.setMinimumSize(QSize(115, 130))
        self.buttonFrame17.setMaximumSize(QSize(115, 130))
        self.buttonFrame17.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame17.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_21.addWidget(self.buttonFrame17)

        self.prof3_line5 = QLineEdit(self.frameout17)
        self.prof3_line5.setObjectName(u"prof3_line5")
        self.prof3_line5.setMinimumSize(QSize(115, 30))
        self.prof3_line5.setMaximumSize(QSize(115, 30))
        self.prof3_line5.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.prof3_line5)


        self.horizontalLayout_8.addWidget(self.frameout17)

        self.frameout18 = QFrame(self.frameAllbutton3)
        self.frameout18.setObjectName(u"frameout18")
        self.frameout18.setMinimumSize(QSize(135, 185))
        self.frameout18.setMaximumSize(QSize(135, 185))
        self.frameout18.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frameout18)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame18 = QFrame(self.frameout18)
        self.buttonFrame18.setObjectName(u"buttonFrame18")
        self.buttonFrame18.setMinimumSize(QSize(115, 130))
        self.buttonFrame18.setMaximumSize(QSize(115, 130))
        self.buttonFrame18.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame18.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_22.addWidget(self.buttonFrame18)

        self.prof3_line6 = QLineEdit(self.frameout18)
        self.prof3_line6.setObjectName(u"prof3_line6")
        self.prof3_line6.setMinimumSize(QSize(115, 30))
        self.prof3_line6.setMaximumSize(QSize(115, 30))
        self.prof3_line6.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.prof3_line6)


        self.horizontalLayout_8.addWidget(self.frameout18)


        self.verticalLayout_23.addWidget(self.frameAllbutton3)

        self.frameSavep3 = QFrame(self.pageProfile3)
        self.frameSavep3.setObjectName(u"frameSavep3")
        self.frameSavep3.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSavep3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frameSavep3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frameSavep3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_11.addWidget(self.frame_11)

        self.btn_saveload3 = QPushButton(self.frameSavep3)
        self.btn_saveload3.setObjectName(u"btn_saveload3")
        self.btn_saveload3.setMinimumSize(QSize(0, 0))
        self.btn_saveload3.setMaximumSize(QSize(16777215, 16777215))
        self.btn_saveload3.setStyleSheet(u"QPushButton {\n"
"    background-color: #58B368;       /* hijau lembut tapi hidup */\n"
"    border: 1.5px solid #4A9A59;     /* diperkecil dari 2px */\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 4px 10px;               /* lebih ramping, teks tetap lega */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #68C179;\n"
"    border: 1.5px solid #3E874D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4C9957;\n"
"    border: 1.5px solid #3A7A44;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A7D9B0;\n"
"    color: #EAF6EC;\n"
"    border: 1.5px solid #8BC59A;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.btn_saveload3)

        self.frame_12 = QFrame(self.frameSavep3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_11.addWidget(self.frame_12)


        self.verticalLayout_23.addWidget(self.frameSavep3)

        self.stackedWidget.addWidget(self.pageProfile3)
        self.pageProfile4 = QWidget()
        self.pageProfile4.setObjectName(u"pageProfile4")
        self.verticalLayout_30 = QVBoxLayout(self.pageProfile4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 10)
        self.layoutTitleprofile4 = QHBoxLayout()
        self.layoutTitleprofile4.setObjectName(u"layoutTitleprofile4")
        self.frame_13 = QFrame(self.pageProfile4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile4.addWidget(self.frame_13)

        self.titlepage4 = QLabel(self.pageProfile4)
        self.titlepage4.setObjectName(u"titlepage4")
        sizePolicy1.setHeightForWidth(self.titlepage4.sizePolicy().hasHeightForWidth())
        self.titlepage4.setSizePolicy(sizePolicy1)
        self.titlepage4.setMinimumSize(QSize(0, 0))
        self.titlepage4.setMaximumSize(QSize(400, 30))
        self.titlepage4.setFont(font2)
        self.titlepage4.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlepage4{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #435663; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlepage4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutTitleprofile4.addWidget(self.titlepage4)

        self.frame_14 = QFrame(self.pageProfile4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile4.addWidget(self.frame_14)


        self.verticalLayout_30.addLayout(self.layoutTitleprofile4)

        self.frameAllbutton4 = QFrame(self.pageProfile4)
        self.frameAllbutton4.setObjectName(u"frameAllbutton4")
        self.frameAllbutton4.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAllbutton4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frameAllbutton4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frameout19 = QFrame(self.frameAllbutton4)
        self.frameout19.setObjectName(u"frameout19")
        self.frameout19.setMinimumSize(QSize(135, 185))
        self.frameout19.setMaximumSize(QSize(135, 185))
        self.frameout19.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frameout19)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame19 = QFrame(self.frameout19)
        self.buttonFrame19.setObjectName(u"buttonFrame19")
        self.buttonFrame19.setMinimumSize(QSize(115, 130))
        self.buttonFrame19.setMaximumSize(QSize(115, 130))
        self.buttonFrame19.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame19.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_24.addWidget(self.buttonFrame19)

        self.prof4_line1 = QLineEdit(self.frameout19)
        self.prof4_line1.setObjectName(u"prof4_line1")
        self.prof4_line1.setMinimumSize(QSize(115, 30))
        self.prof4_line1.setMaximumSize(QSize(115, 30))
        self.prof4_line1.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.prof4_line1)


        self.horizontalLayout_12.addWidget(self.frameout19)

        self.frameout20 = QFrame(self.frameAllbutton4)
        self.frameout20.setObjectName(u"frameout20")
        self.frameout20.setMinimumSize(QSize(135, 185))
        self.frameout20.setMaximumSize(QSize(135, 185))
        self.frameout20.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frameout20)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame20 = QFrame(self.frameout20)
        self.buttonFrame20.setObjectName(u"buttonFrame20")
        self.buttonFrame20.setMinimumSize(QSize(115, 130))
        self.buttonFrame20.setMaximumSize(QSize(115, 130))
        self.buttonFrame20.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame20.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_25.addWidget(self.buttonFrame20)

        self.prof4_line2 = QLineEdit(self.frameout20)
        self.prof4_line2.setObjectName(u"prof4_line2")
        self.prof4_line2.setMinimumSize(QSize(115, 30))
        self.prof4_line2.setMaximumSize(QSize(115, 30))
        self.prof4_line2.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.prof4_line2)


        self.horizontalLayout_12.addWidget(self.frameout20)

        self.frameout21 = QFrame(self.frameAllbutton4)
        self.frameout21.setObjectName(u"frameout21")
        self.frameout21.setMinimumSize(QSize(135, 185))
        self.frameout21.setMaximumSize(QSize(135, 185))
        self.frameout21.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frameout21)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame21 = QFrame(self.frameout21)
        self.buttonFrame21.setObjectName(u"buttonFrame21")
        self.buttonFrame21.setMinimumSize(QSize(115, 130))
        self.buttonFrame21.setMaximumSize(QSize(115, 130))
        self.buttonFrame21.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame21.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_26.addWidget(self.buttonFrame21)

        self.prof4_line3 = QLineEdit(self.frameout21)
        self.prof4_line3.setObjectName(u"prof4_line3")
        self.prof4_line3.setMinimumSize(QSize(115, 30))
        self.prof4_line3.setMaximumSize(QSize(115, 30))
        self.prof4_line3.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_26.addWidget(self.prof4_line3)


        self.horizontalLayout_12.addWidget(self.frameout21)

        self.frameout22 = QFrame(self.frameAllbutton4)
        self.frameout22.setObjectName(u"frameout22")
        self.frameout22.setMinimumSize(QSize(135, 185))
        self.frameout22.setMaximumSize(QSize(135, 185))
        self.frameout22.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frameout22)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame22 = QFrame(self.frameout22)
        self.buttonFrame22.setObjectName(u"buttonFrame22")
        self.buttonFrame22.setMinimumSize(QSize(115, 130))
        self.buttonFrame22.setMaximumSize(QSize(115, 130))
        self.buttonFrame22.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame22.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_27.addWidget(self.buttonFrame22)

        self.prof4_line4 = QLineEdit(self.frameout22)
        self.prof4_line4.setObjectName(u"prof4_line4")
        self.prof4_line4.setMinimumSize(QSize(115, 30))
        self.prof4_line4.setMaximumSize(QSize(115, 30))
        self.prof4_line4.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_27.addWidget(self.prof4_line4)


        self.horizontalLayout_12.addWidget(self.frameout22)

        self.frameout23 = QFrame(self.frameAllbutton4)
        self.frameout23.setObjectName(u"frameout23")
        self.frameout23.setMinimumSize(QSize(135, 185))
        self.frameout23.setMaximumSize(QSize(135, 185))
        self.frameout23.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frameout23)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame23 = QFrame(self.frameout23)
        self.buttonFrame23.setObjectName(u"buttonFrame23")
        self.buttonFrame23.setMinimumSize(QSize(115, 130))
        self.buttonFrame23.setMaximumSize(QSize(115, 130))
        self.buttonFrame23.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame23.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_28.addWidget(self.buttonFrame23)

        self.prof4_line5 = QLineEdit(self.frameout23)
        self.prof4_line5.setObjectName(u"prof4_line5")
        self.prof4_line5.setMinimumSize(QSize(115, 30))
        self.prof4_line5.setMaximumSize(QSize(115, 30))
        self.prof4_line5.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_28.addWidget(self.prof4_line5)


        self.horizontalLayout_12.addWidget(self.frameout23)

        self.frameout24 = QFrame(self.frameAllbutton4)
        self.frameout24.setObjectName(u"frameout24")
        self.frameout24.setMinimumSize(QSize(135, 185))
        self.frameout24.setMaximumSize(QSize(135, 185))
        self.frameout24.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frameout24)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame24 = QFrame(self.frameout24)
        self.buttonFrame24.setObjectName(u"buttonFrame24")
        self.buttonFrame24.setMinimumSize(QSize(115, 130))
        self.buttonFrame24.setMaximumSize(QSize(115, 130))
        self.buttonFrame24.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame24.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_29.addWidget(self.buttonFrame24)

        self.prof4_line6 = QLineEdit(self.frameout24)
        self.prof4_line6.setObjectName(u"prof4_line6")
        self.prof4_line6.setMinimumSize(QSize(115, 30))
        self.prof4_line6.setMaximumSize(QSize(115, 30))
        self.prof4_line6.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_29.addWidget(self.prof4_line6)


        self.horizontalLayout_12.addWidget(self.frameout24)


        self.verticalLayout_30.addWidget(self.frameAllbutton4)

        self.frameSavep4 = QFrame(self.pageProfile4)
        self.frameSavep4.setObjectName(u"frameSavep4")
        self.frameSavep4.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSavep4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frameSavep4)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frameSavep4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.frame_15)

        self.btn_saveload4 = QPushButton(self.frameSavep4)
        self.btn_saveload4.setObjectName(u"btn_saveload4")
        self.btn_saveload4.setMinimumSize(QSize(0, 0))
        self.btn_saveload4.setMaximumSize(QSize(16777215, 16777215))
        self.btn_saveload4.setStyleSheet(u"QPushButton {\n"
"    background-color: #58B368;       /* hijau lembut tapi hidup */\n"
"    border: 1.5px solid #4A9A59;     /* diperkecil dari 2px */\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 4px 10px;               /* lebih ramping, teks tetap lega */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #68C179;\n"
"    border: 1.5px solid #3E874D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4C9957;\n"
"    border: 1.5px solid #3A7A44;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A7D9B0;\n"
"    color: #EAF6EC;\n"
"    border: 1.5px solid #8BC59A;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.btn_saveload4)

        self.frame_16 = QFrame(self.frameSavep4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.frame_16)


        self.verticalLayout_30.addWidget(self.frameSavep4)

        self.stackedWidget.addWidget(self.pageProfile4)
        self.pageProfile5 = QWidget()
        self.pageProfile5.setObjectName(u"pageProfile5")
        self.pageProfile5.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.pageProfile5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 10)
        self.layoutTitleprofile5 = QHBoxLayout()
        self.layoutTitleprofile5.setObjectName(u"layoutTitleprofile5")
        self.frame_17 = QFrame(self.pageProfile5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile5.addWidget(self.frame_17)

        self.titlepage5 = QLabel(self.pageProfile5)
        self.titlepage5.setObjectName(u"titlepage5")
        sizePolicy1.setHeightForWidth(self.titlepage5.sizePolicy().hasHeightForWidth())
        self.titlepage5.setSizePolicy(sizePolicy1)
        self.titlepage5.setMinimumSize(QSize(0, 0))
        self.titlepage5.setMaximumSize(QSize(400, 30))
        self.titlepage5.setFont(font2)
        self.titlepage5.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlepage5{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #435663; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlepage5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutTitleprofile5.addWidget(self.titlepage5)

        self.frame_18 = QFrame(self.pageProfile5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile5.addWidget(self.frame_18)


        self.verticalLayout_37.addLayout(self.layoutTitleprofile5)

        self.frameAllbutton5 = QFrame(self.pageProfile5)
        self.frameAllbutton5.setObjectName(u"frameAllbutton5")
        self.frameAllbutton5.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAllbutton5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frameAllbutton5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frameout25 = QFrame(self.frameAllbutton5)
        self.frameout25.setObjectName(u"frameout25")
        self.frameout25.setMinimumSize(QSize(135, 185))
        self.frameout25.setMaximumSize(QSize(135, 185))
        self.frameout25.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frameout25)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame25 = QFrame(self.frameout25)
        self.buttonFrame25.setObjectName(u"buttonFrame25")
        self.buttonFrame25.setMinimumSize(QSize(115, 130))
        self.buttonFrame25.setMaximumSize(QSize(115, 130))
        self.buttonFrame25.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame25.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_31.addWidget(self.buttonFrame25)

        self.prof5_line1 = QLineEdit(self.frameout25)
        self.prof5_line1.setObjectName(u"prof5_line1")
        self.prof5_line1.setMinimumSize(QSize(115, 30))
        self.prof5_line1.setMaximumSize(QSize(115, 30))
        self.prof5_line1.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_31.addWidget(self.prof5_line1)


        self.horizontalLayout_14.addWidget(self.frameout25)

        self.frameout26 = QFrame(self.frameAllbutton5)
        self.frameout26.setObjectName(u"frameout26")
        self.frameout26.setMinimumSize(QSize(135, 185))
        self.frameout26.setMaximumSize(QSize(135, 185))
        self.frameout26.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frameout26)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame26 = QFrame(self.frameout26)
        self.buttonFrame26.setObjectName(u"buttonFrame26")
        self.buttonFrame26.setMinimumSize(QSize(115, 130))
        self.buttonFrame26.setMaximumSize(QSize(115, 130))
        self.buttonFrame26.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame26.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_32.addWidget(self.buttonFrame26)

        self.prof5_line2 = QLineEdit(self.frameout26)
        self.prof5_line2.setObjectName(u"prof5_line2")
        self.prof5_line2.setMinimumSize(QSize(115, 30))
        self.prof5_line2.setMaximumSize(QSize(115, 30))
        self.prof5_line2.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_32.addWidget(self.prof5_line2)


        self.horizontalLayout_14.addWidget(self.frameout26)

        self.frameout27 = QFrame(self.frameAllbutton5)
        self.frameout27.setObjectName(u"frameout27")
        self.frameout27.setMinimumSize(QSize(135, 185))
        self.frameout27.setMaximumSize(QSize(135, 185))
        self.frameout27.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frameout27)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame27 = QFrame(self.frameout27)
        self.buttonFrame27.setObjectName(u"buttonFrame27")
        self.buttonFrame27.setMinimumSize(QSize(115, 130))
        self.buttonFrame27.setMaximumSize(QSize(115, 130))
        self.buttonFrame27.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame27.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_33.addWidget(self.buttonFrame27)

        self.prof5_line3 = QLineEdit(self.frameout27)
        self.prof5_line3.setObjectName(u"prof5_line3")
        self.prof5_line3.setMinimumSize(QSize(115, 30))
        self.prof5_line3.setMaximumSize(QSize(115, 30))
        self.prof5_line3.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_33.addWidget(self.prof5_line3)


        self.horizontalLayout_14.addWidget(self.frameout27)

        self.frameout28 = QFrame(self.frameAllbutton5)
        self.frameout28.setObjectName(u"frameout28")
        self.frameout28.setMinimumSize(QSize(135, 185))
        self.frameout28.setMaximumSize(QSize(135, 185))
        self.frameout28.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frameout28)
        self.verticalLayout_34.setSpacing(6)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame28 = QFrame(self.frameout28)
        self.buttonFrame28.setObjectName(u"buttonFrame28")
        self.buttonFrame28.setMinimumSize(QSize(115, 130))
        self.buttonFrame28.setMaximumSize(QSize(115, 130))
        self.buttonFrame28.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame28.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_34.addWidget(self.buttonFrame28)

        self.prof5_line4 = QLineEdit(self.frameout28)
        self.prof5_line4.setObjectName(u"prof5_line4")
        self.prof5_line4.setMinimumSize(QSize(115, 30))
        self.prof5_line4.setMaximumSize(QSize(115, 30))
        self.prof5_line4.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_34.addWidget(self.prof5_line4)


        self.horizontalLayout_14.addWidget(self.frameout28)

        self.frameout29 = QFrame(self.frameAllbutton5)
        self.frameout29.setObjectName(u"frameout29")
        self.frameout29.setMinimumSize(QSize(135, 185))
        self.frameout29.setMaximumSize(QSize(135, 185))
        self.frameout29.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frameout29)
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame29 = QFrame(self.frameout29)
        self.buttonFrame29.setObjectName(u"buttonFrame29")
        self.buttonFrame29.setMinimumSize(QSize(115, 130))
        self.buttonFrame29.setMaximumSize(QSize(115, 130))
        self.buttonFrame29.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame29.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_35.addWidget(self.buttonFrame29)

        self.prof5_line5 = QLineEdit(self.frameout29)
        self.prof5_line5.setObjectName(u"prof5_line5")
        self.prof5_line5.setMinimumSize(QSize(115, 30))
        self.prof5_line5.setMaximumSize(QSize(115, 30))
        self.prof5_line5.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_35.addWidget(self.prof5_line5)


        self.horizontalLayout_14.addWidget(self.frameout29)

        self.frameout30 = QFrame(self.frameAllbutton5)
        self.frameout30.setObjectName(u"frameout30")
        self.frameout30.setMinimumSize(QSize(135, 185))
        self.frameout30.setMaximumSize(QSize(135, 185))
        self.frameout30.setFrameShape(QFrame.Shape.NoFrame)
        self.frameout30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frameout30)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(9, 9, 9, 9)
        self.buttonFrame30 = QFrame(self.frameout30)
        self.buttonFrame30.setObjectName(u"buttonFrame30")
        self.buttonFrame30.setMinimumSize(QSize(115, 130))
        self.buttonFrame30.setMaximumSize(QSize(115, 130))
        self.buttonFrame30.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonFrame30.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_36.addWidget(self.buttonFrame30)

        self.prof5_line6 = QLineEdit(self.frameout30)
        self.prof5_line6.setObjectName(u"prof5_line6")
        self.prof5_line6.setMinimumSize(QSize(115, 30))
        self.prof5_line6.setMaximumSize(QSize(115, 30))
        self.prof5_line6.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.verticalLayout_36.addWidget(self.prof5_line6)


        self.horizontalLayout_14.addWidget(self.frameout30)


        self.verticalLayout_37.addWidget(self.frameAllbutton5)

        self.frameSavep5 = QFrame(self.pageProfile5)
        self.frameSavep5.setObjectName(u"frameSavep5")
        self.frameSavep5.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSavep5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frameSavep5)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frameSavep5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_19)

        self.btn_saveload5 = QPushButton(self.frameSavep5)
        self.btn_saveload5.setObjectName(u"btn_saveload5")
        self.btn_saveload5.setMinimumSize(QSize(0, 0))
        self.btn_saveload5.setMaximumSize(QSize(16777215, 16777215))
        self.btn_saveload5.setStyleSheet(u"QPushButton {\n"
"    background-color: #58B368;       /* hijau lembut tapi hidup */\n"
"    border: 1.5px solid #4A9A59;     /* diperkecil dari 2px */\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 4px 10px;               /* lebih ramping, teks tetap lega */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #68C179;\n"
"    border: 1.5px solid #3E874D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4C9957;\n"
"    border: 1.5px solid #3A7A44;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A7D9B0;\n"
"    color: #EAF6EC;\n"
"    border: 1.5px solid #8BC59A;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btn_saveload5)

        self.frame_20 = QFrame(self.frameSavep5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_20)


        self.verticalLayout_37.addWidget(self.frameSavep5)

        self.stackedWidget.addWidget(self.pageProfile5)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.pageSettings.setStyleSheet(u"QCheckBox#cbAutoDetect,\n"
"QCheckBox#cbAutoStartup {\n"
"    color: #2e2a44;\n"
"    font-weight: 600;\n"
"}\n"
"")
        self.verticalLayout_40 = QVBoxLayout(self.pageSettings)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 10)
        self.layoutTitleprofile1_2 = QHBoxLayout()
        self.layoutTitleprofile1_2.setObjectName(u"layoutTitleprofile1_2")
        self.frame_5 = QFrame(self.pageSettings)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile1_2.addWidget(self.frame_5)

        self.titlepage6 = QLabel(self.pageSettings)
        self.titlepage6.setObjectName(u"titlepage6")
        sizePolicy1.setHeightForWidth(self.titlepage6.sizePolicy().hasHeightForWidth())
        self.titlepage6.setSizePolicy(sizePolicy1)
        self.titlepage6.setMinimumSize(QSize(0, 0))
        self.titlepage6.setMaximumSize(QSize(400, 30))
        self.titlepage6.setFont(font2)
        self.titlepage6.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlepage6{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #435663; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlepage6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoutTitleprofile1_2.addWidget(self.titlepage6)

        self.frame_21 = QFrame(self.pageSettings)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)

        self.layoutTitleprofile1_2.addWidget(self.frame_21)


        self.verticalLayout_40.addLayout(self.layoutTitleprofile1_2)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_28 = QFrame(self.pageSettings)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_28)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_28)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(360, 40))
        self.frame_22.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.titlecustom1 = QLabel(self.frame_22)
        self.titlecustom1.setObjectName(u"titlecustom1")
        sizePolicy1.setHeightForWidth(self.titlecustom1.sizePolicy().hasHeightForWidth())
        self.titlecustom1.setSizePolicy(sizePolicy1)
        self.titlecustom1.setMinimumSize(QSize(150, 30))
        self.titlecustom1.setMaximumSize(QSize(150, 30))
        self.titlecustom1.setFont(font2)
        self.titlecustom1.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlecustom1 {\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #424874; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlecustom1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.titlecustom1)

        self.customName1 = QLineEdit(self.frame_22)
        self.customName1.setObjectName(u"customName1")
        self.customName1.setMinimumSize(QSize(200, 30))
        self.customName1.setMaximumSize(QSize(200, 30))
        self.customName1.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.customName1)


        self.verticalLayout_38.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_28)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(360, 40))
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.titlecustom2 = QLabel(self.frame_23)
        self.titlecustom2.setObjectName(u"titlecustom2")
        sizePolicy1.setHeightForWidth(self.titlecustom2.sizePolicy().hasHeightForWidth())
        self.titlecustom2.setSizePolicy(sizePolicy1)
        self.titlecustom2.setMinimumSize(QSize(150, 30))
        self.titlecustom2.setMaximumSize(QSize(150, 30))
        self.titlecustom2.setFont(font2)
        self.titlecustom2.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlecustom2{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #424874; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titlecustom2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.titlecustom2)

        self.customName2 = QLineEdit(self.frame_23)
        self.customName2.setObjectName(u"customName2")
        self.customName2.setMinimumSize(QSize(200, 30))
        self.customName2.setMaximumSize(QSize(200, 30))
        self.customName2.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.horizontalLayout_17.addWidget(self.customName2)


        self.verticalLayout_38.addWidget(self.frame_23)

        self.frame_27 = QFrame(self.frame_28)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(360, 40))
        self.frame_27.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.titlecustom3 = QLabel(self.frame_27)
        self.titlecustom3.setObjectName(u"titlecustom3")
        sizePolicy1.setHeightForWidth(self.titlecustom3.sizePolicy().hasHeightForWidth())
        self.titlecustom3.setSizePolicy(sizePolicy1)
        self.titlecustom3.setMinimumSize(QSize(150, 30))
        self.titlecustom3.setMaximumSize(QSize(150, 30))
        self.titlecustom3.setFont(font2)
        self.titlecustom3.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlecustom3 {\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #424874; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"")
        self.titlecustom3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.titlecustom3)

        self.customName3 = QLineEdit(self.frame_27)
        self.customName3.setObjectName(u"customName3")
        self.customName3.setMinimumSize(QSize(200, 30))
        self.customName3.setMaximumSize(QSize(200, 30))
        self.customName3.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.customName3)


        self.verticalLayout_38.addWidget(self.frame_27)

        self.frame_25 = QFrame(self.frame_28)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(360, 40))
        self.frame_25.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.titlecustom4 = QLabel(self.frame_25)
        self.titlecustom4.setObjectName(u"titlecustom4")
        sizePolicy1.setHeightForWidth(self.titlecustom4.sizePolicy().hasHeightForWidth())
        self.titlecustom4.setSizePolicy(sizePolicy1)
        self.titlecustom4.setMinimumSize(QSize(150, 30))
        self.titlecustom4.setMaximumSize(QSize(150, 30))
        self.titlecustom4.setFont(font2)
        self.titlecustom4.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlecustom4{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #424874; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"")
        self.titlecustom4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.titlecustom4)

        self.customName4 = QLineEdit(self.frame_25)
        self.customName4.setObjectName(u"customName4")
        self.customName4.setMinimumSize(QSize(200, 30))
        self.customName4.setMaximumSize(QSize(200, 30))
        self.customName4.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.customName4)


        self.verticalLayout_38.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_28)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(360, 40))
        self.frame_26.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.titlecustom5 = QLabel(self.frame_26)
        self.titlecustom5.setObjectName(u"titlecustom5")
        sizePolicy1.setHeightForWidth(self.titlecustom5.sizePolicy().hasHeightForWidth())
        self.titlecustom5.setSizePolicy(sizePolicy1)
        self.titlecustom5.setMinimumSize(QSize(150, 30))
        self.titlecustom5.setMaximumSize(QSize(150, 30))
        self.titlecustom5.setFont(font2)
        self.titlecustom5.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titlecustom5{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #424874; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"")
        self.titlecustom5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.titlecustom5)

        self.customName5 = QLineEdit(self.frame_26)
        self.customName5.setObjectName(u"customName5")
        self.customName5.setMinimumSize(QSize(200, 30))
        self.customName5.setMaximumSize(QSize(200, 30))
        self.customName5.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.horizontalLayout_20.addWidget(self.customName5)


        self.verticalLayout_38.addWidget(self.frame_26)


        self.horizontalLayout_25.addWidget(self.frame_28)

        self.frame_24 = QFrame(self.pageSettings)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_24)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_29 = QFrame(self.frame_24)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(360, 40))
        self.frame_29.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.titleinputCOM = QLabel(self.frame_29)
        self.titleinputCOM.setObjectName(u"titleinputCOM")
        sizePolicy1.setHeightForWidth(self.titleinputCOM.sizePolicy().hasHeightForWidth())
        self.titleinputCOM.setSizePolicy(sizePolicy1)
        self.titleinputCOM.setMinimumSize(QSize(160, 30))
        self.titleinputCOM.setMaximumSize(QSize(160, 30))
        self.titleinputCOM.setFont(font2)
        self.titleinputCOM.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titleinputCOM{\n"
"    color: white;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #424874; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"")
        self.titleinputCOM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.titleinputCOM)

        self.inputCOM = QLineEdit(self.frame_29)
        self.inputCOM.setObjectName(u"inputCOM")
        self.inputCOM.setMinimumSize(QSize(200, 30))
        self.inputCOM.setMaximumSize(QSize(200, 30))
        self.inputCOM.setStyleSheet(u"/* ================= CUSTOM LINE EDIT ================= */\n"
"QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0.9);   /* putih lembut, bersih */\n"
"    color: #2e2a44;                               /* teks ungu gelap */\n"
"    \n"
"	font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    font-weight: 700;     \n"
"\n"
"    border: 2px solid #9b8acb;                    /* ungu medium */\n"
"    border-radius: 8px;\n"
"	padding: 2px 4px;\n"
"}\n"
"\n"
"/* ================= DISABLED ================= */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(235, 231, 246, 0.8);   /* abu ungu */\n"
"    color: #9a95b3;\n"
"    border: 2px solid #c7bddf;\n"
"}\n"
"")

        self.horizontalLayout_23.addWidget(self.inputCOM)


        self.verticalLayout_39.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.frame_24)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(350, 0))
        self.frame_31.setMaximumSize(QSize(350, 16777215))
        self.frame_31.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 20, 0)
        self.cbAutostartup = QCheckBox(self.frame_31)
        self.cbAutostartup.setObjectName(u"cbAutostartup")
        self.cbAutostartup.setMinimumSize(QSize(25, 25))
        self.cbAutostartup.setMaximumSize(QSize(25, 25))
        self.cbAutostartup.setStyleSheet(u"/* ================= CHECKBOX ================= */\n"
"QCheckBox {\n"
"    color: #2e2a44;                 /* teks ungu gelap */\n"
"    font: 10pt \"Segoe UI\";\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"/* Kotak checkbox */\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 2px solid #9b8acb;      /* ungu medium */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* Hover */\n"
"QCheckBox::indicator:hover {\n"
"    border-color: #7b5cff;          /* ungu accent */\n"
"}\n"
"\n"
"/* Checked */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #7b5cff;      /* ungu menyala */\n"
"    border-color: #6a55d9;\n"
"}\n"
"\n"
"/* Checked + Hover */\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #8b78ff;\n"
"}\n"
"\n"
"/* Disabled */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #e3ddf5;\n"
"    border-color: #c7bddf;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #9a95b3;\n"
"}\n"
"")

        self.horizontalLayout_24.addWidget(self.cbAutostartup)

        self.titleAutostartup = QLabel(self.frame_31)
        self.titleAutostartup.setObjectName(u"titleAutostartup")
        sizePolicy1.setHeightForWidth(self.titleAutostartup.sizePolicy().hasHeightForWidth())
        self.titleAutostartup.setSizePolicy(sizePolicy1)
        self.titleAutostartup.setMinimumSize(QSize(160, 30))
        self.titleAutostartup.setMaximumSize(QSize(16777215, 30))
        self.titleAutostartup.setFont(font2)
        self.titleAutostartup.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titleAutostartup{\n"
"    color: #4e049b;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #dfd7f4; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titleAutostartup.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.titleAutostartup)


        self.verticalLayout_39.addWidget(self.frame_31)

        self.frame_30 = QFrame(self.frame_24)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(320, 0))
        self.frame_30.setMaximumSize(QSize(320, 16777215))
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 7, 0)
        self.cbAutodetect = QCheckBox(self.frame_30)
        self.cbAutodetect.setObjectName(u"cbAutodetect")
        self.cbAutodetect.setMinimumSize(QSize(25, 25))
        self.cbAutodetect.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.cbAutodetect.setStyleSheet(u"/* ================= CHECKBOX ================= */\n"
"QCheckBox {\n"
"    color: #2e2a44;                 /* teks ungu gelap */\n"
"    font: 10pt \"Segoe UI\";\n"
"    spacing: 8px;\n"
"	weight:bold;\n"
"}\n"
"\n"
"/* Kotak checkbox */\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"\n"
"    border-radius: 4px;\n"
"    border: 2px solid #9b8acb;      /* ungu medium */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* Hover */\n"
"QCheckBox::indicator:hover {\n"
"    border-color: #7b5cff;          /* ungu accent */\n"
"}\n"
"\n"
"/* Checked */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #7b5cff;      /* ungu menyala */\n"
"    border-color: #6a55d9;\n"
"}\n"
"\n"
"/* Checked + Hover */\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #8b78ff;\n"
"}\n"
"\n"
"/* Disabled */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #e3ddf5;\n"
"    border-color: #c7bddf;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #9a95b3;\n"
"}\n"
"")
        self.cbAutodetect.setChecked(False)

        self.horizontalLayout_18.addWidget(self.cbAutodetect)

        self.titleAutodetect = QLabel(self.frame_30)
        self.titleAutodetect.setObjectName(u"titleAutodetect")
        sizePolicy1.setHeightForWidth(self.titleAutodetect.sizePolicy().hasHeightForWidth())
        self.titleAutodetect.setSizePolicy(sizePolicy1)
        self.titleAutodetect.setMinimumSize(QSize(295, 30))
        self.titleAutodetect.setMaximumSize(QSize(16777215, 30))
        self.titleAutodetect.setFont(font2)
        self.titleAutodetect.setStyleSheet(u"\n"
"/* App Title (KeyBloom) */\n"
"#titleAutodetect{\n"
"    color: #4e049b;      \n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    background-color: #dfd7f4; /* ungu menyala lembut */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"")
        self.titleAutodetect.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.titleAutodetect)


        self.verticalLayout_39.addWidget(self.frame_30)

        self.btn_savesettings = QPushButton(self.frame_24)
        self.btn_savesettings.setObjectName(u"btn_savesettings")
        self.btn_savesettings.setMinimumSize(QSize(0, 0))
        self.btn_savesettings.setMaximumSize(QSize(16777215, 16777215))
        self.btn_savesettings.setStyleSheet(u"QPushButton {\n"
"    background-color: #58B368;       /* hijau lembut tapi hidup */\n"
"    border: 1.5px solid #4A9A59;     /* diperkecil dari 2px */\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    padding: 4px 10px;               /* lebih ramping, teks tetap lega */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #68C179;\n"
"    border: 1.5px solid #3E874D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4C9957;\n"
"    border: 1.5px solid #3A7A44;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A7D9B0;\n"
"    color: #EAF6EC;\n"
"    border: 1.5px solid #8BC59A;\n"
"}\n"
"")

        self.verticalLayout_39.addWidget(self.btn_savesettings)


        self.horizontalLayout_25.addWidget(self.frame_24)


        self.verticalLayout_40.addLayout(self.horizontalLayout_25)

        self.stackedWidget.addWidget(self.pageSettings)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.contentFrame)

        self.bottomBar = QFrame(self.bgApp)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 15))
        self.bottomBar.setMaximumSize(QSize(16777215, 15))
        font3 = QFont()
        font3.setPointSize(9)
        self.bottomBar.setFont(font3)
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 0, 3)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)

        self.version.raise_()
        self.frame_size_grip.raise_()
        self.creditsLabel.raise_()

        self.verticalLayout.addWidget(self.bottomBar)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clockInfo.setText(QCoreApplication.translate("MainWindow", u"Friday, 22 August 2025 | 18:22:25", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"KeyBloom", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_profile1.setText(QCoreApplication.translate("MainWindow", u"Profile 1", None))
        self.btn_profile2.setText(QCoreApplication.translate("MainWindow", u"Profile 2", None))
        self.btn_profile3.setText(QCoreApplication.translate("MainWindow", u"Profile 3", None))
        self.btn_profile4.setText(QCoreApplication.translate("MainWindow", u"Profile 4", None))
        self.btn_profile5.setText(QCoreApplication.translate("MainWindow", u"Profile 5", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.titlepage1.setText(QCoreApplication.translate("MainWindow", u"Custom Title #1", None))
        self.btn_saveload1.setText(QCoreApplication.translate("MainWindow", u"Save and Load", None))
        self.titlepage2.setText(QCoreApplication.translate("MainWindow", u"Custom Title #2", None))
        self.btn_saveload2.setText(QCoreApplication.translate("MainWindow", u"Save and Load", None))
        self.titlepage3.setText(QCoreApplication.translate("MainWindow", u"Custom Title #3", None))
        self.btn_saveload3.setText(QCoreApplication.translate("MainWindow", u"Save and Load", None))
        self.titlepage4.setText(QCoreApplication.translate("MainWindow", u"Custom Title #4", None))
        self.btn_saveload4.setText(QCoreApplication.translate("MainWindow", u"Save and Load", None))
        self.titlepage5.setText(QCoreApplication.translate("MainWindow", u"Custom Title #5", None))
        self.btn_saveload5.setText(QCoreApplication.translate("MainWindow", u"Save and Load", None))
        self.titlepage6.setText(QCoreApplication.translate("MainWindow", u"All Settings", None))
        self.titlecustom1.setText(QCoreApplication.translate("MainWindow", u"Profile Name 1", None))
        self.titlecustom2.setText(QCoreApplication.translate("MainWindow", u"Profile Name 2", None))
        self.titlecustom3.setText(QCoreApplication.translate("MainWindow", u"Profile Name 3", None))
        self.titlecustom4.setText(QCoreApplication.translate("MainWindow", u"Profile Name 4", None))
        self.titlecustom5.setText(QCoreApplication.translate("MainWindow", u"Profile Name 5", None))
        self.titleinputCOM.setText(QCoreApplication.translate("MainWindow", u"Input COM (Optional)", None))
        self.cbAutostartup.setText("")
        self.titleAutostartup.setText(QCoreApplication.translate("MainWindow", u"Auto Start Up KeyBloom (Recommended)", None))
        self.cbAutodetect.setText("")
        self.titleAutodetect.setText(QCoreApplication.translate("MainWindow", u"Auto Detect KeyBloom (Recommended)", None))
        self.btn_savesettings.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: SKAR - 2026", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

