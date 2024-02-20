
export function selectButton(){
    document.querySelectorAll('.button-text').forEach(item => {
        item.addEventListener('click', event => {
            event.preventDefault(); // Linkin varsayılan davranışını engelle
    
            // Tıklanan a etiketinin üstündeki .card-button elementini bul
            const cardButton = item.closest('.card-button');
    
            // cardButton elementinin background-color özelliğini değiştir
            cardButton.style.backgroundColor = '#FFFFFF'; // Örnek olarak beyaz renk
    
            // Diğer card-buttonlardaki arka plan rengini sıfırla
            document.querySelectorAll('.card-button').forEach(btn => {
                if (btn !== cardButton) {
                    btn.style.backgroundColor = ''; // Varsayılan rengine geri dön
                }
            });
        });
    });
    
}
