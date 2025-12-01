import unittest
from app import app, warehouses


class TestWebApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        warehouses.clear()

    def tearDown(self):
        warehouses.clear()

    def test_index_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ohtuvarasto', response.data)

    def test_create_warehouse(self):
        response = self.client.post('/create', data={
            'name': 'Test Warehouse',
            'capacity': '100'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Warehouse', warehouses)
        self.assertEqual(warehouses['Test Warehouse'].tilavuus, 100)

    def test_create_warehouse_invalid_capacity(self):
        response = self.client.post('/create', data={
            'name': 'Invalid Warehouse',
            'capacity': '-10'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Invalid Warehouse', warehouses)

    def test_create_warehouse_empty_name(self):
        response = self.client.post('/create', data={
            'name': '',
            'capacity': '100'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(warehouses), 0)

    def test_add_to_warehouse(self):
        self.client.post('/create', data={
            'name': 'Stock Warehouse',
            'capacity': '100'
        })

        response = self.client.post('/update/Stock Warehouse', data={
            'action': 'add',
            'amount': '50'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(warehouses['Stock Warehouse'].saldo, 50)

    def test_take_from_warehouse(self):
        self.client.post('/create', data={
            'name': 'Stock Warehouse',
            'capacity': '100'
        })
        self.client.post('/update/Stock Warehouse', data={
            'action': 'add',
            'amount': '50'
        })

        response = self.client.post('/update/Stock Warehouse', data={
            'action': 'take',
            'amount': '20'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(warehouses['Stock Warehouse'].saldo, 30)

    def test_update_nonexistent_warehouse(self):
        response = self.client.post('/update/Nonexistent', data={
            'action': 'add',
            'amount': '50'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_delete_warehouse(self):
        self.client.post('/create', data={
            'name': 'Delete Me',
            'capacity': '100'
        })

        self.assertIn('Delete Me', warehouses)

        response = self.client.post('/delete/Delete Me', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Delete Me', warehouses)

    def test_delete_nonexistent_warehouse(self):
        response = self.client.post(
            '/delete/Nonexistent',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_warehouse_displays_on_index(self):
        self.client.post('/create', data={
            'name': 'Display Test',
            'capacity': '50'
        })

        response = self.client.get('/')
        self.assertIn(b'Display Test', response.data)
        self.assertIn(b'50', response.data)
