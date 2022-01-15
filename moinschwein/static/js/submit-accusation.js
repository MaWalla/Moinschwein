function submitAccusation(url, csrfToken, formID, buttonID) {
    const form = document.getElementById(formID);
    const submitButton = document.getElementById(buttonID);

    submitButton.onclick = () => {
        const data = new FormData(form);

        fetch(url, {
            method: 'post',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: data,
        }).then(response => {
            if (response.status === 200) {

            } else {

            }

            setTimeout(function () {

            }, 2000);
        })
    }
}