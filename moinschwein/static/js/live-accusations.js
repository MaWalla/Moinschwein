function updateLiveAccusations(url) {
    const container = document.getElementById('live-container');

    setInterval(() => {
        fetch(url).then(response => response.json()).then(data => {
            while (container.lastChild) {
                container.removeChild(container.lastChild);
            }
            data.reverse();
            data.forEach((text) => {
                const element = document.createElement('p');
                element.innerHTML = text;
                container.append(element);
            });
        });
    }, 1000)
}
