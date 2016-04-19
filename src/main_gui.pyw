# -*- coding: gb18030 -*-

import os
import sys
import clean_c_file
import PyQt4.QtGui as Gui
import PyQt4.QtCore as Core

class CleanCFileDlg(Gui.QDialog):
    '''
    New class to define a simple GUI to delete specific
    files in specific directory.
    '''

    def __init__(self, parent = None):
		super(CleanCFileDlg, self).__init__(parent)

		self.__line_dir      = Gui.QLineEdit()
		self.__btn_dir       = Gui.QPushButton(u'&Specific')
		self.__browser_files = Gui.QTextBrowser()
		self.__btn_clear     = Gui.QPushButton(u'&Clear')
		self.__btn_delete    = Gui.QPushButton(u'&Delete')

		self.top_h_layout = Gui.QHBoxLayout()
		self.top_h_layout.addWidget(self.__line_dir)
		self.top_h_layout.addWidget(self.__btn_dir)

		self.down_right_layout = Gui.QVBoxLayout()
		self.down_right_layout.addStretch(2)
		self.down_right_layout.addWidget(self.__btn_clear)
		self.down_right_layout.addWidget(self.__btn_delete)

		self.down_h_layout = Gui.QHBoxLayout()
		self.down_h_layout.addWidget(self.__browser_files)
		self.down_h_layout.addLayout(self.down_right_layout)

		self.layout = Gui.QVBoxLayout()
		self.layout.addLayout(self.top_h_layout)
		self.layout.addLayout(self.down_h_layout)

		self.setLayout(self.layout)
		self.setWindowTitle(u'Clean C Files  -- Gavin.Bai')


def main():
	app = Gui.QApplication(sys.argv)
	win_gui = CleanCFileDlg()
	win_gui.show()

	app.exec_()

if __name__ == "__main__":
    main()
