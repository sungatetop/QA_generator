import jieba
import jieba.posseg as pseg

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
    }
}
def generateQuestions(text):
    gen_questions=[]
    # 分词和词性标注
    words = list(jieba.cut(text))
    tagged = pseg.cut(text)
     # 使用jieba进行命名实体识别，提取实体和实体类型
    entities = []
    for word, flag in tagged:
        if flag.startswith('nr'):  # 人名
            entities.append((word, '人名'))
        elif flag.startswith('ns'):  # 地名
            entities.append((word, '地名'))
        elif flag.startswith('nt'):  # 机构名
            entities.append((word, '机构名'))

    # 遍历实体列表，生成问题
    for entity, entity_type in entities:
        if entity_type in questions:
            for question_type, question in questions[entity_type].items():
                gen_questions.append(question.format(entity))
    return gen_questions

if __name__=="__main__":
    # 示例文本
    text = "乔布斯是美国苹果公司的创始人之一，1955年出生于加利福尼亚。"
    q=generateQuestions(text)
    print(q)