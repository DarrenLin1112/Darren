# encoding=utf-8
import jieba

seg_list = jieba.cut("欢迎来到杭州溜达网络科技有限公司",cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))#全模式

seg_list = jieba.cut("欢迎来到杭州溜达网络科技有限公司,彭长冬是溜达第一帅",cut_all=False)
print("Default Mode: " + "/ ".join(seg_list)) #精确模式

set_list = jieba.cut("欢迎来到杭州溜达网络科技有限公司,彭长冬是溜达第一帅")#默认是精确模式
print("， ".join(seg_list))

seg_list = jieba.cut_for_search("长冬是溜达网络的前端工程师")#搜索引擎模式
print("， ".join(seg_list))
