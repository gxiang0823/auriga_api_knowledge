import matplotlib.pyplot as plt
from matplotlib import ticker
def draw_gantt_chart(tasks_list, bar_height=0.2):
    fig, ax = plt.subplots(figsize=(10, len(tasks_list) * 1))  # 调整图表大小

    max_end = max(task[1] for tasks in tasks_list for task in tasks)
    for i, tasks in enumerate(tasks_list):
        for task in tasks:
            start, end, label = task
            ax.barh(i, end - start, left=start, height=bar_height, align='center', label=label)
            ax.text((start + end) / 2, i, f'{label}\n{round((end-start), 1)} hour', va='center', ha='center', color='black')

    ax.set_yticks(range(len(tasks_list)))
    ax.set_yticklabels([f'Vehicle {i+1}' for i in range(len(tasks_list))])
    ax.set_xlabel('Time')
    ax.set_title('Gantt Chart')

    ax.invert_yaxis()

    ax.xaxis.grid(True)
    ax.set_xlim(6, 20)

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:02d}:{:02d}'.format(int(x // 1), int(x % 1 * 60))))

    plt.show()

# 两个任务列表
tasks_list_1 = [
    (6.2, 10, 'Water'),
    (10.5, 14, 'Sweep'),
    (14, 16, 'Mop'),
    (16.5, 20, 'Dedust')
]

tasks_list_2 = [
    (6, 8.3, 'Inspection'),
    (9, 13.1, 'Sweep'),
    (14, 17.5, 'Pick')
]

tasks_list_3 = [
    (6, 7, 'Equipping'),
    (7, 8, 'Water'),
    (8.5, 11, 'Sweep'),
    (11.5, 14, 'Pick'),
    (15, 20, 'Mop'),

]

tasks_list_4 = [
    (6, 8.1, 'Inspection'),
    (9, 14.1, 'Sweep'),
    (15, 18, 'Pick')
]

draw_gantt_chart([tasks_list_1, tasks_list_2, tasks_list_3, tasks_list_4])  # 绘制两个任务列表的甘特图，柱子宽度为0.6
