---
Universal Resource Locators - Schema for unrCrewGallax
---
#### Authentication Schema
[ Added but not active ]: Authentication uses JWT and custom roles that must be configured manually [ only a supreme user has access to that. ] or must be configured by doing some required activity.

* [ Inactive But added ]Registration: After Succesful registration, user's need to verify their emails or the account will be flagged inactive. 
* [ Inactive But added ]Accounts: InActive Accounts are completly Forbidden from accessing any form of data on server.
---
#### Fetch Requests - Home [ GET ]
    request url: /api/home/
response 👇
```json
[
    {
        "company_banner": "/media/company/back7.jpg",
        "company_logo": "/media/company/logo2.png",
        "home_head": "Build your Future With Corsrex",
        "home_about": "Enhance your knowledge and skills by enrolling in our courses. Expand your expertise and gain valuable insights to further your personal, professional and financial growth. Earn well after starting your learning journey today!",
        "showcase": [
            {
                "id": "6c96b184-fb77-40ee-b75d-e67c8d47185d",
                "updated_at": "2023-09-18",
                "course_banner": "/media/courses/c1.jpg",
                "course_title": "HTML and CSS Beginners Course",
                "rating": 4.2,
                "pricing": "49.99"
            }
        ]
    }
]
```
---
#### Fetch Requests - Single Course [ GET ]
    request url: /api/course/<id>/
* Fetching a single course requires the <code>ID</code> of the course, and type of <code>request: GET</code>.
response 👇
```json
{
    "id": "6c96b184-fb77-40ee-b75d-e67c8d47185d",
    "updated_at": "2023-09-18",
    "course_banner": "/media/courses/c1.jpg",
    "course_title": "HTML and CSS Beginners Course",
    "rating": 4.2,
    "course_taglines": [
        "Modern HTML5 and CSS3 from the Beginning",
        "All the way upto Frameworks like Tailwind and Bootstrap."
    ],
    "course_overview": "Welcome to our HTML and CSS Beginners Course! In the vast world of web development, a strong foundation in HTML and CSS is necessary. These two technologies serve as the backbone of every website on the internet, making them essential skills for aspiring web developers.\r\n\r\nHTML provides structure and semantic meaning to web content, allowing for headings, paragraphs, lists, images, and forms. CSS controls visual presentation and layout, enabling customization of colors, fonts, backgrounds, and more. Together, they create well-organized, accessible websites and transform plain HTML into visually appealing, user-friendly experiences.\r\n\r\nBy mastering HTML and CSS, you will possess the skills to craft stunning, responsive websites that captivate users and convey information effectively. Our HTML and CSS Beginners Course is designed to equip you with hands-on experience and practical knowledge to create professional-looking web pages from scratch.",
    "category": {
        "id": "6130c960-1dbf-43eb-93f9-8ccc30d8a43b",
        "name": "Web Development"
    },
    "benifits": [
        "HTML and CSS from scratch - beginner to advanced",
        "Introduction",
        "Basic HTML Structure and Tags",
        "Basic to Advanced CSS Styling and Layout",
        "Responsive Web Design for Mobile and Tablets",
        "CSS Frameworks like Bootstrap and Tailwind",
        "Web Accessibility and Project-based Learning"
    ],
    "pricing": "49.99",
    "base_currency": "usd",
    "teacher": [
        {
            "id": "96e3625e-301e-422d-8f9f-063611096fe6",
            "instructer_name": "Diana Lopez",
            "instructer_profile": "/media/instructers/pro3.png",
            "instructer_about": "Front-End Developer At Google"
        }
    ],
    "included": [
        {
            "id": "7084df01-075a-46b3-99b9-75a38d3f371b",
            "title": "20+ Hours Video Content",
            "icon": "play_circle"
        },
        {
            "id": "9a89bdd7-7db5-4557-bac1-660db18deb42",
            "title": "75 Technical Articles",
            "icon": "newspaper"
        },
        {
            "id": "e3cea90d-beab-4598-8438-f79ed19fd8d7",
            "title": "Downloadable Resources",
            "icon": "cloud_download"
        },
        {
            "id": "e256ba11-4c6b-4965-a39b-d08522a8ebd2",
            "title": "Full Lifetime Access",
            "icon": "all_inclusive"
        },
        {
            "id": "542662bf-66cb-4f4d-a7f8-a5f0fb487b82",
            "title": "Access on Mobile and Tablet",
            "icon": "devices"
        },
        {
            "id": "33103819-05ce-49cb-b0c7-1104f2c419e0",
            "title": "Assignments & Projects",
            "icon": "edit_document"
        },
        {
            "id": "a0474b5d-bcee-4f1f-b996-03c803d62ae8",
            "title": "Certificate of Completion",
            "icon": "emoji_events"
        }
    ]
}
```
---
#### Fetch Requests - All Courses [ GET ]
    request url: /api/courses/
