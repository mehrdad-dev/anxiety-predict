import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf

st.title('Anxiety Prediction')
st.markdown('Based on Taylor Manifest Anxiety Scale', unsafe_allow_html=True)

st.markdown('&nbsp;', unsafe_allow_html=True)


st.markdown('## Notes:', unsafe_allow_html=True)
notes = """
- This Test have 50 question with True/False answers.
- It's takes 4-10 minutes to complete.
- You shuld to answer all the questions.
"""
st.markdown(notes, unsafe_allow_html=True)
st.markdown('&nbsp;', unsafe_allow_html=True)

## ================================================================================================

answers = []

def create_model_input(answers):
    for key, ans in enumerate(answers):
        if ans == 'True':
            answers[key] = 1
        elif ans == 'False':
            answers[key] = 0
        elif ans == 'Male':
            answers[key] = 1
        elif ans == 'Female':
            answers[key] = 2  
        elif ans == 'Other':
            answers[key] = 3                     
        else:
            answers[key] = ans

    return answers

## ================================================================================================

st.markdown('<h4>How old are you?</h4>', unsafe_allow_html=True)
age = st.slider('', 14, 100, 21)
answers.append(age)

st.markdown('<h4>What is your gender? </h4>', unsafe_allow_html=True)
sex = st.selectbox('', ('Male', 'Female', 'Other'))
answers.append(sex)

st.markdown('<h4>Q1. I do not tire quickly. </h4>', unsafe_allow_html=True)
q1 = st.selectbox('', ('True', 'False'), key='q1')
answers.append(q1)

st.markdown('<h4>Q2. I am troubled by attacks of nausea.</h4>', unsafe_allow_html=True)
q2 = st.selectbox('', ('True', 'False'), key='q2')
answers.append(q2)

st.markdown('<h4>Q3. I believe I am no more nervous than most others.</h4>', unsafe_allow_html=True)
q3 = st.selectbox('', ('True', 'False'), key='q3')
answers.append(q3)

st.markdown('<h4>Q4. I have very few headaches.</h4>', unsafe_allow_html=True)
q4 = st.selectbox('', ('True', 'False'), key='q4')
answers.append(q4)

st.markdown('<h4>Q5. I work under a great deal of tension.</h4>', unsafe_allow_html=True)
q5 = st.selectbox('', ('True', 'False'), key='q5')
answers.append(q5)

st.markdown('<h4>Q6. I cannot keep my mind on one thing.</h4>', unsafe_allow_html=True)
q6 = st.selectbox('', ('True', 'False'), key='q6')
answers.append(q6)

st.markdown('<h4>Q7. I worry over money and business.</h4>', unsafe_allow_html=True)
q7 = st.selectbox('', ('True', 'False'), key='q7')
answers.append(q7)

st.markdown('<h4>Q8. I frequently notice my hand shakes when I try to do something. </h4>', unsafe_allow_html=True)
q8 = st.selectbox('', ('True', 'False'), key='q8')
answers.append(q8)

st.markdown('<h4> Q9. I blush no more often than others.</h4>', unsafe_allow_html=True)
q9 = st.selectbox('', ('True', 'False'), key='q9')
answers.append(q9)

st.markdown('<h4>Q10. I have diarrhea once a month or more. </h4>', unsafe_allow_html=True)
q10 = st.selectbox('', ('True', 'False'), key='q10')
answers.append(q10)

st.markdown('<h4>Q11. I worry quite a bit over possible misfortunes. </h4>', unsafe_allow_html=True)
q11 = st.selectbox('', ('True', 'False'), key='q11')
answers.append(q11)

st.markdown('<h4> Q12. I practically never blush.</h4>', unsafe_allow_html=True)
q12 = st.selectbox('', ('True', 'False'), key='q12')
answers.append(q12)

st.markdown('<h4>Q13. I am often afraid that I am going to blush.</h4>', unsafe_allow_html=True)
q13 = st.selectbox('', ('True', 'False'), key='q13')
answers.append(q13)

st.markdown('<h4>Q14. I have nightmares every few nights. </h4>', unsafe_allow_html=True)
q14 = st.selectbox('', ('True', 'False'), key='q14')
answers.append(q14)

