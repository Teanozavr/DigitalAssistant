async function video_to_txt() {
    const modelResults = {};

    try {
        const response = await fetch(`http://localhost:8000/video_to_txt/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({}) // Если ваш API ожидает данные, добавьте их здесь
        });

        if (response.ok) {
            const result = await response.json();
            modelResults[modelId] = result; // Сохраняем результат для модели
            updateResults();
        } else {
            console.error('Сервер вернул ошибку:', response.statusText);
        }
    } catch (error) {
        console.error('Ошибка при обращении к серверу:', error);
    }

}
