import xlrd

from utils.search_data import SearchHotelsData
from utils.search_data import SearchFlightsData

class ReadExcel:

    @staticmethod
    def get_hotels_data():
        wb = xlrd.open_workbook("../utils/test_data.xls")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchHotelsData(sheet.cell(i, 0).value, sheet.cell(i, 1).value, sheet.cell(i, 2).value,
                                          sheet.cell(i, 3).value, sheet.cell(i, 4).value)
            data.append(search_data)
        return data

    @staticmethod
    def get_flights_data():
        wb = xlrd.open_workbook("../utils/test_data.xls")
        sheet = wb.sheet_by_index(1)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchFlightsData(sheet.cell(i, 0).value, sheet.cell(i, 1).value)
            data.append(search_data)
        return data
