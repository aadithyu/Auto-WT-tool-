import streamlit as st


def main():
    page = st.sidebar.radio("Navigation", ["Home", "Union Info Page" , "Error Info Page"])

    if page == "Home":
        st.markdown("<h1 style='text-align: center;'>AUTO-WT TOOL</h1>", unsafe_allow_html=True)

        # User input area for URL
        url = st.text_input("Enter the URL:")

        # Combo box to select vulnerability type
        vulnerability_type = st.selectbox("Select SQL Injection Vulnerability Type:",
                                          ['Union-based SQLi', 'Error-based SQLi', 'Time-based Blind SQLi', 'Boolean-based Blind SQLi', 'Content-based Blind SQLi', 'Out-of-band Blind SQLi'])

        # 'Start' button to initiate the test
        if st.button("Start"):
            if vulnerability_type == 'Union-based SQLi':
                test_union_based_sqli(url)
            elif vulnerability_type == 'Time-based Blind SQLi':
                test_time_based_sqli(url)
            elif vulnerability_type == 'Error-based SQLi':
                test_error_based_sqli(url)
            elif vulnerability_type == 'Boolean-based Blind SQLi':
                test_boolean_based_sqli(url)
            elif vulnerability_type == 'Content-based Blind SQLi':
                test_content_based_blind_sqli(url)
            elif vulnerability_type == 'Out-of-band Blind SQLi':
                test_out_of_band_sqli(url)

        # 'Clear' button to clear the results
        if st.button("Clear"):
            st.empty()

        st.markdown('<p style="width: 100%; text-align: center;">NOTE: Please ensure that you have proper authorization and permission before conducting any security testing on real-world websites. Use this system for educational purposes.</p>', unsafe_allow_html=True)

    elif page == "Union Info Page":
        st.markdown("<h2 style='text-align: center;'>UNION-BASED SQL Injection</h2>", unsafe_allow_html=True)
        st.write('''Union-based SQL injection is a type of SQL injection attack where an attacker exploits a vulnerability in a web application's input validation mechanism to manipulate the underlying SQL query and retrieve unauthorized data from the database.\n
         This type of attack is particularly effective when the application constructs SQL queries dynamically by concatenating user-supplied input without proper sanitization.\n
            In a union-based SQL injection attack, the attacker leverages the UNION operator, which is used to combine the results of two or more SELECT statements into a single result set. 
            The attacker's goal is to inject a malicious query fragment that retrieves additional data from a different table or performs arbitrary queries.''')

    elif page == "Error Info Page":
        st.markdown("<h2 style='text-align: center;'>ERROR-BASED SQL Injection</h2>", unsafe_allow_html=True)
        st.write('''
            ''')
if __name__ == "__main__":
    main()
