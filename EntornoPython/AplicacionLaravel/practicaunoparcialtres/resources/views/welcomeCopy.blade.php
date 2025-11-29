<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Laravel</title>
    <link href="{{ asset('css/style.css') }}" rel="stylesheet">
    <!-- Styles -->
</head>

<body>
    <div class="mostrargrafico">
        <canvas id="grafico"></canvas>
        <canvas id="grafico_dos"></canvas>
        <canvas id="grafico_tres"></canvas>
        <canvas id="grafico_cuatro"></canvas>
    </div>

    <script src="{{ asset('js/chart.min.js') }}"></script>
    <script>
        let _datos = @json($datos);

        const dat = {
            labels: _datos.map((index) => index),
            datasets: [{
                label: 'Dataset 1',
                data: _datos,
            }, ]
        }

        //Grafico Uno
        const grafico = document.getElementById('grafico');
        // console.log(_datos);
        new Chart(grafico, {
            type: 'bar',
            data: dat,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Chart.js Bar Chart'
                    }
                }
            }
        });

        //Grafico Dos
        const grafico_dos = document.getElementById('grafico_dos');
        // console.log(_datos);
        new Chart(grafico_dos, {
            type: 'pie',
            data: dat,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Chart.js Pie Chart'
                    }
                }
            }
        });

        //Grafico tres
        const grafico_tres = document.getElementById('grafico_tres');
        // console.log(_datos);
        new Chart(grafico_tres, {
            type: 'line',
            data: dat,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Chart.js Line Chart'
                    }
                }
            },
        });

        // //Grafico Cuatro
        //  const grafico_cuatro = document.getElementById('grafico_cuatro');
        // // console.log(_datos);
        new Chart(grafico_cuatro, {
            type: 'doughnut',
            data: dat,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Chart.js Doughnut Chart'
                    }
                }
            },
        });
    </script>



</body>

</html>
