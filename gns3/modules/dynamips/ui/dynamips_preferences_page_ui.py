# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/moores/dev/gns3-gui/gns3/modules/dynamips/ui/dynamips_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DynamipsPreferencesPageWidget(object):
    def setupUi(self, DynamipsPreferencesPageWidget):
        DynamipsPreferencesPageWidget.setObjectName("DynamipsPreferencesPageWidget")
        DynamipsPreferencesPageWidget.resize(435, 242)
        self.vboxlayout = QtWidgets.QVBoxLayout(DynamipsPreferencesPageWidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.uiTabWidget = QtWidgets.QTabWidget(DynamipsPreferencesPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.uiGeneralSettingsTabWidget = QtWidgets.QWidget()
        self.uiGeneralSettingsTabWidget.setObjectName("uiGeneralSettingsTabWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiGeneralSettingsTabWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiDynamipsPathLabel = QtWidgets.QLabel(self.uiGeneralSettingsTabWidget)
        self.uiDynamipsPathLabel.setObjectName("uiDynamipsPathLabel")
        self.verticalLayout_2.addWidget(self.uiDynamipsPathLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiDynamipsPathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDynamipsPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiDynamipsPathLineEdit.setSizePolicy(sizePolicy)
        self.uiDynamipsPathLineEdit.setObjectName("uiDynamipsPathLineEdit")
        self.horizontalLayout.addWidget(self.uiDynamipsPathLineEdit)
        self.uiDynamipsPathToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsTabWidget)
        self.uiDynamipsPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiDynamipsPathToolButton.setObjectName("uiDynamipsPathToolButton")
        self.horizontalLayout.addWidget(self.uiDynamipsPathToolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.uiAllocateAuxConsolePortsCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsTabWidget)
        self.uiAllocateAuxConsolePortsCheckBox.setObjectName("uiAllocateAuxConsolePortsCheckBox")
        self.verticalLayout_2.addWidget(self.uiAllocateAuxConsolePortsCheckBox)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.uiTabWidget.addTab(self.uiGeneralSettingsTabWidget, "")
        self.uiAdvancedSettingsTabWidget = QtWidgets.QWidget()
        self.uiAdvancedSettingsTabWidget.setObjectName("uiAdvancedSettingsTabWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiAdvancedSettingsTabWidget)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiMemoryUsageOptimisationGroupBox = QtWidgets.QGroupBox(self.uiAdvancedSettingsTabWidget)
        self.uiMemoryUsageOptimisationGroupBox.setObjectName("uiMemoryUsageOptimisationGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiMemoryUsageOptimisationGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiGhostIOSSupportCheckBox = QtWidgets.QCheckBox(self.uiMemoryUsageOptimisationGroupBox)
        self.uiGhostIOSSupportCheckBox.setChecked(True)
        self.uiGhostIOSSupportCheckBox.setObjectName("uiGhostIOSSupportCheckBox")
        self.verticalLayout.addWidget(self.uiGhostIOSSupportCheckBox)
        self.uiMmapSupportCheckBox = QtWidgets.QCheckBox(self.uiMemoryUsageOptimisationGroupBox)
        self.uiMmapSupportCheckBox.setChecked(True)
        self.uiMmapSupportCheckBox.setObjectName("uiMmapSupportCheckBox")
        self.verticalLayout.addWidget(self.uiMmapSupportCheckBox)
        self.uiSparseMemorySupportCheckBox = QtWidgets.QCheckBox(self.uiMemoryUsageOptimisationGroupBox)
        self.uiSparseMemorySupportCheckBox.setChecked(False)
        self.uiSparseMemorySupportCheckBox.setObjectName("uiSparseMemorySupportCheckBox")
        self.verticalLayout.addWidget(self.uiSparseMemorySupportCheckBox)
        self.verticalLayout_3.addWidget(self.uiMemoryUsageOptimisationGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.uiTabWidget.addTab(self.uiAdvancedSettingsTabWidget, "")
        self.vboxlayout.addWidget(self.uiTabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(DynamipsPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.vboxlayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DynamipsPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DynamipsPreferencesPageWidget)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiDynamipsPathLineEdit, self.uiDynamipsPathToolButton)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiDynamipsPathToolButton, self.uiGhostIOSSupportCheckBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiGhostIOSSupportCheckBox, self.uiMmapSupportCheckBox)
        DynamipsPreferencesPageWidget.setTabOrder(self.uiMmapSupportCheckBox, self.uiSparseMemorySupportCheckBox)

    def retranslateUi(self, DynamipsPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        DynamipsPreferencesPageWidget.setWindowTitle(_translate("DynamipsPreferencesPageWidget", "Dynamips"))
        self.uiDynamipsPathLabel.setText(_translate("DynamipsPreferencesPageWidget", "Path to Dynamips:"))
        self.uiDynamipsPathToolButton.setText(_translate("DynamipsPreferencesPageWidget", "&Browse..."))
        self.uiAllocateAuxConsolePortsCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Allocate AUX console ports"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiGeneralSettingsTabWidget), _translate("DynamipsPreferencesPageWidget", "General settings"))
        self.uiMemoryUsageOptimisationGroupBox.setTitle(_translate("DynamipsPreferencesPageWidget", "Memory usage optimisation"))
        self.uiGhostIOSSupportCheckBox.setToolTip(_translate("DynamipsPreferencesPageWidget", "The ghost IOS feature is a solution that helps to decrease memory usage by sharing an IOS image between different router instances."))
        self.uiGhostIOSSupportCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Enable ghost IOS support"))
        self.uiMmapSupportCheckBox.setToolTip(_translate("DynamipsPreferencesPageWidget", "The mmap feature tells Dynamips to use disk files instead of real memory for router instances."))
        self.uiMmapSupportCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Enable mmap support"))
        self.uiSparseMemorySupportCheckBox.setToolTip(_translate("DynamipsPreferencesPageWidget", "The sparse memory feature reduces the amount of virtual memory used by router instances."))
        self.uiSparseMemorySupportCheckBox.setText(_translate("DynamipsPreferencesPageWidget", "Enable sparse memory support"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiAdvancedSettingsTabWidget), _translate("DynamipsPreferencesPageWidget", "Advanced settings"))
        self.uiRestoreDefaultsPushButton.setText(_translate("DynamipsPreferencesPageWidget", "Restore defaults"))

