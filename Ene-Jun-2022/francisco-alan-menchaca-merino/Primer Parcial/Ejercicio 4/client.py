from visitor import Dot, Circle, Rectangle
from visitor import XMLExportVisitor as XMLExport
from visitor import JSONExportVisitor as JSONExport
from visitor import YAMLExportVisitor as YAMLExport

if __name__ == '__main__':
    figures = [
        Dot('dot-1', 5, 6),
        Circle('circle-1', 2, 2, 5),
        Rectangle('rectangle-1', -5, -8, 4, 6)
    ]

    visitor = XMLExport()
    for figure in figures:
        figure_xml = figure.accept(visitor)
        print(figure_xml)

    print("")
    visitor = JSONExport()
    for figure in figures:
        figure_xml = figure.accept(visitor)
        print(figure_xml)

    print("")
    visitor = YAMLExport()
    for figure in figures:
        figure_xml = figure.accept(visitor)
        print(figure_xml)
