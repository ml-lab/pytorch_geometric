from unittest import TestCase

from .spline_conv import repeat_to, SplineConv


class SplineConvTest(TestCase):
    def test_repeat_to(self):
        output = repeat_to(2, 5)
        self.assertEqual(output, [2, 2, 2, 2, 2])

        output = repeat_to([2, 4, 3], 5)
        self.assertEqual(output, [2, 4, 3, 3, 3])

        output = repeat_to([2, 4, 3, 7, 2], 5)
        self.assertEqual(output, [2, 4, 3, 7, 2])

    def test_init(self):
        conv = SplineConv(1, 10, dim=3, kernel_size=[4, 8], degree=2)
        self.assertEqual(conv.in_features, 1)
        self.assertEqual(conv.out_features, 10)
        self.assertEqual(conv.kernel_size, [4, 8, 8])
        self.assertEqual(conv.is_open_spline, [True, True, True])
        self.assertEqual(conv.degree, 2)
        self.assertEqual(conv.weight.data.size(), (1 + 4 * 8 * 8, 1, 10))
        self.assertEqual(conv.bias.data.size(), (10, ))
        self.assertEqual(conv.__repr__(), 'SplineConv(1, 10, '
                         'kernel_size=[4, 8, 8], is_open_spline=[True, True, '
                         'True], degree=2)')

        conv = SplineConv(
            1, 10, dim=1, kernel_size=[4], is_open_spline=False, bias=False)
        self.assertEqual(conv.in_features, 1)
        self.assertEqual(conv.out_features, 10)
        self.assertEqual(conv.kernel_size, [4])
        self.assertEqual(conv.is_open_spline, [False])
        self.assertEqual(conv.degree, 1)
        self.assertEqual(conv.weight.data.size(), (1 + 4, 1, 10))
        self.assertIsNone(conv.bias)
        self.assertEqual(conv.__repr__(), 'SplineConv(1, 10, kernel_size=[4], '
                         'is_open_spline=[False], degree=1, bias=False)')
