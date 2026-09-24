import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & PASTEL CUTE STYLING
# ==========================================
st.set_page_config(
    page_title="HSK 5 Pre-class Web App | 黄宝玉老师",
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
        padding-top: 1.8rem;
        padding-bottom: 3rem;
        max-width: 950px;
    }

    /* Header Banner */
    .header-card {
        background: linear-gradient(135deg, #FFE5EC 0%, #F0E6FF 100%);
        border-radius: 24px;
        padding: 24px 28px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(255, 182, 193, 0.3);
        border: 2px solid #FFF;
        margin-bottom: 24px;
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #6C5CE7;
        margin-bottom: 6px;
    }
    .header-subtitle {
        font-size: 1.05rem;
        font-weight: 600;
        color: #B2BEC3;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #EFEAE1;
        padding: 6px;
        border-radius: 18px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 14px;
        color: #636E72;
        font-weight: 700;
        font-size: 0.95rem;
        border: none;
        padding: 0px 16px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF !important;
        color: #6C5CE7 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    /* Flashcard Style */
    .flashcard-box {
        background: #FFFFFF;
        border: 3px solid #E8E0D5;
        border-radius: 24px;
        padding: 36px 20px;
        text-align: center;
        min-height: 240px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 10px 25px rgba(108, 92, 231, 0.08);
        transition: all 0.3s ease;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .flashcard-hanzi {
        font-size: 3.5rem;
        font-weight: 800;
        color: #2D3436;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }
    .flashcard-pinyin {
        font-size: 1.4rem;
        font-weight: 700;
        color: #FF7675;
        margin-bottom: 8px;
    }
    .flashcard-meaning {
        font-size: 1.25rem;
        font-weight: 700;
        color: #00B894;
        margin-bottom: 12px;
    }
    .flashcard-example {
        font-size: 1rem;
        font-weight: 600;
        color: #636E72;
        background: #F8F9FA;
        padding: 8px 16px;
        border-radius: 12px;
        border-left: 4px solid #6C5CE7;
    }

    /* Badge & Cards */
    .badge-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 700;
        background-color: #FFEAA7;
        color: #D63031;
        margin-bottom: 10px;
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
        font-size: 1.8rem;
        font-weight: 800;
        color: #6C5CE7;
    }
    .body-part-meaning {
        font-size: 0.95rem;
        font-weight: 700;
        color: #2D3436;
    }

    /* Custom Input & Buttons */
    .stButton>button {
        border-radius: 16px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 10px 20px !important;
        transition: all 0.2s ease !important;
    }
    
    /* Footer Style */
    .footer {
        text-align: center;
        padding: 30px 10px 10px 10px;
        font-size: 1.1rem;
        font-weight: 800;
        color: #A29BFE;
        letter-spacing: 1px;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

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
# MAIN APP HEADER
# ==========================================
st.markdown("""
<div class="header-card">
    <div class="header-title">🌸 HSK 5 Pre-class Learning Hub</div>
    <div class="header-subtitle">Khung Tự Học Từ Vựng Trọng Điểm Trước Khi Đến Lớp</div>
</div>
""", unsafe_allow_html=True)

# Lesson Level Tabs
lesson_tabs = st.tabs(["📘 Bài 1: 爱的细节", "📗 Bài 2: (Sắp ra mắt)", "📙 Bài 3: (Sắp ra mắt)"])

with lesson_tabs[0]:
    # Inside Lesson 1
    sub_lesson_tabs = st.tabs(["📖 Pre-class (Tự học trước)", "📝 Bài tập (Đang cập nhật)"])
    
    with sub_lesson_tabs[0]:
        # Pre-class Sub-tabs
        pre_class_tabs = st.tabs([
            "🃏 Flashcard Từ Vựng", 
            "🫀 Từ Bổ Sung (Cơ Thể)", 
            "🧩 Bài Tập Kiểm Tra", 
            "✍️ Luyện Tập Đặt Câu"
        ])
        
        # -------------------------------------------------------------------
        # TAB 1: FLASHCARD TỪ VỰNG
        # -------------------------------------------------------------------
        with pre_class_tabs[0]:
            st.markdown("##### 💡 Hướng dẫn: *Mặt trước chỉ hiển thị Chữ Hán. Click 'Lật thẻ' để xem Phiên âm, Nghĩa & Ví dụ.*")
            
            if 'flashcard_idx' not in st.session_state:
                st.session_state.flashcard_idx = 0
            if 'show_back' not in st.session_state:
                st.session_state.show_back = False

            total_vocab = len(VOCAB_LESSON_1)
            current_vocab = VOCAB_LESSON_1[st.session_state.flashcard_idx]

            # Progress Bar
            progress_val = (st.session_state.flashcard_idx + 1) / total_vocab
            st.progress(progress_val)
            st.caption(f"Từ {st.session_state.flashcard_idx + 1} / {total_vocab}")

            # Flashcard Display
            if not st.session_state.show_back:
                # FRONT OF CARD
                st.markdown(f"""
                <div class="flashcard-box">
                    <span class="badge-tag">{current_vocab['type']}</span>
                    <div class="flashcard-hanzi">{current_vocab['hanzi']}</div>
                    <p style="color:#B2BEC3; font-weight:700;">(Chạm 'Lật thẻ' bên dưới để xem đáp án)</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                # BACK OF CARD
                st.markdown(f"""
                <div class="flashcard-box" style="border-color: #A29BFE;">
                    <span class="badge-tag">{current_vocab['type']}</span>
                    <div class="flashcard-hanzi" style="color: #6C5CE7;">{current_vocab['hanzi']}</div>
                    <div class="flashcard-pinyin">[{current_vocab['pinyin']}]</div>
                    <div class="flashcard-meaning">👉 {current_vocab['meaning']}</div>
                    <div class="flashcard-example">📝 <b>Cụm từ / Ví dụ:</b> {current_vocab['example']}</div>
                </div>
                """, unsafe_allow_html=True)

            # Controls
            col1, col2, col3, col4 = st.columns([1, 1.5, 1, 1])
            with col1:
                if st.button("⬅️ Từ trước", use_container_width=True):
                    st.session_state.flashcard_idx = (st.session_state.flashcard_idx - 1) % total_vocab
                    st.session_state.show_back = False
                    st.rerun()
            with col2:
                btn_label = "🙈 Phủ thẻ" if st.session_state.show_back else "🔄 Lật thẻ"
                if st.button(btn_label, use_container_width=True, type="primary"):
                    st.session_state.show_back = not st.session_state.show_back
                    st.rerun()
            with col3:
                if st.button("Từ sau ➡️", use_container_width=True):
                    st.session_state.flashcard_idx = (st.session_state.flashcard_idx + 1) % total_vocab
                    st.session_state.show_back = False
                    st.rerun()
            with col4:
                if st.button("🎲 Ngẫu nhiên", use_container_width=True):
                    st.session_state.flashcard_idx = random.randint(0, total_vocab - 1)
                    st.session_state.show_back = False
                    st.rerun()

        # -------------------------------------------------------------------
        # TAB 2: TỪ VỰNG BỔ SUNG (BỘ PHẬN CƠ THỂ)
        # -------------------------------------------------------------------
        with pre_class_tabs[1]:
            st.markdown("### 🫀 Từ vựng chủ đề: Bộ phận cơ thể (人体器官)")
            st.info("💡 **Mẹo ghi nhớ:** Tận dụng **Âm Hán Việt** để thuộc nhanh từ mới ngay tại lớp!")
            
            # 2 Columns Grid for Mobile Friendliness
            cols = st.columns(2)
            for idx, item in enumerate(BODY_PARTS):
                col = cols[idx % 2]
                with col:
                    st.markdown(f"""
                    <div class="body-part-card">
                        <div style="font-size:2rem; margin-bottom: 4px;">{item['icon']}</div>
                        <div class="body-part-hanzi">{item['hanzi']}</div>
                        <div style="color:#FF7675; font-weight:700; font-size:0.9rem;">[{item['pinyin']}] • Hán Việt: {item['hanviet']}</div>
                        <div class="body-part-meaning">Nghĩa: <b>{item['meaning']}</b></div>
                        <div style="font-size:0.85rem; color:#636E72; background:#F1F2F6; border-radius:8px; padding:4px; margin-top:6px;">
                            🔗 <i>{item['collocation']}</i>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        # -------------------------------------------------------------------
        # TAB 3: BÀI TẬP KIỂM TRA TỪ VỰNG (PURE HANZI - NO PINYIN)
        # -------------------------------------------------------------------
        with pre_class_tabs[2]:
            st.markdown("### 🧩 Kiểm Tra Từ Vựng Ngữ Cảnh (Contextual Quiz)")
            st.warning("⚠️ **Lưu ý:** Bài tập dưới đây không sử dụng Phiên âm (Pinyin) để luyện phản xạ mặt chữ Hán.")
            
            exercise_type = st.radio(
                "Chọn dạng bài tập:",
                ["1. Cloze Test (Điền từ vào chỗ trống)", "2. Matching (Ghép đôi kết hợp từ)"],
                horizontal=True
            )
            
            if "1. Cloze Test" in exercise_type:
                st.markdown("#### 📝 Chọn từ thích hợp điền vào chỗ trống:")
                
                cloze_questions = [
                    {
                        "q": "1. 经过详细的______，我们发现第三种方案效果最好。",
                        "options": ["对比", "抱怨", "瘫痪", "吵架"],
                        "answer": "对比",
                        "explain": "对比 (So sánh / Đối chiếu): Sau khi so sánh chi tiết, chúng tôi phát hiện phương án 3 hiệu quả nhất."
                    },
                    {
                        "q": "2. 他们结婚十几年了，从来没有为任何小事______过。",
                        "options": ["爱护", "吵架", "伸", "递"],
                        "answer": "吵架",
                        "explain": "吵架 (Cãi nhau): Họ kết hôn mười mấy năm rồi, chưa từng vì chuyện nhỏ mà cãi nhau."
                    },
                    {
                        "q": "3. 为了不打扰丈夫睡觉，她______放弃了这次比赛的机会。",
                        "options": ["居然", "如何", "歪歪扭扭", "半夜"],
                        "answer": "居然",
                        "explain": "居然 (Lại/không ngờ): Biểu thị sự kinh ngạc ngoài dự đoán."
                    },
                    {
                        "q": "4. 累的时候，她习惯把头______在丈夫的肩膀上。",
                        "options": ["靠", "喊", "催", "叮"],
                        "answer": "靠",
                        "explain": "靠 (Dựa / Tựa): Tựa đầu vào bờ vai của chồng."
                    }
                ]
                
                score = 0
                for idx, q in enumerate(cloze_questions):
                    st.markdown(f"**{q['q']}**")
                    user_ans = st.selectbox(f"Chọn đáp án câu {idx+1}:", ["-- Chọn --"] + q['options'], key=f"cloze_{idx}")
                    if user_ans == q['answer']:
                        st.success(f"✅ Chính xác! {q['explain']}")
                        score += 1
                    elif user_ans != "-- Chọn --":
                        st.error("❌ Chưa chính xác, hãy thử lại nhé!")
                    st.divider()

            elif "2. Matching" in exercise_type:
                st.markdown("#### 🔗 Ghép Động từ (Cột trái) với Tân ngữ / Cụm từ phù hợp (Cột phải):")
                
                match_pairs = {
                    "1. 抱怨 (Oán trách)": "别人 / 妻子 (Người khác / Vợ)",
                    "2. 爱护 (Bảo vệ / Yêu quý)": "环境 / 公物 (Môi trường / Đồ công cộng)",
                    "3. 伸出 (Chìa ra)": "手指 (Ngón tay)",
                    "4. 递给 (Đưa cho)": "评委 (Ban giám khảo)"
                }
                
                options_right = [
                    "手指 (Ngón tay)",
                    "别人 / 妻子 (Người khác / Vợ)",
                    "评委 (Ban giám khảo)",
                    "环境 / 公物 (Môi trường / Đồ công cộng)"
                ]
                
                user_matches = {}
                cols = st.columns(2)
                for i, (left, right_correct) in enumerate(match_pairs.items()):
                    with cols[0]:
                        st.write(f"**{left}**")
                    with cols[1]:
                        user_matches[left] = st.selectbox(f"Ghép với {i+1}:", ["-- Chọn --"] + options_right, key=f"match_{i}")
                
                if st.button("Kiểm tra kết quả ghép đôi", type="primary"):
                    correct_count = 0
                    for left, right_correct in match_pairs.items():
                        if user_matches[left] == right_correct:
                            correct_count += 1
                    if correct_count == len(match_pairs):
                        st.balloons()
                        st.success("🎉 Xuất sắc! Bạn đã ghép chính xác tất cả các cụm từ kết hợp (Collocations)!")
                    else:
                        st.warning(f"Bạn đã ghép đúng {correct_count}/{len(match_pairs)} cụm. Hãy kiểm tra lại nhé!")

        # -------------------------------------------------------------------
        # TAB 4: LUYỆN TẬP ĐẶT CÂU (SENTENCE CREATION)
        # -------------------------------------------------------------------
        with pre_class_tabs[3]:
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
                    st.success(f"Âm thầm ghi nhận câu của bạn: 『{user_sentence}』 ✅ (Sẽ được giáo viên sửa lỗi trên lớp)")
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
    🌸 黄宝玉老师 • HSK 5 Standard Course 🌸
</div>
""", unsafe_allow_html=True)
