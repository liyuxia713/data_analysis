#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# 注意engine是xlsxwriter, 最后save完才会保存到excel
writer=pd.ExcelWriter('./excelname.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name_1, header=None, index=False)
df2.to_excel(writer, sheet_name_2, header=None, index=False)
writer.save()





''' vim: set expandtab ts=4 sw=4 sts=4 tw=100: '''
