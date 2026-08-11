import streamlit as st
import random as rd
import pandas as pd
import os
import time

if 'page' not in st.session_state:
    st.session_state.page = 'welcome_page'

def guessing_game():
    if 'number' not in st.session_state:
        st.session_state.number = rd.randint(1, 15)
    if 'chance' not in st.session_state:
        st.session_state.chance = 0
    if 'limit' not in st.session_state:
        st.session_state.limit = 3
    with st.form(key='sample form'):
        st.write('ONLY 3 CHANCES')
        
        guess = st.number_input(
            'Enter the guessed number: ',
            min_value=1,
            max_value=15)
        submit_button = st.form_submit_button(label='Enter')
        if submit_button:
            st.session_state.chance += 1
            remaining_chances = st.session_state.limit - st.session_state.chance
            if st.session_state.chance >= st.session_state.limit:
                st.warning('limit over')
                st.write(
                    f'The number is {st.session_state.number} , LOOSER🫵'
                )
                st.write('The winners list is given below👇')
            st.write(f'chance used - {st.session_state.chance}')
            st.write(f'Remaining chances: {remaining_chances}')
            if guess > st.session_state.number:
                st.write('think lower number than this😏')
            elif guess < st.session_state.number:
                st.write('think higher number than this🙄')
            else:
                st.session_state.page = 'Win page'
                st.rerun()


def winner():
    st.balloons()

    st.header('CONGRAGULATIONS, YOU WON🥳')
    st.write('Your name will be diplayed on the website as a winner')

    with st.form(key='list'):
        st.session_state.name = st.text_input('Enter your name: ')
        submit_button = st.form_submit_button(label='submit')
        if submit_button:
            st.success("You are added to the winner's list")
            data = {
                'name': [st.session_state.name],
                'attempts': [st.session_state.chance]
            }
            df = pd.DataFrame(data)
            file_exists = os.path.exists("data.csv")
            df.to_csv(
                "data.csv",
                mode="a",
                index=False,
                header=not file_exists
            )
            time.sleep(2)
            st.session_state.page = 'thanks'
            st.rerun()

if st.session_state.page == 'welcome_page':

    st.header('Welcome to Sidhu games')
    st.subheader('Dare to play😏')
    if st.button("I'm ready"):
        st.session_state.page = 'game pass'
        st.rerun()

elif st.session_state.page == 'game pass':
    st.subheader('Are you better at guessing?🤨')
    st.subheader('Guess the number between 1-15')
    guessing_game()
    st.divider()
    st.subheader('Winners lsit')
    if st.button("click to see"):
        df = pd.read_csv('data.csv')
        st.dataframe(df)

    with st.expander('Click to know about the creator'):
        st.write("Sidharth — 17")
        st.write('Too curious to stay average')
        st.write('Building projects since 2025')
        st.write('')
        st.write('Try to keep up. 😏')
    st.link_button(
        "📸 Instagram",
        "https://www.instagram.com/_sidharthh__._/"
    )
elif st.session_state.page == 'Win page':
    winner()

elif st.session_state.page == 'thanks':
    st.header('Thank you🙌')
    st.header(f'{st.session_state.name}💖')
    st.divider()
    st.subheader('contact me for more👇(click)')
    st.link_button(
        "📸 Instagram",
        "https://www.instagram.com/_sidharthh__._/"
    )
