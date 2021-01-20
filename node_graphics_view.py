from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QDMGraphicsView(QGraphicsView):
    def __init__(self, grScene, parent=None):
        super().__init__(parent)
        self.grScene = grScene
        self.init_ui()
        self.setScene(self.grScene)

        self.zoomInFactor = 1.25
        self.zoom = 10
        self.zoomStep = 1
        self.zoomRange = [0, 10]
        self.zoomClamp = True

    def init_ui(self):
        self.setRenderHints(QPainter.Antialiasing
                            | QPainter.HighQualityAntialiasing
                            | QPainter.TextAntialiasing
                            | QPainter.SmoothPixmapTransform)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def leftMouseButtonPress(self, event: QMouseEvent):
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(), Qt.LeftButton,
                                   Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton,
                                event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)

    def leftMouseButtonRelease(self, event: QMouseEvent):
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton,
                                event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)
        self.setDragMode(QGraphicsView.NoDrag)

    def rightMouseButtonPress(self, event: QMouseEvent):
        print("RM Press")

    def rightMouseButtonRelease(self, event: QMouseEvent):
        print("RM Release")

    def middleMouseButtonPress(self, event: QMouseEvent):
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(), Qt.LeftButton,
                                   Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton,
                                event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event: QMouseEvent):
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton,
                                event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)
        self.setDragMode(QGraphicsView.NoDrag)

    def wheelEvent(self, event: QWheelEvent) -> None:
        zoomOutFactor = 1 / self.zoomInFactor

        if event.angleDelta().y() > 0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep
        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep
        self.zoomClamp = False
        if self.zoom < self.zoomRange[0]:
            self.zoom = self.zoomRange[0]
            self.zoomClamp = True
        if self.zoom > self.zoomRange[1]:
            self.zoom = self.zoomRange[1]
            self.zoomClamp = True

        if not self.zoomClamp:
            self.scale(zoomFactor, zoomFactor)
