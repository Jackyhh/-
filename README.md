# -
项目目的：这个项目主要是为阅读英语书籍时存在大量生词的问题，通过词频统计，筛选出95%的高频词汇，将高频词汇以200 ~ 300个为单位上传到金山词霸/有道词典以便于快速回顾

1. 使用在线文档转换工具——cloudconvert（https://cloudconvert.com/）将 pdf、epub 等格式转换成 txt 格式；
2. 统计文章词频，使用软件：AntConc_64bit.exe（百度云链接：https://pan.baidu.com/s/1yxSAz5qWIQdahFQxlHyPaA 提取码：q8c6）；
3. 将txt词频文件转换成xml文件（python脚本：txt2xml）;
4. 在金山词霸/有道词典中导入xml文件。
