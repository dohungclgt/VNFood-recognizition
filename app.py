import streamlit as st
from PIL import Image
import io, os, shutil
from core.gemini_handler import analyze_food
from core.image_tools import draw_bounding_box
from core.utils import get_cache_key, load_cache, save_cache

# ==============================
# ⚙️ Page setup
# ==============================
st.set_page_config(page_title="🍜 Vietnamese Food Classifier", layout="wide")

# ==============================
# 💄 Custom CSS
# ==============================
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            color: #b33c00;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 15px;
            margin-bottom: 30px;
        }
        .result-card {
            background-color: #fffaf5;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        .stButton>button {
            border-radius: 10px;
            font-weight: 600;
            color: white;
            background-color: #b33c00;
        }
        .stButton>button:hover {
            background-color: #8f2f00;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🍜 Vietnamese Food Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered Vietnamese cuisine recognition and description</div>', unsafe_allow_html=True)

# ==============================
# 🧭 Sidebar - Settings
# ==============================
st.sidebar.header("⚙️ Settings / Cài đặt")

language = st.sidebar.radio("🌐 Language / Ngôn ngữ", ["English", "Tiếng Việt"])
region = st.sidebar.selectbox(
    "📍 Region / Vùng miền",
    ["Northern Vietnam (Miền Bắc)", "Central Vietnam (Miền Trung)", "Southern Vietnam (Miền Nam)"]
)

colA, colB = st.sidebar.columns(2)

with colA:
    if st.button("🧹 Clear Cache / Xóa Cache"):
        cache_dir = "cache"
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
            os.makedirs(cache_dir, exist_ok=True)
        st.sidebar.success("✅ Cache cleared / Đã xóa cache!")

with colB:
    reload_flag = st.button("🔄 Reload Analysis / Phân tích lại")

# ==============================
# 📤 Upload Image
# ==============================
uploaded = st.file_uploader("📸 Upload a Vietnamese food image / Tải lên ảnh món ăn Việt Nam", type=["jpg", "jpeg", "png"])

# Nút phân tích
analyze_clicked = st.button("🔍 Analyze / Phân tích", use_container_width=True)

# ==============================
# 🧠 AI Processing
# ==============================
if uploaded:
    image = Image.open(uploaded)
    buf = io.BytesIO()
    image.save(buf, format="JPEG")
    image_bytes = buf.getvalue()

    cache_key = get_cache_key(image_bytes)
    result = None

    if not reload_flag:
        result = load_cache(cache_key)

    col1, col2 = st.columns([1, 1.2])

    if analyze_clicked or reload_flag:
        with st.spinner("🧠 Analyzing your food..." if language == "English" else "🧠 Đang phân tích món ăn..."):
            result = analyze_food(image_bytes, region, language)
            save_cache(cache_key, result)
    elif result:
        st.toast("✅ Loaded from cache" if language == "English" else "✅ Đã tải từ bộ nhớ cache")
    else:
        st.info("👆 Please click **Analyze / Phân tích** to start recognition." if language == "English"
                else "👆 Hãy bấm **Phân tích** để bắt đầu nhận diện món ăn.")

    # ==============================
    # 🖼️ Display Results
    # ==============================
    if result:
        bbox = result.get("bounding_box", {})
        processed_img = draw_bounding_box(image_bytes, bbox)

        with col1:
            st.image(processed_img, caption="📷 Detected Food" if language == "English" else "📷 Ảnh món ăn", use_column_width=True)

        with col2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)

            if "error" in result:
                st.error("❌ " + (result["error"] if language == "English" else "❌ Lỗi khi phân tích ảnh"))
            elif "raw_output" in result:
                if language == "English":
                    st.warning("⚠️ Unstructured response received:")
                    st.text(result["raw_output"])
                else:
                    st.warning("⚠️ Dữ liệu trả về không đúng định dạng:")
                    st.text(result["raw_output"])
            else:
                if language == "English":
                    st.markdown(f"### 🍽️ **Dish:** {result.get('food_name', 'Unknown')}")
                    st.markdown(f"**🎯 Confidence:** {result.get('confidence', '?')}%")
                    st.markdown(f"**🗺️ Region:** {result.get('region', region)}")
                    st.markdown(f"### 📖 Description\n{result.get('description', 'No description available.')}")
                    st.markdown(f"### 🍳 How to Cook\n{result.get('how_to_cook', 'No information.')}")
                    st.markdown(f"### 🥢 How to Eat\n{result.get('how_to_eat', 'No information.')}")
                else:
                    st.markdown(f"### 🍽️ **Phát hiện món ăn:** {result.get('food_name', 'Không xác định')}")
                    st.markdown(f"**🎯 Độ chính xác:** {result.get('confidence', '?')}%")
                    st.markdown(f"**🗺️ Vùng miền:** {result.get('region', region)}")
                    st.markdown(f"### 📖 Mô tả món ăn\n{result.get('description', 'Không có mô tả.')}")
                    st.markdown(f"### 🍳 Cách chế biến\n{result.get('how_to_cook', 'Không có dữ liệu.')}")
                    st.markdown(f"### 🥢 Cách ăn\n{result.get('how_to_eat', 'Không có dữ liệu.')}")
            st.markdown('</div>', unsafe_allow_html=True)
