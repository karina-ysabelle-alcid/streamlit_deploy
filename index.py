import streamlit as st


def app():
    st.write("""
    # Finals System Web Application Version
    A [CS 321 | CS 322] Project - Recommender System
    """)
    st.write(
        'Alcid, Cuta, Javier, Malibiran, Melegrito, Ramos, Talipnao, Tomelden')


    tabs = st.tabs(['Abstract', 'Introduction', 'Methodology', 'Results and Discussions', 'Conclusion', 'Acknowledgements', 'References'])
    with tabs[0]:
        st.header('Abstract')
        st.write('Contraceptive and maternal health within the Philippines has been a continuous endeavor for decades. With numerous programs and surveys conducted to understand patterns and behaviors from individuals residing in the country, the Philippines would still need to introduce new approaches to increase modern contraceptive use and improve sexual and reproductive health. This paper demonstrates the prospect that current methods have in making such tasks, modern techniques such as applying recommender systems.')
        st.write("The system acquired relevant data from the United States Agency for International Development’s (USAID) Demographic and Health Surveys (DHS) program. Analysis tools from Python libraries were then used to process and analyze the data before designing an appropriate predictor model. The predictor model is the central basis of the system for providing recommendations. The system process involves user profiling, data storage, and machine learning. Feedbacks help the system make an inference. The design of the algorithm of the recommendation process used a content-based filtering approach.")
        st.write("Analysis from ten columns was extracted from the raw dataset for prototyping; this included improving the dataset for efficient data processing through data cleaning. General attributes were reported, with each category being provided with a description. The research group then identified correlations between the respondent’s age and history of pregnancies revealing that most respondents had given birth ten years before their interview.  Furthermore, the analysis revealed that most respondents do not use modern contraceptives when mentioning family planning.")
        st.write("Incorporating modern methods such as recommender systems in SRH could increase awareness and acknowledgments for multiple individuals across the country. The system application will hopefully contribute to the proper and preferred use of modern contraceptives.")
    with tabs[1]:
        st.header('Introduction')
        st.subheader('Background of the Study')
        st.write(
            "The Philippines has continued to rise in economic prowess. However, in terms of modern healthcare, the country still has much room for improvement in the health sector; sexual and reproductive health (SRH) is a department that needs improvement. Even with already established contraceptive methods being developed over the past years, there are still barriers in which individuals will encounter before even accessing any contraceptives—these range from income, political, and religious backgrounds [1].")
        st.write(
            "With laws and bills being passed to assist in SRH, such as the Responsible Parenthood and Reproductive Health Act of 2012 (RH law), the country continues to seek and improve programs and projects that help fulfill the needs of Filipinos in terms of SRH. One such program that has shown promising results is the Usapan program. The program introduces a behavioral approach by raising awareness of male responsibility for reproductive health under the Philippines' Family Planning Organization(FPOP).")
        st.write(
            "Even with established programs such as Usapan, most of the population would still refuse to apply modern contraceptive techniques, which would lead to the rapid growth of HIV cases and adolescent pregnancies[2]. In addition to this, the Philippines has only a 55 % prevalence rate on modern contraceptive use over the past decade. The consideration of existing behaviors and patterns of the preference of traditional contraceptive methods as opposed to modern methods is imperative to the study[3].")
        st.write(
            "Another group of researchers introduced the Systemic Anomalous Case Analysis method (SACA) to understand behaviors and existing research. SACA is a mixed-method approach to review existing research methods on the topic and compare and contrast the results to improve existing theories, measures, and experimental investigations on social phenomena relating to SRH [4].")
        st.write(
            "Additionally, the research itself provides a large amount of data and recorded interviews that span decades which can be utilized further into the study. Educational access to SRH has been taught in various ways, and each variety would yield different results [5].")
        st.write("Similar to the studies conducted by Sarah Jane Arcos Biton, the research results can be applied to existing strategies that can help in further advancing SRH education through campaign development and community seminars which additionally spreads more awareness on the topic.")
        st.write(
            'Implementing already existing technologies will also be considered. Examples of this are integrating smartphones and social media into a newly proposed healthcare system because of their relevance and impact among most of the population, especially for Family Planning (FP) and SRH. Furthermore, a high correlation between FP and smartphone ownership has been observed [6], thus further supporting integrating the technology into an SRH system.')
        st.write(
            'However, it is not smartphone usage alone that can affect contraceptive use and FP; social media is also another important factor in heightening awareness on the topic. The potential social media can assist in SRH is widely underused since there have not been more substantial studies conducted on the potential benefits of social media [7]. The overreliance on smartphones and social media can prove to benefit the research because of its level of necessity the user has towards it, especially among adolescents. Systematic reviews have been utilized to compare various mobile health (mHealth) tactics that have been applied to improve SRH awareness in lower-middle income countries [8].')
        st.write(
            'The trends of sexual health behavior, particularly in maternal and contraceptive health, among women in the age range of 15 to 24 in the Philippines indicate that targeted programs and policies are needed. A study by Juan, Laguna, and Pullum in 2019 concludes that young women in the Philippines were shown to have inconsistent knowledge and exposure to such information [9].')
        st.write(
            'Previous studies have used and developed sexual health information apps to increase sexual and reproductive health knowledge of its users [10, 11]. The studies were able to find that SRH apps are able to deliver sexual and reproductive health knowledge to its users [10].')
        st.write(
            "This lack of sexual health understanding and autonomy represents the need for policies and systems to be put in place as the lack of it increases the prevalence of immature pregnancies and births among the youth. In addition to that, the lack of education about oral or barrier contraceptive methods causes many women and girls to become fearful of potential side effects associated with these methods [7].")
        st.write("This study then intends to contribute to the decline of the trend of adolescent pregnancy, childbirth, sexual diseases among the youth in the Philippines, and encourage sex education through the creation of a recommender system targeted at maternal and contraceptive health. It intends to benefit existing technical solutions in Philippine healthcare regarding recommender systems by providing insight into how to approach maternal health and contraceptive health to prevent cases of early childbirth.")

        st.subheader('Research Gap')
        st.write("In solving the gap for a recommender system in the sub-area of maternal and contraceptive health, a part of the researchers' solution is to preprocess their collected data, design an appropriate model to determine existing trends and predictions, and apply it to a recommender system making use of artificial intelligence.")
        st.write('The researchers then hope that the outcomes of this study would be used for future recommender systems that will tackle other sub-areas of the broad medical field in the Philippines. Additionally, whilst it is proven that there is a deficiency in SRH access in terms of contraceptives, social stigmas, and religious/cultural backgrounds, there still exist drawbacks for contraceptive use. Current studies were able to show that there is a lack of knowledge in sexual reproductive and health knowledge in the Philippines')
        st.write(
            "Additionally, whilst it is proven that there is a deficiency in SRH access in terms of contraceptives, social stigmas, and religious/cultural backgrounds, there still exist drawbacks for contraceptive use. Current studies were able to show that there is a lack of knowledge in sexual reproductive and health knowledge in the Philippines[1, 3, 9]. ")
        st.write(
            'In addition, there were studies that aimed to address the lack of SRH knowledge; however, those studies were limited to certain demographic groups and no research was conducted for the Philippines [10, 11].')

        st.subheader('Objectives of the Study')
        st.write("In this regard, the study aims to target contraceptive and maternal health information specifically to create a recommender system. Specifically:")
        st.markdown(
            "- To analyze the 2017 DHS dataset for insights about SRH in the Philippines.")
        st.markdown("- To develop a prototype recommender system that predicts or recommends contraceptive information from a user's demographic data in tandem with existing literature on SRH and FP.")

        st.subheader('Significance of the Study')
        st.write(
            'Based on already existing frameworks, the group would analyze studies that relate to further improving SRH systems. In this case, examining an e-healthcare management framework applies recommender systems used to sustain health and disease interdiction and the default feature of analyzing user preferences [12, 13].')
        st.write(
            ' Moreover, fully realized recommender systems are able to reduce healthcare costs by a substantial fraction since a ‘similar-outcome low cost’ substitute would be presented to current medical practitioners during prescription can be integrated by clinicians through practice which could then conclude to a lower cost in healthcare [14].')

        st.subheader('Limitations')
        st.write('The broadness of existing recommender systems in healthcare primarily provides general results, as most of them aim to be a straightforward substitute for the proper diagnosis from a medical professional. Notably, with the increase of the audience for a particular recommender system, issues arise in its need for complexity to adapt to all sorts of expected and unexpected inputs.')
        st.write(
            "Healthcare systems that use recommenders will need to cope with imprecise terms (e.g., medical terms that have prefixes or suffixes), colloquial terms (e.g., the equivalence of medical terms to their layman's equivalent), and finally misspellings [15]. This problem is further heightened by the need to be assessed by several health experts regarding its use of vocabulary as descriptions of symptoms vary when other medical fields are involved in the system.")
        st.write("The study then focuses only on contraceptive and maternal health to limit these existing, occurring issues. Accordingly, it also fills in the problem for broad recommender systems, such that there is a lack of recommender systems in this specific sub-area of sexual health. A specific subcategory for a wide health-related field in sexual health allows the researchers to use mainly specific datasets to create and model a recommender system that only targets contraceptive and maternal health. ")

        st.header('Ethical Considerations')
        st.write('The research only considers legal and available contraceptive methods in the Philippines. It does not include outlawed emergency contraceptives (i.e., morning-after pills) used to prevent pregnancy following unprotected sexual intercourse or contraceptive failure. In turn, the contraceptives concerning morning-after pills will not be considered as a value when processing the data. ')
    
    with tabs[2]:
        st.header('Data Gathered')
        st.write("The study made use of the dataset provided by the United States Agency for International Development (USAID) through their Demographic and Health Surveys (DHS) program. The DHS dataset was primarily chosen for its granularity and breadth of data that spans 20 years having specific column features for each sample. Other datasets were also considered, such as the Philippines' Department of Health, National Statistics Office, and the Open Data Repository (data.gov.ph), but ultimately the research group did not choose them for this study as the datasets were not sufficient enough and may not provide the needed data for the study.")
    
        st.header('Data Analysis')
        st.subheader('Data Preparation')
        st.write("For the data to be used, the researchers would request a data drop from the DHS, which will then be used for statistical reporting and analysis. More importantly, it will act as the bulk of the processed data output for the research. Implementing data cleaning to detect and correct inconsistent, incomplete, and inaccurate records; columns on abstinence and sexual activity displayed numerous rows. For example, respondents would reply having sexual activity within four weeks; however, they would also respond that they have been abstinent for multiple months.")
    
        st.subheader('Data Editing and Preprocessing')
        st.write('The process involved importing the DHS dataset, to which null records were removed initially. The dataset was then subjected to the removal of duplicate records and merging identical features. Missing data was either rebuilt or replaced with a global value to implement standardization across all rows. Any column features having numerical values were normalized and any features having categorical data were encoded to keep the dataset purely having one data type. The researchers had converted specific rows to be all numeric values, removing columns that were not about maternal and contraceptive health (e.g., notably columns focusing on various infectious diseases), and replacing empty cells with an appropriate replacement value (e.g., either "0" or "None").') 
        
        st.subheader('Data Features')
        st.write('Of the 1,158 columns visible in the original dataset, 30 columns were extracted due to their relevancy and basing on existing reproductive health counseling [16]. The researchers focused on the following subset of features in the dataset that pertain to maternal and contraceptive health:')
        st.write("""• Age features pertain to a respondent's current age, age during their first birth, and age during their first menstrual period.
                 \n• Sex features pertain to a respondent's age during their first intercourse, and their recent sexual activity.
                 \n• Region features pertain to where the respondent currently resides in the Philippines.
                 \n• Marital status features concern with the civil status of the respondent during the time of their scheduled interview.
                 \n• Pregnancy features concern with the respondent's number of births in the last 5, 3, and past year. It also notes whether a respondent is pregnant and their total number of pregnancies at the time of their interview.
                 \n• Current contraceptive methods concerning the respondent's current contraceptive method and type.
                 \n• Decision features look into the respondent's response about who decided to use a contraception method in their sexual activity.
                 \n• The future feature only looks into the preferred contraception method the respondent wants to use in the future.
                 \n• The smoking history feature pertains to therespondent's use of tobacco through various means.
                 \n• Husband involvement features pertain to the respondent's husband and their involvement with the respondent's marital and reproductive health.""")
        st.write('These features were also seen to have at least 20% correlations with one another and were chosen for the system.')
        heatmap_img_path = f'https://raw.githubusercontent.com/RyanMNST/streamlit_deploy/main/graphs/heatmap.png'
        st.markdown(
                f"<img src='{heatmap_img_path}' style='display: block; margin-left: auto; margin-right: auto; width: 50%;'>", unsafe_allow_html=True)

        st.header('Materials and Model')
        st.subheader('Analysis Tools')
        st.write("The preprocessing and analysis of the dataset involved using available Python libraries that focused on scientific computing, data visualization, data analysis, and machine learning. The following were the primary Python libraries used:")
        st.write("""• NumPy - A versatile library focused on providing vectorization, indexing, and comprehensive mathematical funcions.
                 \n• Pandas - A flexible library that makes use of Dataframes for data manipulation.
                 \n• Matplotlib - A data visualization library used for descriptive analytics
                 \n• Scikit-learn - A library that focuses on providing machine learning functionalities.
                 \n• Seaborn - A statistical data visualization library.
                 \n• Streamlit - An open-source library meant to share user made web applications in Python.""")
        st.subheader('Predictor Model (Machine Learning)')
        st.write("The Random Forest algorithm is used for the predictive model to segment. It analyzes the provided user records in the training data to identify where the patient belongs according to their initial diagnosis. The researchers chose the Random Forest algorithm for the model to provide high accuracy and performance. It was considered to provide accurate predictions even without the initial parameters that can help it increase its initial accuracy rate. Additionally, the algorithm can still be used even at the onset of missing values in the dataset [17, 18]. These data then would provide a predictive model that can show recommendations that are most likely to be used and suitable for an inquiring user regarding their maternal and contraceptive health. The researchers created two versions of the recommender system prototype: an offline version, and an online, web-based version.")

        st.subheader('Model Evaluation')
        st.write("The group evaluated the model based on its performance measures. The researchers used recall and precision, which allows them to take into account the intrinsic variability of performance estimation, and provides more insights on system performance [19]. The DHS dataset used to train the model was the 2017 Birth Recode dataset having 47,244 sample rows, where 70% was used for training and 30% fortesting. The output of the model training and testing had shown a precision of 93%, having correctly predicted the contraceptive to be used, and a recall of 93% having correctly predicted the contraceptive to be used against all observations in the results. Only 93% was observed as the default parameters of the RF model were used. The group had then made use of this result in the creation of the system. However, further changes to the hyperparameters may still improve this result for future iterations.")
        st.markdown(
                f"<img src='figures/figure_1.png' style='display: block; margin-left: auto; margin-right: auto; width: 50%;'>", unsafe_allow_html=True) 
    
        st.subheader('Proposed System Overview')
        st.write("The development of the system consists of building a predictive model of the recommender system by integrating the 2017 DHS dataset as training data. The Random Forest algorithm is then adopted to achieve a highly accurate predictive model for the system. Users can then provide their data, to which the recommender system can provide predictions and recommendations.") 
        st.markdown(
                f"<img src='figures/figure_2.png' style='display: block; margin-left: auto; margin-right: auto; width: 50%;'>", unsafe_allow_html=True)

        st.header('Recommender System Process')
        st.subheader('Focus of the System Process')
        st.write("The concept of a recommender system (RS) pertains to the decision support system, where it can provide the necessary tools to facilitate user decision-making in controlled environments.")
        st.write("The focal point of an RS is to estimate a user's preference. The process is made through the profile that they provide. Prediction tasks constitute processing user data to store later and retrieve and be the main factor for computation in an RS. However, it still needs to be considered that initial evaluations given by clients do not necessarily mean it focuses on the real objective the client wants. [13, 15].")
        st.write("The system utilized the Content-based filtering approach wherein the data that a user inputs in the system is matched with similar inputs and are suggested to them. The content-based approach does not require user data during recommendations [13, 20]. However, the program of the researchers will save inputted data into the system and will be retrained for the next input.")
        st.write("When applying RS in healthcare, users can retrieve relevant information without manually filtering data themselves, unlike most health portals that already exist [21]. With the assistance of multiple recent data, a need for more efficient and optimal problems can be resolved through RS.")

        st.subheader("Creating a User Profile")
        st.write("The initial phase in making a recommendation is gathering information [14]. In this phase, the system collects pertinent user data from the users to create a user profile for prediction tasks. This data includes the user’s age, sexual activity, decision on contraception, smoking history, unmet needs, and information relating to their residential, marital, and pregnancy status. Regarding the unmet needs, additional information for these featured columns pertains to the measure that can infer need for contraception based on current sexual, marital, and reproductive condition. Women who are considered to have an unmet need are sexually active, fecund, and want to avoid pregnancy; but are not using contraceptives [22]. The research group also considered the respondent's type of residence as it could impact the respondent's possible source of the contraceptive due to geographical constraints. It could also indicate underlying health problems due to urbanization, which could affect contraceptive efficacy [23].")

        st.subheader("Offline Version")
        st.write('PySimpleGUI was utilized in creating the GUI of the system. To apply content-based filtering, whenever the program is run the system retrains the dataset to produce pickle files to be utilized for the current session. Every time the user submits their profile for prediction and results are given, they are saved into the dataset and the system gets retrained again.')
    
        st.subheader("Web-based Application")
        st.write("The web-based version utilized Streamlit, a hosting service for Python scripts using an online open-source Python library. Although the aim was to make it function similarly to the offline version, the constraints of Streamlit hindered the full implementation of a content-based filtering approach of the system. Streamlit prevents the system’s way of updating the dataset for every new entry which is crucial for retraining the system.")
    
        st.subheader("Random Forest Classifier")
        st.write('Using the same dataset and parameters as the Random Forest Classifier, this implementation applied Term Frequency-Inverse Document Frequency (TF-IDF) to measure the frequency of a word in a document, regardless of the magnitude or length of the document. The dataset features were converted into String and modified into a matrix of TF-IDF features through the use of the TfidfVectorizer, which was fitted using the corpus of the dataset. The passed user profile is formatted the same way and compared using the TF-IDF matrix to return an index. The index is the data with the most similar attributes to the user’s profile.')

        st.subheader("Cosine Similarity")
        st.write('Using a pre-processed version of the dataset only containing the columns enumerated in the data features, the researchers further filtered the dataset to only contain data wherein the respondents are contraceptive users. Categorical data such as maternal and smoking history were converted into numerical data through the use of a hot encoder in order for the system to read and process the Categorical data. The resulting data was utilized in the training of the Random Forest Classifier. It is intended to predict the contraceptive method suitable for a user, given their profile and similarity to past users using certain contraceptives.')

        st.subheader('Store data/learn')
        st.write('Any user demographic data provided to the proposed RS will be stored and used to train the system itself. This data is processed through the system by users through their profile. Afterwhich, It will be directly added into the database along with the suggested contraceptive.')
        st.markdown(
                f"<img src='figures/figure_3.png' style='display: block; margin-left: auto; margin-right: auto; width: 50%;'>", unsafe_allow_html=True)
    
    with tabs[3]:
        st.header('Output and Study of the Data')
        st.write('Utilizing the aforementioned tools, the research group is able to process the data further and derive the following insights regarding the features that were emphasized:')
        st.write("""• Most of the respondents were 47; the least was at the age of 15.
                 \n• 70% of the respondents came from rural areas as opposed to the 30% that lived in urban areas.
                 \n• 35147 of the respondents were married. 87 respondents, however, were divorced.
                 \n• The respondents' most popular contraceptive method was a pill (9227 respondents), while the least used was a female condom (1 respondent). However, a staggering 21781 of the respondents were not using any contraception method. 
                 \n• 21781 of the respondents had reported that there was no decision-maker in the use of contraception during their sexual activity.
                 \n• Finally, when the respondents were asked what contraception metho they had wanted to use in their future sexual activity, 41174 responded that they would not use one, and 6070 will use a pill, injection, and female sterilization as the three most popular contraception methods.""")
        st.write("In the analysis of the relationship between age features and pregnancy features, the dataset showed that as a respondent's age increases, their total number of pregnancies also increases. Accordingly, the dataset has also displayed that most of the respondents had given birth ten years before their interview.")
        st.markdown(
                f"<img src='figures/figure_3.png' style='display: block; margin-left: auto; margin-right: auto; width: 50%;'>", unsafe_allow_html=True)
    
        st.subheader('Open Issues')
        st.write('In this study, the research group analyzed the given dataset and was able to categorize, count and average featured columns after cleaning the data.')
        st.write('The results derived from the featured columns are then compared and discussed. From the analyzed data, the research group is able to derive insights that pertain to the respondents as a whole. The research group is then able to count the data and find the majority and minorities within the data, such as the majority of respondents being older than 40 and the number of respondents that use contraceptives in a given year.')
        st.write("Regarding age and sex features, most of the respondents had experienced their first menstrual period at the age of 19 and were likely to engage in sexual intercourse at the same age; further, they were already expecting childbirth in the following year. Regarding family planning focusing on contraceptives, forty-six percent of all the respondents, whether married or not, were not using a contraceptive method. However, fifty-four percent of them were using the pill method (20%) and female sterilization (9%).")

        st.subheader('Recommender System')
        st.write("The researchers created a prototype recommender system that takes in the user's demographic data focused on the chosen features specified earlier and uses it to suggest a recommended contraceptive for them to take. The user had the option to choose between using the random forest classifier or the cosine similarity approach to generate the recommended contraceptive method, given the user’s profile, providing them the contraceptive and its information.")

        st.subheader('Implications')
        st.write("The need for policies that educate young Filipino women about maternal health, specifically contraceptives, should be acknowledged to prepare them for family planning and childbearing. Additionally, broader systems for other medical fields should also be considered for analysis and application as a number of the respondents lacked the necessary knowledge and information about their own personal health.")

        st.subheader('Limitations')
        st.write("A limitation to consider is that this study does not integrate the experiences or approval of a healthcare or medical provider in the generation of diagnosis. The system only relies on existing literature. Even with proper data or features chosen by experts, a medical diagnosis requires a medical professional to be present. The main purpose of the system is to lessen the time needed for counseling sessions to move to step 2, which is the recommendation of the discussion of contraceptives. For the next iteration of this research, the researchers consider receiving feedback first from a medical professional. So that user demographic data passes through them first and then the system will provide a more accurate contraceptive or diagnosis for the patient.")

    with tabs[4]:
        st.header('Conclusion')
        st.write("In this study, the research group has discussed applying a recommender system towards contraceptive and maternal health within the Philippines. Additionally, the reviews conducted within the paper will serve as a review on further understanding the state of SRH in the Philippines, its people, and the access to medical services thereof. The incorporations of datasets provided by the international health organization DHS have redounded towards the paper’s data analysis. The data gathered, in turn, assisted in understanding a consensus of a group of individuals in terms of their age, reproductive history, maternal history, smoking history, region, marital tatus, unmet needs (if any), and other factors that may affect the individual's SRH. The raw data is then processed so it may be illustrated graphically through plots and graphs to categorize the data and contribute to the proposed application that integrates processes and techniques from a recommender system, such as content-based filtering. The proposed application will classify proper contraceptive methods and thus support users in making informed decisions in taking better care of their SRH.")
    
    with tabs[5]:
        st.header('Acknowledgements')
        st.write("This paper and the research conducted within it would not be possible without the DHS Program for providing the data sets utilized for the study and as such we wish to show our deepest appreciation. Additionally, we would like to extend our appreciation towards Bridget Wellington, Data Archivist of ICF, from USAID in providing access to the data set as contributing additional references.") 
    
    with tabs[6]:
        st.header('References')
        st.write("""
        [1] Elia Gabarron and Rolf Wynn. 2016. Use of social media for sexual health promotion: a scoping review. Global Health Action ACM 9, 1. DOI: https://doi.org/10.3402/gha.v9.32193 
        \n[2] Sarah Jane Arcos Biton. 2020. Advancing sexual and reproductive health and rights: An overview of the best practices in the Philippines. Asian Journal of Women's Studies, ACM 26, 1, 114-127 pages. DOI: https://doi.org/10.1080/12259276.2019.1690778 
        \n[3] Maria Midea M. Kabamalan, Maria Paz N. Marques, and Elma P. Laguna. 2017. Ten Years of Traditional Contraceptive Method Use in the Philippines: Continuity and Change. ICF. 
        \n[4] Jessica D. Gipson, Jasmine Uysal, Subasri Narasimhan, and  Socorro (Connie) Gultiano. 2020. Using Systematic Anomalous Case Analysis to Examine Sexual and Reproductive Health Outcomes in the Philippines. Studies in Family Planning, ACM 51, 2, 21 pages. DOI: https://doi.org/10.1111/sifp.12115
        \n[5] Judith Odanee G. Magwilang, Eddieson Pasay-an, Petelyne P. Pangket. 2020. Knowledge, attitudes, and practices of adolescents regarding sexuality and reproductive issues in the Cordillera administrative region of the Philippines. Makara Journal of Health Research. ACM 24, 3. DOI: https://doi.org/10.7454/msk.v24i3.1245 
        \n[6] Apoorava Jadhav, & Julianne Weis. 2019. Mobile phone ownership, text messages, and contraceptive use: Is there a digital revolution in family planning?. Contraception. DOI: https://doi.org/10.1016/j.contraception.2019.10.004   
        \n[7] Olivia Rose Wood. 2020. Exploring Factors that Limit Contraception Use Among Adolescent Girls Aged 15-19 in Puerto Princesa, Palawan, Philippines. Colombia Academic Commons. Global Health Certificate, 4-15 pages. DOI: https://doi.org/10.7916/d8-cxme-6r43 
        \n[8] Farina Abrejo, Sumera Aziz Ali, Anam Feroz, Rozina Nuruddin & Sarah Saleem. 2019. Using mobile phones to improve young people’s sexual and reproductive health in low- and middle-income countries: a systematic review protocol to identify barriers, facilitators and reported interventions. Syst Rev. ACM 8, 117.  DOI: https://doi.org/10.1186/s13643-019-1033-5 
        \n[9] Christina P. Juan, Elma P. Laguna, and Thomas W. Pullum. 2019. Trends of Sexual and Reproductive Health Behaviors among Youth in the Philippines: Further Analysis of the 2008, 2013, and 2017 National Demographic and Health Surveys. DHS Further Analysis Reports No. 127. Rockville, Maryland, USA: ICF. https://www.dhsprogram.com/pubs/pdf/FA127/FA127.pdf. 
        \n[10] Lynae Brayboy, Alexandra Sepolen , Taylor Mezoian , Lucy Schultz , Benedict Landgren-Mills, Noelle Spencer, Carol Wheeler, Melissa Clark. 2017. Girl Talk: A Smartphone Application to Teach Sexual Health Education to Adolescent Girls. Journal of Pediatric & Adolescent Gynecology, 30, 1, 23-28. DOI:https://doi.org/10.1016/j.jpag.2016.06.011
        \n[11] Anna Nielsen, Aspasia Bågenholm, and Ayesha De Costa. 2020. Development of a Mobile Phone App to Promote Safe Sex Practice Among Youth in Stockholm, Sweden: Qualitative Study.  JMIR formative research, 4, 1, e12917. DOI:https://doi.org/10.2196/12917
        \n[12] Erni Astutik, Ferry Efendi, and Susy Katikana Sebayang. 2019. Women’s empowerment and the use of antenatal care services: analysis of demographic health surveys in five Southeast Asian countries. Women & Health, 1-17, 1155-1171 pages. DOI: https://doi.org/10.1080/03630242.2019.1593282 
        \n[13] P. Deepalakshmi and P. Nagaraj. 2020. A framework for e-healthcare management service using recommender system. Electronic Government, an International Journal 16, 1/2, 84-100 pages. DOI: https://doi.org/10.1504/EG.2020.105256 
        \n[14] Lina Bouayad, Balaji Padmanabhan, and Kaushal Chari. 2020. Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice. MIS Quarterly 44, 4, 1859-1903. DOI: https://doi.org/10.25300/MISQ/2020/14435  
        \n[15] Duygu Çelik Ertuğrul and Atilla Elçi. 2020. A survey on semanticized and personalized health recommender systems. Expert Systems 37, 4, 1-23. DOI:https://doi.org/10.1111/exsy.12519 """)
