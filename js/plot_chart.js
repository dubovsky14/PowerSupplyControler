
let time    =  JSON.parse(document.getElementById('plotting_data_render_times').innerHTML);
let voltage =  JSON.parse(document.getElementById('plotting_data_render_voltages').innerHTML);
let current =  JSON.parse(document.getElementById('plotting_data_render_currents').innerHTML);

let ctx = document.getElementById('myChart').getContext('2d');
let chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: time,
        datasets: [{
            label: 'Voltage [V] (left)',
            data: voltage,
            yAxisID: 'y-axis-voltage',
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderWidth: 1,
        }, {
            label: 'Current [A] (right)',
            data: current,
            //yAxisID: 'y-axis-current',
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderWidth: 1,
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Time [s]',
                },
            },
            y: {
                position: 'right',
                grid: { display: false, color: 'rgba(54, 162, 235, 1)' }
            }
        }
    }
});
