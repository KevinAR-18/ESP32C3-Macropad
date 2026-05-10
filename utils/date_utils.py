from PySide6.QtCore import QCoreApplication, QDateTime
from PySide6.QtWidgets import QLabel


class Date:
    def update_time(self, label: QLabel):
        current_time = QDateTime.currentDateTime()

        time_text = current_time.toString("HH:mm")
        date_text = current_time.toString("dddd, dd MMMM yyyy")

        label.setText(
            QCoreApplication.translate(
                "MainWindow", f"{time_text} - {date_text}", None
            )
        )
