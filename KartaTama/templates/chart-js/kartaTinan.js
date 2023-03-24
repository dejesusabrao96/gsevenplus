// Java script chart karta tama no sai bazeia ba tinan 

document.addEventListener("DOMContentLoaded", () => {
  new ApexCharts(document.querySelector("#reportsChart2"), {
    series: [{
      name: 'Karta Tama',
      data: ["{% for ii in loopingcartaTinan %}","{{ii.total_carta_tama_tinan|floatformat:'3'}}","{% endfor %}"]
    }, {
      name: 'Karta Sai',
      data: ["{% for ii in loopingcartaTinan %}","{{ii.total_carta_sai_tinan|floatformat:'3'}}","{% endfor %}"]
    }],
    chart: {
      height: 250,
      type: 'bar',
      toolbar: {
        show: false
      },
    },
    markers: {
      size: 12
    },
    colors: ['purple', 'orange','red','green'],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 0,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 90, 100]
      }
    },
    dataLabels: {
      enabled: true,
    },
    stroke: {
      curve: 'smooth',
      width: 1
    },
    xaxis: {
      type: 'text',
      categories: ["{% for ii in loopingcartaTinan %}","{{ii.tinan}}","{% endfor %}"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
  }).render();
});