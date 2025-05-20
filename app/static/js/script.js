document.addEventListener("DOMContentLoaded", function () {
  console.log("Chronos Time Tracker frontend loaded");

  // Basic form validation
  const forms = document.querySelectorAll("form");
  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      const requiredInputs = form.querySelectorAll("[required]");
      let isValid = true;
      requiredInputs.forEach((input) => {
        if (!input.value.trim()) {
          isValid = false;
          input.style.borderColor = "red";
        } else {
          input.style.borderColor = "";
        }
      });
      if (!isValid) {
        e.preventDefault();
        alert("Please fill in all required fields.");
      }
    });
  });
});
