# view/ExcelDrop_view.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ExcelDropView(QWidget):
    def __init__(self):
        super().__init__() # 중요: QWidget 초기화
        self.file_path = None
        self.controller = None # 나중에 연결용
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Excel Import')
        self.resize(400, 200)
        self.setAcceptDrops(True)  # 드롭 허용

        self.layout = QVBoxLayout()
        self.label = QLabel('Arrastre el archivo de Excel aquí', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("border: 2px dashed #aaa; border-radius: 10px; font-size: 15px;")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # 드롭된 파일의 경로 추출
        urls = event.mimeData().urls()
        if urls:
            self.file_path = urls[0].toLocalFile()
            if self.file_path.endswith(('.xlsx', '.xls')):
                self.label.setText(f"Seleccionado: {self.file_path.split('/')[-1]}")
                # 컨트롤러가 연결되어 있다면 실행
                if self.controller:
                    self.controller.handle_excel_import()
            else:
                self.label.setText("Solo se permiten archivos de Excel (.xlsx, .xls).")