import unittest

from visitor import *


class VisitorTest(unittest.TestCase):
    def test_dot(self):
        dot = Dot('dot-1', 5, 6)
        self.assertIsInstance(dot, Shape)
        self.assertIsInstance(dot, Dot)
        self.assertEqual('dot-1', dot.id)
        self.assertEqual(5, dot.x)
        self.assertEqual(6, dot.y)

        dot.move(10, 10)
        self.assertEqual(10, dot.x)
        self.assertEqual(10, dot.y)
        self.assertEqual(
            "Dot 'dot-1' drew at coordinates -> (10, 10)", dot.draw())

    def test_circle(self):
        circle = Circle('circle-1', 2, 2, 5)
        self.assertIsInstance(circle, Shape)
        self.assertIsInstance(circle, Circle)
        self.assertEqual('circle-1', circle.id)
        self.assertEqual(2, circle.x)
        self.assertEqual(2, circle.y)
        self.assertEqual(5, circle.radius)

        circle.move(8, 4)
        self.assertEqual(8, circle.x)
        self.assertEqual(4, circle.y)
        self.assertEqual(
            "Circle 'circle-1' drew at coordinates -> (8, 4)", circle.draw())

    def test_rectangle(self):
        rectangle = Rectangle('rectangle-1', -5, -8, 4, 6)
        self.assertIsInstance(rectangle, Shape)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual('rectangle-1', rectangle.id)
        self.assertEqual(-5, rectangle.x)
        self.assertEqual(-8, rectangle.y)
        self.assertEqual(4, rectangle.width)
        self.assertEqual(6, rectangle.height)

        rectangle.move(-5, 8)
        self.assertEqual(-5, rectangle.x)
        self.assertEqual(8, rectangle.y)
        self.assertEqual(
            "Rectangle 'rectangle-1' drew at coordinates -> (-5, 8)", rectangle.draw())

    def test_xml_visitor(self):
        dot = Dot('dot-xml', 10, 6)
        circle = Circle('circle-xml', 6, 2, 3)
        rectangle = Rectangle('rectangle-xml', -5, 10, 5, 8)
        xml_visitor = XMLExportVisitor()
        self.assertEqual(
            "XML export done for: <dot-xml coordinates=(10, 6)>", xml_visitor.visit_dot(dot))
        self.assertEqual("XML export done for: <circle-xml radius=3 coordinates=(6, 2)>",
                         xml_visitor.visit_circle(circle))
        self.assertEqual("XML export done for: <rectangle-xml width=5 height=8 coordinates=(-5, 10)>",
                         xml_visitor.visit_rectangle(rectangle))

    def test_json_visitor(self):
        dot = Dot('dot-json', 10, 6)
        circle = Circle('circle-json', 6, 2, 3)
        rectangle = Rectangle('rectangle-json', -5, 10, 5, 8)
        json_visitor = JSONExportVisitor()
        self.assertEqual(
            "JSON export done for: <dot-json coordinates=(10, 6)>", json_visitor.visit_dot(dot))
        self.assertEqual("JSON export done for: <circle-json radius=3 coordinates=(6, 2)>",
                         json_visitor.visit_circle(circle))
        self.assertEqual("JSON export done for: <rectangle-json width=5 height=8 coordinates=(-5, 10)>",
                         json_visitor.visit_rectangle(rectangle))

    def test_yaml_visitor(self):
        dot = Dot('dot-yaml', 10, 6)
        circle = Circle('circle-yaml', 6, 2, 3)
        rectangle = Rectangle('rectangle-yaml', -5, 10, 5, 8)
        yaml_visitor = YAMLExportVisitor()
        self.assertEqual(
            "YAML export done for: <dot-yaml coordinates=(10, 6)>", yaml_visitor.visit_dot(dot))
        self.assertEqual("YAML export done for: <circle-yaml radius=3 coordinates=(6, 2)>",
                         yaml_visitor.visit_circle(circle))
        self.assertEqual("YAML export done for: <rectangle-yaml width=5 height=8 coordinates=(-5, 10)>",
                         yaml_visitor.visit_rectangle(rectangle))


if __name__ == "__main__":
    unittest.main()
