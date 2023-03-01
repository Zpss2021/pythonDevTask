# S3_1 字符串操作-学生信息提取
# 张起硕-2125060196
# 2023/02/28

html_str = '''
    <tbody>
        <tr>
            <td><span><span class="c-index c-index-hot1 c-gap-icon-right-small">1</span> 张婷婷 </span></td>
            <td class="opr-toplist-right">92<i class="opr-toplist-st c-icon c-icon-down"></i></td>
        </tr>
        <tr>
            <td><span><span class="c-index c-index-hot2 c-gap-icon-right-small">2</span> 王华 </span></td>
            <td class="opr-toplist-right">91<i class="opr-toplist-st c-icon c-icon-down"></i></td>
        </tr>
        <tr>
            <td><span><span class="c-index c-index-hot3 c-gap-icon-right-small">3</span> 张岚 </span></td>
            <td class="opr-toplist-right">90<i class="opr-toplist-st c-icon c-icon-down"></i></td>
        </tr>
        <tr>
            <td><span><span class="c-index c-gap-icon-right-small">4</span> 孙鸿峰 </span></td>
            <td class="opr-toplist-right">90<i class="opr-toplist-st c-icon c-icon-down"></i></td>
        </tr>
        <tr>
            <td><span><span class="c-index c-gap-icon-right-small">5</span> 周海栋 </span></td>
            <td class="opr-toplist-right">89<i class="opr-toplist-st c-icon c-icon-down"></i></td>
        </tr>
        <tr>
            <td><span><span class="c-index c-gap-icon-right-small">6</span> 武静 </span></td>
            <td class="opr-toplist-right">88<i class="opr-toplist-st c-icon c-icon-down"></i></td>
        </tr>
    </tbody>
'''

tbody = html_str[html_str.find('<tbody>') + len('<tbody>'):html_str.find('</tbody>')]
students = tbody.split('<tr>')[1:]
students_info = []

for stu in students:
    index, index_begin, index_end = 0, 0, 0
    index_spans = stu.split('<span>')[1:]
    for index_span in index_spans:
        index_begin = index_span.find('>') + len('>')
        index_end = index_span.find('</span>')
        index = index_span[index_begin:index_end].strip()
    name_begin = stu.find('</span>', index_end) + len('</span>')
    name_end = stu.find('</span>', name_begin)
    name = stu[name_begin:name_end].strip()
    score_begin = stu.find('<td class="opr-toplist-right">', name_end) + len('<td class="opr-toplist-right">')
    score_end = stu.find('<i', score_begin)
    score = stu[score_begin:score_end].strip()
    students_info.append([index, name, score])

for info in students_info:
    print("序号：{0:3}姓名：{1}\t成绩：{2}".format(info[0], info[1], info[2]))
