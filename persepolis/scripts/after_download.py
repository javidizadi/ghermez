#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

try:
    from PySide6.QtCore import QCoreApplication, QLocale, QPoint, QSettings, QSize, Qt, QTranslator
    from PySide6.QtGui import QCloseEvent, QIcon, QKeyEvent
    from PySide6.QtWidgets import QWidget
except ImportError:
    from PyQt5.QtCore import QCoreApplication, QLocale, QPoint, QSettings, QSize, Qt, QTranslator
    from PyQt5.QtGui import QCloseEvent, QIcon, QKeyEvent


import os

from persepolis.gui.after_download_ui import AfterDownloadWindow_Ui
from persepolis.scripts import osCommands
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PyQt5.QtWidgets import QWidget


class AfterDownloadWindow(AfterDownloadWindow_Ui):
    def __init__(self, parent: QWidget, download_dict: dict[str, str], persepolis_setting: QSettings) -> None:
        super().__init__(persepolis_setting)
        self.persepolis_setting = persepolis_setting
        self.dict = download_dict
        self.parent = parent

        # add support for other languages
        locale = str(self.persepolis_setting.value('settings/locale'))
        QLocale.setDefault(QLocale(locale))
        self.translator = QTranslator()
        if self.translator.load(':/translations/locales/ui_' + locale, 'ts'):
            QCoreApplication.installTranslator(self.translator)

        # connecting buttons
        self.open_pushButtun.clicked.connect(self.openFile)
        self.open_folder_pushButtun.clicked.connect(self.openFolder)
        self.ok_pushButton.clicked.connect(self.okButtonPressed)

        # labels
        # find gid
        gid = self.dict['gid']

        # get file_path from data base
        self.add_link_dict = self.parent.persepolis_db.searchGidInAddLinkTable(gid)
        file_path = self.add_link_dict['download_path']

        # save_as
        self.save_as_lineEdit.setText(file_path)
        self.save_as_lineEdit.setToolTip(file_path)

        # link
        link = str(self.dict['link'])
        self.link_lineEdit.setText(link)
        self.link_lineEdit.setToolTip(link)

        # file_name

        window_title = str(self.dict['file_name'])
        file_name = QCoreApplication.translate('after_download_src_ui_tr', '<b>File name</b>: ') + \
            window_title

        self.setWindowTitle(window_title)

        self.file_name_label.setText(file_name)

        # size
        size = QCoreApplication.translate('after_download_src_ui_tr', '<b>Size</b>: ') + str(self.dict['size'])
        self.size_label.setText(size)

        # disable link_lineEdit and save_as_lineEdit
        self.link_lineEdit.setEnabled(False)
        self.save_as_lineEdit.setEnabled(False)

        # set window size and position
        size = self.persepolis_setting.value(
            'AfterDownloadWindow/size', QSize(570, 290))
        position = self.persepolis_setting.value(
            'AfterDownloadWindow/position', QPoint(300, 300))
        self.resize(size)
        self.move(position)

    def openFile(self) -> None:
        # execute file
        file_path = self.add_link_dict['download_path']

        if os.path.isfile(file_path):
            osCommands.xdgOpen(file_path)

        # close window
        self.close()

    def openFolder(self) -> None:
        # open download folder
        download_path = self.add_link_dict['download_path']

        if os.path.isfile(download_path):
            osCommands.xdgOpen(download_path, 'folder', 'file')

        # close window
        self.close()

    def okButtonPressed(self) -> None:
        if self.dont_show_checkBox.isChecked():
            self.persepolis_setting.setValue('settings/after-dialog', 'no')
            self.persepolis_setting.sync()

        # close window
        self.close()

    # close window with ESC key
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            self.close()


    def closeEvent(self, event: QCloseEvent) -> None:
        # saving window size and position
        self.persepolis_setting.setValue(
            'AfterDownloadWindow/size', self.size())
        self.persepolis_setting.setValue(
            'AfterDownloadWindow/position', self.pos())
        self.persepolis_setting.sync()
        event.accept()

    def changeIcon(self, icons: str) -> None:
        icons = ':/' + str(icons) + '/'
        self.ok_pushButton.setIcon(QIcon(icons + 'ok'))
        self.open_folder_pushButtun.setIcon(QIcon(icons + 'folder'))
        self.open_pushButtun.setIcon(QIcon(icons + 'file'))
