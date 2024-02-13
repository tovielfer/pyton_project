import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from FileOperation import FileOperation
import datetime
import random
import sys


class SalesData:
    def __init__(self, data):
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')

    # מוחק שורות כפולות
    def eliminate_duplicates(self):
        self.data = self.data.drop_duplicates()

    # כמות לכל מוצר
    def calculate_total_sales(self):
        total_sales = self.data.groupby('Product')['Quantity'].sum()
        return total_sales

    # סכום לכל חודש
    def _calculate_total_sales_per_month(self):
        total_sales_per_month = self.data.groupby(self.data['Date'].dt.month)['Total'].sum()
        return total_sales_per_month

    #
    def _identify_best_selling_product(self):
        best_selling_product = self.calculate_total_sales().idxmax()
        return best_selling_product

    def _identify_month_with_highest_sales(self):
        month_with_highest_sales = self._calculate_total_sales_per_month().idxmax()
        return month_with_highest_sales

    def analyze_sales_data(self):
        dicti = {}
        dicti['month_with_highest_sales'] = self._identify_month_with_highest_sales()
        dicti['best_selling_product'] = self._identify_best_selling_product()
        return dicti

    def add_to_dicti_less_avg(self):
        dicti = self.analyze_sales_data()
        dicti['minimest_selling_product'] = self.calculate_total_sales().idxmin()
        dicti['average_of_the_sales_for_all_monthes'] = self._calculate_total_sales_per_month().mean()
        return dicti

    def calculate_cumulative_sales(self):
        total_sales_per_month = \
            self.data.groupby([self.data['Date'].dt.month, self.data['Date'].dt.year, self.data['Product']])[
                'Quantity'].sum()
        return total_sales_per_month

    def add_90_values_column(self):
        self.data['sale'] = self.data['Price'] * 0.9
        return self.data

    def bar_chart_category_sum(self):
        product_sales = self.data.groupby('Product')['Quantity'].sum().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Product', y='Quantity', data=product_sales)
        plt.show()

    # מחזיר ממוצע, חציון ומקסימום שני
    def calculate_mean_quantity(self):
        return np.mean(self.data['Total']), np.median(self.data['Total']), np.sort(self.data['Total'])[-2]

    def filter_by_sellings_or(self):
        sales_summary = self.data
        return sales_summary[(sales_summary['Quantity'] > 5) | (sales_summary['Quantity'] == 0)]['Product']

    def filter_by_sellings_and(self):
        sales_summary = self.data
        return sales_summary[(sales_summary['Price'] > 300) & (sales_summary['Quantity'] > 2)]

    def divide_by_2(self):
        self.data['BlackFridayPrice'] = self.data['Price'] / 2
        return self.data

    def save_modified_sales_data(self):
        analyzed_data = self.analyze_sales_data()
        df_analyzed = pd.DataFrame(analyzed_data.items(), columns=['Metric', 'Value'])
        file_operation = FileOperation()
        file_operation.save_to_csv(df_analyzed, 'analyze_sales_data.csv')

    # ============ציורים===================
    # ===========plt====================
    def plt1(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.plot(p['Date'], p['Total'])
        plt.show()

    def plt2(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.scatter(p['Date'], p['Total'])
        plt.show()

    def plt3(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.bar(p['Date'], p['Total'])
        plt.show()

    def plt4(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.hist(p['Total'])
        plt.show()

    def plt5(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.violinplot(p['Total'])
        plt.show()

    def plt6(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.fill_between(p['Date'], p['Total'])
        plt.show()

    def plt7(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.polar(p['Date'], p['Total'])
        try:
            plt.show()
        except Exception as e:
            self.error(e)

    # =============sns==================

    def drawing1(self):
        product_sales = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Date', y='Total', data=product_sales)
        try:
            plt.show()
        except Exception as e:
            self.error(e)

    def drawing2(self):
        product_sales = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.lmplot(x='Date', y='Total', data=product_sales)
        try:
            plt.show()
        except Exception as e:
            self.error(e)

    def drawing3(self):
        product_sales = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Date', y='Total', data=product_sales)
        try:
            plt.show()
        except Exception as e:
            self.error(e)

    def drawing4(self):
        product_sales = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Date', y='Total', data=product_sales)
        try:
            plt.show()
        except Exception as e:
            self.error(e)

    def drawing5(self):
        product_sales = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Date', y='Total', data=product_sales)
        try:
            plt.show()
        except Exception as e:
            self.error(e)

    # ============משימה 7===================
    # 1.
    def error(self, err):
        print("<{0},{1},{2},type error: {3}<{0}>".format("Tovi", datetime.datetime.now().strftime("%d.%m.%y"),
                                                         datetime.datetime.now().strftime("%H:%M"), err))

    # 2 נמצא בקובץ file operation

    # 3
    def random_me(self, name):
        result = []
        total_sales = self.calculate_total_sales()
        if name in total_sales.index:
            num1 = total_sales[name]
            result.append(num1)
        if name in self.data.groupby(['Product']).max('Price').index:
            num2 = self.data.groupby(['Product']).max('Price').loc[name, 'Price']
            result.append(num2)
        if num1 < num2:
            result.append(random.randint(num1, num2))
        else:
            result.append(random.randint(num2, num1))
        return result

    def version(self):
        print(sys.version)

    # 5
    def process_parameters(self, *args, **kwargs):
        dicty = {}
        for key, value in kwargs.items():
            if value is not None:
                dicty[key] = value
        for value in args:
            if isinstance(value, int):
                print(value)
        return dicty

    def print_table(self):
        print(self.data.head(3))
        print(self.data.tail(2))
        print(self.data.iloc[random.randint(0, len(self.data) - 1)])

    # 7

    def pass_table(self):
        data_array = self.data.select_dtypes(include=['number']).values
        for value in np.nditer(data_array):
            print(value)
