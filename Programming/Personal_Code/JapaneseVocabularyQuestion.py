import random

# 중복 없는 한자 목록 (총 95자)
unique_kanji_list = sorted(set([
    "求", "人", "職", "休", "要", "請", "救", "助", "急", "済", "記", "念", "録", "入", "表", "伝",
    "日", "暗", "号", "者", "起", "床", "世", "紀", "大", "家", "目", "型", "陸", "国", "会", "切", "量",
    "衆", "気", "使", "統", "領", "事", "丈", "根", "臣", "工", "小", "体", "巨", "偉", "犬", "猿",
    "仲", "愛", "太", "力", "協", "努", "能", "実", "圧", "暴", "学", "馬", "治", "医", "診", "僚",
    "官", "寮", "砂", "漠", "然", "募", "金", "公", "暮", "歳", "墓", "地", "規", "模", "様", "範", "義",
    "理", "講", "主", "意", "議", "論", "員", "不", "思", "礼", "儀", "式", "犠", "牲"
]))

# 111개의 뜻 목록 (정답과 매칭)
meanings = [
    "구하다, 요구하다", "구인", "구직", "휴직", "요구", "청구", "구하다, 구조하다", "구조", "구급", "구제",
    "기록하다", "기념", "기록", "기입", "표기", "전기", "일기", "암기", "기호", "기자", "일어나다", "깨우다",
    "기상", "세기", "크다", "집주인", "넉넉함, 관대함", "대형", "대륙", "대국", "대회", "소중하다", "대량",
    "대중", "대기", "대사", "대통령", "소중하다", "괜찮다", "무", "대신", "목수", "대소", "대부분", "거대",
    "위대", "어른", "개", "견원지간", "애견", "굵다", "살찌다", "태양", "힘", "협력", "노력", "능력",
    "실력", "압력", "폭력", "학력", "마력", "인력", "치료", "의료", "진료", "동료", "관료", "기숙사",
    "사막", "막연함", "모집", "모금", "공모", "점점 심해지다, 모집하다", "살다, 거주하다", "연말선물", "묘",
    "묘지", "규모", "모양", "모형", "모범", "의리", "강의", "주의", "의의", "의논", "의원", "신기하다, 이상하다",
    "회의", "예의", "의식", "희생"
]

# 각 뜻에 해당하는 정답 한자 조합
correct_answers = {
    "구하다, 요구하다": "求",
    "구인": "求人",
    "구직": "求職",
    "휴직": "休職",
    "요구": "要求",
    "청구": "請求",
    "구하다, 구조하다": "救",
    "구조": "救助",
    "구급": "救急",
    "구제": "救済",
    "기록하다": "記",
    "기념": "記念",
    "기록": "記録",
    "기입": "記入",
    "표기": "表記",
    "전기": "伝記",
    "일기": "日記",
    "암기": "暗記",
    "기호": "記号",
    "기자": "記者",
    "일어나다": "起",
    "깨우다": "起こす",
    "기상": "起床",
    "세기": "世紀",
    "크다": "大",
    "집주인": "大家",
    "넉넉함, 관대함": "大目",
    "대형": "大型",
    "대륙": "大陸",
    "대국": "大国",
    "대회": "大会",
    "소중하다": "大切だ",
    "대량": "大量",
    "대중": "大衆",
    "대기": "大気",
    "대사": "大使",
    "대통령": "大統領",
    "괜찮다": "大丈夫だ",
    "무": "大根",
    "대신": "大臣",
    "목수": "大工",
    "대소": "大小",
    "대부분": "大体",
    "거대": "巨大",
    "위대": "偉大",
    "어른": "大人",
    "개": "犬",
    "견원지간": "犬猿の仲",
    "애견": "愛犬",
    "굵다": "太い",
    "살찌다": "太る",
    "태양": "太陽",
    "힘": "力",
    "협력": "協力",
    "노력": "努力",
    "능력": "能力",
    "실력": "実力",
    "압력": "圧力",
    "폭력": "暴力",
    "학력": "学力",
    "마력": "馬力",
    "인력": "人力",
    "치료": "治療",
    "의료": "医療",
    "진료": "診療",
    "동료": "同僚",
    "관료": "官僚",
    "기숙사": "寮",
    "사막": "砂漠",
    "막연함": "漠然",
    "모집": "募集",
    "모금": "募金",
    "공모": "公募",
    "점점 심해지다, 모집하다": "募る",
    "살다, 거주하다": "暮らす",
    "연말선물": "歳暮",
    "묘": "墓",
    "묘지": "墓地",
    "규모": "規模",
    "모양": "模様",
    "모형": "模型",
    "모범": "模範",
    "의리": "義理",
    "강의": "講義",
    "주의": "主義",
    "의의": "意義",
    "의논": "議論",
    "의원": "議員",
    "신기하다, 이상하다": "不思議だ",
    "회의": "会議",
    "예의": "礼儀",
    "의식": "儀式",
    "희생": "犠牲"
}

# 퀴즈 출제 함수
def play_quiz():
    print("뜻을 보고 보기에서 한자를 조합하여 답을 입력하세요.\n")

    for meaning, correct_kanji in correct_answers.items():  # 총 111개의 문제
        selected_kanji = random.sample(unique_kanji_list, 15)
        choices = " ".join(selected_kanji)
        
        print(f"뜻: {meaning}")
        print(f"보기: {choices}")

        user_answer = input("한자를 조합하여 입력하세요: ")

        if user_answer == correct_kanji:
            print("정답입니다!\n")
        else:
            print(f"틀렸습니다. 정답은 '{correct_kanji}'입니다.\n")

# 게임 실행
play_quiz()
