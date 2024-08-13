# -----------*----------- coding: utf-8 -----------*----------- #

# ------------------------------------------------------------- #
# Name:                 CleanKG
# Description:          清洁知识图谱
# Author:               Guo
# Date:                 2024/05/17
# ------------------------------------------------------------- #

from py2neo import Graph, Node, Relationship
import os

classification = ['清洁场景', '场景材质', '清洁操作', '清洁配件']
def createEntity0(graph):
    cql = 'CREATE (:清洁图谱{id:\'0\', name:\'清洁图谱\'})'
    graph.run(cql)
    for i, c in enumerate(classification):
        cql = '''
            MERGE (a:清洁图谱分类{id:\'%d\', name:\'%s\'})
            MERGE (b {name: '清洁图谱'})
            MERGE (b)-[:划分]-> (a)
            ''' % (i+1, c)
        graph.run(cql)
    print('类别构建完成')
    #   --------------------------------------------------------------------
    #   场景导入
    #   --------------------------------------------------------------------
    file1 = open('data/场景.txt', 'r', encoding='utf8')
    i = 1
    for name in file1.readlines():
        if len(name) == 0:
            continue
        cql = '''
                    MERGE (a:清洁场景{id:\'%d\', name:\'%s\'})
                    MERGE (b {name: '清洁场景'})
                    MERGE (b)-[:包含]-> (a)
                ''' % (i, name)
        i += 1
        graph.run(cql)
    print('场景导入成功')
    #   --------------------------------------------------------------------
    #   配件导入
    #   --------------------------------------------------------------------
    file2 = open('data/配件.txt', 'r', encoding='utf8')
    i = 1
    for name in file2.readlines():
        if len(name) == 0:
            continue
        cql = '''
                        MERGE (a:清洁配件{id:\'%d\', name:\'%s\'})
                        MERGE (b {name: '清洁配件'})
                        MERGE (b)-[:包含]-> (a)
                    ''' % (i, name)
        i += 1
        graph.run(cql)
    print('配件导入成功')
    #   --------------------------------------------------------------------
    #   操作导入
    #   --------------------------------------------------------------------
    file2 = open('data/操作.txt', 'r', encoding='utf8')
    i = 1
    for name in file2.readlines():
        if len(name) == 0:
            continue
        cql = '''
                        MERGE (a:清洁操作{id:\'%d\', name:\'%s\'})
                        MERGE (b {name: '清洁操作'})
                        MERGE (b)-[:包含]-> (a)
                    ''' % (i, name)
        i += 1
        graph.run(cql)
    print('操作导入成功')
    #   --------------------------------------------------------------------
    #   材质导入
    #   --------------------------------------------------------------------
    file2 = open('data/材质.txt', 'r', encoding='utf8')
    i = 1
    for name in file2.readlines():
        if len(name) == 0:
            continue
        cql = '''
                        MERGE (a:场景材质{id:\'%d\', name:\'%s\'})
                        MERGE (b {name: '场景材质'})
                        MERGE (b)-[:包含]-> (a)
                    ''' % (i, name)
        i += 1
        graph.run(cql)
    print('材质导入成功')

if __name__ == '__main__':
    test_graph = Graph("neo4j://localhost:7474", auth=("username", "userchiper"))   #   更改用户名和密码
    test_graph.run('match(n) detach delete n')
    createEntity0(test_graph)