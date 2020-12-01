import pytest

from decorator import NormalTextComponent, HighlightTextDecorator, ItalicTextDecorator, UnderlineTextDecorator

@pytest.mark.parametrize("input, expected", [
    (
        "Texto normal",
        "Texto normal"
    )
])
def test_default(input, expected):
    obj = NormalTextComponent(input)
    assert expected == obj.render()

@pytest.mark.parametrize("input, expected", [
    (
        "Texto resaltado",
        "<b>Texto resaltado</b>"
    )
])
def test_decorated(input, expected):
    obj = HighlightTextDecorator(NormalTextComponent('Texto resaltado'))
    assert expected == obj.render()

@pytest.mark.parametrize("input, expected", [
    (
        "Texto normal",
        "<b><u>Texto resaltado y subrayado</u></b>"
    )
])
def test_more_than_one_decorator(input, expected):
    obj = HighlightTextDecorator(UnderlineTextDecorator(NormalTextComponent('Texto resaltado y subrayado')))
    assert expected == obj.render()

@pytest.mark.parametrize("input, expected", [
    (
        "Texto normal",
        "<b><i><u>Texto resaltado y subrayado</u></i></b>"
    )
])
def test_all_decorators(input, expected):
    obj = HighlightTextDecorator(ItalicTextDecorator(UnderlineTextDecorator(NormalTextComponent('Texto resaltado y subrayado'))))
    assert expected == obj.render()