import unittest
from django.urls import resolve
from Gov.views import (
    mps_list,
    search_mp_by_constituency,
    senators_list,
    search_senator_by_county,
    governors_list,
    search_governor_by_county,
    mcas_list,
    search_mca_by_ward,
)

class TestUrls(unittest.TestCase):
    def test_mps_list_url_resolves(self):
        resolver = resolve('/mps/')
        self.assertEqual(resolver.func, mps_list)

    def test_search_mp_by_constituency_url_resolves(self):
        resolver = resolve('/mps/example-constituency/')
        self.assertEqual(resolver.func, search_mp_by_constituency)

    def test_senators_list_url_resolves(self):
        resolver = resolve('/senators/')
        self.assertEqual(resolver.func, senators_list)

    def test_search_senator_by_county_url_resolves(self):
        resolver = resolve('/senators/example-county/')
        self.assertEqual(resolver.func, search_senator_by_county)

    def test_governors_list_url_resolves(self):
        resolver = resolve('/governors/')
        self.assertEqual(resolver.func, governors_list)

    def test_search_governor_by_county_url_resolves(self):
        resolver = resolve('/governors/example-county/')
        self.assertEqual(resolver.func, search_governor_by_county)

    def test_mcas_list_url_resolves(self):
        resolver = resolve('/mcas/')
        self.assertEqual(resolver.func, mcas_list)

    def test_search_mca_by_ward_url_resolves(self):
        resolver = resolve('/mcas/example-ward/')
        self.assertEqual(resolver.func, search_mca_by_ward)

if __name__ == '__main__':
    unittest.main()
