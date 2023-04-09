import jiagu

# 定义问题模板
questions = {
    '人名': {
        'who': '谁是{}?',
        'when': '{}是什么时候出生的?',
        'where': '{}来自哪里?',
        'why': '{}为什么有名?',
        'what': '{}因什么而闻名?',
        'how': '{}是怎么样的人?'
    },
    '地名': {
        'who': '{}是谁居住的地方?',
        'when': '{}是什么时候成立的?',
        'where': '{}位于哪里?',
        'why': '{}为什么有名?',
        'what': '{}因什么而闻名?',
        'how': '{}怎么样?'
    },
    '机构名': {
        'who': '{}的创始人是谁?',
        'when': '{}是什么时候成立的?',
        'where': '{}的位置在哪里?',
        'why': '{}为什么成立?',
        'what': '{}做什么?',
        'how': '{}怎么样?'
    },
    '时间': {
        'who': '{}在什么时候发生的?',
        'when': '{}是什么时候?',
        'where': '{}在什么地方发生的?',
        'why': '{}为什么会发生?',
        'what': '{}是什么事件?',
        'how': '{}是如何发生的?'
    },
    '数字': {
        'who': '{}是谁的编号?',
        'when': '{}代表什么?',
        'where': '{}在什么位置?',
        'why': '{}有什么意义?',
        'what': '{}是什么数字?',
        'how': '{}是怎么计算的?'
    },
    '设施名': {
        'who': '{}是谁设计的?',
        'when': '{}是什么时候建造的?',
        'where': '{}位于哪里?',
        'why': '{}为什么建造?',
        'what': '{}是什么设施?',
        'how': '{}是怎么建造的?'
    },
    '地理政治实体': {
        'who': '{}是谁的领土?',
        'when': '{}是什么时候成立的?',
        'where': '{}位于哪里?',
        'why': '{}为什么重要?',
        'what': '{}是什么实体?',
        'how': '{}是怎么成立的?'
    }
}

def generate_questions(text):
    gen_questions = []
    words = jiagu.seg(text) # 分词
    pos = jiagu.pos(words) # 词性标注
    # 使用jiagu进行命名实体识别，提取实体和实体类型
    named_entities = jiagu.ner(words)
    entities=[]
    for i in range(len(named_entities)):
        ent=named_entities[i]
        word=words[i]
        if ent=="B-PER":
            entities.append((word, '人名'))
        if ent=="B-LOC":
            entities.append((word, '地名'))
        if ent=="B-TIME":
            entities.append((word, '时间'))
        if ent=="B-NUM":
            entities.append((word, '数字'))
        if ent=="B-FAC":
            entities.append((word, '设施名'))
        if ent=="B-GPE":
            entities.append((word, '地理政治实体'))

    # 遍历实体列表，生成问题
    for entity, entity_type in entities:
        if entity_type in questions:
            for question_type, question in questions[entity_type].items():
                gen_questions.append(question.format(entity))
    return gen_questions

if __name__ == "__main__":
    # 示例文本
    text = "乔布斯是美国苹果公司的创始人之一,1955年出生于加利福尼亚。"
    q = generate_questions(text)
    print(q)
