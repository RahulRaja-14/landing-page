import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="NVidya", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .headline {
        font-size: 50px;
        color: orange;
        font-weight: bold;
        text-align: center;
    }
    .subtext {
        font-size: 20px;
        color: skyblue;
        text-align: center;
        margin-left:5px;
    }
    .footer {
        font-size: 14px;
        color: #888;
        text-align: center;
        margin-top: 50px;
    }
    .team-name {
        font-size: 24px;
        font-weight: bold;
        color: #555;
        text-align: center;
    }
    .images-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-left: 100px;
    }
    .image-container img {
        width: 200px;
        margin: 100px;
        margin-top: 10px;
        gap:100px;
        margin-left: 80px; 
    }
    .social-icons {
        display: flex;
        justify-content: center;
        gap:10px;
    }
    .social-icons a img {
        width: 20px; /* Adjust size of the icons */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main headline
st.markdown('<div class="headline">CMR - TECHFEST 2025</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext"><b>Team Name:</b> Transformers</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext"><b>Problem Statement Number:</b> 37 (Generative AI)</div>', unsafe_allow_html=True)

# Add spacing
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

# Side-by-side layout with columns
col1, col2 = st.columns([1, 2])

# Left column: Logo with space in front
with col1:
    # Display logo with custom inline CSS styling
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-top: 50px; margin-left: 100px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 1);">
            <img src="https://media-hosting.imagekit.io//3d71e8deb79f4ba8/Logo-3.png?Expires=1830942360&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=S0fYWLovCQHJlCqBX7JLB4ZNuWnVgCETUFkiz6oMWYUFnNi8BHaEuPmVfWOvJFp7PyyTFHkCtw61DuEPnAjjI1JwFraBxVSdLWt3q0dJJQTdjXlyWdZU6umg6rTTJ8jQkpD4tcWwmfTECUk9BQhHbo5brMXk9WmMI-yoJcpEFRcwD6JdUqzDSGYB~Kfe2GKRN0PTeSTtLgvYWWlkfb2q8JDHA4wUlBKvehHVvbyyUFeOAtx-m4go4t8BeQAaQoHp3bEnGpn3jCcbCKtyVX1ywKPIevPtR1SJ1F6MusJhcD2OTm3HVfonaj74CONyyDuIQU4ZHFkezs~WDKCSiiQ5GA__" width="500" alt="CMR Logo" style="border-radius: 200px;">
        </div>
        """,
        unsafe_allow_html=True,
    )

# Right column: Project description
with col2:
    st.markdown(
        """
        ### NVidya - Learning Made Easy

        **NVidya AI** is your intelligent learning partner, designed to simplify education through the power of AI. 
        Our application generates high-quality, customized educational content tailored to your needs. Whether you’re 
        a student, teacher, or lifelong learner, NVidya AI helps create quizzes, lessons, and resources that match 
        your curriculum and grade level. With a focus on accuracy, ease, and innovation, we aim to make learning smarter, 
        faster, and more effective.

        At NVidya-AI, we understand the importance of personalized and reliable educational content. That’s why our 
        platform ensures that every resource aligns with your learning objectives, making it easier to grasp complex 
        topics and achieve your goals.

        *Experience the future of education with NVidya-AI!*
        """,
        unsafe_allow_html=True,
    )

# Add CSS for styling
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
        margin-left: 200px;
    }
    .stButton button {
        width: 200px;
        height: 50px;
        font-size: 20px;
        margin-left: 600px;
    }
    </style>
""", unsafe_allow_html=True)

# Center the button
st.markdown('<div class="button-container">', unsafe_allow_html=True)

