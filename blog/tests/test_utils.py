from django.test import TestCase
from ..utils import Highlighter


class HighlighterTestCase(TestCase):
    def test_highlight(self):
        document = "This is a long title to test if the key word will be cut off."
        highlighter = Highlighter("Title")
        expected = 'This is a long <span class="highlighted">title</span> to test if the key word will be cut off.'
        self.assertEqual(highlighter.highlight(document), expected)

        highlighter = Highlighter("keyword highlight")
        expected = 'This is a long title to test if the <span class="highlighted">key word</span> will be cut off.'
        self.assertEqual(highlighter.highlight(document), expected)

        highlighter = Highlighter("Tile")
        document = "This is a long title over 200 words. It should be cut" + "Hello Django" * 200
        self.assertTrue(
            highlighter.highlight(document).startswith(
                '...<span class="highlighted">Title</span>，shoud be cut'
            )
        )
