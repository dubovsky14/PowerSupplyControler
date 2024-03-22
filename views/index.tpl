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
            label: 'Voltage',
            data: voltage,
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
        }, {
            label: 'Current',
            data: current,
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
        }]
    },
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Time [s]'
                }
            },
            y: {
                beginAtZero: true
            }
        }
    }
});
</script>




% include('footer.tpl')