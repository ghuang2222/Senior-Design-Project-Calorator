document.addEventListener("DOMContentLoaded", () => {
    // Initialize navigation
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();
            const pageId = event.target.closest('a').getAttribute("href").substring(1);
            showPage(pageId);
        });
    });

    // Function to show a specific page and update active nav link
    window.showPage = function(pageId) {
        // Hide all pages
        document.querySelectorAll(".page").forEach(page => page.classList.remove("active"));
        
        // Show the selected page
        const targetPage = document.getElementById(pageId);
        if (targetPage) {
            targetPage.classList.add("active");
        }
        
        // Update active state in navigation
        document.querySelectorAll(".nav-link").forEach(navLink => {
            navLink.classList.remove("active");
            navLink.removeAttribute("aria-current");
        });
        
        // Set active class on the clicked nav link
        const activeNavLink = document.querySelector(`.nav-link[href="#${pageId}"]`);
        if (activeNavLink) {
            activeNavLink.classList.add("active");
            activeNavLink.setAttribute("aria-current", "page");
        }
    }

    // Handle scroll effect for navbar
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    // Handle meal image analysis
    document.getElementById("mealImage").addEventListener("change", function(e) {
        handleFiles(this.files);
    });
    
    // Handle form submissions
    const loginForm = document.querySelector("#loginForm");
    const registerForm = document.querySelector("#registerForm");
    
    if (loginForm) {
        loginForm.addEventListener("submit", loginUser);
    }
    
    if (registerForm) {
        registerForm.addEventListener("submit", registerUser);
    }

    // Initialize MDB form elements
    document.querySelectorAll('.form-outline').forEach((formOutline) => {
        new mdb.Input(formOutline).init();
    });

    // Toggle between login and register cards
    window.toggleAuthCards = function(showCardId) {
        const loginCard = document.getElementById('loginCard');
        const registerCard = document.getElementById('registerCard');
        
        if (showCardId === 'loginCard') {
            loginCard.classList.remove('d-none');
            registerCard.classList.add('d-none');
        } else {
            loginCard.classList.add('d-none');
            registerCard.classList.remove('d-none');
        }
    }

    // Login functionality
    function loginUser(event) {
        event.preventDefault();
        
        // Get form elements
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const loginButton = document.getElementById("loginButton");
        const loginSpinner = document.getElementById("loginSpinner");
        const loginAlert = document.getElementById("loginAlert");
        
        // Validate form
        if (!username || !password) {
            showMessage("loginAlert", "Please enter both username and password", "danger");
            return;
        }
        
        // Show loading state
        loginButton.disabled = true;
        loginSpinner.classList.remove("d-none");
        
        // Clear previous alerts
        clearMessage("loginAlert");
        
        // Simulate API call (replace with actual backend call)
        setTimeout(() => {
            // For demo purposes - in real app, this would be an API call
            if (username === "admin" && password === "password") {
                // Successful login
                showMessage("loginAlert", "Login successful! Redirecting...", "success");
                
                // Store login state
                sessionStorage.setItem('isLoggedIn', 'true');
                
                // Show user as logged in
                setTimeout(() => {
                    showUserLoggedIn();
                    showPage('home');
                }, 1000);
            } else {
                // Failed login
                showMessage("loginAlert", "Invalid username or password", "danger");
                loginButton.disabled = false;
                loginSpinner.classList.add("d-none");
            }
        }, 1500);
    }
    
    // Registration functionality
    function registerUser(event) {
        event.preventDefault();
        
        // Get form elements
        const fullName = document.getElementById("fullName").value;
        const email = document.getElementById("email").value;
        const username = document.getElementById("newUsername").value;
        const password = document.getElementById("newPassword").value;
        const registerButton = document.getElementById("registerButton");
        const registerSpinner = document.getElementById("registerSpinner");
        
        // Validate form
        if (!fullName || !email || !username || !password) {
            showMessage("registerAlert", "Please fill in all fields", "danger");
            return;
        }
        
        // Show loading state
        registerButton.disabled = true;
        registerSpinner.classList.remove("d-none");
        
        // Clear previous alerts
        clearMessage("registerAlert");
        
        // Simulate API call (replace with actual backend call)
        setTimeout(() => {
            // For demo purposes - in real app, this would be an API call
            showMessage("registerAlert", "Registration successful! Please sign in.", "success");
            
            // Reset form
            document.getElementById("registerForm").reset();
            
            // Switch to login form after short delay
            setTimeout(() => {
                toggleAuthCards('loginCard');
            }, 2000);
            
            // Reset button state
            registerButton.disabled = false;
            registerSpinner.classList.add("d-none");
        }, 1500);
    }
    
    // Function to show message
    function showMessage(alertId, message, type) {
        const alert = document.getElementById(alertId);
        alert.textContent = message;
        alert.classList.remove("d-none", "alert-danger", "alert-success");
        alert.classList.add("d-block", `alert-${type}`);
    }
    
    // Function to clear message
    function clearMessage(alertId) {
        const alert = document.getElementById(alertId);
        alert.classList.remove("d-block", "alert-danger", "alert-success");
        alert.classList.add("d-none");
    }
    
    // Function to show logged in state
    function showUserLoggedIn() {
        document.getElementById('loginBtn').classList.add('d-none');
        document.getElementById('userDropdown').classList.remove('d-none');
    }
    
    // Logout functionality
    window.logoutUser = function() {
        document.getElementById('loginBtn').classList.remove('d-none');
        document.getElementById('userDropdown').classList.add('d-none');
        
        // Clear login state
        sessionStorage.removeItem('isLoggedIn');
        
        // Redirect to home
        showPage('home');
    }
    
    // Check if user is already logged in
    if (sessionStorage.getItem('isLoggedIn') === 'true') {
        showUserLoggedIn();
    }

    // Track Meal Page Functionality
    const uploadArea = document.getElementById('uploadArea');
    const uploadContent = document.getElementById('uploadContent');
    const previewArea = document.getElementById('previewArea');
    const imagePreview = document.getElementById('imagePreview');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const analysisResults = document.getElementById('analysisResults');
    const mealImage = document.getElementById('mealImage');

    // Drag and drop functionality
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, unhighlight, false);
    });

    function highlight(e) {
        uploadArea.classList.add('dragover');
    }

    function unhighlight(e) {
        uploadArea.classList.remove('dragover');
    }

    uploadArea.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
    }

    // File input change handler
    mealImage.addEventListener('change', function(e) {
        handleFiles(this.files);
    });

    function handleFiles(files) {
        if (files.length > 0) {
            const file = files[0];
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    imagePreview.src = e.target.result;
                    uploadContent.classList.add('d-none');
                    previewArea.classList.remove('d-none');
                    analyzeBtn.disabled = false;
                    
                    // Reset analysis results when new image is uploaded
                    analysisResults.classList.add('d-none');
                }
                reader.readAsDataURL(file);
            } else {
                alert('Please upload an image file');
                removeImage();
            }
        }
    }

    // Make removeImage function global
    window.removeImage = function() {
        imagePreview.src = '';
        uploadContent.classList.remove('d-none');
        previewArea.classList.add('d-none');
        analyzeBtn.disabled = true;
        analysisResults.classList.add('d-none');
        mealImage.value = '';
    }

    // Make analyzeMeal function global
    window.analyzeMeal = function() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        const loadingText = document.getElementById('loadingText');
        const analyzeBtn = document.getElementById('analyzeBtn');
        
        // Show loading overlay
        loadingOverlay.style.display = 'flex';
        loadingText.textContent = 'Analyzing your meal...';
        analyzeBtn.disabled = true;

        // Simulate API call with timeout
        setTimeout(() => {
            // Hide loading overlay
            loadingOverlay.style.display = 'none';
            analyzeBtn.disabled = false;
            
            // Show results
            analysisResults.classList.remove('d-none');
            
            // Scroll to results
            analysisResults.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 5000); // 5 seconds delay
    }

    // Make trackMeal function global
    window.trackMeal = function() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        const loadingText = document.getElementById('loadingText');
        const trackBtn = document.getElementById('trackMealBtn');
        
        // Show loading overlay
        loadingOverlay.style.display = 'flex';
        loadingText.textContent = 'Tracking your meal...';
        trackBtn.disabled = true;

        // Simulate API call with timeout
        setTimeout(() => {
            // Hide loading overlay
            loadingOverlay.style.display = 'none';
            trackBtn.disabled = false;
            
            // Reset the form
            removeImage();
            analysisResults.classList.add('d-none');
            
            // Show success message
            showToast('Meal tracked successfully!', 'success');
        }, 2000); // 2 seconds delay
    }

    function showToast(message, type = 'success') {
        // Create toast element
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0 position-fixed bottom-0 end-0 m-3`;
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');
        
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;
        
        document.body.appendChild(toast);
        
        // Initialize and show the toast
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        // Remove the toast after it's hidden
        toast.addEventListener('hidden.bs.toast', function() {
            document.body.removeChild(toast);
        });
    }
});
