mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"ai.mayurpatil@gmail.com\"\n\
"> ~/.stramlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
"> ~/.streamlit/config.toml