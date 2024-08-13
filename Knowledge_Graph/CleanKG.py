from py2neo import Graph, Node, Relationship
import pandas as pd
import csv
import os

def createEntity0(graph):
    with open('.\\data\\Final_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        Master = Node('清洁图谱', name='清洁图谱')
        graph.create(Master)

        created_sub_nodes = {}
        created_obj_nodes = {}

        for i in range(1, len(data)):
            Sub_name = data[i][0]
            Obj_name = data[i][3]

            if Sub_name not in created_sub_nodes:
                Sub = Node(data[i][1], name=data[i][0])
                graph.create(Sub)
                created_sub_nodes[Sub_name] = Sub
            else:
                Sub = created_sub_nodes[Sub_name]

            if Obj_name not in created_obj_nodes:
                Obj = Node(data[i][4], name=Obj_name)
                graph.create(Obj)
                # 将新创建的节点添加到已创建节点的字典中
                created_obj_nodes[Obj_name] = Obj
            else:
                Obj = created_obj_nodes[Obj_name]

            Scene = Relationship(Master, '场景', Sub)
            graph.create(Scene)

            Relation = Relationship(Sub, data[i][2], Obj)
            graph.create(Relation)

def get_relation(graph, Scene_name):
    query = (
        "MATCH (parent)-[relation]->(child) "
        "WHERE parent.name = $Scene_name "
        "RETURN COALESCE(type(relation), 'UNKNOWN') AS relationship_type, COLLECT(child.name) AS child_names"
    )
    result = graph.run(query, Scene_name=Scene_name)
    return result

if __name__ == '__main__':
    test_graph = Graph("neo4j://localhost:7474", auth=("username", "userchiper")) # 更改地址、用户名和密码为你的地址、用户名和密码
    test_graph.run('match(n) detach delete n')
    createEntity0(test_graph)

    # 开始主循环
    while True:

        # 从终端输入场景名称
        Scene_name = input("请输入场景名称：")

        # 获取该场景的所有子节点
        child_nodes = get_relation(test_graph, Scene_name)

        # 输出子节点及其关系
        for record in child_nodes:
            relationship_type = record["relationship_type"]
            child_names = record["child_names"]
            print(relationship_type)
            print(child_names)

        User_Input = input("是否继续？(yes/no): ")
        if User_Input.lower() != "yes":
            break


