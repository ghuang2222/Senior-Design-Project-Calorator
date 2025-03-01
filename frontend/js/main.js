document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();
            showPage(event.target.getAttribute("href").substring(1));
        });
    });

    function showPage(pageId) {
        document.querySelectorAll(".page").forEach(page => page.classList.remove("active"));
        document.getElementById(pageId).classList.add("active");
    }

    document.getElementById("meal-image").addEventListener("change", analyzeMeal);
    document.querySelector("form").addEventListener("submit", loginUser);

    function analyzeMeal() {
        let output = document.getElementById("meal-output");
        output.innerText = "Analyzing meal...";
        setTimeout(() => output.innerText = "Estimated calories: 500 kcal", 2000);
    }

    function loginUser(event) {
        event.preventDefault();
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;
        alert(username === "admin" && password === "password" ? "Login successful!" : "Invalid credentials");
    }
});
