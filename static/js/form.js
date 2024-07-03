<script>
document.getElementById('submitAppointment').addEventListener('click', function() {
    var form = document.getElementById('appointmentForm');
    var formData = new FormData(form);

    var message = 'Новая заявка на прием:\n';
    message += 'Имя: ' + formData.get('name') + '\n';
    message += 'Email: ' + formData.get('email') + '\n';
    message += 'Телефон: ' + formData.get('phone') + '\n';
    message += 'Доктор: ' + formData.get('doctor') + '\n';
    message += 'Дата: ' + formData.get('date') + '\n';
    message += 'Время: ' + formData.get('time') + '\n';
    message += 'Проблема: ' + formData.get('problem') + '\n';

    // Замените YOUR_BOT_TOKEN и YOUR_CHANNEL_ID на соответствующие значения
    var botToken = '7004032681:AAHroW2_ZA01ingIwYEyRmH7gM0Oo558Jl8';
    var channelId = '-1002242936359';

    fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            chat_id: channelId,
            text: message
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.ok) {
            alert('Ваша заявка успешно отправлена!');
            form.reset();
        } else {
            alert('Произошла ошибка при отправке заявки. Пожалуйста, попробуйте еще раз.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Произошла ошибка при отправке заявки. Пожалуйста, попробуйте еще раз.');
    });
});
</script>