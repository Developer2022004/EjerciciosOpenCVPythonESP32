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
    <div class="mostrar-grafico">
        <canvas id="grafico"></canvas>
        <canvas id="grafico_dos"></canvas>
        <canvas id="grafico_tres"></canvas>
        <canvas id="grafico_cuatro"></canvas>
    </div>

    <script src="{{ asset('js/chart.min.js') }}"></script>
    <script>
        let _datos = @json($datos);
        let etiquetas = _datos.map((_, index) => "Valor " + (index + 1));

        const chartBar = new Chart(document.getElementById('grafico'), {
            type: 'bar',
            data: {
                labels: etiquetas,
                datasets: [{
                    label: 'Sensor Uno',
                    data: _datos,
                    borderWidth: 2
                }]
            },
            options: {
                response: false
            }
        });

        const chartLine = new Chart(document.getElementById('grafico_dos'), {
            type: 'line',
            data: {
                labels: etiquetas,
                datasets: [{
                    label: 'Sensor Uno',
                    data: _datos,
                    borderWidth: 2
                }]
            },
            options: {
                response: false
            }
        });

        //Grafico tres

        const chartPie = new Chart(document.getElementById('grafico_tres'), {
            type: 'pie',
            data: {
                // labels: etiquetas,
                datasets: [{
                    // label: 'Sensor Uno',
                    data: _datos,
                    // borderWidth: 2
                }]
            },
            options: {
                response: false
            }
        });

        //Grafico 4

        const chartDoughnut = new Chart(document.getElementById('grafico_cuatro'), {
            type: 'doughnut',
            data: {
                // labels: etiquetas,
                datasets: [{
                    // label: 'Sensor Uno',
                    data: _datos,
                    // borderWidth: 2
                }]
            },
            options: {
                response: false
            }
        });

        setInterval(async () => {
            try {
                const respuesta = await fetch("/");
                const html = await respuesta.text();
                const match = html.match(/\[(.*?)\]/);

                if (!match) return;

                console.log(match);
                //Obtenemos el json de la raiz
                let nuevo_dato = JSON.parse("[" + match[1] + "]");
                console.log(nuevo_dato);
                let nuevo_labels = nuevo_dato.map((_, index) => 'Dato' + (index + 1));

                chartBar.data.labels = nuevo_labels;
                chartBar.data.datasets[0].data = nuevo_dato;
                chartBar.update();

                chartLine.data.label = nuevo_labels;
                chartLine.data.datasets[0].data = nuevo_dato;
                chartLine.update();

                chartPie.data.label = nuevo_labels;
                chartPie.data.datasets[0].data = nuevo_dato;
                chartPie.update();

                chartDoughnut.data.label = nuevo_labels;
                chartDoughnut.data.datasets[0].data = nuevo_dato;
                chartDoughnut.update();
            } catch (error) {
                console.error(error);
            }
        }, 3000);
    </script>

</body>

</html>
