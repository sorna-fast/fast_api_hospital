import streamlit as st
import requests
import json

# URL پایه API
BASE_URL = "http://127.0.0.1:8000"

# تابع برای ارسال درخواست به API
def send_request(endpoint, method="GET", data=None):
    url = f"{BASE_URL}{endpoint}"
    headers = {"Content-Type": "application/json"}
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=json.dumps(data))
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=json.dumps(data))
        elif method == "DELETE":
            response = requests.delete(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

# منوی اصلی
st.title("Streamlit Menu")

menu = ["Home", "Doctors", "Employees", "Nurses", "Parts", "Patients", "Posts", "Files"]
choice = st.sidebar.selectbox("Menu", menu)

def handle_crud_operations(entity, endpoint, fields):
    action = st.selectbox(f"{entity} Actions", ["View All", "View One", "Add", "Update", "Delete"])

    if action == "View All":
        response = send_request(f"{endpoint}/get_all_{entity}/", "GET")
        if response:
            st.write(response)

    elif action == "View One":
        id = st.number_input("ID", min_value=1)
        if st.button("Get"):
            response = send_request(f"{endpoint}/get_one_{entity}/{id}", "GET")
            if response:
                st.write(response)

    elif action == "Add":
        data = {}
        for field in fields:
            data[field] = st.text_input(f"{field} for {entity}")

        if st.button("Submit"):
            response = send_request(f"{endpoint}/create_user_{entity}/", "POST", data)
            if response:
                st.write(response)

    elif action == "Update":
        id = st.number_input("ID", min_value=1)
        data = {}
        for field in fields:
            data[field] = st.text_input(f"{field} for {entity} (Update)")

        if st.button("Submit"):
            response = send_request(f"{endpoint}/update_user_{entity}/{id}", "PUT", data)
            if response:
                st.write(response)

    elif action == "Delete":
        id = st.number_input("ID", min_value=1)

        if st.button("Submit"):
            response = send_request(f"{endpoint}/delete_user_{entity}/{id}", "DELETE")
            if response:
                st.write(response)

if choice == "Home":
    st.subheader("Home")
    st.write("Welcome to the Home page.")

elif choice == "Doctors":
    st.subheader("Doctors")
    fields = ["id", "name", "family", "password", "part_id"]
    handle_crud_operations("Dr", "/Dr", fields)

elif choice == "Employees":
    st.subheader("Employees")
    fields = ["id", "name", "family", "password", "part_id"]
    handle_crud_operations("Employee", "/Employee", fields)

elif choice == "Nurses":
    st.subheader("Nurses")
    fields = ["id", "name", "family", "password", "part_id"]
    handle_crud_operations("Nurse", "/Nurse", fields)

elif choice == "Parts":
    st.subheader("Parts")
    fields = ["id", "part"]
    handle_crud_operations("Part", "/parts", fields)

elif choice == "Patients":
    st.subheader("Patients")
    fields = ["id", "name_Patient", "family_Patient", "password", "parts_Patient", "dr_id_Patient", "employee_id", "nurse_id", "National_Code"]
    handle_crud_operations("Patient", "/Patients", fields)

elif choice == "Posts":
    st.subheader("Posts")
    fields = ["image_url", "image_url_type", "caption", "creator_id"]
    handle_crud_operations("Post", "/post", fields)

elif choice == "Files":
    st.subheader("Files")
    file_action = st.selectbox("File Actions", ["Upload", "Download"])

    if file_action == "Upload":
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            files = {"file": uploaded_file}
            response = requests.post(f"{BASE_URL}/file/uploadfile", files=files)
            if response:
                st.write(response.json())

    elif file_action == "Download":
        file_name = st.text_input("Enter the file name to download")
        if st.button("Download"):
            response = requests.post(f"{BASE_URL}/file/download/{file_name}")
            if response:
                st.write(response)