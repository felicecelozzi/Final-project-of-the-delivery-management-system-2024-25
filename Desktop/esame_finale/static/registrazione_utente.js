    const form = document.getElementById('registrationForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
    const error = document.getElementById('error');

    form.addEventListener('submit', function(e) {
      e.preventDefault();

      if (password.value !== confirmPassword.value) {
        error.classList.remove('hidden');
        return;
      } else {
        error.classList.add('hidden');
      }

      // Simulazione invio dati
      const userData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        password: password.value
      };

      console.log('Dati utente registrato:', userData);
      alert('Registrazione avvenuta con successo!');
      form.reset();
    });