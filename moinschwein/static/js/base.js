function manageBackground(url, fallback) {
    const body = document.getElementById('body')
    let backgroundUrl = sessionStorage.getItem('backgroundImage');

    if (backgroundUrl) {
        body.style.backgroundImage = `url(${backgroundUrl})`;
    } else {
        if (url) {
            sessionStorage.setItem('backgroundImage', url);
            body.style.backgroundImage = `url(${url})`;
        } else {
            body.style.backgroundImage = `url(${fallback})`;
        }
    }
}