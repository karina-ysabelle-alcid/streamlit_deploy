# Dependencies and Libraries
# from sklearn.utils import resample
import streamlit as st
import numpy as np
import pandas as pd
# import sklearn as skl
# import matplotlib as plt
# import seaborn as sns
# from PIL import Image
from pathlib import Path

# Classifer Library
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
# from sklearn.metrics import classification_report
import category_encoders as ce

# Cosine Similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ============================================================
# Result Function : Cosine Similarity Implementation
def cosine_implementation(user_data):
    # m_path = Path(__file__).parent.parent
    # path = m_path.joinpath('dataset/clean_data.csv')
    # df = pd.read_csv(str(path))
    df = pd.read_csv("dataset/clean_data.csv")

    df = df.loc[df['Current contraceptive method'] != 'Not using']
    df.drop(columns=['Unnamed: 0'], axis=1)

    df['Current contraceptive method'] = df['Current contraceptive method'].replace(
        'Calendar or rhythm method/Periodic abstinence', 'Periodic abstinence', regex=True)
    df['Current contraceptive method'] = df['Current contraceptive method'].replace(
        'Implants/Norplant', 'Implants', regex=True)
    df['Current contraceptive method'] = df['Current contraceptive method'].replace(
        'Mucus/Billing/Ovulation', 'Ovulation', regex=True)

    vectorizer = TfidfVectorizer()
    # convert all columns to str
    for column_name in df.columns:
        df[column_name] = df[column_name].astype(str)

    for column_name in user_data.columns:
        user_data[column_name] = user_data[column_name].astype(str)

    # Constructing the corpus
    corp = df.to_numpy()
    corpus = corp.flatten().tolist()

    # Fitting the vectorizer using the corpus
    trsfm = vectorizer.fit_transform(corpus)

    # Generating the prediction through cosine similarity
    user_data = user_data.values.flatten().tolist()
    user_data = vectorizer.transform(user_data).toarray()
    index = np.argmax(cosine_similarity(trsfm, user_data))
    return df.iloc[index]['Current contraceptive method']

# ============================================================
# Result Function : Random Forest Implementation
def predict(user_data):
    m_path = Path(__file__).parent
    path = m_path.joinpath('dataset/clean_data.csv')
    df = pd.read_csv(str(path))

    df = df.loc[df['Current contraceptive method'] != 'Not using']
    df['Current contraceptive method'] = df['Current contraceptive method'].replace(
        'Calendar or rhythm method/Periodic abstinence', 'Periodic abstinence', regex=True)
    df['Current contraceptive method'] = df['Current contraceptive method'].replace(
        'Implants/Norplant', 'Implants', regex=True)
    df['Current contraceptive method'] = df['Current contraceptive method'].replace(
        'Mucus/Billing/Ovulation', 'Ovulation', regex=True)

    columns = ["Current age",
               'Age of respondent at 1st birth',
               'Age at first menstrual period',
               'Recent sexual activity',
               'Region',
               'Type of place of residence',
               'Current marital status',
               'Births in last five years',
               'Births in last three years',
               'Births in past year',
               'Currently pregnant',
               'Total number all pregnacies',
               'Decision maker for using contraception',
               'Decision maker for not using contraception',
               'Preferred future method',
               'Smokes cigarettes',
               'Smokes pipe full of tobacco',
               'Chews tobacco',
               'Snuffs by nose',
               'Smokes kreteks',
               'Smokes cigars, cheroots or cigarillos',
               'Smokes water pipe',
               'Snuff by mouth',
               'Chews betel quid with tobacco',
               "Husbands desire for children",
               'Exposure',
               'Unmet need',
               'Unmet need (definition 2)',
               'Unmet need for contraception (definition 3)'
               ]
    X = df[columns]
    y = df['Current contraceptive method']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)

    X_encoder = ce.OneHotEncoder(cols=[
        'Recent sexual activity',
        'Region',
        'Type of place of residence',
        'Current marital status',
        'Currently pregnant',
        'Decision maker for using contraception',
        'Decision maker for not using contraception',
        'Preferred future method',
        'Smokes cigarettes',
        'Smokes pipe full of tobacco',
        'Chews tobacco',
        'Snuffs by nose',
        'Smokes kreteks',
        'Smokes cigars, cheroots or cigarillos',
        'Smokes water pipe',
        'Snuff by mouth',
        'Chews betel quid with tobacco',
        "Husbands desire for children",
        'Exposure',
        'Unmet need',
        'Unmet need (definition 2)',
        'Unmet need for contraception (definition 3)'
    ])

    # X_train = X_encoder.fit_transform(X_train)
    # X_test = X_encoder.transform(X_test)
    rf_classifier = RandomForestClassifier(n_estimators=100)
    # rf_classifier.fit(X_train, y_train)

    # Preprocess, Use Model, and Train
    model = Pipeline([("preprocessing", X_encoder),
                     ("model", rf_classifier)]).fit(X_train, y_train)
    user_encode = model.predict(user_data)

    # Retrieve and return text
    result_text = user_encode[0]
    return result_text


