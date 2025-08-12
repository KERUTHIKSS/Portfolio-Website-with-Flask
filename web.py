from flask import Flask, render_template_string, request

# Initialize the Flask application
app = Flask(__name__)

# --- HTML Template ---
# This string contains the entire HTML and CSS for the portfolio website.
# Using a single template string makes this a self-contained, easy-to-run example.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <style>
        /* Basic CSS for styling the portfolio */
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
        }
        .container {
            max-width: 960px;
            margin: auto;
            overflow: hidden;
            padding: 0 20px;
        }
        header {
            background: #333;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
            border-bottom: #0779e4 3px solid;
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        header p {
            margin: 0;
            font-size: 1.2rem;
            color: #ccc;
        }
        #about, #projects, #contact {
            padding: 4rem 0;
            border-bottom: 1px solid #ddd;
        }
        h2 {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2rem;
            color: #333;
        }
        #about img {
            display: block;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 0 auto 1rem;
            border: 3px solid #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }
        .project-card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-card h3 {
            margin-top: 0;
            color: #0779e4;
        }
        #contact-form {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 1rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box; /* Important for padding */
        }
        .btn {
            display: inline-block;
            background: #0779e4;
            color: #fff;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            text-align: center;
            width: 100%;
            transition: background-color 0.3s ease;
        }
        .btn:hover {
            background: #0056b3;
        }
        footer {
            text-align: center;
            padding: 2rem 0;
            background: #333;
            color: #fff;
            margin-top: 2rem;
        }
    </style>
</head>
<body>

    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Your Name</h1>
            <p>Web Developer | Data Scientist | Tech Enthusiast</p>
        </div>
    </header>

    <!-- About Me Section -->
    <section id="about" class="container">
        <h2>About Me</h2>
        <img src="https://placehold.co/150x150/0779e4/white?text=You" alt="A placeholder image of you">
        <p style="text-align:center;">
            Hi, I'm [Your Name]! I am a passionate and creative developer based in [Your City]. I specialize in building modern, responsive, and user-friendly web applications. My journey in tech started with a curiosity for how things work, and it has evolved into a career where I can build meaningful products.
        </p>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="container">
        <h2>My Projects</h2>
        <div class="project-grid">
            <div class="project-card">
                <h3>Project One</h3>
                <p>A brief description of your first amazing project. Explain the technology used and its purpose.</p>
            </div>
            <div class="project-card">
                <h3>Project Two</h3>
                <p>A brief description of your second amazing project. Explain the technology used and its purpose.</p>
            </div>
            <div class="project-card">
                <h3>Project Three</h3>
                <p>A brief description of your third amazing project. Explain the technology used and its purpose.</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="container">
        <h2>Contact Me</h2>
        <div id="contact-form">
            <form action="/submit_form" method="post">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" rows="5" required></textarea>
                </div>
                <button type="submit" class="btn">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 Your Name. All Rights Reserved.</p>
    </footer>

</body>
</html>
"""

# --- Flask Routes ---

@app.route('/')
def home():
    """
    Renders the main portfolio page.
    """
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """
    Handles the contact form submission.
    In a real-world app, you would send an email or save to a database here.
    """
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # For this example, we'll just print the data to the console.
        print(f"--- New Contact Form Submission ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print(f"------------------------------------")

        # You can return a simple confirmation message or redirect.
        # For a better user experience, you could create a 'thank you' page.
        return "Thank you for your message! I will get back to you soon."

# --- Main Execution ---
if __name__ == '__main__':
    # To run this app:
    # 1. Make sure you have Flask installed (`pip install Flask`).
    # 2. Save this code as a Python file (e.g., `portfolio_app.py`).
    # 3. Run it from your terminal (`python portfolio_app.py`).
    # 4. Open your web browser and go to http://127.0.0.1:5000
    app.run(debug=True)