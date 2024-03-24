% include('header.tpl')

<script src="js/Chart.js"></script>

<center>

<div class="container" style="padding-bottom: 3rem">
    Start of the measurement: {{measurement_start}} <br>
    Charge Total: {{Ah}} Ah
</div>

<canvas id="myChart"></canvas>

</center>

<script>
let time = JSON.parse('{{times}}');
let voltage = JSON.parse('{{voltages}}');
let current = JSON.parse('{{currents}}');

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
</script>




% include('footer.tpl')