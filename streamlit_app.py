import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & PASTEL CUTE STYLING
# ==========================================
st.set_page_config(
    page_title="HSK 5 Pre-class & Rractice | 黄宝玉老师",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Pastel, Cute Rounded Cards, Bold Fonts, Mobile Responsiveness
CUSTOM_CSS = """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', 'Noto Sans SC', sans-serif;
        background-color: #FAF7F2;
        color: #2D3436;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 980px;
    }

    /* Header Banner */
    .header-card {
        background: linear-gradient(135deg, #FFE5EC 0%, #F0E6FF 100%);
        border-radius: 24px;
        padding: 22px 26px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(255, 182, 193, 0.3);
        border: 2px solid #FFF;
        margin-bottom: 20px;
    }
    .header-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #6C5CE7;
        margin-bottom: 4px;
    }
    .header-subtitle {
        font-size: 1.05rem;
        font-weight: 700;
        color: #B2BEC3;
    }

    /* User Box & Leaderboard Card */
    .user-box {
        background: #FFFFFF;
        border: 2px solid #FFEAA7;
        border-radius: 20px;
        padding: 16px 20px;
        box-shadow: 0 6px 15px rgba(253, 203, 110, 0.2);
        margin-bottom: 20px;
    }

    .leaderboard-card {
        background: linear-gradient(135deg, #FFF9E6 0%, #FFF3CD 100%);
        border: 2px solid #FDCB6E;
        border-radius: 20px;
        padding: 16px 20px;
        box-shadow: 0 6px 15px rgba(253, 203, 110, 0.25);
        margin-bottom: 20px;
    }
    .leaderboard-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #D63031;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .leaderboard-item {
        font-size: 1rem;
        font-weight: 700;
        color: #2D3436;
        padding: 6px 12px;
        background: #FFFFFF;
        border-radius: 12px;
        margin-bottom: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #FFEAA7;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #EFEAE1;
        padding: 6px;
        border-radius: 18px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 46px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 14px;
        color: #636E72;
        font-weight: 700;
        font-size: 0.92rem;
        border: none;
        padding: 0px 14px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF !important;
        color: #6C5CE7 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    }

    /* Flashcard Style */
    .flashcard-back-box {
        background: #FFFFFF;
        border: 3px solid #A29BFE;
        border-radius: 24px;
        padding: 30px 20px;
        text-align: center;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 10px 25px rgba(108, 92, 231, 0.12);
        margin-bottom: 15px;
    }
    
    .flashcard-hanzi {
        font-size: 3.8rem;
        font-weight: 800;
        color: #2D3436;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }
    .flashcard-pinyin {
        font-size: 1.4rem;
        font-weight: 700;
        color: #FF7675;
        margin-bottom: 6px;
    }
    .flashcard-meaning {
        font-size: 1.3rem;
        font-weight: 800;
        color: #00B894;
        margin-bottom: 10px;
    }
    .flashcard-example {
        font-size: 1rem;
        font-weight: 600;
        color: #4A5568;
        background: #F8F9FA;
        padding: 10px 16px;
        border-radius: 14px;
        border-left: 4px solid #6C5CE7;
        margin-top: 6px;
    }

    /* Quiz Box Style */
    .quiz-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 24px;
        border: 2px solid #E2E8F0;
        box-shadow: 0 6px 16px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }
    .quiz-question {
        font-size: 1.35rem;
        font-weight: 800;
        color: #2D3436;
        margin-bottom: 16px;
    }

    /* Badge & Cards */
    .badge-tag {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 12px;
        font-size: 0.88rem;
        font-weight: 800;
        background-color: #FFEAA7;
        color: #D63031;
        margin-bottom: 12px;
    }

    .body-part-card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 16px;
        border: 2px solid #F1F2F6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        margin-bottom: 12px;
        text-align: center;
    }
    .body-part-hanzi {
        font-size: 1.9rem;
        font-weight: 800;
        color: #6C5CE7;
    }

    /* Custom Input & Buttons */
    .stButton>button {
        border-radius: 16px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 10px 20px !important;
        transition: all 0.2s ease !important;
    }

    /* Flashcard Large Flip Button Style */
    .flip-btn-style button {
        background: linear-gradient(135deg, #6C5CE7 0%, #818CF8 100%) !important;
        color: #FFFFFF !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        padding: 45px 20px !important;
        border-radius: 24px !important;
        box-shadow: 0 10px 20px rgba(108, 92, 231, 0.2) !important;
        line-height: 1.4 !important;
    }
    
    /* Footer Style */
    .footer {
        text-align: center;
        padding: 30px 10px 10px 10px;
        font-size: 1.15rem;
        font-weight: 800;
        color: #A29BFE;
        letter-spacing: 1px;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = {
        "Nguyễn Văn A": 28,
        "Trần Thị B": 22,
        "Lê Hoàng C": 15
    }

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if 'flashcard_idx' not in st.session_state:
    st.session_state.flashcard_idx = 0

if 'show_back' not in st.session_state:
    st.session_state.show_back = False

# ==========================================
# DATA: VOCABULARY & EXERCISES (LESSON 1)
# ==========================================

VOCAB_LESSON_1 = [
    {"hanzi": "细节", "pinyin": "xìjié", "type": "dt", "meaning": "Chi tiết", "example": "生活的细节 (Chi tiết của cuộc sống)"},
    {"hanzi": "电台", "pinyin": "diàntái", "type": "dt", "meaning": "Đài phát thanh", "example": "电台主持人 (MC đài phát thanh)"},
    {"hanzi": "恩爱", "pinyin": "ēn'ài", "type": "tt", "meaning": "Ân ái, yêu thương nhau", "example": "最恩爱夫妻 (Cặp vợ chồng yêu thương nhau nhất)"},
    {"hanzi": "对比", "pinyin": "duìbǐ", "type": "dgt/dt", "meaning": "So sánh, đối chiếu", "example": "经过详细对比 (Sau khi so sánh chi tiết)"},
    {"hanzi": "入围", "pinyin": "rùwéi", "type": "dgt", "meaning": "Vào vòng trong", "example": "有三对夫妻入围 (Có 3 cặp vợ chồng vào vòng trong)"},
    {"hanzi": "评委", "pinyin": "píngwěi", "type": "dt", "meaning": "Ban giám khảo", "example": "评委们都很感动 (Ban giám khảo đều rất cảm động)"},
    {"hanzi": "如何", "pinyin": "rúhé", "type": "đt", "meaning": "Như thế nào, ra sao", "example": "如何解决这个问题 (Giải quyết vấn đề này thế nào)"},
    {"hanzi": "瘫痪", "pinyin": "tānhuàn", "type": "dgt", "meaning": "Liệt, tàn phế", "example": "瘫痪在床 (Liệt giường)"},
    {"hanzi": "离婚", "pinyin": "líhūn", "type": "dgt", "meaning": "Ly hôn", "example": "申请离婚 (Nộp đơn ly hôn)"},
    {"hanzi": "自杀", "pinyin": "zìshā", "type": "dgt", "meaning": "Tự sát", "example": "放弃自杀念头 (Từ bỏ ý định tự sát)"},
    {"hanzi": "抱怨", "pinyin": "bàoyuàn", "type": "dgt", "meaning": "Oán trách, phàn nàn", "example": "从不抱怨 (Không bao giờ phàn nàn)"},
    {"hanzi": "爱护", "pinyin": "àihù", "type": "dgt", "meaning": "Yêu quý, bảo vệ", "example": "爱护环境 (Bảo vệ môi trường)"},
    {"hanzi": "婚姻", "pinyin": "hūnyīn", "type": "dt", "meaning": "Hôn nhân", "example": "幸福的婚姻 (Cuộc hôn nhân hạnh phúc)"},
    {"hanzi": "吵架", "pinyin": "chǎojià", "type": "dgt", "meaning": "Cãi nhau", "example": "从来没吵过架 (Chưa từng cãi nhau bao giờ)"},
    {"hanzi": "相敬如宾", "pinyin": "xiāngjìng-rúbīn", "type": "thng", "meaning": "Kính trọng nhau như khách", "example": "夫妻俩相敬如宾 (Hai vợ chồng kính trọng nhau như khách)"},
    {"hanzi": "暗暗", "pinyin": "àn'àn", "type": "phó", "meaning": "Thầm, ngầm", "example": "暗暗点头 (Gật đầu thầm)"},
    {"hanzi": "轮", "pinyin": "lún", "type": "dgt", "meaning": "Luân phiên, đến lượt", "example": "轮到第三对夫妻 (Đến lượt cặp vợ chồng thứ ba)"},
    {"hanzi": "不耐烦", "pinyin": "bú nàifán", "type": "tt", "meaning": "Sốt ruột, bực mình", "example": "等得有些不耐烦 (Đợi đến mức có chút sốt ruột)"},
    {"hanzi": "靠", "pinyin": "kào", "type": "dgt", "meaning": "Dựa, tựa, kề sát", "example": "靠在肩膀上 (Tựa vào bờ vai)"},
    {"hanzi": "肩膀", "pinyin": "jiānbǎng", "type": "dt", "meaning": "Bờ vai, vai", "example": "靠着肩膀 (Tựa vào bờ vai)"},
    {"hanzi": "喊", "pinyin": "hǎn", "type": "dgt", "meaning": "Kêu, gọi, hét", "example": "喊醒他 (Gọi anh ấy thức dậy)"},
    {"hanzi": "伸", "pinyin": "shēn", "type": "dgt", "meaning": "Duỗi, chìa ra", "example": "伸手指 (Chìa ngón tay ra)"},
    {"hanzi": "手指", "pinyin": "shǒuzhǐ", "type": "dt", "meaning": "Ngón tay", "example": "伸出手指 (Chìa ngón tay ra)"},
    {"hanzi": "歪歪扭扭", "pinyin": "wāiwāiniǔniǔ", "type": "tt", "meaning": "Xiêu vẹo, ngoằn ngoèo", "example": "字写得歪歪扭扭 (Chữ viết xiêu vẹo)"},
    {"hanzi": "递", "pinyin": "dì", "type": "dgt", "meaning": "Đưa, chuyền qua", "example": "递给评委 (Đưa cho ban giám khảo)"},
    {"hanzi": "脑袋", "pinyin": "nǎodai", "type": "dt", "meaning": "Đầu", "example": "让脑袋靠着 (Để đầu tựa vào)"},
    {"hanzi": "女士", "pinyin": "nǚshì", "type": "dt", "meaning": "Quý bà, quý cô", "example": "这位女士 (Người phụ nữ này)"},
    {"hanzi": "叙述", "pinyin": "xùshù", "type": "dgt", "meaning": "Thuật lại, kể lại", "example": "听你们的叙述 (Nghe câu chuyện thuật lại của hai bạn)"},
    {"hanzi": "居然", "pinyin": "jūrán", "type": "phó", "meaning": "Lại, không ngờ", "example": "居然放弃这次机会 (Không ngờ lại từ bỏ cơ hội này)"},
    {"hanzi": "催", "pinyin": "cuī", "type": "dgt", "meaning": "Thúc giục, hối thúc", "example": "先不催他们 (Tạm thời không thúc giục họ)"},
    {"hanzi": "等待", "pinyin": "děngdài", "type": "dgt", "meaning": "Đợi, chờ", "example": "等待一段时间 (Chờ đợi một khoảng thời gian)"},
    {"hanzi": "蚊子", "pinyin": "wénzi", "type": "dt", "meaning": "Con muỗi", "example": "半夜有蚊子 (Nửa đêm có muỗi)"},
    {"hanzi": "半夜", "pinyin": "bànyè", "type": "dt", "meaning": "Nửa đêm", "example": "半夜被叮醒 (Nửa đêm bị đốt tỉnh)"},
    {"hanzi": "叮", "pinyin": "dīng", "type": "dgt", "meaning": "Đốt, chích", "example": "被蚊子叮了 (Bị muỗi đốt)"},
    {"hanzi": "老婆", "pinyin": "lǎopo", "type": "dt", "meaning": "Vợ (khẩu ngữ)", "example": "怕老婆被吵醒 (Sợ vợ bị làm phiền tỉnh giấc)"},
    {"hanzi": "吵", "pinyin": "chǎo", "type": "dgt/tt", "meaning": "Làm ồn, ồn ào", "example": "怕吵醒她 (Sợ làm ồn cô ấy tỉnh)"},
    {"hanzi": "项", "pinyin": "xiàng", "type": "lượng", "meaning": "Hạng mục, giải thưởng", "example": "增加了两项奖项 (Thêm hai hạng mục giải thưởng)"},
    {"hanzi": "患难与共", "pinyin": "huànnàn-yǔgòng", "type": "thng", "meaning": "Hoạn nạn có nhau", "example": "患难与共夫妻 (Cặp vợ chồng hoạn nạn có nhau)"}
]

BODY_PARTS = [
    {"hanzi": "脑袋", "pinyin": "nǎodai", "hanviet": "Não đại", "meaning": "Đầu", "icon": "🧠", "collocation": "脑袋晕 / 拍拍脑袋"},
    {"hanzi": "脖子", "pinyin": "bózi", "hanviet": "Bột tử", "meaning": "Cổ", "icon": "🦒", "collocation": "脖子酸 / 缩缩脖子"},
    {"hanzi": "肩膀", "pinyin": "jiānbǎng", "hanviet": "Kiên bảng", "meaning": "Bờ vai", "icon": "💪", "collocation": "靠在肩膀上 / 肩膀宽"},
    {"hanzi": "胸", "pinyin": "xiōng", "hanviet": "Hung", "meaning": "Ngực", "icon": "🫁", "collocation": "挺胸 / 胸口"},
    {"hanzi": "腰", "pinyin": "yāo", "hanviet": "Yêu", "meaning": "Lưng / Thắt lưng", "icon": "🧘", "collocation": "伸伸腰 / 腰酸背痛"},
    {"hanzi": "后背", "pinyin": "hòubèi", "hanviet": "Hậu bối", "meaning": "Tấm lưng", "icon": "🧍", "collocation": "拍拍后背 / 靠着后背"},
    {"hanzi": "手指", "pinyin": "shǒuzhǐ", "hanviet": "Thủ chỉ", "meaning": "Ngón tay", "icon": "👆", "collocation": "伸出手指 / 手指灵巧"},
    {"hanzi": "眉毛", "pinyin": "méimao", "hanviet": "Mi mao", "meaning": "Lông mày", "icon": "🤨", "collocation": "皱眉毛 / 眉毛弯弯"},
    {"hanzi": "嗓子", "pinyin": "sǎngzi", "hanviet": "Tảng tử", "meaning": "Cổ họng / Giọng", "icon": "🗣️", "collocation": "嗓子疼 / 嗓子哑了"},
    {"hanzi": "牙齿", "pinyin": "yáchǐ", "hanviet": "Nha xỉ", "meaning": "Răng", "icon": "🦷", "collocation": "刷牙齿 / 牙齿整齐"}
]

SENTENCE_MAKING_WORDS = [
    {
        "word": "抱怨",
        "meaning": "Oán trách, phàn nàn",
        "examples": [
            "遇到困难时，与其抱怨，不如想办法解决。(Khi gặp khó khăn, thay vì phàn nàn, chi bằng tìm cách giải quyết.)",
            "这几年他一直默默照顾瘫痪的妻子，从来没有一句抱怨。(Mấy năm nay anh ấy luôn âm thầm chăm sóc người vợ bị liệt, chưa từng một lời oán trách.)"
        ]
    },
    {
        "word": "靠",
        "meaning": "Dựa vào, kề sát",
        "examples": [
            "累的时候，她喜欢把头靠在丈夫的肩膀上。(Khi mệt mỏi, cô ấy thích tựa đầu vào bờ vai của chồng.)",
            "在家靠父母，出门靠朋友，团队合作非常重要。(Ở nhà dựa vào bố mẹ, ra ngoài dựa vào bạn bè, hợp tác đội ngũ rất quan trọng.)"
        ]
    },
    {
        "word": "居然",
        "meaning": "Lại, không ngờ (kinh ngạc)",
        "examples": [
            "这么简单的语法题，你居然做错了！(Đề ngữ pháp đơn giản thế này mà bạn lại làm sai rồi!)",
            "为了不打扰丈夫睡觉，她居然放弃了这次获奖的机会。(Vì không muốn làm phiền chồng ngủ, cô ấy lại từ bỏ cơ hội đoạt giải lần này.)"
        ]
    }
]

# ==========================================
# GENERATE 100 RANDOM QUESTION BANK
# ==========================================

def generate_100_question_bank():
    questions = []
    
    # 50 Questions Type A: Meaning of Hanzi
    type_a_base = [
        ("细节", "Chi tiết", ["Đài phát thanh", "Hôn nhân", "Bờ vai"]),
        ("电台", "Đài phát thanh", ["Chi tiết", "Ban giám khảo", "Giải thưởng"]),
        ("恩爱", "Ân ái, yêu thương nhau", ["Cãi nhau", "Tự sát", "Phàn nàn"]),
        ("对比", "So sánh, đối chiếu", ["Kể lại", "Hối thúc", "Hoàn thành"]),
        ("入围", "Vào vòng trong", ["Bị loại", "Ly hôn", "Thất bại"]),
        ("评委", "Ban giám khảo", ["Ký giả", "Thí sinh", "Khán giả"]),
        ("如何", "Như thế nào, ra sao", ["Tại sao", "Ở đâu", "Bao giờ"]),
        ("瘫痪", "Liệt, tàn phế", ["Bệnh nhẹ", "Khỏe mạnh", "Bị cảm"]),
        ("离婚", "Ly hôn", ["Kết hôn", "Hẹn hò", "Sinh con"]),
        ("自杀", "Tự sát", ["Cứu người", "Bảo vệ", "Yêu thương"]),
        ("抱怨", "Oán trách, phàn nàn", ["Khen ngợi", "Cảm ơn", "Yêu quý"]),
        ("爱护", "Yêu quý, bảo vệ", ["Phá hoại", "Phàn nàn", "Cãi nhau"]),
        ("婚姻", "Hôn nhân", ["Tình bạn", "Sự nghiệp", "Học tập"]),
        ("吵架", "Cãi nhau", ["Thương lượng", "Tâm sự", "Khen ngợi"]),
        ("相敬如宾", "Kính trọng nhau như khách", ["Cãi nhau liên tục", "Xa lạ", "Oán trách nhau"]),
        ("暗暗", "Thầm, ngầm", ["Công khai", "To tiếng", "Trực tiếp"]),
        ("轮", "Luân phiên, đến lượt", ["Dừng lại", "Từ bỏ", "Bắt đầu"]),
        ("不耐烦", "Sốt ruột, bực mình", ["Kiên nhẫn", "Vui vẻ", "Bình tĩnh"]),
        ("靠", "Dựa, tựa, kề sát", ["Rời xa", "Đẩy ra", "Bay lên"]),
        ("肩膀", "Bờ vai, vai", ["Ngón tay", "Cổ họng", "Lông mày"]),
        ("喊", "Kêu, gọi, hét", ["Thầm thì", "Im lặng", "Mỉm cười"]),
        ("伸", "Duỗi, chìa ra", ["Thu lại", "Gập lại", "Giấu đi"]),
        ("手指", "Ngón tay", ["Bờ vai", "Thắt lưng", "Cổ"]),
        ("歪歪扭扭", "Xiêu vẹo, ngoằn ngoèo", ["Thẳng tắp", "Vuông vắn", "Đẹp đẽ"]),
        ("递", "Đưa, chuyền qua", ["Giữ lại", "Vứt đi", "Lấy về"]),
        ("脑袋", "Đầu", ["Ngực", "Răng", "Lưng"]),
        ("女士", "Quý bà, quý cô", ["Nam giới", "Trẻ em", "Học sinh"]),
        ("叙述", "Thuật lại, kể lại", ["Lắng nghe", "Im lặng", "Dự đoán"]),
        ("居然", "Lại, không ngờ (kinh ngạc)", ["Đương nhiên", "Tất nhiên", "Có lẽ"]),
        ("催", "Thúc giục, hối thúc", ["Trì hoãn", "Chờ đợi", "Ngừng lại"]),
        ("等待", "Đợi, chờ", ["Thúc giục", "Rời đi", "Chạy trốn"]),
        ("蚊子", "Con muỗi", ["Con ruồi", "Con kiến", "Con ong"]),
        ("半夜", "Nửa đêm", ["Buổi sáng", "Giữa trưa", "Hoàng hôn"]),
        ("叮", "Đốt, chích (côn trùng)", ["Vuốt ve", "Liếm", "Thổi"]),
        ("老婆", "Vợ (khẩu ngữ)", ["Chồng", "Mẹ", "Con gái"]),
        ("吵", "Làm ồn, ồn ào", ["Yên tĩnh", "Trật tự", "Thì thầm"]),
        ("项", "Hạng mục, giải thưởng", ["Con đường", "Bức tranh", "Bài hát"]),
        ("患难与共", "Hoạn nạn có nhau", ["Chia rẽ", "Xem như người dưng", "Ghen tị"]),
        ("脖子", "Cổ", ["Thắt lưng", "Lông mày", "Răng"]),
        ("胸", "Ngực", ["Cổ", "Bờ vai", "Ngón tay"]),
        ("腰", "Lưng / Thắt lưng", ["Đầu", "Ngực", "Lông mày"]),
        ("后背", "Tấm lưng", ["Bụng", "Mặt", "Ngón tay"]),
        ("眉毛", "Lông mày", ["Tóc", "Mũi", "Tai"]),
        ("嗓子", "Cổ họng / Giọng nói", ["Răng", "Lưỡi", "Mắt"]),
        ("牙齿", "Răng", ["Môi", "Cổ", "Vai"]),
        ("突发", "Bột phát, đột ngột xảy ra", ["Dần dần", "Từ từ", "Kế hoạch"]),
        ("重病", "Bệnh nặng", ["Bệnh nhẹ", "Khỏe mạnh", "Bị thương nhẹ"]),
        ("照顾", "Chăm sóc", ["Bỏ mặc", "Đánh đập", "Trêu chọc"]),
        ("放弃", "Từ bỏ", ["Kiên trì", "Giữ lại", "Tiếp tục"]),
        ("后半夜", "Nửa đêm về sáng", ["Buổi sáng sớm", "Chiều tối", "Giữa trưa"])
    ]
    
    for item in type_a_base:
        hanzi, correct_m, wrong_list = item[0], item[1], item[2]
        opts = [correct_m] + wrong_list
        random.seed(len(questions) + 42)
        random.shuffle(opts)
        questions.append({
            "type": "Nghĩa của chữ Hán",
            "prompt": f"Chữ Hán 『 **{hanzi}** 』 có nghĩa là gì?",
            "options": opts,
            "answer": correct_m
        })

    # 50 Questions Type B: Hanzi from Meaning
    type_b_base = [
        ("Chi tiết", "细节", ["电台", "对比", "评委"]),
        ("Đài phát thanh", "电台", ["细节", "婚姻", "项"]),
        ("Ân ái, yêu thương nhau", "恩爱", ["吵架", "抱怨", "离婚"]),
        ("So sánh, đối chiếu", "对比", ["叙述", "催", "等待"]),
        ("Vào vòng trong", "入围", ["瘫痪", "自杀", "轮"]),
        ("Ban giám khảo", "评委", ["女士", "老婆", "蚊子"]),
        ("Như thế nào, ra sao", "如何", ["居然", "暗暗", "歪歪扭扭"]),
        ("Liệt, tàn phế", "瘫痪", ["入围", "爱护", "叮"]),
        ("Ly hôn", "离婚", ["婚姻", "恩爱", "相敬如宾"]),
        ("Tự sát", "自杀", ["抱怨", "吵架", "喊"]),
        ("Oán trách, phàn nàn", "抱怨", ["爱护", "叙述", "递"]),
        ("Yêu quý, bảo vệ", "爱护", ["抱怨", "催", "吵"]),
        ("Hôn nhân", "婚姻", ["细节", "电台", "肩膀"]),
        ("Cãi nhau", "吵架", ["恩爱", "相敬如宾", "患难与共"]),
        ("Kính trọng nhau như khách", "相敬如宾", ["患难与共", "歪歪扭扭", "不耐烦"]),
        ("Thầm, ngầm", "暗暗", ["居然", "如何", "歪歪扭扭"]),
        ("Luân phiên, đến lượt", "轮", ["靠", "喊", "伸"]),
        ("Sốt ruột, bực mình", "不耐烦", ["相敬如宾", "歪歪扭扭", "患难与共"]),
        ("Dựa, tựa, kề sát", "靠", ["伸", "递", "催"]),
        ("Bờ vai, vai", "肩膀", ["脑袋", "手指", "脖子"]),
        ("Kêu, gọi, hét", "喊", ["催", "叮", "吵"]),
        ("Duỗi, chìa ra", "伸", ["递", "靠", "轮"]),
        ("Ngón tay", "手指", ["肩膀", "脑袋", "眉毛"]),
        ("Xiêu vẹo, ngoằn ngoèo", "歪歪扭扭", ["相敬如宾", "不耐烦", "患难与共"]),
        ("Đưa, chuyền qua", "递", ["伸", "催", "靠"]),
        ("Đầu", "脑袋", ["肩膀", "脖子", "胸"]),
        ("Quý bà, quý cô", "女士", ["老婆", "评委", "电台"]),
        ("Thuật lại, kể lại", "叙述", ["对比", "抱怨", "等待"]),
        ("Lại, không ngờ (kinh ngạc)", "居然", ["如何", "暗暗", "歪歪扭扭"]),
        ("Thúc giục, hối thúc", "催", ["等待", "递", "喊"]),
        ("Đợi, chờ", "等待", ["催", "叙述", "对比"]),
        ("Con muỗi", "蚊子", ["脑袋", "手指", "肩膀"]),
        ("Nửa đêm", "半夜", ["细节", "婚姻", "电台"]),
        ("Đốt, chích (côn trùng)", "叮", ["吵", "喊", "靠"]),
        ("Vợ (khẩu ngữ)", "老婆", ["女士", "评委", "脑袋"]),
        ("Làm ồn, ồn ào", "吵", ["叮", "喊", "催"]),
        ("Hạng mục, giải thưởng", "项", ["细节", "电台", "对比"]),
        ("Hoạn nạn có nhau", "患难与共", ["相敬如宾", "歪歪扭扭", "不耐烦"]),
        ("Cổ", "脖子", ["脑袋", "肩膀", "胸"]),
        ("Ngực", "胸", ["腰", "后背", "眉毛"]),
        ("Thắt lưng, lưng", "腰", ["胸", "脖子", "嗓子"]),
        ("Tấm lưng", "后背", ["胸", "腰", "牙齿"]),
        ("Lông mày", "眉毛", ["手指", "脖子", "嗓子"]),
        ("Cổ họng / Giọng nói", "嗓子", ["牙齿", "眉毛", "脖子"]),
        ("Răng", "牙齿", ["嗓子", "眉毛", "脑袋"]),
        ("Cống hiến", "贡献", ["抱怨", "爱护", "对比"]),
        ("Cơ hội", "机会", ["细节", "婚姻", "电台"]),
        ("Hành động, cử chỉ", "动作", ["细节", "叙述", "对比"]),
        ("Tấm giấy, mảnh giấy", "纸条", ["电台", "评委", "细节"]),
        ("Môi trường", "环境", ["婚姻", "细节", "电台"])
    ]

    for item in type_b_base:
        meaning, correct_h, wrong_h_list = item[0], item[1], item[2]
        opts = [correct_h] + wrong_h_list
        random.seed(len(questions) + 99)
        random.shuffle(opts)
        questions.append({
            "type": "Chữ Hán của từ",
            "prompt": f"Từ mang nghĩa 『 **{meaning}** 』 tương ứng với Chữ Hán nào?",
            "options": opts,
            "answer": correct_h
        })

    return questions

QUESTION_BANK_100 = generate_100_question_bank()

# ==========================================
# MAIN APP HEADER
# ==========================================
st.markdown("""
<div class="header-card">
    <div class="header-title">🌸 HSK 5 Pre-class Learning Hub</div>
    <div class="header-subtitle">Khung Tự Học Từ Vựng Trọng Điểm Trước Khi Đến Lớp • 黄宝玉老师</div>
</div>
""", unsafe_allow_html=True)

# User Identification Bar & Bảng Vàng Top 3
st.markdown("#### 👤 Đăng Nhập Học Viên & 🏆 Bảng Vàng Lật Thẻ")
col_u1, col_u2 = st.columns([1.2, 1])

with col_u1:
    st.markdown("""
    <div class="user-box">
        <div style="font-weight:800; font-size:1.05rem; color:#6C5CE7; margin-bottom:8px;">
            ✍️ Nhập Họ & Tên học viên để tham gia lật thẻ:
        </div>
    """, unsafe_allow_html=True)
    input_name = st.text_input("Tên học viên:", value=st.session_state.user_name, placeholder="Ví dụ: Nguyễn Văn Ánh...", label_visibility="collapsed")
    if input_name != st.session_state.user_name:
        st.session_state.user_name = input_name.strip()
        if st.session_state.user_name and st.session_state.user_name not in st.session_state.leaderboard:
            st.session_state.leaderboard[st.session_state.user_name] = 0
        st.rerun()
    
    if st.session_state.user_name:
        st.success(f"👋 Xin chào học viên: **{st.session_state.user_name}** | Số lần lật thẻ: **{st.session_state.leaderboard.get(st.session_state.user_name, 0)}** lần")
    else:
        st.warning("⚠️ *Vui lòng điền tên trước khi sử dụng Flashcard.*")
    st.markdown("</div>", unsafe_allow_html=True)

with col_u2:
    # Sort Leaderboard Top 3
    sorted_lb = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)[:3]
    medals = ["🥇 Top 1", "🥈 Top 2", "🥉 Top 3"]
    
    lb_html = """
    <div class="leaderboard-card">
        <div class="leaderboard-title">🏆 BẢNG VÀNG LẬT THẺ (TOP 3)</div>
    """
    for rank, (name, count) in enumerate(sorted_lb):
        m_tag = medals[rank] if rank < 3 else f"#{rank+1}"
        lb_html += f"""
        <div class="leaderboard-item">
            <span><b>{m_tag}:</b> {name}</span>
            <span style="color:#6C5CE7; font-weight:800;">{count} lần</span>
        </div>
        """
    lb_html += "</div>"
    st.markdown(lb_html, unsafe_allow_html=True)

# Lesson Level Tabs
lesson_tabs = st.tabs(["📘 Bài 1: 爱的细节", "📗 Bài 2: (Sắp ra mắt)", "📙 Bài 3: (Sắp ra mắt)"])

with lesson_tabs[0]:
    # Inside Lesson 1
    sub_lesson_tabs = st.tabs(["📖 Pre-class (Tự học trước)", "📝 Bài tập (Đang cập nhật)"])
    
    with sub_lesson_tabs[0]:
        # Pre-class Sub-tabs (With Random Quiz right next to Flashcard)
        pre_class_tabs = st.tabs([
            "🃏 Flashcard Từ Vựng", 
            "🎲 Câu Hỏi Ngẫu Nhiên", 
            "🫀 Từ Bổ Sung (Cơ Thể)", 
            "🧩 Bài Tập Kiểm Tra (10 Câu)", 
            "✍️ Luyện Tập Đặt Câu"
        ])
        
        # -------------------------------------------------------------------
        # SUB-TAB 1: FLASHCARD TỪ VỰNG (CARD CLICK TO FLIP)
        # -------------------------------------------------------------------
        with pre_class_tabs[0]:
            st.markdown("##### 💡 Hướng dẫn: *Bấm trực tiếp vào khung thẻ bên dưới để Lật/Phủ thẻ!*")
            
            if not st.session_state.user_name:
                st.error("🔒 **Yêu cầu bắt buộc:** Vui lòng điền Họ & Tên của bạn ở ô phía trên trước khi bắt đầu lật thẻ!")
            else:
                total_vocab = len(VOCAB_LESSON_1)
                current_vocab = VOCAB_LESSON_1[st.session_state.flashcard_idx]

                # Progress Bar
                progress_val = (st.session_state.flashcard_idx + 1) / total_vocab
                st.progress(progress_val)
                st.caption(f"Từ {st.session_state.flashcard_idx + 1} / {total_vocab}")

                # INTERACTIVE FLIP CARD CONTAINER
                if not st.session_state.show_back:
                    # FRONT
                    st.markdown("<div class='flip-btn-style'>", unsafe_allow_html=True)
                    card_btn_label = f"🎴 [{current_vocab['type'].upper()}]\n\n{current_vocab['hanzi']}\n\n👉 (Bấm vào thẻ để lật)"
                    if st.button(card_btn_label, key="flashcard_btn_front", use_container_width=True):
                        st.session_state.show_back = True
                        # Increment Flip Count for User
                        st.session_state.leaderboard[st.session_state.user_name] = st.session_state.leaderboard.get(st.session_state.user_name, 0) + 1
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    # BACK
                    st.markdown(f"""
                    <div class="flashcard-back-box">
                        <span class="badge-tag">{current_vocab['type']}</span>
                        <div class="flashcard-hanzi" style="color: #6C5CE7;">{current_vocab['hanzi']}</div>
                        <div class="flashcard-pinyin">[{current_vocab['pinyin']}]</div>
                        <div class="flashcard-meaning">👉 {current_vocab['meaning']}</div>
                        <div class="flashcard-example">📝 <b>Ví dụ:</b> {current_vocab['example']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("🙈 (Bấm vào đây để phủ lại thẻ)", key="flashcard_btn_back", use_container_width=True):
                        st.session_state.show_back = False
                        st.rerun()

                # Navigation Controls
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    if st.button("⬅️ Từ trước", use_container_width=True):
                        st.session_state.flashcard_idx = (st.session_state.flashcard_idx - 1) % total_vocab
                        st.session_state.show_back = False
                        st.rerun()
                with col2:
                    if st.button("Từ sau ➡️", use_container_width=True):
                        st.session_state.flashcard_idx = (st.session_state.flashcard_idx + 1) % total_vocab
                        st.session_state.show_back = False
                        st.rerun()
                with col3:
                    if st.button("🎲 Ngẫu nhiên", use_container_width=True):
                        st.session_state.flashcard_idx = random.randint(0, total_vocab - 1)
                        st.session_state.show_back = False
                        st.rerun()

        # -------------------------------------------------------------------
        # SUB-TAB 2: CÂU HỎI NGẪU NHIÊN (10 CÂU / LẦN TỪ KHO 100 CÂU)
        # -------------------------------------------------------------------
        with pre_class_tabs[1]:
            st.markdown("### 🎲 Câu Hỏi Ngẫu Nhiên (Trắc nghiệm HSK 5)")
            st.info("💡 **Quy tắc:** Kho có 100 câu hỏi ngẫu nhiên. Mỗi lượt hệ thống rút 10 câu. **Nếu chọn sai, bạn không thể qua câu tiếp theo cho đến khi chọn đúng!**")

            # Initialize Random Quiz Session
            if 'quiz_random_indices' not in st.session_state:
                st.session_state.quiz_random_indices = random.sample(range(len(QUESTION_BANK_100)), 10)
                st.session_state.quiz_current_step = 0
                st.session_state.quiz_completed = False

            current_step = st.session_state.quiz_current_step
            indices = st.session_state.quiz_random_indices

            if not st.session_state.quiz_completed and current_step < 10:
                q_real_idx = indices[current_step]
                q_item = QUESTION_BANK_100[q_real_idx]

                st.progress((current_step + 1) / 10)
                st.caption(f"Câu {current_step + 1} / 10 • Dạng: {q_item['type']}")

                st.markdown(f"""
                <div class="quiz-card">
                    <div class="quiz-question">{q_item['prompt']}</div>
                </div>
                """, unsafe_allow_html=True)

                user_choice = st.radio(
                    "Chọn 1 đáp án đúng:",
                    q_item['options'],
                    key=f"rand_q_{current_step}_{q_real_idx}"
                )

                if user_choice:
                    if user_choice == q_item['answer']:
                        st.success("🎉 **Chính xác!** Bạn đã chọn đúng đáp án.")
                        
                        # Next button enabled only when correct
                        if st.button("➡️ Câu tiếp theo", type="primary", use_container_width=True):
                            if current_step + 1 < 10:
                                st.session_state.quiz_current_step += 1
                            else:
                                st.session_state.quiz_completed = True
                            st.rerun()
                    else:
                        st.error("❌ **Chưa chính xác!** Bạn phải chọn đúng đáp án mới có thể chuyển sang câu tiếp theo.")

            else:
                # COMPLETED 10 QUESTIONS
                st.balloons()
                st.markdown("""
                <div style="text-align:center; padding: 30px; background:#E6FFFA; border-radius:24px; border:2px solid #38B2AC; margin-bottom:20px;">
                    <h2 style="color:#2C7A7B; margin-bottom:10px;">🏆 HOÀN THÀNH XUẤT SẮC 10 CÂU NGẪU NHIÊN!</h2>
                    <p style="font-size:1.1rem; color:#2D3436; font-weight:700;">Bạn đã vượt qua thử thách trắc nghiệm 10 câu thành công.</p>
                </div>
                """, unsafe_allow_html=True)

                if st.button("🔄 Làm tiếp (Lấy 10 câu ngẫu nhiên mới)", type="primary", use_container_width=True):
                    st.session_state.quiz_random_indices = random.sample(range(len(QUESTION_BANK_100)), 10)
                    st.session_state.quiz_current_step = 0
                    st.session_state.quiz_completed = False
                    st.rerun()

        # -------------------------------------------------------------------
        # SUB-TAB 3: TỪ VỰNG BỔ SUNG (BỘ PHẬN CƠ THỂ)
        # -------------------------------------------------------------------
        with pre_class_tabs[2]:
            st.markdown("### 🫀 Từ vựng chủ đề: Bộ phận cơ thể (人体器官)")
            st.info("💡 **Mẹo ghi nhớ:** Tận dụng **Âm Hán Việt** để thuộc nhanh từ mới ngay tại lớp!")
            
            cols = st.columns(2)
            for idx, item in enumerate(BODY_PARTS):
                col = cols[idx % 2]
                with col:
                    st.markdown(f"""
                    <div class="body-part-card">
                        <div style="font-size:2rem; margin-bottom: 4px;">{item['icon']}</div>
                        <div class="body-part-hanzi">{item['hanzi']}</div>
                        <div style="color:#FF7675; font-weight:700; font-size:0.9rem;">[{item['pinyin']}] • Hán Việt: {item['hanviet']}</div>
                        <div style="font-size:1rem; font-weight:700; color:#2D3436;">Nghĩa: <b>{item['meaning']}</b></div>
                        <div style="font-size:0.85rem; color:#636E72; background:#F1F2F6; border-radius:8px; padding:4px; margin-top:6px;">
                            🔗 <i>{item['collocation']}</i>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        # -------------------------------------------------------------------
        # SUB-TAB 4: BÀI TẬP KIỂM TRA TỪ VỰNG (10 CÂU MỖI DẠNG)
        # -------------------------------------------------------------------
        with pre_class_tabs[3]:
            st.markdown("### 🧩 Kiểm Tra Từ Vựng Ngữ Cảnh (10 Câu Mỗi Dạng)")
            st.warning("⚠️ **Lưu ý:** Tất cả bài tập không sử dụng Phiên âm (Pinyin) để luyện phản xạ chữ Hán.")
            
            exercise_type = st.radio(
                "Chọn dạng bài tập:",
                ["1. Cloze Test (10 câu điền từ)", "2. Matching (10 cặp kết hợp từ)"],
                horizontal=True
            )
            
            if "1. Cloze Test" in exercise_type:
                st.markdown("#### 📝 Điền từ thích hợp vào chỗ trống (Trích Sách Bài Tập HSK 5):")
                
                cloze_10_questions = [
                    {
                        "q": "1. 经过详细的______，我们发现第三种方案效果最好。",
                        "options": ["对比", "抱怨", "瘫痪", "吵架"],
                        "answer": "对比",
                        "explain": "对比 (So sánh / Đối chiếu)"
                    },
                    {
                        "q": "2. 他们结婚十几年了，从来没有为任何小事______过。",
                        "options": ["爱护", "吵架", "伸", "递"],
                        "answer": "吵架",
                        "explain": "吵架 (Cãi nhau)"
                    },
                    {
                        "q": "3. 为了不打扰丈夫睡觉，她______放弃了这次比赛的机会。",
                        "options": ["居然", "如何", "歪歪扭扭", "半夜"],
                        "answer": "居然",
                        "explain": "居然 (Lại/không ngờ)"
                    },
                    {
                        "q": "4. 累的时候，她习惯把头______在丈夫的肩膀上。",
                        "options": ["靠", "喊", "催", "叮"],
                        "answer": "靠",
                        "explain": "靠 (Dựa / Tựa)"
                    },
                    {
                        "q": "5. 我们应该认真倾听对方的______，不要轻易下结论。",
                        "options": ["叙述", "蚊子", "脑袋", "手指"],
                        "answer": "叙述",
                        "explain": "叙述 (Lời thuật lại / Kể lại)"
                    },
                    {
                        "q": "6. 时间太紧了，妈妈一直在旁边的______我快点准备。",
                        "options": ["催", "轮", "递", "伸"],
                        "answer": "催",
                        "explain": "催 (Thúc giục)"
                    },
                    {
                        "q": "7. 她把写好的便条小心地______给了现场的评委。",
                        "options": ["递", "喊", "吵", "靠"],
                        "answer": "递",
                        "explain": "递 (Đưa / Chuyền qua)"
                    },
                    {
                        "q": "8. 夫妻俩在生活中互相理解、______，感情非常深厚。",
                        "options": ["爱护", "自杀", "瘫痪", "抱怨"],
                        "answer": "爱护",
                        "explain": "爱护 (Yêu quý / Bảo vệ)"
                    },
                    {
                        "q": "9. 昨晚______有蚊子叮我，害得我没睡好觉。",
                        "options": ["半夜", "如何", "歪歪扭扭", "细节"],
                        "answer": "半夜",
                        "explain": "半夜 (Nửa đêm)"
                    },
                    {
                        "q": "10. 这对夫妻共同经历了许多困难，属于真正的______夫妻。",
                        "options": ["患难与共", "相敬如宾", "歪歪扭扭", "不耐烦"],
                        "answer": "患难与共",
                        "explain": "患难与共 (Hoạn nạn có nhau)"
                    }
                ]
                
                cloze_score = 0
                for idx, q in enumerate(cloze_10_questions):
                    st.markdown(f"**{q['q']}**")
                    user_ans = st.selectbox(f"Chọn đáp án câu {idx+1}:", ["-- Chọn --"] + q['options'], key=f"cloze_10_{idx}")
                    if user_ans == q['answer']:
                        st.success(f"✅ Chính xác! Đáp án: {q['explain']}")
                        cloze_score += 1
                    elif user_ans != "-- Chọn --":
                        st.error("❌ Chưa chính xác, hãy thử lại nhé!")
                    st.divider()

            elif "2. Matching" in exercise_type:
                st.markdown("#### 🔗 Ghép Động từ (Cột trái) với Tân ngữ / Cụm từ phù hợp (Cột phải):")
                
                match_10_pairs = {
                    "1. 抱怨 (Oán trách)": "别人 / 妻子",
                    "2. 爱护 (Bảo vệ / Yêu quý)": "环境 / 公物",
                    "3. 伸出 (Chìa ra)": "手指",
                    "4. 递给 (Đưa cho)": "评委",
                    "5. 喊醒 (Kêu tỉnh)": "丈夫",
                    "6. 赶走 (Xua đuổi)": "蚊子",
                    "7. 放弃 (Từ bỏ)": "机会",
                    "8. 表达 (Biểu thị)": "感激",
                    "9. 照顾 (Chăm sóc)": "病人",
                    "10. 增加 (Gia tăng)": "奖项"
                }
                
                right_options_10 = [
                    "手指",
                    "别人 / 妻子",
                    "评委",
                    "环境 / 公物",
                    "蚊子",
                    "丈夫",
                    "感激",
                    "机会",
                    "奖项",
                    "病人"
                ]
                
                user_matches_10 = {}
                cols = st.columns(2)
                for i, (left, right_correct) in enumerate(match_10_pairs.items()):
                    with cols[0]:
                        st.write(f"**{left}**")
                    with cols[1]:
                        user_matches_10[left] = st.selectbox(f"Ghép câu {i+1}:", ["-- Chọn --"] + right_options_10, key=f"match_10_{i}")
                
                if st.button("Kiểm tra 10 kết quả ghép đôi", type="primary"):
                    correct_count = 0
                    for left, right_correct in match_10_pairs.items():
                        if user_matches_10[left] == right_correct:
                            correct_count += 1
                    if correct_count == 10:
                        st.balloons()
                        st.success("🎉 Hoàn hảo! Bạn đã ghép chính xác toàn bộ 10 cụm từ kết hợp (Collocations)!")
                    else:
                        st.warning(f"Bạn đã ghép đúng {correct_count}/10 cụm. Hãy kiểm tra và điều chỉnh lại nhé!")

        # -------------------------------------------------------------------
        # SUB-TAB 5: LUYỆN TẬP ĐẶT CÂU (SENTENCE CREATION)
        # -------------------------------------------------------------------
        with pre_class_tabs[4]:
            st.markdown("### ✍️ Diễn Đàn Đặt Câu Ngữ Cảnh")
            st.info("💡 **Nhiệm vụ:** Đọc kỹ 2–3 câu ví dụ mẫu cho mỗi từ trọng điểm, sau đó đặt **01 câu mới** theo ngữ cảnh cuộc sống/công việc của bạn. Cô Hoàng Bảo Ngọc sẽ nhận bài và sửa trên lớp!")
            
            for item in SENTENCE_MAKING_WORDS:
                st.markdown(f"#### 🔹 Từ trọng điểm: **{item['word']}** *({item['meaning']})*")
                st.markdown("**Câu ví dụ mẫu:**")
                for ex in item['examples']:
                    st.markdown(f"- 📖 *{ex}*")
                
                user_sentence = st.text_input(
                    f"Nhập câu tự đặt của bạn với từ 『{item['word']}』:", 
                    placeholder="Gõ câu tiếng Trung của bạn vào đây...",
                    key=f"input_sent_{item['word']}"
                )
                
                if user_sentence:
                    st.success(f"Ghi nhận câu của học viên: 『{user_sentence}』 ✅ (Sẽ được giáo viên sửa lỗi trên lớp)")
                st.divider()

    with sub_lesson_tabs[1]:
        st.markdown("""
        <div style="text-align:center; padding: 40px; background:#FFF; border-radius:20px; border: 2px dashed #CBD5E1;">
            <div style="font-size:3rem;">⏳</div>
            <h3 style="color:#64748B;">Nội dung Bài Tập Trên Lớp & Về Nhà</h3>
            <p style="color:#94A3B8;">Sẽ được mở khóa sau khi hoàn thành buổi học trên lớp cùng giáo viên!</p>
        </div>
        """, unsafe_allow_html=True)

with lesson_tabs[1]:
    st.info("🚧 Bài 2 đang được biên soạn nội dung...")

with lesson_tabs[2]:
    st.info("🚧 Bài 3 đang được biên soạn nội dung...")

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class="footer">
    黄宝玉老师
</div>
""", unsafe_allow_html=True)
