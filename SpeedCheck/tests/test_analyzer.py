import unittest
from analyzer import (
    calculate_average_ping,
    calculate_jitter,
    calculate_packet_loss,
    classify_quality
)


class AnalyzerTests(unittest.TestCase):

    def test_average_ping(self):
        self.assertEqual(calculate_average_ping([10, 20, 30]), 20)

    def test_jitter(self):
        # Diferencias: 10 y 10; media = 10.
        self.assertEqual(calculate_jitter([10, 20, 30]), 10)

    def test_packet_loss(self):
        self.assertEqual(calculate_packet_loss(10, 8), 20)

    def test_excellent_quality(self):
        self.assertEqual(classify_quality(20, 2, 0), "Excelente")


if __name__ == "__main__":
    unittest.main()
