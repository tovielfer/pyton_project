from FileOperation import FileOperation
from SalesData import SalesData


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
fileOperation = FileOperation()
sales = SalesData(fileOperation.read_csv("YafeNof.csv"))

print(sales.add_90_values_column())
sales.bar_chart_category_sum()
print(sales.calculate_mean_quantity())
print(sales.filter_by_sellings_or())
print(sales.filter_by_sellings_and())
sales.save_modified_sales_data()
# sales.plt1()
# sales.plt2()
# sales.plt3()
# sales.plt4()
# sales.plt5()
# sales.plt6()
# sales.plt7()
# sales.drawing1()
# sales.drawing2()
# sales.drawing3()
# sales.drawing4()
# sales.drawing5()
fileOperation.read_file("lll")
print(sales.random_me("Sidur"))
sales.version()
print(sales.process_parameters("ee", 1, 78, kkk="jj", hh=7))
sales.print_table()
sales.pass_table()