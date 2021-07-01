'''
程序思想：
有两个本地语音库，美音库Speech_US，英音库Speech_US
调用有道api，获取语音MP3，存入对应的语音库中
'''

import os


'''
将解析出的单词写成有道云词典的xml

'''
sigma = "sigma-95"
filename = "Learning Python-" + sigma

def word_convert_xml(word_list,xml_name):
    xml_file = open(xml_name,'w');
    xml_file.write('<wordbook>') #xml起始位置
    for word in word_list:
        xml_file.write('<item>')
        xml_file.write('    <word>' + word + '</word>\n')
        xml_file.write('    <trans>' + '<![CDATA[]]>' +  '</trans>\n')
        xml_file.write('    <tags>'+ filename +'</tags>\n') #reading是你单词本的名字，你可以改成自己的
        xml_file.write('    <progress>1</progress>\n')
        xml_file.write('</item>')
    xml_file.write('</wordbook>')#xml结束位置
# word_convert_xml(test_list,'d1.xml');
# print("单词个数:",len(test_list));

# learning_python_filename = '2013_Learning Python 5th Ed - antconc_results.txt'
learning_python_filename = sigma + ".txt"
test_list = []

with open(learning_python_filename, 'r') as txt_file:
    data_lists = txt_file.readlines()
    print(len(data_lists))
    for data in data_lists:
        # words = data.split('\t')
        # print(data)
        test_list.append(data)
    word_convert_xml(test_list, filename + ".xml")
    print("单词个数:", len(test_list))