response 👇
```json
[
    {
        "id": "6c96b184-fb77-40ee-b75d-e67c8d47185d",
        "updated_at": "2023-09-18",
        "course_banner": "/media/courses/c1.jpg",
        "course_title": "HTML and CSS Beginners Course",
        "rating": 4.2,
        "pricing": "49.99"
    }
]
```
* At the time of creating this readme, I only added one course to the Database for testing. But this is an <code>Array or List</code> of courses.
---
#### Fetch Requests - All Blogs [ GET ]
    request url: /api/blogs/
response 👇
```json
[
    {
        "id": "886e0797-f08f-4c1b-a080-3ccaaaaf9a04",
        "updated_at": "2023-09-18",
        "title": "Learn Web Developement in the Easiest Way",
        "banner": "/media/blogs/b1.jpg",
        "truncated_description": "Are you itching to dive into the world of web development but feeling overwhelmed by the sheer volume of information and technologies out there? Don't worry; you're not alone. Web development may seem complex at first glance, but with the right approach, it can be an exciting and accessible journey..."
    }
]
```
* At the time of creating this readme, I only added one Blog to the Database for testing. But this is an <code>Array or List</code> of Blogs.
---
#### Fetch Requests - Single Blog [ GET ]
    request url: /api/blog/<id>/
* Fetching a single blog requires the <code>ID</code> of the object, and type of <code>request: GET</code>.
response 👇
```json
{
    "id": "886e0797-f08f-4c1b-a080-3ccaaaaf9a04",
    "updated_at": "2023-09-18",
    "title": "Learn Web Developement in the Easiest Way",
    "banner": "/media/blogs/b1.jpg",
    "description": "Are you itching to dive into the world of web development but feeling overwhelmed by the sheer volume of information and technologies out there? Don't worry; you're not alone. Web development may seem complex at first glance, but with the right approach, it can be an exciting and accessible journey. In this blog post, we'll guide you through the easiest way to learn web development, step by step.\r\n\r\nStep 1: Start with HTML and CSS\r\n\r\nThe foundation of web development lies in two core technologies: HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets). HTML is used to structure web content, while CSS is used for styling. These are the building blocks of every web page.\r\n\r\nTo start, head to online tutorials and documentation, such as Mozilla Developer Network (MDN) or W3Schools, and learn the basics of HTML and CSS. These resources provide interactive examples and clear explanations to get you started.\r\n\r\nStep 2: JavaScript - The Language of the Web\r\n\r\nJavaScript is the language of interactivity on the web. It allows you to create dynamic and responsive web applications. Once you have a solid grasp of HTML and CSS, start learning JavaScript.\r\n\r\nPopular online platforms like Codecademy, freeCodeCamp, and JavaScript.info offer comprehensive JavaScript courses. Take your time to understand fundamental concepts like variables, functions, and event handling.\r\n\r\nStep 3: Responsive Web Design\r\n\r\nAs you learn HTML, CSS, and JavaScript, start exploring responsive web design. Responsive design ensures that your web applications look great and function well on various devices, from desktops to smartphones.\r\n\r\nMastering responsive design involves learning about media queries and flexible layouts. CSS frameworks like Bootstrap and Flexbox can simplify this process.\r\n\r\nStep 4: Explore Front-end Frameworks\r\n\r\nFront-end frameworks like React, Angular, and Vue.js simplify web development by providing pre-built components and a structured approach. Choose one that suits your preferences and start building with it.\r\n\r\nStep 5: Back-end Development\r\n\r\nTo create dynamic and data-driven web applications, you'll need to understand back-end development. Popular back-end languages include Node.js (JavaScript), Python, Ruby, and PHP. Explore server-side programming, databases (SQL or NoSQL), and RESTful APIs.\r\n\r\nStep 6: Version Control with Git\r\n\r\nVersion control is crucial for collaborating with others and keeping track of your code changes. Learn Git, a widely-used version control system, to manage your code effectively. Platforms like GitHub and GitLab provide hosting and collaboration tools for your projects.\r\n\r\nStep 7: Deploy Your Projects\r\n\r\nOnce you've built some web applications, it's time to showcase your work to the world. Learn about web hosting, domain management, and deployment processes. Services like Netlify and Vercel make it easy to deploy web projects with just a few clicks.\r\n\r\nStep 8: Continuous Learning\r\n\r\nWeb development is a constantly evolving field. Stay updated by following blogs, attending webinars, and participating in online communities. Engage with fellow developers, share your knowledge, and continue to explore new technologies and trends.\r\n\r\nRemember, learning web development is a journey, not a destination. Take your time, practice regularly, and don't be afraid to make mistakes. The web development community is vast and supportive, and there are plenty of resources available to help you succeed. Start small, be persistent, and before you know it, you'll be creating amazing web applications with ease. Happy coding!"
}
```
---
#### Delete Requests - Single Course or Blog [ DELETE ]
    request url: /api/course/<id>/
* Deleting a course or blog requires the <code>ID</code> of the object, and type of <code>request: DELETE</code>.
* Only Registerd Users can Delete from the server.
response [ non-registered user ] 👇
```json
{
    "status": "Forbidden"
}
```
response [ registered user ] 👇
```json
{
    "status": "Deleted"
}
```