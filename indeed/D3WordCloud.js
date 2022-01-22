function wordCloud(selector) {

    var fill = d3.scale.category20();

    //Construct the word cloud's SVG element
    var svg = d3.select(selector).append("svg")
        .attr("width", 500)
        .attr("height", 500)
        .append("g")
        .attr("transform", "translate(250,250)");

    //Draw the word cloud
    function draw(words) {
        var cloud = svg.selectAll("g text")
                        .data(words, function(d) { return d.text; })

        //Entering words
        cloud.enter()
            .append("text")
            .style("font-family", "Impact")
            .style("fill", function(d, i) { return fill(i); })
            .attr("text-anchor", "middle")
            .attr('font-size', 1)
            .text(function(d) { return d.text; });

        //Entering and existing words
        cloud
            .transition()
                .duration(600)
                .style("font-size", function(d) { return d.size + "px"; })
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .style("fill-opacity", 1);

        //Exiting words
        cloud.exit()
            .transition()
                .duration(200)
                .style('fill-opacity', 1e-6)
                .attr('font-size', 1)
                .remove();
    }


    return {
        update: function(words) {
            d3.layout.cloud().size([500, 500])
                .words(words)
                .padding(5)
                .rotate(function() { return ~~(Math.random() * 2) * 90; })
                .font("Impact")
                .fontSize(function(d) { return d.size; })
                .on("end", draw)
                .start();
        }
    }

}

var words = [
    "FedEx Delivery Driver Catalina Island $25/hr",
    "Find jobs with Flexible Hours!",
    "Permits Supervisor",
    "Visitor Service Center Agent",
    "U.S. Secret Service Criminal Investigator (Special Agent)",
    "Marine Interdiction Agent CBP LIVE Recruitment Webinar",
    "Part-time Guest Services Representative",
    "Border Patrol Agent GL-9",
    "Limpia de casa",
    "Utility Pole Inspection Foreman",
    "Executive Assistant",
    "Full-time Guest Services Representative",
    "Airport Operations Assistant Manager",
    "Operations Analyst",
    "Manager",
    "Front Desk / Guest Services Agent",
    "Plant Equipment Operator",
    "Fitness Center CSR",
    "Housekeeper",
    "Game Host for Unique Sightseeing Tour",
    "Food Service Worker",
    "Distribution Journeyman Lineman - Catalina Island",
    "Housekeeping Supervisor",
    "Communications Operator-Customer Service Rep",
    "TMV Trucking Inc",
    "Indeed Gigs",
    "Catalina Island Conservancy",
    "Catalina Island Company",
    "United States Secret Service",
    "U.S. Customs and Border Protection",
    "Catalina Island Medical Center",
    "Osmose Utility Services Inc",
    "Boldly",
    "MMW Hospitality Corp",
    "Hotel Vista Del Mar",
    "Southern California Edison",
    "Fantastic Race",
    "Inspire Malibu"
];

//Prepare one of the sample sentences by removing punctuation,
// creating an array of words and computing a random size attribute.
function getWords(i) {
    return words[i]
            .replace(/[!\.,:;\?]/g, '')
            .split(' ')
            .map(function(d) {
                return {text: d, size: 10 + Math.random() * 60};
            })
}


// user input or some other source.
function showNewWords(vis, i) {
    i = i || 0;

    vis.update(getWords(i ++ % words.length))
    setTimeout(function() { showNewWords(vis, i + 1)}, 2000)
}

//Create a new instance of the word cloud visualization.
var myWordCloud = wordCloud('body');

//Start cycling through the demo data
showNewWords(myWordCloud);
