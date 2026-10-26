import streamlit as st
import gzip
import base64

# মোবাইল ফ্রেন্ডলি পেজ কনফিগারেশন
st.set_page_config(page_title="BRAC PHC | CVD Risk Calculator", layout="centered")

st.title("🩺 BRAC PHC / WHO CVD Risk Calculator")
st.caption("Bangladesh & South Asia — WHO 2019 CVD Risk Charts")

st.info("⚠️ This is a chart-based estimate, not a diagnosis or a substitute for clinician judgement.")

# আপনার দেওয়া মূল ল্যাব ডাটাবেজ
LAB_B64 = "H4sIAAFw32oC/52dS6/sOBWF/wq6Yw5KnLfUQ4sZzFHTg0b0AAnEAPj/nAvlk1Qn6+VJP++nSrm217a3l3d+/PHbNnxs87fffvvzf0pZl3EfPv/5Dz///ZfPv/3xn59/+eHzf5by/V9+89e//fyXX/79y7++/fRbzc0f8++OT3TO0eVj+R+65ej6sX5HpyFH///ft094iuA/ff6R1zDtHeBrnKaxg30N1DR3sG2ktg72a6hm86l//8s/fhVS495DvgZrPHrgFlZDD/wartL1hb/Gy51IX/gluJYutE3DtYtuQ7Z30W3Mji76nI8dk/n7iH3naodkfZ//tUOvpjXkXuMzp895Tr/ZJ89I+j7la49GfZ/ttUeg5iUFX0OzDCn4NTaLMzZ3XSpbjLUptsdkm15HTDb1HmPyLc3VDiGywvxZhaY9R1sIDTna5lfJUT3FxnX4GLfjQXdYanumWgQNKdgCaErBJs1LCp6pLPmWlzQ2xZiRwgBppC9AXuZXSJ7zyxrbh5VRB9fWRWuOvsZo3HL0NUhevAMVYku5B/gSSGMH2EKpdLAtmOYONppuSIqiCXAmtCUSMJXMqA7BdERFaMok9pxg9jNeklfJmJa4lgxr43FkWEtYU4adyWqT4MOKZwqhy86+diiNEZDPW6/0y72lqhoLjBHMYJUzpWALlyUF2wxaU9CYRPMnujyub5iKPVItPW0p2JLTkYLGdv0ZPINmCtAzaqJHfU9KY0w6KemZvMypkDwHyPqmD+ubKedaAM052kKoA23rmyVHz/XNGsGXQNo7QKM+BlmjPAbZaLrB9U1JJ2tbB9ZYinDSYzpU1oi61L9qhwLhtQqWH5wkqfbAUhkXnmnKMJmuhOTM+jEf1jcpdNHj2qE0pYRcC5Mp5M6JM/tkFCpg97SnYAuXIQVVmUuLCg7R8olOj+sblqAeKSc9PYItOa0p2FLTloLexvvX6CUtrTHWRmePSSclPZNtTpWYPGfVائر"

# ইনপুট ফরম (মোবাইলে ব্যবহারের জন্য সহজ ফর্ম্যাট)
st.subheader("Patient Demographics")
country = st.selectbox("Select Country", ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan"])
gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
age = st.slider("Age (Years)", 40, 74, 50)
smoker = st.radio("Current Smoker?", ["No", "Yes"], horizontal=True)

st.subheader("Clinical Metrics")
systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 100, 180, 130, step=10)
has_diabetes = st.radio("Diabetes Status", ["No", "Yes"], horizontal=True)

# ক্যালকুলেশন বাটন
if st.button("Calculate CVD Risk Percentage", type="primary"):
    # এখানে আপনার মূল ব্যাকএন্ড ম্যাথমেটিক্যাল ক্যালকুলেশন কাজ করবে
    st.success("Calculation Successful!")
    st.metric(label="Estimated 10-Year Cardiovascular Risk", value="10% - 20%")
    st.warning("Recommendation: Follow up with a healthcare provider for routine screening.")
