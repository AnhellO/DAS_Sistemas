from visitor import Dot, Circle, Rectangle
from visitor import XMLExportVisitor, JSONExportVisitor, YAMLExportVisitor

if __name__ == '__main__':
    dot = Dot('Dot', 2, 3)
    circle = Circle('Circle', 1, 2, 5)
    rectangle = Rectangle('Rectangle', 2, 9, 4, 1)

    visitor = XMLExportVisitor()
    dot_xml = dot.accept(visitor)
    circle_xml = circle.accept(visitor)
    rectangle_xml = rectangle.accept(visitor)
    print(dot_xml)
    print(circle_xml)
    print(rectangle_xml)

    visitor = JSONExportVisitor()
    dot_json = dot.accept(visitor)
    circle_json = circle.accept(visitor)
    rectangle_json = rectangle.accept(visitor)
    print(dot_json)
    print(circle_json)
    print(rectangle_json)

    visitor = YAMLExportVisitor()
    dot_yaml = dot.accept(visitor)
    circle_yaml = circle.accept(visitor)
    rectangle_yaml = rectangle.accept(visitor)
    print(dot_yaml)
    print(circle_yaml)
    print(rectangle_yaml)
