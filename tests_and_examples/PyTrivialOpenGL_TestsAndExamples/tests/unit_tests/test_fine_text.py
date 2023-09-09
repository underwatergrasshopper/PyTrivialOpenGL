def test_constructor():
    from PyTrivialOpenGL.FineText import FineText, Text, TextHorizontalSpacer, ColorF, ColorB

    assert FineText().to_elements() == []

    assert FineText(Text("")).to_elements()                 == [Text("")]
    assert FineText(Text("xxx")).to_elements()              == [Text("xxx")]
    assert FineText(ColorF(1, 0, 1, 0)).to_elements()       == [ColorF(1, 0, 1, 0)]
    assert FineText(ColorB(1, 2, 3, 4)).to_elements()       == [ColorB(1, 2, 3, 4)]
    assert FineText(TextHorizontalSpacer(123)).to_elements() == [TextHorizontalSpacer(123)]

    assert FineText("").to_elements()                       == [Text("")]
    assert FineText("xxx").to_elements()                    == [Text("xxx")]
    assert FineText((1, 2, 3, 4)).to_elements()             == [ColorB(1, 2, 3, 4)]
    assert FineText(123).to_elements()                      == [TextHorizontalSpacer(123)]

    assert FineText(Text("xxx"), ColorB(1, 2, 3, 4), TextHorizontalSpacer(123)).to_elements() == [Text("xxx"), ColorB(1, 2, 3, 4), TextHorizontalSpacer(123)]
    assert FineText("xxx", (1, 2, 3, 4), 123).to_elements() == [Text("xxx"), ColorB(1, 2, 3, 4), TextHorizontalSpacer(123)]

    class SomethingElse:
        pass

    try:
        fine_text = FineText(SomethingElse())
    except Exception as e:
        assert str(e) == "At 0 element from 'elements'. Unexpected type."
