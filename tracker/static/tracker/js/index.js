var data = [
  {
    values: [70, 20, 10],

    labels: ["Fat", "Protein", "Carbohydrates"],

    type: "pie",

    textinfo: "label+percent",
    textposition: "inside",
    showlegend: true,
    automargin: true,
  },
];
var layout = {
  title: "Keto Macronutrients",


 

};


var config = { responsive: true };
Plotly.newPlot("macroChart", data, layout, config);


var layout = {
  title: "Fasting Timeline",
  showlegend: true,

  xaxis: {
    title: {
      text: "Time [Hours]",

      font: {
        family: "",

        size: 18,

        color: "#7f7f7f",
      },
    },
  },

  yaxis: {
    title: {
      text: "%",

      font: {
        family: "",

        size: 18,

        color: "#7f7f7f",
      },
    },
  },
  yaxis2: {
    title: "%",

    titlefont: { color: "rgb(148, 103, 189)" },

    tickfont: { color: "rgb(148, 103, 189)" },

    overlaying: "y",

    side: "right",
  },
};


var trace1 = {
  y: [100,100,75,75+12,75,75-12,50,80,55,50,50,50,65,50,50,45,40,50,30,25,20,20,20,20,20,20],

  x: [0, 5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125],

  type: "scatter",
  name: "Glucose and Insulin",

};

var trace2 = {
  y: [0,0,0,0,0,12,12,20,23,25,35,40,55,55,55,55,60,65,70,75,75,80,85,90,95,100],

  x: [0, 5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125],

  type: "scatter",
  name: "Weight Loss and Keytones",
  
};

var trace3 = {
  y: [
    0, 0, 0, 0, 0,0, 30,35,40,45,50,55,60,70,70,70,75,80,80,85,85,85,85,85,85,85
  ],

  x: [
    0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
    95, 100, 105, 110, 115, 120, 125,
  ],

  type: "scatter",
  name: "Stem Cells",

};

var trace4 = {
  y: [0],

  x: [
72
  ],

  type: "scatter",
  name: "72 Hours",
  
};

var trace5 = {
  y: [
    0, 0, 0, 10, 15, 20, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 85, 80, 70,
    60, 50, 40, 30, 20, 10, 0,
  ],

  x: [
    0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 72, 75, 80, 85, 90,
    95, 100, 105, 110, 115, 120, 125,
  ],

  type: "scatter",
  name: "Autophagy and Hgh",

};
var trace6 = {
  x: [72, 72],

  y: [100, 0],

  mode: "text+lines",

  type: "scatter",

  name: "Peak Muscle Protection",

  text: ["Peak Muscle Protection 72 Hours"],

  textfont: {
    family: "Times New Roman",
  },

  textposition: "top center",

  marker: { size: 12 },
};







var data = [trace1,trace2,trace3,trace6,trace5];

Plotly.newPlot("hghChart", data, layout, config);