import unittest
from util import validate_reference, UserInputError
from entities.article import Article
from entities.book import Book


class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_length_does_not_raise_error(self):
        validate_reference(
            Article(
                1, "Author", "Title", "Journal", "2023", "3", "", "5000", "", "note"
            )
        )
        validate_reference(
            Article(
                1,
                ["j", "j"],
                "h" * 100,
                "m" * 100,
                "2023",
                "3",
                "7",
                "5000",
                "4",
                "note" * 49,
            )
        )

    def test_too_short_or_long_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(1, "", "Title", "Journal", "2023",
                        "3", "", "5000", "", "note")
            )
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "koodaa" * 201,
                    "Title",
                    "Journal",
                    "2023",
                    "3",
                    "",
                    "5000",
                    "",
                    "note" * 45,
                )
            )

    def test_year_too_much_or_str_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "200000",
                    "3",
                    "",
                    "5000",
                    "",
                    "note",
                )
            )
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "testi",
                    "3",
                    "",
                    "5000",
                    "",
                    "note",
                )
            )

    def test_vol_too_much_or_str_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "2023",
                    "3000000000",
                    "",
                    "5000",
                    "",
                    "note",
                )
            )
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "2023",
                    "testi",
                    "",
                    "5000",
                    "",
                    "note",
                )
            )

    def test_number_too_much_or_str_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "2023",
                    "3",
                    "40000000000",
                    "5000",
                    "",
                    "note",
                )
            )
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "2023",
                    "3",
                    "testi",
                    "5000",
                    "",
                    "note",
                )
            )

    def test_month_too_much_or_str_raises_error(self):
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "2023",
                    "3",
                    "",
                    "5000",
                    "13",
                    "note",
                )
            )
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    "Author",
                    "Title",
                    "Journal",
                    "2023",
                    "3",
                    "",
                    "5000",
                    "testi",
                    "note",
                )
            )

    def test_too_many_authors(self):
        with self.assertRaises(UserInputError):
            validate_reference(
                Article(
                    1,
                    [f"author{author}" for author in range(22)],
                    "Title",
                    "Journal",
                    "2023",
                    "3",
                    "",
                    "5000",
                    "12",
                    "note",
                )
            )