st.markdown('<h4>Q15. My hands and feet are usually warm. </h4>', unsafe_allow_html=True)
q15 = st.selectbox('', ('True', 'False'), key='q15')
answers.append(q15)

st.markdown('<h4> Q16. I sweat very easily even on cool days.</h4>', unsafe_allow_html=True)
q16 = st.selectbox('', ('True', 'False'), key='q16')
answers.append(q16)

st.markdown('<h4> Q17. Sometimes when embarrassed, I break out in a sweat.</h4>', unsafe_allow_html=True)
q17 = st.selectbox('', ('True', 'False'), key='q17')
answers.append(q17)

st.markdown('<h4>Q18. I hardly ever notice my heart pounding and I am seldom short of breath. </h4>', unsafe_allow_html=True)
q18 = st.selectbox('', ('True', 'False'), key='q18')
answers.append(q18)

st.markdown('<h4> Q19. I feel hungry almost all the time.</h4>', unsafe_allow_html=True)
q19 = st.selectbox('', ('True', 'False'), key='q19')
answers.append(q19)

st.markdown('<h4>Q20. I am very seldom troubled by constipation. </h4>', unsafe_allow_html=True)
q20 = st.selectbox('', ('True', 'False'), key='q20')
answers.append(q20)

st.markdown('<h4>Q21. I have a great deal of stomach trouble.</h4>', unsafe_allow_html=True)
q21 = st.selectbox('', ('True', 'False'), key='q21')
answers.append(q21)

st.markdown('<h4>Q22. I have had periods in which I lost sleep over worry. </h4>', unsafe_allow_html=True)
q22 = st.selectbox('', ('True', 'False'), key='q22')
answers.append(q22)

st.markdown('<h4>Q23. My sleep is fitful and disturbed. </h4>', unsafe_allow_html=True)
q23 = st.selectbox('', ('True', 'False'), key='q23')
answers.append(q23)

st.markdown('<h4>Q24. I dream frequently about things that are best kept to myself. </h4>', unsafe_allow_html=True)
q24 = st.selectbox('', ('True', 'False'), key='q24')
answers.append(q24)

st.markdown('<h4>Q25. I am easily embarrassed. </h4>', unsafe_allow_html=True)
q25 = st.selectbox('', ('True', 'False'), key='q25')
answers.append(q25)

st.markdown('<h4>Q26. I am more sensitive than most other people. </h4>', unsafe_allow_html=True)
q26 = st.selectbox('', ('True', 'False'), key='q26')
answers.append(q26)

st.markdown('<h4>Q27. I frequently find myself worrying about something. </h4>', unsafe_allow_html=True)
q27 = st.selectbox('', ('True', 'False'), key='q27')
answers.append(q27)

st.markdown('<h4>Q28. I wish I could be as happy as others seem to be. </h4>', unsafe_allow_html=True)
q28 = st.selectbox('', ('True', 'False'), key='q28')
answers.append(q28)

st.markdown('<h4>Q29. I am usually calm and not easily upset. </h4>', unsafe_allow_html=True)
q29 = st.selectbox('', ('True', 'False'), key='q29')
answers.append(q29)

st.markdown('<h4>Q30. I cry easily. </h4>', unsafe_allow_html=True)
q30 = st.selectbox('', ('True', 'False'), key='q30')
answers.append(q30)

st.markdown('<h4>Q31. I feel anxiety about something or someone almost all the time. </h4>', unsafe_allow_html=True)
q31 = st.selectbox('', ('True', 'False'), key='q31')
answers.append(q31)

st.markdown('<h4>Q32. I am happy most of the time. </h4>', unsafe_allow_html=True)
q32 = st.selectbox('', ('True', 'False'), key='q32')
answers.append(q32)

st.markdown('<h4>Q33. It makes me nervous to have to wait. </h4>', unsafe_allow_html=True)
q33 = st.selectbox('', ('True', 'False'), key='q33')
answers.append(q33)

st.markdown('<h4>Q34. I have periods of such great restlessness that I cannot sit long I a chair. </h4>', unsafe_allow_html=True)
q34 = st.selectbox('', ('True', 'False'), key='q34')
answers.append(q34)

