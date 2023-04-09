import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
questions = {
    'PERSON': {
        'who': 'Who is {}?',
        'when': 'When was {} born?',
        'where': 'Where is {} from?',
        'why': 'Why is this person famous?',
        'what': 'What is {} known for?',
        'how': 'How did {} become famous?'
    },
    'GPE': {
        'who': 'Who lives in {}?',
        'when': 'When was {} founded?',
        'where': 'Where is {} located?',
        'why': 'Why is {} famous?',
        'what': 'What is {} known for?',
        'how': 'How did {} gain its fame?'
    },
    'ORG': {
        'who': 'Who are the founders of {}?',
        'when': 'When was {} established?',
        'where': 'Where is the headquarters of {}?',
        'why': 'Why was {} created?',
        'what': 'What does {} do?',
        'how': 'How does {} operate?'
    },
    'TIME': {
        'who': 'Who experienced {}?',
        'when': 'When did {} occur?',
        'where': 'Where did {} happen?',
        'why': 'Why did {} take place?',
        'what': 'What happened during {}?',
        'how': 'How did {} come about?'
    },
    'QUANTITY': {
        'who': 'Who deals with {}?',
        'when': 'When was {} measured?',
        'where': 'Where is {} usually used?',
        'why': 'Why is {} important?',
        'what': 'What is the significance of {}?',
        'how': 'How is {} measured or quantified?'
    },
    'MONEY': {
        'who': 'Who deals with {}?',
        'when': 'When was {} used?',
        'where': 'Where is {} currency?',
        'why': 'Why is {} valuable?',
        'what': 'What can you buy with {}?',
        'how': 'How is {} used as currency?'
    },
    'EVENT': {
        'who': 'Who participated in {}?',
        'when': 'When did {} happen?',
        'where': 'Where did {} take place?',
        'why': 'Why did {} occur?',
        'what': 'What is {} about?',
        'how': 'How did {} unfold or occur?'
    },
    'DATE': {
        'who': 'Who experienced {}?',
        'when': 'When is {}?',
        'where': 'Where is {} celebrated?',
        'why': 'Why is {} important?',
        'what': 'What is the significance of {}?',
        'how': 'How is {} celebrated or observed?'
    },
    'PRODUCT': {
        'who': 'Who uses {}?',
        'when': 'When was {} created?',
        'where': 'Where is {} produced?',
        'why': 'Why was {} invented?',
        'what': 'What are the features of {}?',
        'how': 'How does {} work or function?'
    }
}

def generateQuestions(text):
    gen_questions=[]
     # 分词和词性标注
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    # 使用 nltk.ne_chunk() 进行命名实体识别，生成树形结构（Tree）
    entities = nltk.ne_chunk(tagged)
    # 遍历树形结构，找到有用的实体
    for entity in entities:
        if isinstance(entity, Tree):
            # 这是一个实体，提取实体名称并标注实体类型
            entity_type = entity.label()
            entity_name = ' '.join(i[0] for i in entity.leaves())

            # 如果实体类型在问题列表中存在，则根据实体类型和问题类型生成问题
            if entity_type in questions:
                for question_type, question in questions[entity_type].items():
                    gen_questions.append(question.format(entity_name))
    return gen_questions

if __name__=="__main__":
    # 打印生成的问题句子
    # for question in questions:
    #     print(question)

    # 示例文本
    text = "Barack Obama is a former president of the United States who was born in Honolulu, Hawaii."
    q=generateQuestions(text)
    print(q)
