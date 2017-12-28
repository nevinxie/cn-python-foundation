"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

number_received_call = set()
number_sent_or_received_text = set()
number_make_call_out = set()
suspected_tele_marketer = set()

for text in texts:
	number_sent_or_received_text.add(text[0])
	number_sent_or_received_text.add(text[1]) 

for call in calls:
	number_make_call_out.add(call[0])
	number_received_call.add(call[1])

for number in number_make_call_out:
	if (number not in number_received_call
		and number not in number_sent_or_received_text):
		suspected_tele_marketer.add(number)

sorted_suspected_tele_marketer = list(suspected_tele_marketer)
sorted_suspected_tele_marketer.sort()

print("These numbers could be telemarketers: ")
for number in sorted_suspected_tele_marketer:
	print(number)