st.markdown('<h4>Q35. Sometimes I become so excited that I find it hard to get to sleep. </h4>', unsafe_allow_html=True)
q35 = st.selectbox('', ('True', 'False'), key='q35')
answers.append(q35)

st.markdown('<h4>Q36. I have sometimes felt that difficulties were piling up so high that I could not overcome them. </h4>', unsafe_allow_html=True)
q36 = st.selectbox('', ('True', 'False'), key='q36')
answers.append(q36)

st.markdown('<h4>Q37. I must admit that I have at times been worried beyond reason over something that really did not matter. </h4>', unsafe_allow_html=True)
q37 = st.selectbox('', ('True', 'False'), key='q37')
answers.append(q37)

st.markdown('<h4>Q38. I have very few fears compared to my friends. </h4>', unsafe_allow_html=True)
q38 = st.selectbox('', ('True', 'False'), key='q38')
answers.append(q38)

st.markdown('<h4>Q39. I have been afraid of things or people that I know could not hurt me. </h4>', unsafe_allow_html=True)
q39 = st.selectbox('', ('True', 'False'), key='q39')
answers.append(q39)

st.markdown('<h4>Q40. I certainly feel useless at times. </h4>', unsafe_allow_html=True)
q40 = st.selectbox('', ('True', 'False'), key='q40')
answers.append(q40)

st.markdown('<h4>Q41. I find it hard to keep my mind on a task or job. </h4>', unsafe_allow_html=True)
q41 = st.selectbox('', ('True', 'False'), key='q41')
answers.append(q41)

st.markdown('<h4>Q42. I am usually self-conscious. </h4>', unsafe_allow_html=True)
q42 = st.selectbox('', ('True', 'False'), key='q42')
answers.append(q42)

st.markdown('<h4>Q43. I am inclined to take things hard. </h4>', unsafe_allow_html=True)
q43 = st.selectbox('', ('True', 'False'), key='q43')
answers.append(q43)

st.markdown('<h4>Q44. I am a high-strung person. </h4>', unsafe_allow_html=True)
q44 = st.selectbox('', ('True', 'False'), key='q44')
answers.append(q44)

st.markdown('<h4>Q45. Life is a trial for me much of the time. </h4>', unsafe_allow_html=True)
q45 = st.selectbox('', ('True', 'False'), key='q45')
answers.append(q45)

st.markdown('<h4>Q46. At times I think I am no good at all. </h4>', unsafe_allow_html=True)
q46 = st.selectbox('', ('True', 'False'), key='q46')
answers.append(q46)

st.markdown('<h4>Q47. I am certainly lacking in self-confidence. </h4>', unsafe_allow_html=True)
q47 = st.selectbox('', ('True', 'False'), key='q47')
answers.append(q47)

st.markdown('<h4>Q48. I sometimes feel that I am about to go to pieces. </h4>', unsafe_allow_html=True)
q48 = st.selectbox('', ('True', 'False'), key='q48')
answers.append(q48)

st.markdown('<h4> Q49. I shrink from facing crisis of difficulty.</h4>', unsafe_allow_html=True)
q49 = st.selectbox('', ('True', 'False'), key='q49')
answers.append(q49)

st.markdown('<h4>Q50. I am entirely self-confident. </h4>', unsafe_allow_html=True)
q50 = st.selectbox('', ('True', 'False'), key='q50')
answers.append(q50)


left_column, right_column = st.columns(2)
pressed = left_column.button('Predict!')
if pressed:
    model_input = create_model_input(answers)
    model = tf.keras.models.load_model('model')
    model_input = np.array([model_input])
    temp_df = pd.DataFrame(model_input.T)
    pred = model.predict(temp_df)
    right_column.info('Your Score is:' + str(pred[0][0]))
#    right_column.write('Your Score is:' + str(pred[0][0]))


# st.info('This is a purely informational message')

#expander = st.expander("FAQ")
#expander.write("Here you could put in some really, really long explanations...")

#title = st.text_input('Movie title', 'Life of Brian')


#option = st.sidebar.selectbox(
#    'Which number do you like best?',
#     '1')
