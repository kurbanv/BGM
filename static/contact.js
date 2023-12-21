document.querySelector('#contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    e.target.elements.name.value = 'name';
    e.target.elements.email.value = 'email';
    e.target.elements.message.value = 'message';
  });
