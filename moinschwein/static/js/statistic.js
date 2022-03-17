function drawChart(data, colorData, canvasID) {
    let labels = [];
    let amounts = [];
    let colors = [];
    data.forEach((user) => {
        if (user.amount > 0) {
            labels = [
                ...labels,
                `${user.first_name} ${user.last_name}`,
            ]

            amounts = [
                ...amounts,
                user.amount,
            ]

            colors = [
                ...colors,
                colorData[user.id],
            ]
        }

    });

    const chartData = {
        labels: labels,
        datasets: [{
            label: 'My First dataset',
            data: amounts,
            backgroundColor: colors,
        }]
    };

    const config = {
        type: 'doughnut',
        data: chartData,
        options: {},
    };

    return  new Chart(
        document.getElementById(canvasID),
        config,
    );
}

async function overallStatistic(url) {
    const response = await fetch(url);
    const data = await response.json();

    let colors = {};

    // JavaScript is such a whack language :D
    const getColorValue = () => Math.floor(Math.random() * 256);
    data.user_ids.forEach((id) => colors[id] = `rgb(${getColorValue()}, ${getColorValue()}, ${getColorValue()})`);

    const accusedChart = drawChart(data.accused, colors, 'accused');
    const accusingChart = drawChart(data.accusing, colors, 'accusing');
}
