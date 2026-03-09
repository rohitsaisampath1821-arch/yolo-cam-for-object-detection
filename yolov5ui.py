import streamlit as st
import base64
from pathlib import Path

img_path = Path("images/Gym full figma (Community).png")
if img_path.exists():
    with open(img_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
    bg_url = f"data:image/png;base64,{img_base64}"
else:
    bg_url = "url('images/Gym full figma (Community).png')"

st.markdown(f"""
    <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
        
        .stApp {{
            background-image: 
                linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)),
                url('{bg_url}');
            background-attachment: fixed;
            background-size: 100% 100%;
            background-position: bottom;
            background-repeat: no-repeat;
            font-family: 'Poppins', sans-serif;
        }}
        
        [data-testid="stSidebar"] {{
            background: rgba(0, 0, 0, 0.5) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(147, 112, 219, 0.3) !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
            overflow: hidden !important;
        }}
        
        [data-testid="stSidebar"] > div:first-child {{
            background: rgba(0, 0, 0, 0.5) !important;
        }}
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
            color: #fff !important;
        }}
        
        .sidebar-title {{
            color: #fff;
            font-size: 25px;
            font-weight: 500;
            text-align: center;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
        }}
        
        [data-testid="stRadio"] {{
            margin-top: 20px !important;
            padding: 0 10px !important;
        }}
        
        [data-testid="stRadio"] > div {{
            gap: 12px !important;
        }}
        
        [data-testid="stRadio"] input[type="radio"] {{
            display: none !important;
        }}
        
        [data-testid="stRadio"] label > div:first-child {{
            display: none !important;
        }}
        
        [data-testid="stRadio"] label {{
            color: #fff !important;
            font-size: 18px !important;
            font-weight: 400 !important;
            padding: 12px 18px !important;
            margin: 0 !important;
            border-radius: 10px !important;
            width: 100% !important;
            background: rgba(0, 0, 0, 0.4) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            box-shadow: 0 4px 15px 0 rgba(0, 0, 0, 0.3) !important;
            transition: all 0.3s ease !important;
        }}
        
        [data-testid="stRadio"] label:hover {{
            background: rgba(0, 0, 0, 0.6) !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
            box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.5) !important;
            transform: translateY(-2px) !important;
            cursor: pointer !important;
        }}
        
        [data-testid="stRadio"] label[data-checked="true"] {{
            background: rgba(147, 112, 219, 0.4) !important;
            border: 1px solid rgba(147, 112, 219, 0.6) !important;
            box-shadow: 0 6px 20px 0 rgba(147, 112, 219, 0.4) !important;
        }}
        
        .glass-container {{
            background: rgba(0, 0, 0, 0.9);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 15px;
            border: none;
            padding: 1rem 2rem;
            margin: -2rem auto 1rem auto;
            max-width: fit-content;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }}
        
        .custom-title {{
            color: #FFFFFF;
            text-align: center;
            font-size: 1.8rem;
            font-weight: 600;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            padding: 0;
            margin: 0;
            letter-spacing: 1px;
            text-transform: uppercase;
            background: linear-gradient(135deg, #000000 0%, #00FF00 50%, #00DD00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            white-space: nowrap;
        }}
        
        .stMarkdown {{
            color: #FFFFFF;
        }}
        
        p, div, span {{
            color: #FFFFFF !important;
        }}
        
        [data-testid="stCameraInput"] {{
            background-color: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            border: 1px solid rgba(147, 112, 219, 0.5);
        }}
        
        [data-testid="stCameraInput"] button {{
            background-color: #9370DB !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 600 !important;
            border: none !important;
        }}
        
        [data-testid="stCameraInput"] button:hover {{
            background-color: #b093e8 !important;
        }}
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <div class="sidebar-title">Menu</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio("", ["⌂ Home", "◉ Description", "✉ Contact Us"], label_visibility="collapsed")

st.markdown(
    "<div class='glass-container'><h1 class='custom-title'>YOLOV5 OBJECT DETECTION</h1></div>",
    unsafe_allow_html=True
)

if page == "⌂ Home":
    st.markdown(
        "<p style='color:#FFFFFF; text-align:center; font-size:1.2rem; padding:0.5rem 1.5rem; margin-top:-1rem; font-style:italic; border-bottom:2px solid #666666;'>Advanced Computer Vision With Python Web App With Streamlit</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("START", key="start_btn", use_container_width=True):
            st.session_state.camera_started = True
            st.success("Camera Started!")

    with col3:
        if st.button("⏹ STOP", key="stop_btn", use_container_width=True):
            st.session_state.camera_started = False
            st.info("Camera Stopped!")

    if st.session_state.get('camera_started', False):
        picture = st.camera_input("Take a picture")
        if picture:
            st.image(picture, use_column_width=True)

elif page == "◉ Description":
    st.markdown("""
    <div style='background-color: rgba(0, 0, 0, 0.6); border: 2px solid #9370DB; border-radius: 15px; padding: 2rem; margin-top: 2rem;'>
        <h2 style='color:#00D4FF; text-align:center;'>🔍 YOLOv5 Face Detection</h2>
        
        <p style='color:#FFFFFF; font-size:1.1rem; line-height:1.8;'>
            <strong style='color:#FF1493;'>What is YOLOv5?</strong><br>
            YOLOv5 is a state-of-the-art real-time object detection model that can identify faces with high accuracy and speed.
        </p>
        
        <p style='color:#FFFFFF; font-size:1.1rem; line-height:1.8;'>
            <strong style='color:#FF1493;'>Key Features:</strong><br>
            ✓ Real-time detection<br>
            ✓ High accuracy<br>
            ✓ Lightweight model<br>
            ✓ Works on multiple platforms
        </p>
        
        <p style='color:#FFFFFF; font-size:1.1rem; line-height:1.8;'>
            <strong style='color:#FF1493;'>How it works:</strong><br>
            The model analyzes video frames and identifies faces using advanced neural networks trained on millions of images.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "✉ Contact Us":
    st.markdown("""
    <div style='background-color: rgba(0, 0, 0, 0.6); border: 2px solid #9370DB; border-radius: 15px; padding: 2rem; margin-top: 2rem;'>
        <h2 style='color:#00D4FF; text-align:center;'>📧 Get In Touch</h2>
        
        <div style='text-align:center; margin: 1.5rem 0;'>
            <p style='color:#FFFFFF; font-size:1.1rem;'>
                <strong style='color:#FF1493;'>Email:</strong><br>
                <span style='color:#4169E1;'>contact@computervision.com</span>
            </p>
        </div>
        
        <div style='text-align:center; margin: 1.5rem 0;'>
            <p style='color:#FFFFFF; font-size:1.1rem;'>
                <strong style='color:#FF1493;'>Follow Us:</strong><br>
                🐦 Twitter | 📘 Facebook | 🔗 LinkedIn
            </p>
        </div>
        
        <div style='text-align:center; margin: 1.5rem 0;'>
            <p style='color:#FFFFFF; font-size:1.1rem;'>
                <strong style='color:#FF1493;'>Address:</strong><br>
                <span style='color:#4169E1;'>Tech City, Innovation Hub</span>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)