if st.button("Launch NVidya AI"):
    st.markdown('<meta http-equiv="refresh" content="0;URL=https://cmr-hackfest.streamlit.app/">', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Set the page title and header
st.title("Discover the Features")
st.subheader(
    "NVidya AI offers tailored educational tools to enhance learning for students, teachers, and lifelong learners.")

st.markdown("<br><br>", unsafe_allow_html=True)

# Create four equal columns for the features
col1, col2, col3, col4 = st.columns(4)

# Add content to the first column
with col1:
    st.image(
        "https://media-hosting.imagekit.io//89fcc553d3404484/th%20(2).jpg?Expires=1832952209&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=w5Ft0j3uH66njLJ824O7T-hKSiXIYLrQm7cEIoQdHBvS7tlAqkiqABb7NPCgR3NdpzKJos7dcRVh~x9m-5HQPP2HjZfs2t~9S-gyspcGgvlOekZnvsA54c2IFyT68PUfU73PFin2rYsjFSkOSTGeDyOxawsYIvs57U7QwdfNNWvYc1vwLID0RgfPRbieBdNI-NXEc3SdReMzL7xeAnjfVz5EOqQWuLh8uWwwY8ar0LnHRXJb9CVejGWVUDYKuVR5vrfYEUlcd-UvAidusu-6o~45Y6iB21jvwJbwi8OR-egF2XBpXN6T1bMGJbRUiuQif2xGV6a4AFyYKvAqL4BSSg__",
        width=30)  # Replace with your icon URL or local path
    st.subheader("Content Personalization")
    st.write(
        "Generate quizzes, lessons, and study materials tailored to specific grade levels, subjects, and curricula for personalized learning experiences."
    )

# Add content to the second column
with col2:
    st.image(
        "https://media-hosting.imagekit.io//5718d87e4c9a41b8/th%20(3).jpg?Expires=1832952209&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Z91lIOg~AUYPougbuTRvl~-bd3S1HgtJLD5WD7FEG5DRf70Zn46Dhr66Ucg3O9DZa8QEhz3guXtB-dxaPu6lXY9C7vgn-jC5v3oFyvFGFSAA83bm4HvvfiNrVmfqeyRDAilPP8zUqVRdL~94nGuy75irIEldr3~Y~b3lgUeUPsJJbCbaZMfkaFAGqO8qhWV21j53kCYi8RG5ToIpV1li2IHS7ov~7HpZXU22rAlTMJUFgXDqz1R9mRr5ITbM-J0Y1c4TG1QMvGAeaska3Wl2bxENQ9yU6ExlkdySxX-TU9pMGEYLmes-4xYdZc799U4R8oJFQWkvpoL88lnDGbQxWA__",
        width=30)  # Replace with your icon URL or local path
    st.subheader("AI-Powered Insights")
    st.write(
        "Get data-driven recommendations and performance insights to identify strengths and improve learning effectively."
    )

# Add content to the third column
with col3:
    st.image(
        "https://media-hosting.imagekit.io//decd685bc882480c/a3ea4c90a81a5713113fd42e20bb312f-e-learning-logo-design.jpg?Expires=1832952209&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=2uqz8lr0358v3qCuJPGmLscXNKFAHaX4k9Xtd7K~SreUwhQ9LeVGIwMqU1sxC88EBZPvYRciEcD2hqZBhmjWtMC5c~-lw3JMwNfwDg5ZGBgCzOx3kU~KqY2rxECieZsjL~zYrMLvgg54WTp3ulrf~qWKMS6itKMyO99dACRoIKqqiH5xrUty~TUz0u1zLJzAJD49sZKcKW6tWxEwNCYsCWB83Qp1QGjX2o0AHAmxeZ0fG8Ebj88~X~NgzG8t-pmGVtxLPf2nW9ExgKGD1tPwqZZjVYxQPWueEv04uYAIFSlq4boFdGCh~~9DD1wu4tli1vAePXShIoU1zzUGmGBb-g__",
        width=30)  # Replace with your icon URL or local path
    st.subheader("Interactive Learning Tools")
    st.write(
        "Explore dynamic tools such as flashcards, concept maps, and practice quizzes to make complex topics engaging and easy to understand."
    )
# Add content to the fourth column
with col4:
    st.image(
        "https://media-hosting.imagekit.io//976051510c9a4869/th%20(5).jpg?Expires=1832952209&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=j1q92PJHkMUr3qNssTEQQjguagqj9ucOhu512DlFDJT1BjhpSJQumvm8hiL08oTpbMOUpNK9Xe0UpYfiEmyQBVmTpmMUPkNYH2sZ7VWrmnXm6Giar48x9nbZ~RWY53cSG93JXd-MDZHT~BfymljEfZLnKnp-zn9GFg5mwDrFMaZF1Bo53zQSXnOKy7SrCmLxxvMbr8Q-rXva38SSnrKfiIOf5bnZ05gur0IY-NFPKOyuW6eQWyI8q4wnpnrzC1yAOyLIeDYZg-ihpitKYYgKHBxGP6Vg9hPWHZd2EUm5unm0HJ~goSto3eByDHVos2W7q-OGTVXAsDtyrxmqGfv~Og__",
        width=30)  # Replace with your icon URL or local path
    st.subheader("Multi-Language Support")
    st.write(
        "Access educational content in multiple languages to cater to diverse learners and ensure inclusivity in education."
    )

# Add styling
st.markdown(
    """
    <style>
    .stImage > img {
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="subtext"><h1>Team Transformers</h1></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Separate data into two lists
team_images = [
    {
        "image": "https://media-hosting.imagekit.io//e1657929bf734b4d/125.jpg?Expires=1832954170&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=R4DuufkY8EHjs0lyZhntDE~3seN5cyfaNlqdxTjYOira~vZm8GSNGf2PS8LWtBq2eDadU7GKlEtH0Nwr92eFhyS-OfBWTsEvvbVM~RAZVT-jUltPeWtntI1LoJozGZ2BOAjGebZNpV1SVTNRE-1DLPnlhsqrztGQq740qHg6yqfFpJVdu1zGB0wSBiyn0SN10khsTYnC5KQk~8TLuYPEtiwQKbq3Zsw149mbKkEjYHorkqChUGkR0FyD~5rzr4S3RErkT1voqSUkZI8AEMYBBpbfUkBRBJN-pin~aRV9pJZbGmtDYFaEA9WN7uRaI6FR9y3gonYwmcj9gzs2lbiITg__",
        "name": "Dharan Balaji S B"
    },
    {
        "image": "https://media-hosting.imagekit.io//665bce29497d465a/IMG_6289.JPEG.jpg?Expires=1832954170&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Co3zyAGppF0CC2H9rFdg3Kp8GtWX~WIAHlT9WseMJjz97h1Z1Tp-9cBgxhdaqWkEbuFtbs0kEBf-m1u7HKOzHe-zNNkjG722JHaoF608hW-C~HxJFirWBjeNA6HDZ2TrDwLUOkOBB6EtbuAN3Q9TBPbmaKdKBb~nU-EtlW6CTNv5kpoCRjarEilqE~M2GcnNWzHTifOHwe8R4a1-M6DgkEj5~-yHHSqik5AzL71Cgt4W3HWWIoqlfbiUKeb3H~tn84su~RTKCwDUAepFqkVeDzdp5Nr97ctTt7R5J-1pAsbPveytlnm120Oa5r~OZJ76ZpTA9mvmKugjvDdIRYC-Qw__",
        "name": "Akash Selvadoss N"
    },
    {
        "image": "https://media-hosting.imagekit.io//b4e22b71610d4ad0/1000017789%20(413%C3%97531).jpg?Expires=1832967432&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=jmZ~nl3-2nOZuK9rlcu9~zrt0Mw45hWYtEWeTz-ONiGSjMLViGbpg-0zyMHIf61IxYF6WQXDOWED3vk43Sd6y-c1sNAPXI4FRKr0hmjbxKFqRSJrTQEmNXis0~HbvTIZINAE0bLJHl4Msy6U8yilQ7o-hg-uppIHfnhqgqrY7lcv7n4kAZ-rMARvUdsfFmxqxpq4wtKow6LLd8DIBxLnhOAZunOIux3pdzdD~BpkPdQo3V14r28TBd94eC9fv5WhElpTnwreq69bx9HVzcRWIKrE3Rxfo4hnCpO2XBxDfAGoqwGZoQyAeQj6lDf2s8R3j2WXgj62dL6mvb1P5Ugmtg__",
        "name": "Rahul Raja P"
    },
    {
        "image": "https://media-hosting.imagekit.io//ae2e28b70d50441d/Pi7_Passport_Photo.jpeg?Expires=1830867446&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=gGWPE2JiuUA7h92OTWGjFKkMstd1F8l0g4NNIujz6G4nn15M4plc5dfoNKUEbaikvIUfFyKQnZh69wm0h-k~lftIaCW6ptlGsR02VkFobW-sOOuB8~fOhm0vyNYPDcpKh9y0ZnGsrmVRMwA9y9EnILJTtsAb6IKjeFSyeKN~kxi43oSDL4wnymxRZQp3DOgvosfYgsrwAqnGmdFN-J~WaS5MU-NM~HHfOWUxESM01XFimDYodVNqF6l7~Q-JB81s0omd6M8qj~z7w1BnkKDNt19lXndWOAIXAw2S-t9UPvUHLGSlSNH37rRYvi1vRZKR3PyG7xHINjdytjFjZVcS0A__",
        "name": "Malaiarasu G"
    },
]

social_links = [
    {
        "linkedin": "https://www.linkedin.com/in/dharan-balaji-s-b-50aa80320/",
        "github": "https://github.com/dharanbalaji"
    },
    {
        "linkedin": "https://www.linkedin.com/in/akash-selvadoss-n-542765252",
        "github": "https://github.com/akashdoss"
    },
    {
        "linkedin": "https://www.linkedin.com/in/rahul-raja-p-124639252?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BRpRxBb1QRq60x%2Fs1FFKTcA%3D%3D",
        "github": "https://github.com/RahulRaja-14"
    },
    {
        "linkedin": "https://www.linkedin.com/in/malaiarasu-g-raj-38b695252",
        "github": "https://github.com/MalaiarasuGRaj"
    },
]

# Create columns to display the team members
cols = st.columns(4)

# Display images
for i, col in enumerate(cols):
    with col:
        member = team_images[i]

        # Adjust alignment by wrapping the image in a div with inline styles
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; margin-left: 5px;">
                <img src="{member['image']}" style="width: 150px; margin-bottom: 10px;">
            </div>
            <div style="text-align: center; font-size: 14px; font-weight: bold;">
                {member['name']}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Add spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Display social links
for i, col in enumerate(cols):
    with col:
        links = social_links[i]
        st.markdown(
            f"""
            <div class="social-icons">
                <a href="{links['linkedin']}" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
                </a>
                <a href="{links['github']}" target="_blank">
                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
