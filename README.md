# Personal Blog

## Architecture

This project is a simple personal blog web application built with Python and Flask. The application uses server-side rendering with Jinja2 templates for all pages, providing a straightforward and SEO-friendly experience. The backend is responsible for handling routing, authentication, and file-based article storage, while the frontend uses HTML and CSS for layout and styling.

Articles are stored as individual JSON files in the `articles/` directory. Each file contains the article's title, content, and publication date. This approach keeps the storage simple and easy to manage, making it ideal for small-scale personal projects.

## Functionality

- **Guest Section:**
  - Home page lists all published articles with their titles and dates.
  - Article page displays the full content and publication date of a selected article.
- **Admin Section:**
  - Login/logout with basic authentication (hardcoded credentials).
  - Dashboard to view, add, edit, and delete articles.
  - Forms for creating and editing articles, including title, content, and date fields.

All admin routes are protected and require authentication. The application uses Flask sessions to manage admin login state.

## Testing

Manual testing can be performed by running the Flask app locally and interacting with the web interface:

1. Start the app: `python app.py`
2. Visit `http://127.0.0.1:5000` to view the blog as a guest.
3. Go to `/login` to access the admin dashboard (default credentials: `admin` / `password`).
4. Add, edit, or delete articles and verify changes on the home page.

For automated testing, you can extend the project with unit tests for the article storage logic and integration tests for the Flask routes using tools like `pytest` and `Flask-Testing`.

## Reflection

Building this project provided hands-on experience with full stack web development using Python and Flask. I learned how to design a simple file-based storage system, implement basic authentication, and create a clean, user-friendly interface with HTML and CSS. The iterative process of developing, testing, and refactoring the code helped me improve my problem-solving skills and deepen my understanding of both backend and frontend technologies.

This project also reinforced the importance of clear code structure, modular design, and user experience. By integrating authentication and admin features, I gained practical knowledge in securing web applications and managing user sessions. Overall, this project has been a valuable step in my journey as a web developer.