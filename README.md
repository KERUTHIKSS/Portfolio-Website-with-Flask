# Flask Portfolio Website

A simple, self-contained personal portfolio website built with Python and Flask. This project is designed to be easy to set up and customize, even for those new to Flask.

---

## Description

This is a single-file Flask application that serves a complete portfolio website. It includes sections for "About Me," "Projects," and a functional "Contact Me" form. All the HTML, CSS, and Python code is located in a single `app.py` file for simplicity.

---

## Features

-   **Single Page Layout:** A clean, modern, one-page design.
-   **Responsive Design:** Looks great on desktops, tablets, and mobile devices.
-   **Contact Form:** A working contact form that prints submissions to the console.
-   **Easy to Customize:** All content is within a single file, making it straightforward to edit personal information and projects.
-   **Self-Contained:** No need for separate HTML or CSS files, making it easy to run and deploy.

---

## Requirements

-   Python 3.x
-   Flask

---

## Setup and Installation

1.  **Clone the repository or download the source code.**
    (If you haven't, just save the Python code from the Canvas into a file named `app.py`).

2.  **Navigate to the project directory:**
    ```bash
    cd path/to/your/project
    ```

3.  **(Optional but Recommended) Create and activate a virtual environment:**
    -   **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

4.  **Install the required packages:**
    ```bash
    pip install Flask
    ```

---

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Open your web browser** and navigate to the following address:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

You should now see your portfolio website running locally! Any submissions to the contact form will be printed in the terminal where the application is running.

---

## Customization

To customize the website with your own information:

1.  **Open `app.py`** in a code editor.
2.  **Find the `HTML_TEMPLATE` string variable.**
3.  **Edit the HTML content directly:**
    -   Replace `"Your Name"` with your actual name.
    -   Update the bio in the "About Me" section.
    -   Fill in the "Projects" section with details about your work.
    -   Change the placeholder image URL in the "About Me" section to a link to your own photo.
