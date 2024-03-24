document.getElementById('redirect-button').addEventListener('click', function() {
    var intervalStart = document.getElementById('interval_start').value;
    var intervalEnd = document.getElementById('interval_end').value;
    var nPoints = document.getElementById('n_points').value;


    var current_url = window.location.href;
    var newUrl = current_url + "?" +
        'interval_start=' + encodeURIComponent(intervalStart) + '&' +
        'interval_end=' + encodeURIComponent(intervalEnd) + '&' +
        'n_points=' + encodeURIComponent(nPoints);

    window.location.href = newUrl;
});