import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # ✅ Test penjumlahan
    def test_tambah_positif(self):
        self.assertEqual(self.calc.tambah(2, 3), 5)

    def test_tambah_negatif(self):
        self.assertEqual(self.calc.tambah(-2, -3), -5)

    def test_tambah_campuran(self):
        self.assertEqual(self.calc.tambah(-2, 3), 1)

    # ✅ Test pengurangan
    def test_kurang(self):
        self.assertEqual(self.calc.kurang(10, 4), 6)

    # ✅ Test perkalian
    def test_kali(self):
        self.assertEqual(self.calc.kali(3, 5), 15)

    def test_kali_dengan_nol(self):
        self.assertEqual(self.calc.kali(5, 0), 0)

    # ✅ Test pembagian
    def test_bagi_biasa(self):
        self.assertAlmostEqual(self.calc.bagi(10, 2), 5)

    def test_bagi_float(self):
        self.assertAlmostEqual(self.calc.bagi(7, 2), 3.5)

    def test_bagi_negatif(self):
        self.assertAlmostEqual(self.calc.bagi(-10, 2), -5)

    # ✅ Test error
    def test_bagi_dengan_nol(self):
        with self.assertRaises(ValueError):
            self.calc.bagi(10, 0)

    # ✅ Test tipe data salah
    def test_input_bukan_angka(self):
        with self.assertRaises(TypeError):
            self.calc.tambah("a", 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)