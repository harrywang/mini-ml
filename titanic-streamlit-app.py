import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.title('Titanic Survival Analysis and Prediction')
# load dataset
df = pd.read_csv('titanic.csv')

# show the entire dataframe
st.write(df)

# f-string
st.subheader('Survival Rate')
survival_count = df['Survived'].value_counts()
st.text(f'Survival rate = {survival_count.values[1]/sum(survival_count):.2%}')

# simple plotting
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
survival_count.plot.bar(ax=ax[0])
df['Age'].plot.hist(ax=ax[1])
st.pyplot(fig)


st.subheader('Making Prediction')
st.markdown('**Please provide passenger information**:')  # you can use markdown like this


# load models
tree_clf = joblib.load('clf-best.pickle')

# get inputs

sex = st.selectbox('Sex', ['female', 'male'])
age = int(st.number_input('Age:', 0, 120, 20))
sib_sp = int(st.number_input('# of siblings / spouses aboard:', 0, 10, 0))
#par_ch = int(st.number_input('# of parents / children aboard:', 0, 10, 0))
pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
fare = int(st.number_input('# of parents / children aboard:', 0, 100, 0))
#embarked = st.selectbox('Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)', ['C', 'Q', 'S'])

# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

passenger = pd.DataFrame(
    {
        'Pclass': [pclass],
        'Sex': [sex], 
        'Age': [age],
        'SibSp': [sib_sp],
#        'Parch': [par_ch],
        'Fare': [fare],
#        'Embarked': [embarked],
    }
)

y_pred = tree_clf.predict(passenger)

if y_pred[0] == 0:
    msg = 'This passenger is predicted to be: **died**'
else:
    msg = 'This passenger is predicted to be: **survived**'

prediction_state.markdown(msg)