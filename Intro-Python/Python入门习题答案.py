##请在本页面（或者下载至本地后用文本编辑器打开的页面）使用Ctrl + F搜索习题标题，以便快速定位答案

#平均电费
print((23 + 32 + 64)/3)


#计算和格式
# Fill this in with an expression that calculates how many tiles are needed.
print(9*7 + 5*7)

# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7 + 5*7))


#里约热内卢或旧金山哪个人口更密集？
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# 修复引号
# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."


#编写服务器日志信息
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message incorporating the strings above.
# The message should be use the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)


#len
given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name_length = len(given_name + middle_names + family_name) + 2

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)


#销售总额
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


#使用字符串格式化简化代码
city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

#todo rewrite this line to use the format method rather than string concatenation
alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city,
                                                                                                              low_temperature,
                                                                                                              high_temperature,
                                                                                                              temperature_unit,
                                                                                                              weather_conditions)
# print the alert
print(alert)


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


#前三名
def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    return sorted(input_list, reverse=True)[:3]


#列表的总和
def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for elem in input_list:
        sum += elem
    return sum

#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))


#XML标签计数器
"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and end with a right angle bracket ">".
"""
#TODO: Define the tag_count function
def tag_count(tokens):
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))


#创建HTML列表
#define the  html_list function
#define the  html_list function
def html_list(list_items):
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string

list1 = ['first string','second string']
html_list(list1)


#最大平方数
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2


##断开字符串
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(len(news_ticker))

#重构代码
def check_answer(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers(my_answers,answers):
    #Checks the five answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass."

#用户（按国家/地区）
from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country not in country_counts:
        country_counts[country] = 1
    else:
        country_counts[country] += 1


#多产的一年
def most_prolific(discs):
#We will store a dictionary of years
#and number of albums per year
    years = {}
    maxyears = []
    maxnumber = 0
    for disc in discs:
        year = discs[disc]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

#find the year in which the maximum
#number of albums was published
#there are more elegant ways of accomplishing this,
#but the code below works
    for year in years:
        if years[year] > maxnumber:
            maxyears=[]
            maxyears.append(year)
            maxnumber = years[year]
        elif years[year] == maxnumber and not (year in maxyears):
            maxyears.append(year)
    if (len(maxyears) == 1):
        return maxyears[0]
    else:
        return maxyears


#在嵌套字典肿添加值
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True


#飞行马戏团记录
monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}
def total_takings(yearly_record):
    #total is used to sum up the monthly takings
    total = 0
    for month in yearly_record.keys():
        #I use the Python function sum to sum up over
        #all the elements in a list
        total = total + sum(yearly_record[month])
    return total


#天和小时
def hours2days(input_hours):
    days = input_hours // 24
    hours = input_hours % 24
    return days, hours


#默认参数
def print_list(l, numbered = False, bullet_character = '-'):
    """Prints a list on multiple lines, with numbers or bullets

    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))


#找到最大公因子
# TODO: print e to the power of 3 using the math module
import math
print(math.exp(3))


#将链接添加到文章链
def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        article_chain.append(first_link)
        # add the first link to article chain
        # delay for about two seconds


#稍等片刻！
#TODO: import something?
import time

while continue_crawl(article_chain, target_url):
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
