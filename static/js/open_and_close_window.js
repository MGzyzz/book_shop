document.getElementById('author-form').onsubmit = function(e) {
    e.preventDefault(); // Предотвращаем обычную отправку формы
    var formData = new FormData(this);

    fetch(this.action, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            window.opener.postMessage('AuthorCreated', '*'); // Уведомляем родительское окно
            window.close(); // Закрываем всплывающее окно
        } else {
            alert('Ошибка при отправке формы.');
        }
    })
    .catch(error => console.error('Ошибка AJAX:', error));
};
