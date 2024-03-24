% include('header.tpl')

<script src="js/Chart.js"></script>

<center>


<div style="display:none" id="plotting_data_render_times">{{ times }}</div>
<div style="display:none" id="plotting_data_render_voltages">{{ voltages }}</div>
<div style="display:none" id="plotting_data_render_currents">{{ currents }}</div>

<div class="container" style="padding-bottom: 2rem">
    <b>Start of the measurement:</b> {{measurement_start}} <br>
    <b>Current voltage:</b> {{current_voltage}} V <br>
    <b>Charge Total:</b> {{Ah}} Ah
</div>

<canvas id="myChart"></canvas>
<script src="js/plot_chart.js"></script>

<label for="interval_start">Start time:</label>
<input type="number" id="interval_start" name="interval_start" value="{{time_start}}"/>

<label for="interval_end">End time:</label>
<input type="number" id="interval_end" name="interval_end" value="{{time_end}}"/>

<label for="n_points">N points:</label>
<input type="number" id="n_points" name="n_points" value="{{sampling_n_points}}"/>

<p>
<button id="redirect-button">Confirm</button>
<script src="js/interval_selector.js"></script>

<p>
<a href={{log_address}}> Download data as csv </a>

</center>





% include('footer.tpl')