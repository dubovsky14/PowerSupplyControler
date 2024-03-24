% include('header.tpl')

<script src="js/Chart.js"></script>

<center>


<div style="display:none" id="plotting_data_render_times">{{ times }}</div>
<div style="display:none" id="plotting_data_render_voltages">{{ voltages }}</div>
<div style="display:none" id="plotting_data_render_currents">{{ currents }}</div>

<div class="container" style="padding-bottom: 3rem">
    Start of the measurement: {{measurement_start}} <br>
    Charge Total: {{Ah}} Ah
</div>

<canvas id="myChart"></canvas>

</center>

<script src="js/plot_chart.js"></script>




% include('footer.tpl')