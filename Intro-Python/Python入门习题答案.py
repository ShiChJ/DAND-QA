##请在本页面（或者下载至本地后用文本编辑器打开的页面）使用Ctrl + F搜索习题标题，以便快速定位答案

#平均电费
print((23 + 32 + 64)/3)


#计算
# Fill this in with an expression that calculates how many tiles are needed.
print(9*7 + 5*7)

# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7 + 5*7))


#哪个地区人口密度更高？里约还是旧金山？
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# 修正引言
# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."


#总销量
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write several lines of code before the print statement.
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convert the type back!!
print("This week's total sales: " + weekly_sales)


#列表索引
def how_many_days(month_number):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]

# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))


#列表切片
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


#在嵌套字典中添加值
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
