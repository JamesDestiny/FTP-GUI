from main import *
import sys
if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = mainwid()
    ui.show()
    sys.exit(app.exec_())#系统退出