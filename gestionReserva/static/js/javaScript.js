function eliminar(producto_id, csrfToken) {
    if (confirm('¿Estás seguro de que deseas eliminar este producto?')) {
        fetch(`/eliminarProducto/${producto_id}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    console.error('Error al eliminar el producto');
                }
            })
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
            });
    }
}




document.getElementById('cancelButton').addEventListener('click', function () {
    // Redirigir al usuario a la página anterior
    window.history.back();
});




document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'es', // Configurar el idioma a español
        dayRender: function (info) {
            var today = new Date().toISOString().slice(0, 10);
            if (info.date.toISOString().slice(0, 10) === today) {
                var marker = document.createElement('div');
                marker.className = 'current-day-marker';
                info.el.appendChild(marker);
            }
        }
    });
    calendar.render();
});






function generarEstrellas(puntaje) {
    var estrellas = '';
    for (var i = 0; i < 5; i++) {
        if (puntaje >= (i + 1) * 20) {
            estrellas += '&#9733;'; // Código HTML de una estrella
        } else {
            estrellas += '&#9734;'; // Código HTML de una estrella vacía
        }
    }
    return estrellas;
}