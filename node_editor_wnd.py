from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from node_graphics_scene import QDMGraphicsScene
from node_graphics_view import QDMGraphicsView


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(800,600,1280,720)

        # 创建画布
        self.grScene = QDMGraphicsScene()
        self.view = QDMGraphicsView(self.grScene,self)


        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(5,5,5,5)
        box_layout.addWidget(self.view)
        self.setLayout(box_layout)
        self.setWindowTitle("Node Editor")
        self.show()

        self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addEllipse(0,0,100,100,outlinePen,greenBrush)
        rect.setFlag(QGraphicsRectItem.ItemIsMovable)
