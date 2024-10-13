import sys
from PyQt5.QtWidgets import QApplication

import DigitalClock

def main():
    app = QApplication(sys.argv)

    weather_app = DigitalClock.DigitalClock()
    weather_app.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()