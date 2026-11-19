# Mukesh — Hospitality Technology Portfolio

A dependency-free, static portfolio for a hospitality application migration and delivery professional.

## Run locally

From the repository root, start Python's built-in static web server:

```powershell
python -m http.server 8000 --directory portfolio
```

Then open <http://localhost:8000>.

## Structure

- `index.html` — accessible, semantic page content and navigation.
- `styles.css` — design tokens, reusable layout/card patterns, and responsive styles.
- `app.js` — progressive enhancements for the mobile menu and current year.

The page content is kept in HTML, visual components are kept in CSS, and behavior is kept in a small JavaScript module. This separation makes it straightforward to add sections or replace the static content source later.

## Privacy and security

The page itself does not use cookies, analytics, external assets, embedded third-party content, or forms. Its Content Security Policy limits resources to the same origin, blocks frames and plugins, and the page does not store or submit visitor information. Hosting infrastructure may still log request metadata such as IP addresses; review the hosting provider, log retention, and any applicable privacy notice or other GDPR obligations before publishing. Reassess privacy requirements before adding contact forms, analytics, or other data processing.

Before publishing, replace the contact placeholder with Mukesh's preferred contact channel and confirm the biographical details.
