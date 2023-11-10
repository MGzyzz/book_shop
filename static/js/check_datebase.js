window.addEventListener('message', function(event) {
    if (event.data === 'AuthorCreated') {
        window.location.reload(); // Перезагружаем родительское окно
    }
}, false);
