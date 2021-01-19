import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._color_background = QColor("#393939")
        self._color_light = QColor("#2f2f2f")
        self._color_dark = QColor("#292929")
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        # 设置
        self.gridSize = 20
        self.gridSquares = 5
        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width, self.scene_height)
        self.setBackgroundBrush(self._color_background)

    def drawBackground(self, painter: QPainter, rect: QRectF) -> None:
        super().drawBackground(painter, rect)

        # 创建grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)

        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.gridSize):
            line = QLine(x, first_top, x, bottom)
            if x % (self.gridSize * self.gridSquares) == 0:
                lines_dark.append(line)
            else:
                lines_light.append(line)

        for y in range(first_top, bottom, self.gridSize):
            line = QLine(first_left, y, right, y)
            if y % (self.gridSize * self.gridSquares) == 0:
                lines_dark.append(line)
            else:
                lines_light.append(line)

        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)

        painter.setPen(self._pen_dark)
        painter.drawLines(*lines_dark)
