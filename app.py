# restart
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
import google.generativeai as genai

 


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""1. Full Name: Priya Sharma  
2. Email: priyasharma123@gmail.com, Phone: +91 9876543210, LinkedIn: linkedin.com/in/priyasharma  
3. Career Objective: Seeking a challenging role as a software developer where I can apply my coding and problem-solving skills to deliver innovative solutions.  
4. Work Experience:  
   - Job Title: Software Engineer  
     Company: Infosys, Bangalore  
     Duration: Jan 2022 – Present  
     Responsibilities:  
       • Developed scalable web applications using React and Node.js  
       • Integrated REST APIs and optimized frontend performance  
   - Job Title: Intern  
     Company: Wipro  
     Duration: June 2021 – Dec 2021  
     Responsibilities:  
       • Assisted in developing internal tools using Python and Flask  
       • Created test cases and supported QA team  

5. Education:  
   - B.Tech in Computer Science, VIT University, 2021, CGPA: 8.7  
   - 12th CBSE, Delhi Public School, 2017, 90%  

6. Skills: JavaScript, Python, React, Node.js, SQL, Git, Problem Solving, Communication  

7. Certifications:  
   - AWS Certified Cloud Practitioner, 2023  
   - Coursera: Full Stack Web Development, 2022  

8. Projects:  
   - Title: Task Manager App  
     Description: A full-stack task management app using MERN stack.  
     Technologies: MongoDB, Express, React, Node.js  

9. Languages: English, Hindi  

10. Hobbies: Reading Tech Blogs, Playing Chess  
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Re-Evaluating the Approach**

I've realized the user didn't engage with the intended step-by-step guidance. They provided all information upfront, which requires me to re-evaluate my approach to efficiently process their direct input. I need to figure out how to best handle this single-shot input while still ensuring a polished final result.


**Directly Processing Input**

I've decided to directly process the user's input, as they provided all resume details upfront. Instead of the planned step-by-step interaction, I'll now focus on extracting key information and formatting it professionally. I'm building a robust system to handle this \"direct input\" scenario efficiently, delivering a polished final resume directly.


**Streamlining Resume Generation**

I've decided to prioritize processing the complete input and streamlining the resume generation process. Instead of adhering rigidly to the planned step-by-step approach, I'm now focused on directly formatting the user's information. I'll acknowledge their complete input and then proceed to structure it into the desired professional format, ensuring a quick and efficient result. I am now working on the specific sections and headings to use.


**Refining Resume Structure**

I'm now focusing on a robust structure for the resume. I'll acknowledge the complete input and prioritize organizing the content into distinct sections: Header, Career Objective, Work Experience, Education, Skills, Certifications, Projects, Languages, and Hobbies. Each section will be carefully formatted for clarity and professionalism, ensuring a smooth flow of information. I'm working on the placement and formatting of each section.


**Directly Constructing Resume**

I've determined the best approach is to directly construct the resume from the user's input. Rather than the intended dialogue, I will acknowledge their comprehensive information and immediately begin formatting. My focus is on creating a clear, ATS-friendly resume. This involves structuring the content logically and presenting it professionally within a plain text code block.


**Directly Generating the Resume**

Having analyzed the user's input, I've decided to directly generate the resume. Instead of the planned step-by-step questions, I'm now structuring the provided information. I'll acknowledge the complete input and prioritize organizing it into a clear, ATS-friendly format, acknowledging the comprehensive data provided by the user. I'll then generate a well-formatted plain text code block.


"""),
                types.Part.from_text(text="""Of course! It looks like you've provided all the necessary information. I will now compile it into a professional, ATS-friendly resume for you.

Here is your resume, formatted in plain text. You can easily copy and paste this into a document editor like Google Docs or Microsoft Word.

```
PRIYA SHARMA
+91 9876543210 | priyasharma123@gmail.com | linkedin.com/in/priyasharma

--------------------------------------------------------------------------------

CAREER OBJECTIVE

Seeking a challenging role as a software developer where I can apply my coding and problem-solving skills to deliver innovative solutions.

--------------------------------------------------------------------------------

WORK EXPERIENCE

Software Engineer | Infosys, Bangalore
(Jan 2022 – Present)
• Developed scalable web applications using React and Node.js
• Integrated REST APIs and optimized frontend performance

Intern | Wipro
(June 2021 – Dec 2021)
• Assisted in developing internal tools using Python and Flask
• Created test cases and supported QA team

--------------------------------------------------------------------------------

EDUCATION

B.Tech in Computer Science | VIT University
(2021)
• CGPA: 8.7

12th CBSE | Delhi Public School
(2017)
• Percentage: 90%

--------------------------------------------------------------------------------

SKILLS

• Technical: JavaScript, Python, React, Node.js, SQL, Git
• Soft Skills: Problem Solving, Communication

--------------------------------------------------------------------------------

PROJECTS

Task Manager App
• A full-stack task management application built using the MERN stack.
• Technologies: MongoDB, Express, React, Node.js

--------------------------------------------------------------------------------

CERTIFICATIONS

• AWS Certified Cloud Practitioner (2023)
• Coursera: Full Stack Web Development (2022)

--------------------------------------------------------------------------------

LANGUAGES

• English
• Hindi

--------------------------------------------------------------------------------

HOBBIES & INTERESTS

• Reading Tech Blogs
• Playing Chess
```"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a professional Resume Builder Assistant.

Your job is to help users create a professional, ATS-friendly resume. Ask users for the required information step-by-step. At the end, generate a resume in plain text format, formatted neatly inside a code block (```), so it can be easily copied, pasted into MS Word or Google Docs, and exported as a PDF or DOC file.

Follow this process:

1. Start with a warm welcome and tell the user:  
   “I'll ask you a few questions to help you build a downloadable resume.”

2. Ask one question at a time:
   - Full Name
   - Email and Phone Number
   - LinkedIn/Portfolio (optional)
   - Career Objective or Summary
   - Work Experience: for each role, ask for Job Title, Company, Location, Duration, Responsibilities
   - Education: Degree, Institution, Year, Grade
   - Skills (Technical + Soft)
   - Certifications or Awards (optional)
   - Projects (optional): Name, Description, Tech Used
   - Languages Known (optional)
   - Hobbies/Interests (optional)

3. After collecting all info, output the resume in clean, professional format like this:

Wrap the entire resume in a markdown code block:
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
