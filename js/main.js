"use strict";

document.addEventListener("DOMContentLoaded", () => {
  const contactForm = document.getElementById("contactForm");
  const formFeedback = document.getElementById("formFeedback");

  if (!contactForm || !formFeedback) return;

  contactForm.addEventListener("submit", event => {
    event.preventDefault();

    if (!contactForm.checkValidity()) {
      contactForm.reportValidity();
      return;
    }

    const data = new FormData(contactForm);
    const name = String(data.get("name") || "").trim();

    formFeedback.textContent =
      `Thank you, ${name}. Your enquiry details are valid. ` +
      "The website is currently in preview mode; online delivery will be connected after contact details and backend are configured.";

    formFeedback.setAttribute("aria-live", "polite");
  });
});