# ============================================================
# Show Result Function
def show_result(contraceptive_result):
    m_path = Path(__file__).parent

    img_url = f'https://raw.githubusercontent.com/RyanMNST/streamlit_deploy/main/contraceptives/{contraceptive_result}/{contraceptive_result}.png'
    text_path = m_path.joinpath(
        'contraceptives/' + contraceptive_result + '/'+contraceptive_result+'.txt')
    lines = text_path.read_text()
    f_lines = lines.encode('cp1252')
    # lines = f_lines.decode('UTF-8')
    lines = f_lines.decode('ISO 8859-1')

    st.markdown("<h1 style='text-align: center; color: black;'>" +
                contraceptive_result+"</h1>", unsafe_allow_html=True)
    st.markdown("<img src='"+img_url +
                "' style='display: block; margin-left: auto; margin-right: auto; width: 50%;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; text-align: justify;'>" +
                lines + "</p>", unsafe_allow_html=True)


def app():
    st.write("""
    # Finals System Web Application Version
    A [CS 321 | CS 322] Project - Recommender System
    """)

    with st.form("Counseling_Form"):
        # ============================================================
        # Residential Status Features
        st.markdown("**Residential Status Features**")
        rs_1, rs_2 = st.columns(2)

        with rs_1:
            residential_status = st.selectbox(
                label="Region",
                options=[
                    'Autonomous Region in Muslim Mindanao',
                    'Bicol',
                    'Cagayan Valley',
                    'Calabarzon',
                    'Caraga',
                    'Central Luzon',
                    'Central Visayas',
                    'Cordillera',
                    'Davao',
                    'Eastern Visayas',
                    'Ilocos',
                    'Mimaropa',
                    'National Capital',
                    'Northern Mindanao',
                    'Soccskargen',
                    'Western Visayas',
                    'Zamboanga Peninsula',
                ],
                index=7
            )

        with rs_2:
            rural_area = st.selectbox(
                label="Area",
                options=[
                    'Rural',
                    'Urban'
                ],
                index=1
            )

        # ============================================================
        # Age Features
        st.markdown("**Age Features**")
        a_1, a_2, a_3 = st.columns(3)

        with a_1:
            current_age = st.number_input(
                label="Current Age",
                min_value=0,
                max_value=49,
            )

        with a_2:
            age_first_birth = st.number_input(
                label="Age at First Birth",
                min_value=0,
                max_value=49,
            )

        with a_3:
            age_first_period = st.number_input(
                label="Age at First Menstrual Period",
                min_value=0,
                max_value=49,
            )

        # ============================================================
        # Sexual Activity Information Features
        st.markdown("**Sexual Activity Information Features**")
        recent_sex_act = st.selectbox(
            label="Recent Sexual Activity",
            options=[
                'Active in last 4 weeks',
                'Not active in last 4 weeks - not postpartum abstinence',
                'Not active in last 4 weeks - postpartum abstinence'
            ],
            index=0
        )

        husband_desire = st.selectbox(
            label="Husband's Desire for Children",
            options=[
                "No desire",
                "Both want same",
                "Husband wants fewer",
                "Husband wants more",
                "Don't know",
            ],
            index=0
        )

        # ============================================================
        # Status of Woman and Pregnancy Features
        st.markdown("**Status of Woman and Pregnancy Features**")
        swp_1 = st.selectbox(
            label="Current pregnancy status?",
            options=[
                'Fecund',
                'Postpartum Amenorrheic',
                'Infecund, menopausal',
                'Pregnant'
            ],
            index=0
        )

        swp_3_1, swp_2_1 = st.columns(2)

        with swp_2_1:
            swp_2 = st.radio(
                label="Currently pregnant?",
                options=['Yes', 'No or unsure'],
                index=1
            )

        with swp_3_1:
            swp_3 = st.number_input(
                label="Total number of pregnancies",
                min_value=0,
            )

        # ============================================================
        # Recent Births Features
        st.markdown("**Recent Births Features**")
        rb_1 = st.selectbox(
            label="Current Marital Status",
            options=[
                'Never in union',
                'Living with partner',
                'Married',
                'Widowed',
                'Divorced',
                'No longer living together/separated',
            ],
            index=0
        )

        rb_2_1, rb_3_1, rb_4_1 = st.columns(3)

        with rb_2_1:
            rb_2 = st.number_input(
                label="Births in last five (5) years",
                min_value=0,
            )

        with rb_3_1:
            rb_3 = st.number_input(
                label="Births in last three (3) years",
                min_value=0,
            )

        with rb_4_1:
            rb_4 = st.number_input(
                label="Births in past year",
                min_value=0,
            )

        # ============================================================
        # Decision on Contraception Features
        st.markdown("**Decision on Contraception Features**")
        dc_1_1, dc_2_1 = st.columns(2)

        with dc_1_1:
            dc_1 = st.selectbox(
                label="Decision maker for using a contraception",
                options=[
                    'None',
                    'Mainly respondent',
                    'Mainly husband, partner',
                    'Joint decision',
                    'Other'
                ],
                index=0
            )

        with dc_2_1:
            dc_2 = st.selectbox(
                label="Decision maker for not using a contraception",
                options=[
                    'None',
                    'Mainly respondent',
                    'Mainly husband, partner',
                    'Joint decision',
                    'Other',
                ],
                index=0
            )

        dc_3 = st.selectbox(
            label="Preferred future contraception method",
            options=[
                'Not using',
                'Pill',
                'Injections',
                'Female sterilization',
                'Withdrawal',
                'IUD',
                'Implants/Norplant',
                'Calendar or rhythm method/Periodic abstinence',
                'Male condom',
                'Other traditional method',
                'Patch',
                'Sympothermal',
                'Male sterilization',
                'Standard days method (SDM)',
                'Other modern method',
                'Mucus/Billing/Ovulation',
                'Female condom',
                'Basal Body temperature',
            ],
            index=0
        )

        # ============================================================
        # Do you smoke/indulge in the following?
        st.markdown("**Vices Features**")

        vice_1_1, vice_2_1, vice_3_1 = st.columns(3)

        with vice_1_1:
            vice_1 = st.radio(
                label="Do you use cigarettes?",
                options=['Yes', 'No'],
                index=1
            )

        with vice_2_1:
            vice_2 = st.radio(
                label="Do you snuff by nose?",
                options=['Yes', 'No'],
                index=1
            )

        with vice_3_1:
            vice_3 = st.radio(
                label="Do you smoke a water pipe?",
                options=['Yes', 'No'],
                index=1
            )

        vice_4_1, vice_5_1, vice_6_1 = st.columns(3)

        with vice_4_1:
            vice_4 = st.radio(
                label="Do you smoke a tobacco pipe?",
                options=['Yes', 'No'],
                index=1
            )

        with vice_5_1:
            vice_5 = st.radio(
                label="Do you use kreteks?",
                options=['Yes', 'No'],
                index=1
            )

        with vice_6_1:
            vice_6 = st.radio(
                label="Do you snuff by mouth?",
                options=['Yes', 'No'],
                index=1
            )

        vice_7_1, vice_8_1, vice_9_1 = st.columns(3)

        with vice_7_1:
            vice_7 = st.radio(
                label="Do you chew tobacco?",
                options=['Yes', 'No'],
                index=1
            )

        with vice_8_1:
            vice_8 = st.radio(
                label="Do you use cigars, cheroots, cigarillos?",
                options=['Yes', 'No'],
                index=1
            )

        with vice_9_1:
            vice_9 = st.radio(
                label="Do you chew betel quid with tobacco?",
                options=['Yes', 'No'],
                index=1
            )

        # ============================================================
        # Unmet Needs Features
        st.markdown("**Unmet Needs Features**")
        unmet_need_1 = st.selectbox(
            label="Unmet Need (1)",
            options=[
                'No unmet need',
                'Unmet need for limiting',
                'Unmet need for spacing',
                'Not married and no sex in last 30 days',
                'Using for limiting',
                'Using for spacing',
                'Infecund, menopausal',
                '99',
            ],
            index=0
        )

        unmet_need_2 = st.selectbox(
            label="Unmet Need (2)",
            options=[
                'No unmet need',
                'Unmet need for limiting',
                'Unmet need for spacing',
                'Not married and no sex in last 30 days',
                'Using for limiting',
                'Using for spacing',
                'Infecund, menopausal',
                '99',
            ],
            index=0
        )

        unmet_need_3 = st.selectbox(
            label="Unmet Need (3)",
            options=[
                'No unmet need',
                'Unmet need for limiting',
                'Unmet need for spacing',
                'Not married and no sex in last 30 days',
                'Using for limiting',
                'Using for spacing',
                'Infecund, menopausal',
                '99',
            ],
            index=0
        )

        submit_button_DS = st.form_submit_button(
            label="Submit Information - Random Forest")
        submit_button_AI = st.form_submit_button(
            label="Submit Information - Cosine Similarity")

        if submit_button_DS:
            st.write("Your suggested contraceptive is...")

            user_df = pd.DataFrame({
                "Current age": [current_age],
                'Age of respondent at 1st birth': [age_first_birth],
                'Age at first menstrual period': [age_first_period],
                'Recent sexual activity': [recent_sex_act],
                'Region': [residential_status],
                'Type of place of residence': [rural_area],
                'Current marital status': [rb_1],
                'Births in last five years': [rb_2],
                'Births in last three years': [rb_3],
                'Births in past year': [rb_4],
                'Currently pregnant': [swp_2],
                'Total number all pregnacies': [swp_3],
                'Decision maker for using contraception': [dc_1],
                'Decision maker for not using contraception': [dc_2],
                'Preferred future method': [dc_3],
                'Smokes cigarettes': [vice_1],
                'Smokes pipe full of tobacco': [vice_4],
                'Chews tobacco': [vice_7],
                'Snuffs by nose': [vice_2],
                'Smokes kreteks': [vice_5],
                'Smokes cigars, cheroots or cigarillos': [vice_8],
                'Smokes water pipe': [vice_3],
                'Snuff by mouth': [vice_6],
                'Chews betel quid with tobacco': [vice_9],
                "Husbands desire for children": [husband_desire],
                'Exposure': [swp_1],
                'Unmet need': [unmet_need_1],
                'Unmet need (definition 2)': [unmet_need_2],
                'Unmet need for contraception (definition 3)': [unmet_need_3],
            })

            # Show prediction
            result_holder = predict(user_df)
            show_result(result_holder)

        if submit_button_AI:
            st.write("Your suggested contraceptive is...")

            user_df = pd.DataFrame({
                "Current age": [current_age],
                'Age of respondent at 1st birth': [age_first_birth],
                'Age at first menstrual period': [age_first_period],
                'Recent sexual activity': [recent_sex_act],
                'Region': [residential_status],
                'Type of place of residence': [rural_area],
                'Current marital status': [rb_1],
                'Births in last five years': [rb_2],
                'Births in last three years': [rb_3],
                'Births in past year': [rb_4],
                'Currently pregnant': [swp_2],
                'Total number all pregnacies': [swp_3],
                'Decision maker for using contraception': [dc_1],
                'Decision maker for not using contraception': [dc_2],
                'Preferred future method': [dc_3],
                'Smokes cigarettes': [vice_1],
                'Smokes pipe full of tobacco': [vice_4],
                'Chews tobacco': [vice_7],
                'Snuffs by nose': [vice_2],
                'Smokes kreteks': [vice_5],
                'Smokes cigars, cheroots or cigarillos': [vice_8],
                'Smokes water pipe': [vice_3],
                'Snuff by mouth': [vice_6],
                'Chews betel quid with tobacco': [vice_9],
                "Husbands desire for children": [husband_desire],
                'Exposure': [swp_1],
                'Unmet need': [unmet_need_1],
                'Unmet need (definition 2)': [unmet_need_2],
                'Unmet need for contraception (definition 3)': [unmet_need_3],
            })

            # Show prediction
            result_holder = cosine_implementation(user_df)
            show_result(result_holder)
