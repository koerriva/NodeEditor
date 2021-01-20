from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from node_graphics_view import QDMGraphicsView
from node_node import Node
from node_scene import Scene


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 600, 1280, 720)

        # 创建画布
        self.scene = Scene()
        # self.grScene = self.scene.grScene
        self.view = QDMGraphicsView(self.scene.grScene, self)

        node = Node(self.scene,"My First Node")

        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(5, 5, 5, 5)
        box_layout.addWidget(self.view)
        self.setLayout(box_layout)
        self.setWindowTitle("Node Editor")
        self.show()

        # self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addEllipse(0, 0, 100, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsRectItem.ItemIsMovable)
