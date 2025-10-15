    document.getElementById('loginForm').addEventListener('submit', function(e) {
      e.preventDefault();
      // Mock check login
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      if (email === "admin@demo.it" && password === "demo") {
        localStorage.setItem('auth', true);
        window.location.href = "login.html";
      } else {
        alert("Credenziali errate");
      }
    });