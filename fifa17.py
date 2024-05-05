import streamlit as st
import pandas as pd
import random

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.alphacoders.com/718/718668.jpg");
    background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    st.markdown("<h1 style='text-align: center;'>Auction Bot</h1>", unsafe_allow_html=True)
    st.write("Upload a CSV file with names")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        names_data = pd.read_csv(uploaded_file)

        chosen_names = st.session_state.get('chosen_names', [])

        if st.button("Choose Random Name"):
            available_names = names_data[~names_data['Name'].isin(chosen_names)]
            if len(available_names) > 0:
                random_entry = random.choice(available_names.index)
                chosen_entry = available_names.loc[random_entry]
                # display all details of chosen name
                st.write("Chosen entry:")
                st.dataframe(chosen_entry)
                chosen_name = chosen_entry['Name']
                chosen_names.append(chosen_name)
                st.session_state.chosen_names = chosen_names

                st.write("Remaining entries:")
                st.dataframe(available_names)
            else:
                st.write("All names have been chosen.")

if __name__ == '__main__':
    main()