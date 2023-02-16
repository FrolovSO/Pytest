from triangle.triangle import Triangle
import pytest


class TestTriangleUnitToPtest:

    def test_triangle_perimetr(self):
        first = Triangle(7, 8, 9)
        assert first.perimetr() == 24

    def test_square(self, square_value_triangle):
        second = square_value_triangle
        assert second.square() == 10.825317547305483

    @pytest.mark.parametrize("a, b, c",
                             [(7, 8, 9), (9, 7, 8)])
    @pytest.mark.parametrize("q, w, e",
                             [(7, 8, 9)])
    def test_triangle_eq(self, a, b, c, q, w, e):
        first = Triangle(a, b, c)
        second = Triangle(q, w, e)
        assert first == second

    def test_triangle_ne(self):
        first = Triangle(7, 8, 9)
        second = Triangle(6, 9, 8)
        assert first != second

    def test_triangle_lt(self):
        first = Triangle(7, 8, 9)
        second = Triangle(8, 9, 10)
        assert second > first

    def test_triangle_gt(self):
        first = Triangle(7, 8, 9)
        second = Triangle(8, 9, 10)
        assert first < second

    def test_triangle_le(self):
        first = Triangle(7, 8, 9)
        second = Triangle(8, 9, 10)
        assert first <= second

    def test_triangle_ge(self):
        first = Triangle(7, 8, 9)
        second = Triangle(8, 9, 10)
        assert second >= first

    def test_triangle_equal_to_other(self):
        first = Triangle(7, 8, 9)
        second = Triangle(18, 16, 14)
        assert first.equal(second)

    def test_is_right_angled(self):
        second = Triangle(3, 4, 5)
        assert second.is_right_angled()

    def test_is_right_triangle(self):
        second = Triangle(5, 5, 5)
        assert second.is_right_triangle()

    def test_two_sides_eq(self):
        second = Triangle(4, 4, 5)
        assert second.two_sides_eq()
