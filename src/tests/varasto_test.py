import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_invalid_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_invalid_otto_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_otto_yli_saldon_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_negatiivinen_tilavuus_nollaa_tilavuuden(self):
        negatiivinen_varasto = Varasto(-5)

        self.assertAlmostEqual(negatiivinen_varasto.tilavuus, 0)

    def test_konstruktori_negatiivinen_alku_saldo_nollaa_saldon(self):
        negatiivinen_varasto = Varasto(10, -3)

        self.assertAlmostEqual(negatiivinen_varasto.saldo, 0)

    def test_konstruktori_alku_saldo_suurempi_kuin_tilavuus_tayttaa_varaston(self):
        varasto = Varasto(10, 15)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_str_metodi_toimii_oikein(self):
        # Tyhjä varasto
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

        # Varasto johon lisätty tavaraa
        self.varasto.lisaa_varastoon(3)
        self.assertEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")

        # Täysi varasto
        self.varasto.lisaa_varastoon(7)
        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")
