import config
from src.DataAccessObjects.InvoiceDao import InvoiceDao
import csv
from src.DataObjects.Invoice import Invoice
from src.DataObjects.Employee import Employee
from src.DataObjects.Customer import Customer
import unittest


class InvoiceDaoTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.FILE_PATH = config.TEST_DATA_PATH + 'invoices_data_testing.csv'
        cls.invoice_dao = InvoiceDao(is_testing=True)

    def read_file(self):
        with open(self.FILE_PATH) as data_file:
            return list(csv.DictReader(data_file))

    def test_create_invoice(self):
        invoices = self.read_file()
        for invoice in invoices:
            invoice['products'] = invoice['products'].split('|')
        print('Invoices testing data: ', invoices)
        for invoice in invoices:
            new_invoice = self.invoice_dao.create_invoice(Invoice(serial_number=invoice['serial_number'],
                                                          date=invoice['date'],
                                                          employee=Employee(id=invoice['employee_id']),
                                                          customer=Customer(id=invoice['customer_id']),
                                                          products=invoice['products']))
            print('New invoice: ', new_invoice)
            self.assertFalse(new_invoice is None)
            self.assertGreater(new_invoice, 0)

    def test_get_invoice_by_serial_number(self):
        self.invoice_dao = InvoiceDao()
        serial_number = '231564897222'
        invoice_date = '2022-02-08'
        conditions = [
            {
                'column': 'serial_number',
                'value': '231564897222',
                'operator': '=',
                'options': '',
                'logic': '',
            }
        ]
        invoice = self.invoice_dao.get_invoices(conditions=conditions)[0]
        self.assertTrue(isinstance(invoice, Invoice))
        self.assertEqual(invoice.get_serial_number(), serial_number)
        self.assertEqual(invoice.get_date(), invoice_date)

    def test_get_invoice_by_date(self):
        from_date = '2022-01-01'
        to_date = '2022-02-08'
        conditions = [
            {
                'column': "date",
                'value': f"{from_date}",
                'operator': '>',
                'options': '',
                'logic': '',
                'parameter': 'from_date'
            },
            {
                'column': "date",
                'value': f"{to_date}",
                'operator': '<',
                'options': '',
                'logic': 'AND',
                'parameter': 'to_date'
            }
        ]
        [self.assertTrue(invoice.get_date() > from_date and invoice.get_date() < to_date) for invoice in self.invoice_dao.get_invoices(conditions=conditions)]

    def test_get_invoices_by_serial_number_and_date(self):
        from_date = '2022-01-01'
        to_date = '2022-02-08'
        serial_number = '231564897221'
        conditions = [
            {
                'column': 'serial_number',
                'value': str(serial_number),
                'operator': '=',
                'options': '',
                'logic': ''
            },
            {
                'column': "date",
                'value': f"{from_date}",
                'operator': '>',
                'options': '',
                'logic': 'AND',
                'parameter': 'from_date'
            },
            {
                'column': "date",
                'value': f"{to_date}",
                'operator': '<',
                'options': '',
                'logic': 'AND',
                'parameter': 'to_date'
            }

        ]
        invoices = self.invoice_dao.get_invoices(conditions=conditions)
        self.assertEqual(len(invoices), 1)
        self.assertTrue(isinstance(invoices[0], Invoice))
        self.assertEqual(invoices[0].get_serial_number(), serial_number)
        self.assertTrue(invoices[0].get_date() > from_date and invoices[0].get_date() < to_date)
        print('Invoice date: ', invoices[0].get_date())
        print('Invoice serial number: ', invoices[0].get_serial_number())

    def test_get_invoices_data_frame(self):
        print(self.invoice_dao.get_invoices_dataframe())




if __name__ == '__main__':
    unittest.main()


