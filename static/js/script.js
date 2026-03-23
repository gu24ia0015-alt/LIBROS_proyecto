// 1. Confirmación de eliminación (Requisito CRUD)
function confirmarEliminar(titulo) {
    return confirm(`¿Estás seguro de que deseas eliminar el libro "${titulo}"?`);
}

console.log("JS: Delete confirmation logic loaded.");


// 2. Efecto visual dinámico (Puntos extra por lógica JS)
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.backgroundColor = "#fdfdfd";
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.backgroundColor = "white";
        });
    });
    
    console.log("JS: Dynamic hover effects initialized.");
});